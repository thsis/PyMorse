# PyMorse: Morse Code in Python

It does exactly what you think it does. 
Did you ever want to learn morse code but never had the time?
Never could be arsed to just do it?
Look no further, friend.
And, most importantly, don't waste your time.
This marvellous piece of `Python` technology is here to help you.

Convert clear text into morse code and vice versa with the convenience and nerdiness only a command line 
program can provide.

## Installation

To use these scripts clone the repo and install the modules in editable mode:

```bash
$ pip install -e .
``` 

## Encode Text

Just provide the input in the natural way, i.e. words are separated by whitespace, sentences are delimited by dots ('.').
Note that the end of a word is demarcated by a forward slash `/`.

### Example:

```bash
$ python pymorse.py encode 'sos. We are going to sink.'
... --- ... .-.-.- / .-- . / .- .-. . / --. --- .. -. --. / - --- / ... .. -. -.-
```


## Decode Morse

Provide the input morse code, where the end of a word is again demarcated as a forward slash. 
The end of a character is denoted by whitespace.
Note that the output string will be all upper case.

### Example:

```bash
$ python pymorse.py decode '... --- ... .-.-.- / .-- . / .- .-. . / --. --- .. -. --. / - --- / ... .. -. -.-'
SOS. WE ARE GOING TO SINK
```

## Dealing with Files

If you want to translate the content of a file you can specify the `-f` or `--file` flag. 

### Example: Convert File
```bash
$ python pymorse.py encode tests/example.txt -f
.-- .... .- - / .... .- - .... / --. --- -.. / .-- .-. --- ..- --. .... - ..--..
```

The content can be then saved by piping it into a different or even the same path
```bash
$ python pymorse.py encode tests/example.txt -f > tests/example.txt
```
