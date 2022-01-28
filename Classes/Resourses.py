class Resourses:
    def __init__(self, money = 1000, wood = 200, stone = 200, iron = 50, med = 70):
        self.money = money
        self.wood = wood
        self.stone = stone
        self.iron = iron
        self.med = med

    def __str__(self):
        return str(vars(self))

    def __add__(self, other):
        res = [self_ + other_ for self_, other_ in zip(vars(self).values(), vars(other).values())]
        return Resourses(*res)

    def __sub__(self, other):
        res = [self_ - other_ for self_, other_ in zip(vars(self).values(), vars(other).values())]
        return Resourses(*res)

    def __lt__(self, other):
        for self_, other_ in zip(vars(self).values(), vars(other).values()):
            if self_ < other_:
                return True
        return False

    def __gt__(self, other):
        for self_, other_ in zip(vars(self).values(), vars(other).values()):
            if self_ < other_:
                return False
        return True

    def __le__(self, other):
        for self_, other_ in zip(vars(self).values(), vars(other).values()):
            if self_ <= other_:
                return True
        return False

    def __ge__(self, other):
        for self_, other_ in zip(vars(self).values(), vars(other).values()):
            if self_ <= other_:
                return False
        return True

    def __eq__(self, other):
        for self_, other_ in zip(vars(self).values(), vars(other).values()):
            if self_ != other_:
                return False
        return True

    def __ne__(self, other):
        return not (self == other)