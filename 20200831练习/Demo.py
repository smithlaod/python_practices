class Person(object):
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("我的名字是：", self.name)

    def walk(self):
        print("{}在走路".format(self.name))


class Chinese(Person):
    def __init__(self, name, msg="我爱中国"):
        Person.__init__(self, name)
        self.msg = msg

    def say(self):
        print("我是中国人：", self.msg)


p = Person("Tom")
p.talk()
p.walk()

c = Chinese("狼王")
c.say()
