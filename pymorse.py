import argparse
from translator.pymorse import MorseTranslator


def encode(args):
    translator = MorseTranslator()
    if args.file:
        res = translator.encode_document(args.input)
    else:
        res = translator.encode(args.input)
    print(res)


def decode(args):
    translator = MorseTranslator()
    if args.file:
        res = translator.decode_document(args.input)
    else:
        res = translator.decode(args.input)
    print(res)


parent_parser = argparse.ArgumentParser(description="Convert clear text to morse code or vice versa")
subparsers = parent_parser.add_subparsers(title="actions")
parser_encode = subparsers.add_parser("encode",
                                      add_help=False,
                                      description="The encode parser",
                                      help="encode clear text to morse code")
parser_encode.add_argument("input", help="string or file to be converted")
parser_encode.add_argument("-f", "--file", action="store_true", default=False, help="use file")
parser_encode.set_defaults(func=encode)
parser_decode = subparsers.add_parser("decode",
                                      add_help=False,
                                      description="The decode parser",
                                      help="decode morse code into clear text")
parser_decode.add_argument("input", help="string or file to be converted")
parser_decode.add_argument("-f", "--file", action="store_true", default=False, help="use file")
parser_decode.set_defaults(func=decode)
args = parent_parser.parse_args()
args.func(args)