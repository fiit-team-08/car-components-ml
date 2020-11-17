"""
How to install the MATLAB Engine API:
https://ch.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html

"""

from matlab.engine import start_matlab
from matlab import double
import io 

out = io.StringIO()
err = io.StringIO()
eng = start_matlab()

def steering_command(refPose: list, currPose: list, velocity: float):
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
    """

    refPose = double(refPose)
    currPose = double(currPose)
    cmd = eng.lateralControllerStanley(refPose, currPose, velocity,\
        stdout=out, stderr=err)
    log()
    return cmd

def log():
    output = out.getvalue()
    if output != '':
        print(output)

    error = err.getvalue()
    if error != '':
        print(error)

