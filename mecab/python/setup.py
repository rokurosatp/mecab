#!/usr/bin/env python

import os
from distutils.core import setup,Extension,os

def cmd1(str):
    return os.popen(str).readlines()[0][:-1]

def cmd2(str):
    return cmd1(str).split()

def get_mecab_bin():
    home = os.getenv("MECAB_HOME", "")
    if not home:
        raise Exception("Please set MECAB_HOME environmental variable.")
    return os.path.join(home, "sdk")
    
setup(name = "mecab-python",
	version = "0.996",
	py_modules=["MeCab"],
	ext_modules = [
		Extension("_MeCab",
			["MeCab_wrap.cxx",],
			include_dirs=[get_mecab_bin()],
			library_dirs=[get_mecab_bin()],
			libraries=["libmecab"])
			])
