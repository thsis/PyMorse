"""
Test Suite for `MorseTranslator`
"""
import os
import unittest
from translator.pymorse import MorseTranslator


class TestMorseTranslator(unittest.TestCase):
    """
    Test single input strings as well as phrases.
    """

    def setUp(self):
        self.translator = MorseTranslator()

        with open(os.path.join("tests", "morse_single.txt")) as ms:
            self.morse_single = ms.read().splitlines()

        with open(os.path.join("tests", "text_single.txt")) as ts:
            self.text_single = ts.read().splitlines()

        with open(os.path.join("tests", "morse_phrase.txt")) as mp:
            self.morse_phrase = mp.read().splitlines()

        with open(os.path.join("tests", "text_phrase.txt")) as tp:
            self.text_phrase = tp.read().splitlines()

    def test_decode_single(self):
        for input_string, answer in zip(self.morse_single, self.text_single):
            with self.subTest(input_string=input_string, answer=answer):
                output_string = self.translator.decode(input_string)
                self.assertEqual(output_string, answer.upper())

    def test_encode_single(self):
        for input_string, answer in zip(self.text_single, self.morse_single):
            with self.subTest(input_string=input_string, answer=answer):
                output_string = self.translator.encode(input_string)
                self.assertEqual(output_string, answer)

    def test_decode_phrase(self):
        for input_string, answer in zip(self.morse_phrase, self.text_phrase):
            with self.subTest(input_string=input_string, answer=answer):
                output_string = self.translator.decode(input_string)
                self.assertEqual(output_string, answer.upper())

    def test_encode_phrase(self):
        for input_string, answer in zip(self.text_phrase, self.morse_phrase):
            with self.subTest(input_string=input_string, answer=answer):
                output_string = self.translator.encode(input_string)
                self.assertEqual(output_string, answer)

    def test_encode_failures(self):
        for char in list("äöüáéíóúâêîôûàèìòùãñ".upper()):
            with self.subTest(char=char):
                self.assertRaises(ValueError, self.translator.encode, char)

    def test_decode_failures(self):
        for code in ["---...---", "-.-..--", "......", "------"]:
            with self.subTest(code=code):
                self.assertRaises(ValueError, self.translator.decode, code)

    def test_decode_document(self):
        input_files = [os.path.join("tests", f) for f in ("morse_single.txt", "morse_phrase.txt")]
        output_files = [os.path.join("tests", f) for f in ("text_single.txt", "text_phrase.txt")]

        for input_file, answer_file in zip(input_files, output_files):
            with open(answer_file) as f:
                answer = f.read()

            with self.subTest(filepath=input_file, answer=answer):
                output = self.translator.decode_document(input_file)
                self.assertEqual(output, answer.upper())

    def test_encode_document(self):
        input_files = [os.path.join("tests", f) for f in ("text_single.txt", "text_phrase.txt")]
        output_files = [os.path.join("tests", f) for f in ("morse_single.txt", "morse_phrase.txt")]

        for input_file, answer_file in zip(input_files, output_files):
            with open(answer_file) as f:
                answer = f.read()

            with self.subTest(filepath=input_file, answer=answer):
                output = self.translator.encode_document(input_file)
                self.assertEqual(output, answer)



if __name__ == "__main__":
    unittest.main()