# Dragon-Curve
Just a silly dragon curve generator

# Concept
1st iteration: 90°
2nd iteration: 90° 90° -90°
3rd iteration: 90° 90° -90° 90° 90° -90° -90°

The pattern goes like this:
1. First add a 90° after the previous iteration
2. Times the previous iteration by -1
3. Mirror it and append to the next iteration

# How it works
It works by first calculate the change pattern according to the iteration input by user (to put it simple the change pattern list will be consist 1 and -1), once the calculation is done, it will return a long list of 1 and -1 that covers the iteration specify. It will run a for loop and times that change pattern list with the degree of changes input by the user.

# Result
![dragon curve](https://github.com/user-attachments/assets/7518ec4c-5af5-4bf3-a988-d70d31295ec3)

This is done with the following settings:
Iteration: 17
Length of segment: 0.3
Turning angle: 80
Curve's color: White
Background color: Black

* There is an option for the user to choose for instant result or watch the Python Turtle draw itself, preferrably will be instant result because let it draw itself will takes too much time since each iteration grows exponentially
