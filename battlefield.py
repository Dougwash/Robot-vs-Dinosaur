from robot import Robot
from dinosaur import Dinosaur


class BattleField:
    def __init__(self) -> None:
        # self.greeting ()
        # self.robot= Robot.choice_robot
        # self.dino = Dinosaur.choose_dino
        # self.run_game ()
        pass

    def greeting (self):
        print ('Welcome to Robot vs Dinosaur')
        
    def run_game (self):
        self.greeting (self)
        robo = Robot.choice_robot(self)
        dino = Dinosaur.choose_dino(self)
        Robot.rob_attack (self, robo)
        Dinosaur.Dino_attact (self,dino)
        # self.Fight (self)

    # def Fight (self):

    # def choose_rob_dino (self):
    #     Robot.choice_robot
    #     Dinosaur.
