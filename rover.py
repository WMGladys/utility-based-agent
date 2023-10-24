import random

class RoverPerformance:
    def __init__(self):
        self.sampled_locations = set()  # Initialize an empty set to store sampled locations

    def record_sample(self, location):
        self.sampled_locations.add(location)  # Add the sampled location to the set

    def is_location_sampled(self, location):
        return location in self.sampled_locations  # Check if the location has been sampled before


class MarsEnvironment:
    def __init__(self):
        self.locations = {'A': 0, 'B': 0, 'C': 0, 'D': 0}  # Initialize the locations dictionary with no rocks available

    def change_environment(self):
        for location in self.locations:
            self.locations[location] = random.randint(0, 1)  # Randomly update the availability of rocks in each location

    def is_location_available(self, location):
        return self.locations[location] == 1  # Check if the location has rocks available


class RoverAgent:
    def __init__(self, performance, environment):
        self.performance = performance  # Store the RoverPerformance object
        self.environment = environment  # Store the MarsEnvironment object
        self.current_location = None  # Initialize the current location as None

    def explore(self, venture_num):
        print(f"----Exploration Venture {venture_num}------")  # Print the venture number

        self.environment.change_environment()  # Change the environment before starting the exploration venture

        self.current_location = random.choice(list(self.environment.locations.keys()))  # Randomly select the current location

        print(self.environment.locations)  # Print the current environment state

        print("Rover is in location", self.current_location)  # Print the rover's current location

        if self.environment.is_location_available(self.current_location):  # Check if current location has rocks
            if not self.performance.is_location_sampled(self.current_location):  # Check if location has been sampled
                self.performance.record_sample(self.current_location)  # Record the sample
                print(self.current_location, "rocks sampled.")  # Print the message
            else:
                print(self.current_location, "location has been sampled before.")
        else:
            print(self.current_location, "has no rocks.")

        for location in self.environment.locations:  # Iterate over the remaining locations
            if location != self.current_location:
                if self.environment.is_location_available(location):  # Check if location has rocks
                    if not self.performance.is_location_sampled(location):  # Check if location has been sampled
                        self.performance.record_sample(location)  # Record the sample
                        print(location, "rocks sampled.")  # Print the message
                    else:
                        print(location, "location has been sampled before.")
                else:
                    print(location, "has no rocks.")

          # Print the performance


performance = RoverPerformance()  # Create a RoverPerformance object
environment = MarsEnvironment()  # Create a MarsEnvironment object
rover = RoverAgent(performance, environment)  # Create a RoverAgent object with the RoverPerformance and MarsEnvironment objects

rover.explore(0)  # Perform the first exploration venture
rover.explore(1)  # Perform the second exploration venture
performance = (len(performance.sampled_locations) / 8) *100  # Calculate the performance
print("Rover's performance:", performance, "%")
