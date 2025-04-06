import time 
import math
from spherov2 import scanner 
from spherov2.sphero_edu import SpheroEduAPI

def spiral_movement(initial_radius=0.2, radius_increment=0.05, angle_speed=90, max_radius=1.0):
    """Moves R2-D2 outward in a spiral by increasing the radius after each full rotation."""
    # Locate the R2-D2 bot; complete the function call with any required parameters
    toy = scanner.find_toy(toy_name="Q5-D924")
    if not toy:
        print("No R2-D2 found!")
        return
        
    with SpheroEduAPI (toy) as droid:
      
        current_radius = initial_radius  # Start with the base "radius" (really speed)
        print(f"Starting new revolution at radius:{current_radius:.2f}")
        heading = 0  # Start facing forward (0°)
        
        while current_radius <= max_radius:
            revolution_time = 360.0 / angle_speed  #Calculate time for one full revolution.
            start_time = time.time()
            
            # Perform a full circular revolution at current radius
            while time.time () - start_time < revolution_time:
                # Update heading gradually based on angle_speed.
                heading = int ((heading + angle_speed * 0.1) % 360)# Gradual turn
                droid.roll(heading, int(current_radius * 255), 0.1)  # Speed scaled 0–255
                time.sleep(0.1)  # Wait before next update
            current_radius += radius_increment #Increase the radius for the next revolution.
            print(f"Expanding spiral: next radius will be {current_radius:.2f}")

        
        droid.roll(0,0,1)
        print("Spiral movement complete.")

spiral_movement ()