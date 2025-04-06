import time
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color

def acceleration_pattern(accel_rate=10, cruise_speed=80, decel_rate=10, cruise_duration=3):
    """ Gradually accelerates up to a target speed, cruises, then
    decelerates back to zero. """

    # Locate the R2-D2 bot; complete the function call and add any necessary parameters.
    toy = scanner.find_toy(toy_name="Q5-D924")
    if not toy:
        print("No R2-D2 found!")
        return
    print("Connected")

    # Initialize the bot's API interface using the found toy.
    with SpheroEduAPI(toy) as droid:
        current_speed = 0

        # Accelerate phase: increase the speed until cruise_speed is reached.
        while current_speed < cruise_speed:
            current_speed += accel_rate  # Increase by acceleration rate.
            print(f"Accelerating to {current_speed}")
            if current_speed > cruise_speed:
                current_speed = cruise_speed
            droid.roll(0, current_speed, 1)  # Provide direction and duration.
            time.sleep(0.1)  # Wait for the motion to take effect.

        # Cruise phase: maintain the speed for a fixed duration.
        print("Cruising")
        droid.roll(0,current_speed,cruise_duration)
        time.sleep(0.1)  #Cruise for cruise_duration seconds.

        # Decelerate phase: decrease the speed gradually to zero
        while current_speed > 0:
            current_speed -= decel_rate  # Decrease by deceleration rate.
            print(f"Decelerating to {current_speed}")
            if current_speed < 0:
                current_speed = 0
            droid.roll(0, current_speed, 1)  # Continue forward while slowing down
            time.sleep(0.1)  # Wait for the motion to take effect.

        # Final stop: ensure the bot is completely stationary.
        droid.roll(0, 0, 1)  # Stop completely (speed 0)
        print("Stopped")

# Call the function to run the acceleration pattern.
acceleration_pattern()
