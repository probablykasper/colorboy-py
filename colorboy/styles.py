def generate(code):
  return '\033[' + str(code) + 'm'

normal_style = generate(22)

def bright(text): return generate(1)+text+normal_style
def dim(text):    return generate(2)+text+normal_style

__all__ = [
    'bright',
    'dim',
]
