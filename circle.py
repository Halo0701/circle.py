class Circle():
    #class object attribute
    pi = 3.14
    def __init__(self,yaricap=1):
        self.yaricap = yaricap
    #methods
    def cevre_cal(self):
        return 2*self.pi*self.yaricap
    def alan_cal(self):
        return self.pi*(self.yaricap**2)
    
c1 = Circle()
c2 = Circle()

print(f'c1 alan: {c1.alan_cal()} çevre: {c1.cevre_cal()}')
print(f'c1 alan: {c2.alan_cal()} çevre: {c2.cevre_cal()}')
