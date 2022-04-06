class FlyBehavior():
    def fly(self):
        raise NotImplementedError

class FlyWithWings(FlyBehavior):
    def fly(self):
        print('i am flying')

class FlyNoWay(FlyBehavior):
    def fly(self):
        print('i can not fly')

class QuackBehavior():
    def quack(self):
        raise NotImplementedError

class Quack(QuackBehavior):
    def quack(self):
        print('quack quack')

class MuteQuack(QuackBehavior):
    def quack(self):
        print('(...)')

class Squeak(QuackBehavior):
    def quack(self):
        print('squeak')


class Duck():
    def __init__(self):
        self.fly_behavior = None
        self.quack_behavior = None
    # class QuackBehavior():

    def set_fly_behavior(self, fly_b):
        self.fly_behavior = fly_b

    def set_quack_behavior(self, quack_b):
        self.quack_behavior = quack_b

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()

    def display(self):
        raise NotImplementedError

    def swim(self):
        print('all the ducks can float')


class ModelDuck(Duck):
    def __init__(self):
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = MuteQuack()
    def display(self):
        print('i am a model duck')

model = ModelDuck()
model.perform_fly()
model.perform_quack()
model.swim()
model.display()
model.set_fly_behavior(FlyWithWings())
model.perform_fly()
