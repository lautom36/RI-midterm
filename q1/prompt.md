1.  (20 points) Moving in a car
    I would like you to use a skid steer model of a robot that is 75cm long and 55cm wide and
    run a few simple experiments with it. Please upload your resulting figures and python
    (or other) code:

    (a) (5 points) Make a list of commands (at t=0.1) that will allow this robot to traverse
        along the edge of a 5m diameter circle. The robot starts off in the center of the
        circle (0,0), and you cannot leave the circle’s border. Plot both the resulting path
        (x, y) and trajectory (x, y, and angular velocities). Assume a constant velocity of
        8m/s

    (b) (5 points) Do the same as the above for a traditional car (Ackermann steering).

    (c) (10 points) If the car is traveling for 10s, what is my position error using the dis-
        cretized equations of motion if I define my time steps at ∆t = 1,0.1,0.01 ? Plot
        the errors and computing time for the Ackermann vehicle in these cases. Use the
        forward Euler approach and compute a total error based on the distance difference
        from the analytical circle to the discrete-time equations.

    (d) (10 points) Graduate Student Question Compute part c again where road fric-
        tions are much lower (due to rain or ice). Slip causes your tires to respond very
        differently. Assume that your theta is θactual = θ(1 −0.08) and velocity is vactual =
        v(1 −0.04).