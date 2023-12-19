class Statistic:
    def __init__(self) -> None:
        self.sum = 0     
        self.variances = 0   
        pass
    
    def mean(self, *values):
        for value in values:
            self.sum += value
        return self.sum/len(values)
    
    def variance(self, *values):
        mean = self.mean(*values)
        for value in values:
            self.variances += (value - mean)**2
        return self.variances/len(values)
    
    def standardDeviation(self, *values):
        return self.variance(*values)**0.5
    
    