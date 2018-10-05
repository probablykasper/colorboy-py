import colorama
colorama.init()

def dim(text):          return colorama.Style.DIM    +text+colorama.Style.NORMAL
def bright(text):       return colorama.Style.BRIGHT +text+colorama.Style.NORMAL

__all__ = [
    'dim',
    'bright'
]