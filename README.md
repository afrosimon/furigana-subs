## This project

Small app to parse through Japanese subtitles and complement the kanjis with their
associated furigana (pronunciation of the kanji). Got to a point where I wanted
to watch movies to further my learning but had too much of a hard time with the kanjis.
This tool aims to fill that gap.

This app was built with Flask & Mecab (morphological analyzer for the Japanese language)

## Installation

Use virtualenvwrapper to create a Python 3 environment:

```
$ cd path/to/furigana-subs
$ mkvirtualenv -p python3.6 furigana-subs
(furigana-subs)$ setvirtualenvproject
```

To install system and the project dependencies you can run the install.sh script.
This will only work on debian based systems, otherwise make sure you have these
packages installed : 

mecab mecab-ipadic-utf8 libmecab-dev

and run this command :

```
$ pip install -r requirements.txt
```
