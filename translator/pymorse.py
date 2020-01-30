import json


class MorseTranslator:
    """
    De- and Encoding suite for Morse Code.

    Translate clear text strings or file contents into morse code and vice versa.

    Attributes
    ----------
    char2morse : dict
        Mapping of ASCII characters to morse code.
    morse2char : dict
        Mapping of morse code to ASCII characters

    Methods
    -------
    encode(char)
        Encode string of ASCII character into morse code.
    decode(char)
        Decode morse code to ASCII characters.
    encode_document(input_path, output_path=None)
        Read file and encode content into morse code.
    decode_document(input_path, output_path=None)
        Read file and decode content into ASCII characters.

    """
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
        """
        Encode string of ASCII characters into morse code.

        Parameters
        ----------
        string : str
            Input string to be encoded. Whitespace will be converted to a forward slash.

        Returns
        -------
        out : str
            Encoded input string.

        Raises
        ------
        Value Error
            If a character of the input string is not a valid ASCII character.

        """
        out = ' '.join(self.__encode_char(s) for s in string.upper())
        return out.strip()

    def __encode_char(self, char):
        try:
            out = self.char2morse[char]
            return out
        except KeyError:
            raise ValueError(f"{char} is not a valid ASCII character.")

    def decode(self, string):
        """
        Decode string of morse code into ASCII characters.

        Parameters
        ----------
        string : str
            Input string to be decoded. End of words should be declared by a forward slash.

        Returns
        -------
        out : str
            Decoded input string.

        Raises
        ------
        ValueError
            If a provided sequence is not a valid morse code.

        """
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
        """
        Read content of file and decode morse code into clear text.

        Parameters
        ----------
        input_path : str
            Path to morse encoded file.
        output_path : str or None
            Path to write result to. Defaults to None, in this case no file is written.

        Returns
        -------
        out : str
            Decoded document content.


        Raises
        ------
        ValueError
            If a provided sequence in the input document is not a valid morse code.

        """
        out = ""
        with open(input_path) as f:
            for line in f.read().splitlines():
                out += self.decode(line) + "\n"

        self.__write_if_path_provided(out, output_path)
        return out

    def encode_document(self, input_path, output_path=None):
        """
        Read content of file and encode into morse code.

        Parameters
        ----------
        input_path : str
            Path to file.
        output_path : str or None
            Path to write result to. Defaults to None, in this case no file is written.

        Returns
        -------
        out : str
            Encoded document content.

        Raises
        ------
        ValueError
            If a character in the document is not in the ASCII set.

        """

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

