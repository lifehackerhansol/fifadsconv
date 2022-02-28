#!/usr/bin/env python3

# Requirements:
# pip3 install pillow

"""
fifadsconv.py
CLI frontend under CC0-1.0 public domain, by lifehackerhansol

all submodules are Copyright © 2022 Pk11, MIT license
"""


import argparse

from convert.dst2png import dst2png
from convert.tlb2png import tlb2png
from convert.tbf2png import tbf2png
from convert.png2tlb import png2tlb
from convert.png2tbf import png2tbf
from convert.png2dst import png2dst

parser = argparse.ArgumentParser(description="FIFA DS Image Converter")
subparser = parser.add_subparsers(title='Functions')
subparser.required = True

tlb2pngarg = subparser.add_parser(name="tlb2png", description="Converts a TLB file to image(s)")
tlb2pngarg.add_argument("input", metavar="in.tlb", type=argparse.FileType("rb"), help="input file")
tlb2pngarg.add_argument("--output", "-o", metavar="out.png", type=str, help="output name")
tlb2pngarg.add_argument("--alpha", "-a", action="store_true", help="make transparent pixel transparent instead of #FF00FF (may break reverse conversion)")
tlb2pngarg.set_defaults(func=tlb2png)

tbf2pngarg = subparser.add_parser(name="tbf2png", description="Converts a TBF file to an image")
tbf2pngarg.add_argument("input", metavar="in.tbf", type=argparse.FileType("rb"), help="input file")
tbf2pngarg.add_argument("--output", "-o", metavar="out.png", type=str, help="output name")
tbf2pngarg.set_defaults(func=tbf2png)

png2tlbarg = subparser.add_parser(name="png2tlb", description="Converts image(s) to a TLB")
png2tlbarg.add_argument("input", metavar="in.png", nargs="*", type=str, help="input image(s)")
png2tlbarg.add_argument("--output", "-o", metavar="out.tlb", type=argparse.FileType("wb"), help="output file")
png2tlbarg.add_argument("--colors", "-c", type=int, help="number of colors in the palette (only used if input is RGB(A))")
png2tlbarg.set_defaults(func=png2tlb)

png2tbfarg = subparser.add_parser(name='png2tbf', description="Converts an image to a TBF")
png2tbfarg.add_argument("input", metavar="in.png", type=str, help="input image")
png2tbfarg.add_argument("--output", "-o", metavar="out.tbf", type=argparse.FileType("wb"), help="output file")
png2tbfarg.set_defaults(func=png2tbf)

png2dstarg = subparser.add_parser(name='png2dst', description="Converts an image to a DST")
png2dstarg.add_argument("input", metavar="in.png", type=str, help="input image")
png2dstarg.add_argument("--output", "-o", metavar="out.dst", type=argparse.FileType("wb"), help="output file")
png2dstarg.set_defaults(func=png2dst)

dst2pngarg = subparser.add_parser(name='dst2png', description="Converts a DST file to image(s)")
dst2pngarg.add_argument("input", metavar="in.dst", type=argparse.FileType("rb"), help="input file")
dst2pngarg.add_argument("--output", "-o", metavar="out.png", type=str, help="output name")
dst2pngarg.set_defaults(func=dst2png)

args = parser.parse_args()
args.func(args)
