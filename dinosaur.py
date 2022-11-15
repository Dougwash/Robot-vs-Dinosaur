class Dinosaur:
    def __init__(self, name, attact_power:int, health:int) -> None:
        
        self.name = name
        self.attact_power:attact_power
        self.health = health

    def Dino_attact (sef,robot):
        while robot.health > 0:
            robot.health - Dinosaur.attach_power
            if robot.health == 0:
                print("Dino wins")
            

    def t_rex (self):
        Dinosaur("T Rex", 50, 1000)

    def razo_back (self):
        Dinosaur("Razor Back", 25, 350 )

    def raptor (self):
        Dinosaur("Raptor", 75, 300)

    def choose_dino (self):
        dino_choice = input('Please choose your Dinosaur \n T Rex \n Razor Back \n Raptor \n: ')
        if dino_choice == "T Rex":
            Dinosaur.t_rex
            return

        if dino_choice == "Razor Back":
            Dinosaur.razo_back
            return

        if dino_choice == 'Raptor':
            Dinosaur.raptor
            return

        else:
            print("Please choose from the following list: \n T Rex \n Razor Back \n Raptor \n:")