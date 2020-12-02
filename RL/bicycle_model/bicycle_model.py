class BicycleKinematicModel:
    
    def __init__(self, x, y, steering_angle, heading_angle):
        self._x = x
        self._y = y
        self._steering_angle = steering_angle
        self._heading_angle = heading_angle

    def get_state(self):
        return self._x, self._y, self._steering_angle, self._heading_angle

    def change_state(self):
        pass

    
