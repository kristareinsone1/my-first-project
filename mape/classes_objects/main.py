class Dog:
    def __init__(self,name):
        self.name = name

    def introduce (self):   
        print(f"Čau,mani sauc {self.name}!")

    def  walk(self,steps):
        print(f"{self.name} nostaigāja {steps} soļus.")  

dog_1 = Dog ("Reksis")
dog_2= Dog ("Luna")    

dog_1.introduce()
dog_1.walk(10)
dog_1.name = "Lūsis"
dog_1.introduce()