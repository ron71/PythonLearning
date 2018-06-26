import random


class Enemy(object):
    """It is the super class for various enemies added in game."""

    def __init__(self, name='Enemy', hit_points=0, lives=1):
        self._name = name
        self._hit_points = hit_points
        self._lives = lives
        self._alive = True

    def take_damage(self, damage):
        remaining_points = self._hit_points - damage
        if remaining_points >= 0:
            self._hit_points = remaining_points
            print("I took {} points damage and have {} left.".format(damage, self._hit_points))
        else:
            self._lives -= 1
            if self._lives > 0:
                print("{0._name} lost a life.".format(self))
            else:
                self._alive = False
                print("{0._name} is dead.".format(self))

    def __str__(self):
        return "Name : {0._name}\tHit_points : {0._hit_points}\tLives : {0._lives}".format(self)


# Inheriting Enemy Class :
class Troll(Enemy):
    """Every class which is independent is inherited from object class.
    In python 3 'class Enemy(object)' and 'class Enemy' are same.
    But in Python 2 they both resemble different style of class.
    So we should not change the class declaration in Python 2 written codes
    NOTE : Python supports multiple inheritance too"""
    def __init__(self, name):
        """ we will just pass the name of the troll and rest will be initialised by parent constructor called by super
         keyword and we aill customise the default values for this class"""
        # Enemy.__init__(self, name=name, lives=1, hit_points=23)
        # Above line can also be written using super
        # super(Troll, self).__init__(name=name, hit_points=23, lives=1)
        # super can also be written in following way
        super().__init__(name=name, hit_points=23, lives=1)
    # pass
    # pass keyword is used when we don't want to add any thing in the class

    def grunt(self):
        print("Me {0._name}. {0._name} stomp you.".format(self))


class Vampire(Enemy):
    def __init__(self, name):
        super().__init__(name=name, hit_points=12, lives=3)

    # Override

    def dodge(self):
        """ Vampire has one chance to dodge the attack. If charm =3 then we will dodge"""
        charm = random.randint(1, 3)
        if charm == 3:
            print("***********{0._name} dodges the attack.*************".format(self))
            return True
        return False

    def take_damage(self, damage):
        if not self.dodge():
            super().take_damage(damage=damage)
            

""" Now we can observe all the members are public so to make the look private we gonna add '_' at beginning of them 
using refactor tool.
Although we did using refactor, we still have error as the print statements with replacement fields still have
wrong names.
So to correct it we will take help of the concept of regular expressions (regx) anf find and replace tool (ctrl + r)of intelLiJ.
In toolbar first check the Regex option. Then type: '(\{\d\.)' where d means digits. 
And in replace string field type type : '$0_.' This means the zero will we replaced by '0_'

"""

# Hierarchy Inheritance


class VampireKing(Vampire):

    def __init__(self, name):
        super().__init__(name=name)
        self._hit_points = 140

    def take_damage(self, damage):
        super().take_damage(damage//4)
