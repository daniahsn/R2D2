import time
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color

def timed_led_transitions(interval=2):
    # Locate the R2-D2 bot; complete the function call with any required parameters
    toy = scanner.find_toy(toy_name="Q5-D924")
    if not toy:
        print("No R2-D2 found!")
        return
    
    with SpheroEduAPI(toy) as droid:
        # Define a list of colors; you may add more or modify the RGB values.
        colors = [Color (255, 0, 0), Color(0, 0, 255), Color(0,255, 0)]
        heading = 0 # Starting heading.
        speed = 200 # Movement speed (e.g., 50) .
        
        # Iterate for a fixed number of cycles (increase if needed) 
        for i in range(6): # e.g., 6 cycles for two full iterations
            color = colors[i % len(colors)]
            droid.set_main_led(color)
            droid.roll(heading, speed, interval)
            time. sleep(interval)
            # Update heading by a fixed angle.
            heading = (heading + 60) % 360
        
        # Final Stop
        droid.roll(heading,0,1)
        print("LED movement sequence complete.")

timed_led_transitions()
