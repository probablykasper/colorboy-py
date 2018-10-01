# colorboy

Easily add color to your strings

# Installation
pip install colorboy

# Usage
```python
import colorboy as cb
print(cb.cyan('Globgogabgalab'))

from colorboy import cyan, red # import a specific colors, bg_colors and styles
print(cyan('Piz')+red('za'))

from colorboy import * # import all colors, bg_colors and styles
print(green('Mayonnaise'))

from colorboy.colors import * # import all colors
print(red('EDEN'))
from colorboy.bg_colors import * # import all bg_colors
print(black_bg('Stephen'))
from colorboy.styles import * # import all styles
print(bright('Crywolf'))
```

# Colors
These are all the color functions available through colorboy:
```python
# colors - available by importing colorboy or colorboy.colors
black
red
green
yellow
blue
magenta
cyan
white

# bg_colors - available by importing colorboy or colorboy.bg_colors
black_bg
red_bg
green_bg
yellow_bg
blue_bg
magenta_bg
cyan_bg
white_bg

# styles - available by importing colorboy or colorboy.styles
dim
bright

```

# Dev Instructions
### Installation
1. Install Python (Python 3.7 works, probably other versions too)
2. Install [Poetry](https://poetry.eustace.io). Poetry is used to manage dependencies, the virtual environment and publishing to PyPI, so it's worth learning.
3. Run `poetry install` to install Python package dependencies.

For VSCode to detect the Python virtual environment that Poetry creates, I ran `poetry config settings.virtualenvs.in-project true`. This command makes Poetry create your Python virtual environment inside the project folder. Now, you can set the `python.pythonPath` setting to `${workspaceFolder}/.venv/bin/python` in your workspace settings (or global if you want this to be the default).