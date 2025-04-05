import time
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color

toy = scanner.find_toy(toy_name="Q5-D924")
if not toy:
    print("R2-D2 not found.")
else:
    with SpheroEduAPI(toy) as droid:
        print("Connected!")
        droid.set_main_led(Color(0, 0, 255))  # Blue!
        droid.roll(0, 80, 2)           # Try to move forward for 2 seconds
        time.sleep(2)
        droid.roll(0, 0, 1)            # Stop