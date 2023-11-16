class player () :
    def __init__(self, name, age, goals,Nationality):
        self.name=name
        self.age=age
        self.goals=goals
        self.Nationality=Nationality

    def info(self):
        print("the player name is ",self.name,"his age is ",self.age)
        print("Number of goals in his career is ", self.goals, " and his Nationality is",self.Nationality)

P1 = player("Cristiano Ronaldo" , 38 , 864 , "Portugal")
P2 = player("Lionel Messi", 36, 821 ,"Argentina") 
P3 = player("Robert Lewandowski",35,610,"Poland")

P1.info()
P2.info()
P3.info()