from os import system
import sys

colors = [
  "white",
  "orange",
  "magenta",
  "aqua",
  "yellow",
  "lime",
  "purple",
  "blue",
  "red"
]

path = sys.argv[1]

for color in colors:
  print('"%s": "%s/%s",'%(color, path, color))