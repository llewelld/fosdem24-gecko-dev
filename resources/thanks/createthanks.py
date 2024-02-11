#!/bin/python
# vim: tabstop=2 shiftwidth=2 expandtab

import drawsvg as dw
import csv
import random
import argparse
from math import cos, sin, pi, floor

# drawsvg 2.3.0
# https://pypi.org/project/drawsvg/
# https://github.com/cduck/drawsvg/blob/master/docs/index.md

class Thanks:
  def __init__(self):
    self.d = dw.Drawing(1280, 720, origin=(0, 0), id_prefix='thanks')
    self.grid = False

  def plot(self, infile, grid=False):
    with open(infile) as namesfile:
      names = csv.reader(namesfile)
      border = 40
      width = 1280 - 2 * border
      if grid:
        print('Using grid formation')
        count = 0
        xstep = 80
        ystep = 60
        jitter = 20
        for row in names:
          if len(row) > 1:
            distance = random.random() * jitter
            angle = random.random() * 2.0 * pi
            x = 2 * border + ((count * xstep) % width) + distance * cos(angle)
            y = 2 * border + ystep * floor(xstep * count / width) + distance * sin(angle)
            self.create_user(row[0].strip(), row[1].strip(), x, y, 0.2)
            count += 1
      else:
        print('Using random formation')
        height = 720 - 2 * border
        radius = 60
        coords = []
        total = 144
        count = 0
        for row in names:
          if len(row) > 1:
            name = row[0].strip()
            filename = row[1].strip()
            found = False
            while not found:
              x = border + random.random() * width
              y = border + random.random() * height
              found = True
              for count in range(len(coords)):
                if ((coords[count][0] - x)**2 + (coords[count][1] - y)**2) < radius**2:
                  found = False
                  break;
            coords.append((x, y))

            self.create_user(name, filename, x, y, 0.25)
            count += 1
            print(f'{count/total*100:.0f}%\r', end='', flush=True)
        print()

  def export(self, filename):
    self.d.save_svg(filename)
    print(f'Exported to {filename}')

  def create_user(self, name, imagename, x, y, scale=1.0):
    size = scale * 200
    half = size / 2
    fontsize = scale * 50
    group = dw.Group()
    group.append(dw.Image(x - half, y - half, size, size, f'masked/{imagename}', embed=True))
    group.append(dw.Text(f'{name}', font_size=fontsize, x=x, y=y + half + fontsize, text_anchor='middle', font_family='Sans Source Pro'))
    self.d.append(group)

if __name__ == '__main__':
  parser = argparse.ArgumentParser(
    prog='createthanks',
    description='Output an SVG image filled with avatars',
  )

  parser.add_argument('infile')
  parser.add_argument('outfile')
  parser.add_argument('--grid', action=argparse.BooleanOptionalAction)
  args = parser.parse_args()

  thanks = Thanks()
  thanks.plot(args.infile, args.grid)
  thanks.export(args.outfile)

