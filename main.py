#A utility-based agent for a rover in mars to count rocks in 4 different locations.
import random
import time

#class for utility / performance
class performance(object):
    def __init__ (self):
        self.sampledLocations = []
    def addSampledLocations(self, location):
        self.sampledLocations.append(location)
    def displaySampledLocations (self):
        print('sampled locations')
        for location in self.sampledLocations:
            print(location)
    def calculatePerformace(self):
        numberOfUniqueLocations = len(set(self.sampledLocations))
        totalSamples = len(self.sampledLocations)
        utility = (numberOfUniqueLocations/totalSamples) * 100
        print('The score is ', utility)

        return  numberOfUniqueLocations,  totalSamples


    #method to display the score
    # def display (self):
    #     print('The score is ', self.score)
    #     print('The utility is ', self.performance, '%')




#class for environment
class environment (object):
    def __init__ (self):
        self.location = ['A', 'B', 'C', 'D']
        #0 means has rocks and 1 means no rocks.
        self.locationCondition = {'A' : 0, 'B' : 0, 'C' : 0, 'D' : 0}
        self.locationCondition['A'] = random.randint(0, 1)
        self.locationCondition['B'] = random.randint(0, 1)
        self.locationCondition['C'] = random.randint(0, 1)
        self.locationCondition['D'] = random.randint(0, 1)
        #putting the rover location
        self.roverLocation = random.choice(self.location)
        #create the modes for sampled or unsampled
        self.mode = ['sampled', 'unsampled']
        #intitially, all locations are unsampled
        self.sampleStatus = {'A' : 'unsampled', 'B' : 'unsampled', 'C' : 'unsampled', 'D' : 'unsampled'}
        self.sampleStatus['A'] = random.choice(self.mode)
        self.sampleStatus['B'] = random.choice(self.mode)
        self.sampleStatus['C'] = random.choice(self.mode)
        self.sampleStatus['D'] = random.choice(self.mode)


#class for agent
class agent (environment, performance):
    def __init__(self, environment, performance):
        print('Condition to check if location has rocks or not - ',environment.locationCondition,
              'Condition to check where the rover is - ', environment.roverLocation,
              'condition to check if location has been sampled or not', environment.sampleStatus)
        count = 0
        while count < 2:
            #first check if location where rover is has rocks, then if it was previously sampled
            if environment.locationCondition[environment.roverLocation] == 0:
                print('The location where the rover is has rocks')
                if environment.sampleStatus[environment.roverLocation] ==  'unsampled':
                    print(environment.roverLocation, ' - This location has rocks and has been sampled')
                    environment.sampleStatus[environment.roverLocation] = 'sampled'
                else:
                    environment.sampleStatus[environment.roverLocation] =  'sampled'
            #if location where rover is has no rocks
            else:
                if environment.locationCondition[environment.roverLocation] == 1:
                    if environment.sampleStatus[environment.roverLocation] == 'unsampled':
                        print(environment.roverLocation, '- This location has no rocks and has been sampled')
                        environment.sampleStatus[environment.roverLocation] = 'sampled'
                    else:
                        environment.sampleStatus[environment.roverLocation] = 'sampled'

            newIndex = environment.location.index(environment.roverLocation) + 1
            if newIndex == 4:
                newIndex = 0
            environment.roverLocation = environment.location[newIndex]
            count += 1
        print("new conditions - ", environment.locationCondition)
        print("updated history - ", environment.sampleStatus)


#creating instances of the classes
theScore = performance()
x = 0
while x < 4:
    e1 = environment()
    a1 = agent(e1, theScore)
    x += 1
    time.sleep(10)
theScore.displaySampledLocations()


# {} () : _