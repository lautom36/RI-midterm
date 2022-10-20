(20 points) Moving in a car
I would like you to use a skid steer model of a robot that is 75cm long and 55cm wide and
run a few simple experiments with it. Please upload your resulting figures and python
(or other) code:

(a) (5 points) Make a list of commands (at t=0.1) that will allow this robot to traverse
    along the edge of a 5m diameter circle. The robot starts off in the center of the
    circle (0,0), and you cannot leave the circle’s border. Plot both the resulting path
    (x, y) and trajectory (x, y, and angular velocities). Assume a constant velocity of
    8m/s

(b) (5 points) Do the same as the above for a traditional car (Ackermann steering).

(c) (10 points) Your Ackermann vehicle (with the same dimensions as described for the
    skid steer), is driving on a circle of radius 2.5m. Assume that you begin on the edge
    of the circle. Calculate the positional error with our computational approximation
    using the forward Euler method, as referred to in the course notes and illustrated
    in Reading 2, eq. 1.6. Graph the errors and computing time for three different
    time-steps (∆t = 1,0.1,0.01), error is defined as the absolute distance between the
    expected (from equations) to real x,y position (defined analytically) over time.
    Brief notes on what this problem is about: Imagine that you are moving a semi-truck
    and you have GPS positions (somewhat accurate) and an internal prediction model.
    We want the internal models to be updated based on ”ground truth” information
    to build better estimates of the vehicle motion over time.