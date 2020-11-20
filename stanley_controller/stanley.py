"""
How to install the MATLAB Engine API:
https://ch.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html

"""

from matlab.engine import start_matlab
from matlab import double
import io 

class MatlabWrapper:

    def __init__(self):    
        self._out = io.StringIO()
        self._err = io.StringIO()
        self._eng = start_matlab()


    def __del__(self):
        self._eng.quit()
        self._out.close()
        self._err.close()


    def steering_command(self, refPose: list, currPose: list, velocity: float):
    """
    Computes the steering angle command steerCmd, in degrees, using the  
    Stanley method.

    Parameters
        ----------
        refPose : str
            Reference pose, specified as an [x, y, Θ] vector. x and y are in meters, and Θ is in degrees.
            x and y specify the reference point to steer the vehicle toward. 
            Θ specifies the orientation angle of the path at this reference point and is positive in the counterclockwise direction.
        currPose : str
            Current pose of the vehicle, specified as an [x, y, Θ] vector. x and y are in meters, and Θ is in degrees.
            x and y specify the location of the vehicle, which is defined as the center of the vehicle's rear axle.
            Θ specifies the orientation angle of the vehicle at location (x,y) and is positive in the counterclockwise direction.
        velocity : float
            Current longitudinal velocity of the vehicle. Units are in meters per second.

        Returns
        ----------
            A steering angle command in degrees.
    """

    refPose = double(refPose)
    currPose = double(currPose)
        cmd = self._eng.lateralControllerStanley(refPose, currPose, velocity,\
            stdout=self._out, stderr=self._err)
        self._log()
    return cmd

    def _log(self):
        output = self._out.getvalue()
    if output != '':
        print(output)

        error = self._err.getvalue()
    if error != '':
        print(error)

