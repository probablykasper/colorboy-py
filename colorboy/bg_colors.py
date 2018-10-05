import colorama
colorama.init()

def black_bg(text):     return colorama.Back.BLACK   +text+colorama.Back.RESET
def red_bg(text):       return colorama.Back.RED     +text+colorama.Back.RESET
def green_bg(text):     return colorama.Back.GREEN   +text+colorama.Back.RESET
def yellow_bg(text):    return colorama.Back.YELLOW  +text+colorama.Back.RESET
def blue_bg(text):      return colorama.Back.BLUE    +text+colorama.Back.RESET
def magenta_bg(text):   return colorama.Back.MAGENTA +text+colorama.Back.RESET
def cyan_bg(text):      return colorama.Back.CYAN    +text+colorama.Back.RESET
def white_bg(text):     return colorama.Back.WHITE   +text+colorama.Back.RESET

__all__ = [
    'black_bg',
    'red_bg',
    'green_bg',
    'yellow_bg',
    'blue_bg',
    'magenta_bg',
    'cyan_bg',
    'white_bg'
]