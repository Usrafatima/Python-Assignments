class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return number * self.factor


mult = Multiplier(5)


print(callable(mult))  


result = mult(10)
print(result)  
