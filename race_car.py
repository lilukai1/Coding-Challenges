class RaceCar():
    
    def __init__(self, color, fuel_remaining, **kwargs):
        self.color = color
        self.fuel_remaining = fuel_remaining
        self.laps = 0
        
        for key, value in kwargs.items():
            setattr(self, key, value)

    
    def __str__(self):
        print(f"This is a {str(self.color)} car with {str(self.fuel_remaining)} fuel left on lap {str(self.laps)}")
    
    def run_lap(self, length):
        self.fuel_remaining -= length * .125
        self.laps += 1

