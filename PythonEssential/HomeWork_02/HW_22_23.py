class GraphicObject(object):

    _dimensions = 2
    _display = True
    _background = 'white'
    _style = 'custom'
    _position_X = 0
    _position_Y = 0
    _width = 1
    _height = 1

    def __init__(self, dim , display, background , style, position_x, position_y, width, height):
        self._dimensions = dim
        self._display = display
        self._background = background
        self._style = style
        self._position_X = position_x
        self._position_Y = position_y
        self._width = width
        self._height = height

    def __str__(self):
        if self._display:
            print(f'Graphic Object: {self._dimensions}D, background is {self._background},{self._style} '
                  f'style,geometry {self._width}x{self._height} ')
        else:
            print('Impossible to display an object')

    def draw(self):
        self.__str__()

    def move(self, x, y):
        print(f'Initial position:{self._position_X}, {self._position_Y}')
        self._position_X = x
        self._position_Y = y
        print(f'Position changed to:{self._position_X}, {self._position_Y}')


class Rectangle(GraphicObject):

    def __str__(self):
        if self._display:
            print(f'Rectangle : {self._dimensions}D, background is {self._background},{self._style} style, '
                  f'geometry {self._width}x{self._height} ')
        else:
            print('Impossible to display an object')

    def draw(self):
        self.__str__()


class Clickable(object):

    _action = 'Do something'
    _trigger = 'Mouse click'
    _args = []

    def __init__(self, action, args, trigger):
        self._action = action
        self._trigger = trigger
        self._args = args

    def on_trigger(self):
        print('Waiting for a trigger')
        while True:
            trigger = input('Trigger is:')
            if trigger.casefold() == self._trigger.casefold():
                if isinstance(self._action, str):
                    print(f'{self._action} execution started!')
                else:
                    self._action(self._args)
                break
            else:
                print('Waiting for a needed trigger...')


class Button(Rectangle, Clickable):

    def __init__(self,dim, display, background, style, position_X, position_Y, width, height, action, args=[],
                 trigger='Click'):
        Rectangle.__init__(self, dim, display, background , style, position_X, position_Y, width, height)
        Clickable.__init__(self, action, args, trigger)


if __name__ == '__main__':

    rect = Rectangle(3, True, 'green', 'custom', 0, 0, 20, 50)
    rect.draw()
    rect.move(40, 50)

    button = Button(3, True, 'green', 'custom', 0, 0, 20, 50, rect.move, [60, 3], 'Click')
    button.draw()
    button.move(30, 20)
    # button.on_trigger()

    rect.move(0, 0)

    print(Button.__mro__)
    print(Rectangle.__mro__)
