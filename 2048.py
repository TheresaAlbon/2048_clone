from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.core.window import Window
import random
import math


class GameBoard(GridLayout):

    # Override the initialization
    def __init__(self, **kwargs):
    
        # Call the super constructor and then set the number of columns
        super(GameBoard, self).__init__(**kwargs)
        self.cols = 4
        self.rows = 4

        # Add the grid of blocks (first row)
        self.c11 = Label(text='11')
        self.add_widget(self.c11)
        self.c12 = Label(text='12')
        self.add_widget(self.c12)
        self.c13 = Label(text='13')
        self.add_widget(self.c13)
        self.c14 = Label(text='14')
        self.add_widget(self.c14)

        # Add the grid of blocks (second row)
        self.c21 = Label(text='21')
        self.add_widget(self.c21)
        self.c22 = Label(text='22')
        self.add_widget(self.c22)
        self.c23 = Label(text='23')
        self.add_widget(self.c23)
        self.c24 = Label(text='24')
        self.add_widget(self.c24)

        # Add the grid of blocks (third row)
        self.c31 = Label(text='31')
        self.add_widget(self.c31)
        self.c32 = Label(text='32')
        self.add_widget(self.c32)
        self.c33 = Label(text='33')
        self.add_widget(self.c33)
        self.c34 = Label(text='34')
        self.add_widget(self.c34)

        # Add the grid of blocks (fourth row)
        self.c41 = Label(text='41')
        self.add_widget(self.c41)
        self.c42 = Label(text='42')
        self.add_widget(self.c42)
        self.c43 = Label(text='43')
        self.add_widget(self.c43)
        self.c44 = Label(text='44')
        self.add_widget(self.c44)

        # Add the keyboard listener
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self, 'text')
        if self._keyboard.widget:
            pass
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    # Function for releasing the keyboard
    def _keyboard_closed(self):
        
        print('My keyboard has been closed!')
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None
    
    # Function for listening to the key presses
    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        
        # Keycode is composed of an integer + a string
        print('The key', keycode, 'have been pressed')
        
        # If we hit escape, release the keyboard
        if keycode[1] == 'escape':
            keyboard.release()
        
        # Return True to accept the key. Otherwise, it will be used by the system.
        return True

class Run2048(App):
    
    def build(self):
        return GameBoard()


if __name__ == '__main__':
    Run2048().run()