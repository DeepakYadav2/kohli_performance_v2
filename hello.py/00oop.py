class SuperHeroes():
     def __init__(self,name,superpower):
        self.name=name
        self.superpower= superpower

     def get_superpower(self):
         print(f"I am {self.name} and my power is {self.superpower}")

ironMan =SuperHeroes(
    name="Iron Man",
 superpower="suit"
)           

ironMan.get_superpower()