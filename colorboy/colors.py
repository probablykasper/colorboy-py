def generate(code):
  return '\033[' + str(code) + 'm'

reset = generate(39)

def black(text):    return generate(30)+text+reset
def red(text):      return generate(31)+text+reset
def green(text):    return generate(32)+text+reset
def yellow(text):   return generate(33)+text+reset
def blue(text):     return generate(34)+text+reset
def magenta(text):  return generate(35)+text+reset
def cyan(text):     return generate(36)+text+reset
def white(text):    return generate(37)+text+reset

__all__ = [
    'black',
    'red',
    'green',
    'yellow',
    'blue',
    'magenta',
    'cyan',
    'white',
]
