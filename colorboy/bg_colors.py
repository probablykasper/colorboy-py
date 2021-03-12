def generate(code):
  return '\033[' + str(code) + 'm'

reset_bg = generate(49)

def black_bg(text):   return generate(40)+text+reset_bg
def red_bg(text):     return generate(41)+text+reset_bg
def green_bg(text):   return generate(42)+text+reset_bg
def yellow_bg(text):  return generate(43)+text+reset_bg
def blue_bg(text):    return generate(44)+text+reset_bg
def magenta_bg(text): return generate(45)+text+reset_bg
def cyan_bg(text):    return generate(46)+text+reset_bg
def white_bg(text):   return generate(47)+text+reset_bg

__all__ = [
    'black_bg',
    'red_bg',
    'green_bg',
    'yellow_bg',
    'blue_bg',
    'magenta_bg',
    'cyan_bg',
    'white_bg',
]
