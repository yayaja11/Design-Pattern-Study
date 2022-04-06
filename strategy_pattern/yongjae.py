class HitBehavior():
    def hit(self):
        raise NotImplementedError

class HitWithFist(HitBehavior):
    def hit(self):
        print('i hit yongjae with fist ')

class HitNo(HitBehavior):
    def hit(self):
        print('i didn\'t hit yongjae ㅠㅠ')

class TortureBehavior():
    def torture(self):
        raise NotImplementedError

class Water(TortureBehavior):
    def torture(self):
        print('Yongjae drank 100L Water Wow!')

class Food(TortureBehavior):
    def torture(self):
        print('Yongjae ate 100 hamburgers Wow!')

class Breath(TortureBehavior):
    def torture(self):
        print('Yongjae didn\'t breath for 100 seconds Wow!')


class Yongjae():
    def __init__(self):
        self.hit_behavior = None
        self.torture_behavior = None
    # class QuackBehavior():

    def set_hit_behavior(self, hit_b):
        self.hit_behavior = hit_b

    def set_torture_behavior(self, torture_b):
        self.torture_behavior = torture_b

    def perform_hit(self):
        self.hit_behavior.hit()

    def perform_torture(self):
        self.torture_behavior.torture()

    def display(self):
        raise NotImplementedError


class firstday(Yongjae):
    def __init__(self):
        self.hit_behavior = HitWithFist()
        self.torture_behavior = Breath()


happy = firstday()
happy.perform_hit()
happy.perform_torture()

happy.set_hit_behavior(HitNo())
happy.perform_hit()

happy.set_torture_behavior(Food())
happy.perform_torture()
