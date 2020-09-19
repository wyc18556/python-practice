class Player:
    def __init__(self, name, hp):
        self.__name = name
        self.hp = hp

    def to_string(self):
        print(f"name={self.__name},hp={self.hp}")

    def set_name(self, new_name):
        self.__name = new_name


tom = Player("tom", 80)
jerry = Player("jerry", 99)

tom.to_string()
tom.set_name("tom_up")
# 以 '__' 开头的属性必须通过方法才能修改
tom.__name = "tom_down"
tom.hp = 95
tom.to_string()
jerry.to_string()


class Monster:
    """怪物类"""

    def __init__(self, hp=500):
        self.hp = hp

    def say(self):
        if self.hp >= 300:
            print("i'm ok, bang bang bang")
        else:
            print("i'm bad")


class Animal(Monster):
    """普通怪物"""

    def __init__(self, hp=100):
        super().__init__(hp)


class Boss(Monster):
    """BOSS"""

    def __init__(self, hp=1000):
        super().__init__(hp)

    def say(self):
        print("i'm boss, i must beat you")


animal = Animal(80)
animal.say()
monster = Monster()
monster.say()
boss = Boss(900)
boss.say()

print(isinstance(animal, Monster))
print(isinstance(animal, Boss))
