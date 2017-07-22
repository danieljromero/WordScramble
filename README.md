# WordScramble v0.1

 A command line word game using Python3

### Getting Started

It is highly recommended to use a Python3 Virtual Environment (virtualenv) for managing dependencies, creating isolated python project environments and, most importantly, not breaking your system wide Python installation. Anyways, let's begin!

### Prerequisites

Check Python3 version, requires **Python 3.4+**
```
$ python3 --version
```
Check if **pip** is installed
```
$ pip --version
```

### Requirements

This module requires:

- Click 6.X (http://click.pocoo.org/6/)

### Installation

Use Virtual Environment (**if installed**)
```
$ workon somevirtualenv
```
Clone repository
```
$ git clone https://github.com/romerodan/WordScramble.git
```
Navigate inside directory
```
$ cd WordScramble
```
Use pip
```
$ pip install --editable .
```
Check if installed correctly, you should see **WordScramble** listed
```
$ pip list
```
At this point you are ready to play the game!

## Playing the game

To see parameters needed for the game
```
$ wordscramble --help
```
- **DICTIONARY** parameter are any file with **.txt** extension that contain a list of words that you want to use.
- **MAX_LENGTH** parameter is the highest word length you want use for the game
    - It is recommended to use anything < 8, unless you're a pro

### Example

Move to **WordScramble** directory
```
$ cd ~/path/to/WordScramble/
```
Then do
```
$ wordscramble dictionaries/large.txt 4
```
Enjoy!

## Uninstalling

First do
```
$ pip uninstall wordscramble
```

Then delete directory
```
$ rm -rf ~/path/to/WordScramble/
```

## Contributing

_Under Construction_
