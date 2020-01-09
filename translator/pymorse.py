import json


class MorseTranslator:
    def __init__(self):
        self.char2morse = self.__get_char2morse()
        self.morse2char = self.__get_morse2char()

    @staticmethod
    def __get_char2morse():
        with open("morse.json") as morse:
            char2morse = json.load(morse)
            char2morse[" "] = "/"
        return char2morse

    @staticmethod
    def __get_morse2char():
        with open("morse.json") as morse:
            char2morse = json.load(morse)
            morse2char = {v: k for k, v in char2morse.items()}
            morse2char["/"] = " "
            morse2char[" "] = ""
        return morse2char

    def encode(self, string):
        out = ' '.join(self.__encode_char(s) for s in string.upper())
        return out.strip()

    def __encode_char(self, char):
        try:
            out = self.char2morse[char]
            return out
        except KeyError:
            raise ValueError(f"{char} is not a valid ASCII character.")

    def decode(self, string):
        words = string.split("/")
        out = ' '.join(self.__decode_word(word) for word in words)
        return out.strip()

    def __decode_code(self, code):
        try:
            out = self.morse2char[code]
            return out
        except KeyError:
            raise ValueError(f"{code} is not a valid morse code.")

    def __decode_word(self, word):
        chars = word.split(" ")
        out = ''.join(self.__decode_code(c) for c in chars)
        return out

    def decode_document(self, input_path, output_path=None):
        out = ""
        with open(input_path) as f:
            for line in f.read().splitlines():
                out += self.decode(line) + "\n"

        self.__write_if_path_provided(out, output_path)
        return out

    def encode_document(self, input_path, output_path=None):
        out = ""
        with open(input_path) as f:
            for line in f.read().splitlines():
                out += self.encode(line) + "\n"
        self.__write_if_path_provided(out, output_path)
        return out

    @staticmethod
    def __write_if_path_provided(content, path):
        if path:
            with open(path, "w") as f:
                f.write(content)

