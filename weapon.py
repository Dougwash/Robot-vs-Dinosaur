class Weapon:
    def __init__(self, name, attact_power:int) -> None:
        
        self.name=name
        self.attact_power = attact_power

   
    def ray_gun (self):
        self.attact_power = 150
        self.name = "Ray Gun"
        
    def sonic_boom (self):
        self.name = 'Sonic Boom'
        self.attact_power = 200

    def saw_hands (self):
        self.name = "Saw Hands"
        self.attact_power = 75

    def choose_weapon (self):
       choice = input('choose your Robot: \n Ray Gun \n Sonic Boom \n Saw Hands \n:')
       if choice == 'Ray Gun':
        Weapon.ray_gun ()

       if choice == 'Sonic Boom':
        Weapon.sonic_boom ()

       if choice == 'Saw Hands':
        Weapon.saw_hands ()
       else:
        print('please select from one of the following choices \n Ray Gun \n Sonic Boom \n Saw Hands \n: ')
