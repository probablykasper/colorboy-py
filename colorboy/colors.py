import colorama
colorama.init()

def black(text):        return colorama.Fore.BLACK   +text+colorama.Fore.RESET
def red(text):          return colorama.Fore.RED     +text+colorama.Fore.RESET
def green(text):        return colorama.Fore.GREEN   +text+colorama.Fore.RESET
def yellow(text):       return colorama.Fore.YELLOW  +text+colorama.Fore.RESET
def blue(text):         return colorama.Fore.BLUE    +text+colorama.Fore.RESET
def magenta(text):      return colorama.Fore.MAGENTA +text+colorama.Fore.RESET
def cyan(text):         return colorama.Fore.CYAN    +text+colorama.Fore.RESET
def white(text):        return colorama.Fore.WHITE   +text+colorama.Fore.RESET

__all__ = [
    'black',
    'red',
    'green',
    'yellow',
    'blue',
    'magenta',
    'cyan',
    'white'
]