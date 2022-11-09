class Train:
    locations=["A - The Mines","B - Town A","C - The Market","D - The Train Yard","E - The Factory","F - Town B","G - The Farms"]
    #A is the mines
    #B is Town A
    #C is the Market
    #D is the Train Yard
    #E is the Factory
    #F is Town B
    #G is the Farms
    
    def __init__(self):
        self.funds=100
        self.iron=0
        #passangers going to town A
        self.townAPassengers=0
        #passangers going to town B
        self.townBPassengers=0
        self.produce=0
        self.position=3
        
        