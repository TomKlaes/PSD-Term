import random
class randomintgen:

    def gen(self,amount,minRange,maxRange):
        for item in amount,minRange,maxRange:
        	if not isinstance(item, int) :
		        raise TypeError('Please make sure all inputs are integers')
        if amount > 100:
            raise TypeError("Please lower your amount")
        result=random.choices(range(minRange,maxRange), weights = None, k = amount)
        if isinstance(result,list):
            if len(result)==amount:
                return result 
        else:
            raise TypeError("Unexpected output format")

#Testing testing testing