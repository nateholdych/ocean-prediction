#Logic for determining personality characteristics based on OCEAN traits
#Nate Holdych 2/23/2021

class Characteristic:
    # Class defining characteristics to be calculated using OCEAN traits
    
    def __init__(self, name, o, c, e, a, n, description = ""):
        # Every parameter is the weight of each respective OCEAN trait for the calculated characteristic
        # Pass a weight of 0 if trait is not used
        
        self.weightO = o
        self.weightC = c
        self.weightE = e
        self.weightA = a
        self.weightN = n
        self.weights = [o,c,e,a,n]

        self.name = name
        self.description = description
class Score:
    # For OCEAN scores such as user score and average score
    
    def __init__(self, o, c, e, a, n):
        # Pass the scores for each trait (0 - 100)
        
        self.o = o
        self.c = c
        self.e = e
        self.a = a
        self.n = n
        self.traits = [o,c,e,a,n]
        
    def calc(self, characteristic, average):
        # Calculate a characteristic based on personal score compared to average
        # Pass an object of the Characteristic class and one of Score
    
        maxVal = 0
        minVal = 0
        totalVal = 0
        
        for i in range(5):
            # Calculate personal characteristic score by iterating through each trait
            
            totalVal += (self.traits[i] - average.traits[i]) * characteristic.weights[i]
            
            if characteristic.weights[i] > 0:
                maxVal += characteristic.weights[i] * (100 - average.traits[i])
                minVal += characteristic.weights[i] * (0 - average.traits[i])
            else:
                minVal += characteristic.weights[i] * (100 - average.traits[i])
                maxVal += characteristic.weights[i] * (0 - average.traits[i])

        # Now set totalVal between -1 and 1
        if totalVal > 0:
            totalVal /= maxVal
        elif totalVal < 0:
            totalVal /= minVal * -1

        return totalVal
