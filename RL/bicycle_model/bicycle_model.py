from math import cos, sin, tan

class BicycleKinematicModel:
    
    def __init__(self, x, y, steering_angle, heading_angle, bicycle_len = 1.5):
        self._x = x                                 # meters
        self._y = y                                 # meters
        self._steering_angle = steering_angle       # radians
        self._heading_angle = heading_angle         # radians
        self.bicycle_len = bicycle_len              # meters

    def get_state(self):
        return self._x, self._y, self._steering_angle, self._heading_angle

    def change_state(self, velosity, steering_rate):
        R = self.bicycle_len / tan(self._steering_angle)    
        rotation_rate = velosity / R

        delta_x = velosity * cos(self._heading_angle)
        delta_y = velosity * sin(self._heading_angle)
        delta_theta = rotation_rate 
        delta_sigma = steering_rate

        self._x += delta_x
        self._y += delta_y
        self._heading_angle += delta_theta
        self._steering_angle += delta_sigma
    

        

    
