import random
class RandomDiceGenerator():
    """
    Represents a random dice roll generator which has an amount of dice
    and a number of sides per dices.
    Includes methods to generate the rolls and getters and setters.
    also includes a result and a sum variable which represent the results of each roll
    """
    def __init__(self, amount=1, sides=1):
        self.amount = amount
        self.sides = sides
        self.result = {
            "rolls" : [],
            "score" : 0
            }
        

    def set_sides(self, sides=6):
        """
        Function to change the amount of sides pper dice
        
        Args:
            sides (int, optional): # of sides per dice. Defaults to 6.
        """
        self.sides = sides


    def set_amount(self, amount=1):
        """
        Function to set the amount of dice to roll
        
        Args:
            amount (int, optional): # of dice. Defaults to 1.
        """
        self.amount = amount

        
    def roll_dice(self):
        """
        Function that generates random dice rolls.
        
        """       
        for _ in range(self.amount): # for each side:
            self.result["rolls"].append(random.randint(1,self.sides))
        self.result["score"] = sum(self.result["rolls"])


    def get_results(self):
        """
        Returns a results objects.
        
        Returns:
            [dict]: result dictionary with the 
        """
        return self.result
    
        
        


