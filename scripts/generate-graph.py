"""
Constructs a graph via matplotlib from a CSV file.

"""

import csv
import argparse
import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path

parser = argparse.ArgumentParser(description='Constructs a graph via matplotlib from a CSV file.')
parser.add_argument('input', type=str, help='The filepath to the CSV file containing the graph data.')
parser.add_argument('--title', type=str, help='The title of the graph.')
parser.add_argument('--label', type=str, help='The label of the plotted curve.')
parser.add_argument('--colour', type=str, help='The colour of the graph.', default='blue')
parser.add_argument('--xlabel', type=str, help='The label on the x-axis.', default='x')
parser.add_argument('--ylabel', type=str, help='The label on the y-axis.', default='y')
parser.add_argument('--xscale', type=str, help='The x-axis scale to apply.', default='linear')
parser.add_argument('--yscale', type=str, help='The y-axis scale to apply.', default='linear')
parser.add_argument('--axhline', type=float, help='The horizontal axis line.')
parser.add_argument('--axhline-style', type=str, help='The style of the horizontal axis line.', default='-')
parser.add_argument('--axhline-colour', type=str, help='The colour of the horizontal axis line.', default='red')
parser.add_argument('--legend', dest='legend', help='Enable the legend.', action='store_true')
parser.add_argument('--legend-loc', type=str, help='The location of the legend.', default='upper right')
parser.add_argument('--export-tikz', dest='export_tikz', help='Export the graph as a LaTeX file using PGF/TikZ.', action='store_true')
parser.set_defaults(legend=False)
parser.set_defaults(export_tikz=False)
args = parser.parse_args()

input_filepath = Path(args.input)
if input_filepath.exists() and input_filepath.is_file():
    if args.axhline is not None:
        plt.axhline(y=args.axhline, color=args.axhline_colour, linestyle=args.axhline_style)
    
    x, y = np.loadtxt(input_filepath, delimiter=',', unpack=True)
    plt.plot(x, y, label=args.label, color=args.colour)
    if args.title is not None:
        plt.title(args.title)
    
    plt.xlabel(args.xlabel)
    plt.ylabel(args.ylabel)
    plt.xscale(args.xscale)
    plt.yscale(args.yscale)

    if args.legend:
        plt.legend(loc=args.legend_loc)
    
    plt.show()
else:
    print('Error: The provided CSV graph data file does not exist or is not a file.')
    