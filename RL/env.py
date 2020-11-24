# https://stable-baselines.readthedocs.io/en/master/guide/custom_env.html
import gym
from gym import spaces
import pandas as pd
import numpy as np
import shapely.geometry as geom
from obspy.geodetics import degrees2kilometers
from stanley_controller.stanley import MatlabWrapper


class CarEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self, filename='../data/ref1_v2.csv', type='continuous',
                 action_dim=1, verbose=1):

        super(CarEnv, self).__init__()

        self.type = type
        self.action_dim = action_dim
        self.verbose = verbose
        self.df = self._read_df(filename)
        self.road = self._create_road()

        # x: x coord in meters
        # y: y coord in meters
        # theta: vehicle heading angle in radians
        # v: velocity in m/s
        # psi: steering angle in radians
        # 130 km/h ~= 36 m/s
        self.observation_space = spaces.Box(
            low=np.array([-np.inf, -np.inf, -np.pi, 0., -(np.pi/4)]),
            high=np.array([np.inf, np.inf, np.pi, 36., np.pi/4])
        )

        # steering cmd a.k.a. psi
        # let's keep the speed constant as 2 m/s so that the action space is 1D
        self.action_space = spaces.Box(
            low=np.array([-(np.pi/4)]),
            high=np.array([np.pi/4])
        )

        self.viewer = None
        self.init_x = self.df['LON'][0]
        self.init_y = self.df['LAT'][0]
        self.init_theta = self.df['CRS'][0]
        self.init_v = 2.0
        self.init_psi = 0.0
        self.init_observation = np.array([self.init_x, self.init_y,
                                          self.init_theta, self.init_v,
                                          self.init_psi])
        self.state = None
        self.matlab = MatlabWrapper()

    @staticmethod
    def _read_df(filename: str) -> pd.DataFrame:
        df = pd.read_csv(filename)
        # covert degrees to meters and degrees to radians
        df['LAT'] = df['LAT'].apply(lambda deg: degrees2kilometers(deg) * 1000)
        df['LON'] = df['LON'].apply(lambda deg: degrees2kilometers(deg) * 1000)
        df['CRS'] = df['CRS'].apply(lambda deg: np.deg2rad(deg))

        return df

    def _create_road(self):
        points = list()

        for index, row in self.df.iterrows():
            points.append(geom.Point(row['LON'], row['LAT']))

        road = geom.LineString(points)

        return road

    def step(self, action):
        # action = delta_psi in radians (delta of the steering command)
        # action = steering command a.k.a. angle psi in radians

        done = False
        info = {'current_state': {'x': self.state[0],
                                  'y': self.state[1],
                                  'theta': self.state[2],
                                  'v': self.state[3],
                                  'psi': self.state[4]},
                'action': action}

        x = self.state[0]
        y = self.state[1]
        theta = self.state[2]
        v = self.state[3]
        psi = self.state[4] + action[0]

        new_coords = self.matlab.bicycle_kinematic_model(x, y, theta, v, psi)
        new_point = geom.Point(new_coords[0], new_coords[1])
        distance = self.road.distance(new_point)

        if distance > 0.5:
            reward = -100
            done = True
        else:
            reward = (0.5 - distance) * 10.0

        new_x = new_coords[0]
        new_y = new_coords[1]
        new_theta = new_coords[2]
        self.state = [new_x, new_y, new_theta, v, psi]

        info['distance'] = distance
        info['reward'] = reward
        info['new_state'] = {'x': self.state[0],
                             'y': self.state[1],
                             'theta': self.state[2],
                             'v': self.state[3],
                             'psi': self.state[4]}

        # update info (include previous state, new state and reward)
        observation = self.state

        return observation, reward, done, info

    def reset(self):
        self.state = self.init_observation

        return self.init_observation

    def render(self, mode='human'):
        pass

    def close(self):
        if self.viewer is not None:
            self.viewer.close()
            self.viewer = None


if __name__ == '__main__':

    env = CarEnv()
    for i_episode in range(10):
        observation = env.reset()
        for t in range(10000):
            # env.render()
            # with each action just turn the wheel +0.05 rad
            action = np.array([0.05])
            observation, reward, done, info = env.step(action)
            print(info)
            if done:
                print("Episode finished after {} timesteps".format(t + 1))
                break
    env.close()
