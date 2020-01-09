from argparse import ArgumentParser
from translator.pymorse import MorseTranslator

parser = argparse.ArgumentParser(prog="pymorse")
parser.add_argument("-f", "--file", help="input file")
subparsers = parser.add_subparsers(help="sub-command help")

# TODO: Add subparsers to the main-file that make it possible to
#  * encode an input string
#  * encode a file
#  * decode an input string
#  * decode an input_file