import time
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI

def star_path(speed=80, roll_duration=3):
    """Draws a five-point star by moving forward and turning 144° after each edge."""

    # Locate and connect to the bot
    toy = scanner.find_toy(toy_name="Q5-D924")
    if not toy:
        print("No R2-D2 found!")
        return

    # Keep everything inside the context manager!
    with SpheroEduAPI(toy) as droid:
        heading = 0  # Initial direction

        for _ in range(5):  # 5 points = 5 moves
            droid.roll(int(heading), speed, roll_duration)
            time.sleep(roll_duration)  # Wait for movement to finish

            heading = (heading + 144) % 360  # Turn right 144 degrees

        # Final stop inside the context manager
        droid.roll(0, 0, 1)
        print("Star path complete.")

# Run the function
star_path(speed=80, roll_duration=3)