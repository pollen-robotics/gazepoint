# gazepoint
Python library to get gaze point from gazepoint device GP3

## Installation

You need lxml to launch:

```pip install lxml```

## Setting up your gazepoint device

Follow the instruction at this link: http://www.gazept.com/dl/gazepoint_quick_start.pdf

## Accessing gaze position in Python

First open the GazePoint Control software and leave it in the background.

Then in Python you can do (Python 2.7 required for now):

```python
# Create a GazePoint Instance
# This will start a calibration procedure after a few seconds
# Make sure the user is ready and the device is set before runnign this line
gazetracker = GazePoint()

# Get the gaze position
# x and y and relative coordinate to the screen
# (0, 0) is the upper left corner
# (1, 1) is the lower rigth corner
x, y = gazetracker.get_gaze_position()

# You can query gaze position as fast as desired
# Here for 5 seconds at 10Hz
start = time.time()
while time.time() - start < 5:
    print gazetracker.get_gaze_position()
    time.sleep(0.1)

# Once done think of stopping the gazetracker, 
# It closes the connection properly and can take a few seconds
gazetracker.stop()
```

Have fun controlling everything with your eye!
