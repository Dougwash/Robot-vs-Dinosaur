from weapon import Weapon

class Robot:
    def __init__(self, name, health:int,) -> None:

        self.name = name
        self.health = health
        self.active_weapon = Weapon



    def rob_attack (self, dino):
        while dino.health > 0 :
            dino.health - Robot.weapon.active
        if dino.health == 0:
            print ("robot wins Battle")
            
        

    def rob_mike (self):
        Robot("Mike",100)
        Weapon.choose_weapon

    def rob_frank (self):
        Robot('Frank',125)
        Weapon.choose_weapon

    def rob_jon(self):
        Robot('Jon', 200)
        Weapon.choose_weapon

    def choice_robot (self):
        robot_choice = input ('please choose your robot: \n Mike \n Frank \n Jon \n: ')
        if robot_choice == "Mike":
            Robot.rob_mike
            return
        if robot_choice == "Frank":
             Robot.rob_frank
             return

        if robot_choice == "Jon":
            Robot.rob_jon
            return

        else:
            print('Please choose form the list: \n Mike \n Frank \n Jon \n:')

        pass
