from setuptools import setup
from setuptools.extension import Extension
from Cython.Build import cythonize

extensions = [
    Extension(
        "WordScramble",
        ["wordscramble.pyx"],
    ),        
]

setup(
    name = 'WordScramble',
    ext_modules = cythonize(extensions),        
)
