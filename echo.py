#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "Andrew Fillenwarth \
            special thanks to Chris Warren and Janell!"


import sys
import argparse


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    parser = argparse.ArgumentParser(
       description="Perform transformation on input text.")
    parser.add_argument('text', help='text to be manipulated')
    parser.add_argument(
        '-u', '--upper', help='convert text to uppercase', action='store_true')
    parser.add_argument(
        '-l', '--lower', help='convert text to lowercase', action='store_true')
    parser.add_argument(
        '-t', '--title', help='convert text to titlecase', action='store_true')
    return parser


def main(args):
    parser = create_parser()
    ns = parser.parse_args(args)
    text = ns.text
    result = ''
    if not ns:
        parser.print_usage()
        sys.exit(1)
    if len(args) == 1:
        result = text
    if ns.upper:
        result = text.upper()
    if ns.lower:
        result = text.lower()
    if ns.title:
        result = text.title()
    return print(result)


if __name__ == '__main__':
    main(sys.argv[1:])
