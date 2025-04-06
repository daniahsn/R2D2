import time
from spherov2 import scanner 
from spherov2.sphero_edu import SpheroEduAPI
def programmable_shape_drawer ():
    """ Lets the user input (distance, angle) pairs to command R2-D2 to draw a custom shape. """
    
    shape_instructions = []
    
    # Keep asking the user for input until they type 'quit'
    while True:
        user_input = input ("Enter distance and angle (or 'quit'): ")
        if user_input. lower () == 'quit' :
            break
        try:
            # Split the input into distance and angle
            dist_str, angle_str = user_input.split ()
            dist = float (dist_str)
            angle = float (angle_str)
            shape_instructions.append((dist, angle))
        except ValueError:
            print ("Invalid input. Please enter two numbers or 'quit'.")
   
    # Locate the R2-D2 bot; complete the function call with any required parameters
    toy = scanner.find_toy(toy_name="Q5-D924")
    if not toy:
        print("No R2-D2 found!")
        return
    
    # Initialize the API with the located bot.
    with SpheroEduAPI (toy) as droid:
        heading = 0 # Initial heading (in degrees) (0° means forward relative to robot's current orientation)
        total_distance = 0 #To track how far the robot has traveled in total
        
        for dist, angle in shape_instructions:
            # Calculate travel time based on distance and a fixed speed.
            speed = 200
            travel_time = abs (dist) / speed # Assuming speed of 50.
            if dist < 0: 
                # Negative distance means move backward
                # Add 180° to heading to go in the opposite direction
                move_heading = (heading + 180) % 360
                droid.roll(int(move_heading),speed,travel_time)
            else: 
                # Move forward with the current heading. 
                droid.roll(int(heading), speed, travel_time)
            
            time.sleep(travel_time) # Pause while movement finishes
            total_distance += abs (dist) #Accumulate distance regardless of direction
            
            # Update heading after moving.
            heading = (heading + angle) % 360
            
            # Brief pause after turning to stabilize the movement.
            droid.roll(int(heading), 0, 0.1)
            time.sleep(0.5)
        print (f"Shape complete! Total distance traveled: {total_distance:.2f}")
        droid.roll(0,0,1)  # Full stop command

# Call the function to start drawing the shape.
programmable_shape_drawer ()