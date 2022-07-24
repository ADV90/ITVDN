class English:
    def greeting(self):
        return 'Hello'


class Espanol:
    def greeting(self):
        return 'Ola!'


friend = English()
amigo = Espanol()


def hello_friend():
    p = friend
    print(p.greeting())
    p = amigo
    print(p.greeting())


hello_friend()
