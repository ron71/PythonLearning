"""Each player we have its name and no of lives and their score"""


class Player:

    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0

    def _get_name(self):
        return self.name

    def _get_lives(self):
        return self.lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives cannot be negative")
            self._lives = 0

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level > self._level:
            self._score += 1000 * (level - self._level)
            self._level = level
        else:
            if level >= 1:
                self._score -= 1000 * (self._level - level)
                self._level = level

    lives = property(_get_lives, _set_lives)
    level = property(_get_level, _set_level)

    @property               # this is an alternative and more used way for providing property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    # We must keep the property name different from all the data attribute of the class
    # property(fget=None, fset=None, fdel=None, doc=None) -> property attribute
    #
    # fget is a function to be used for getting an attribute value, and likewise
    # fset is a function for setting, and fdel a function for del'ing, an
    # attribute.

    def __str__(self):
        """ It is a built-in function which can be used to display details of an object"""

        return "Name : {0.name}, Lives : {0._lives}, Level : {0.level}, Score : {0.score}".format(self)
    
