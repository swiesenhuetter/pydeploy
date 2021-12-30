from setuptools import setup, find_packages
from setuptools.dist import Distribution

from Cython.Build import cythonize
from Cython.Compiler import Options

with open("README.md", 'r') as f:
    long_description = f.read()

files = ["main.py", "gui/gui.py"]
cython_excludes = []

class BinDist(Distribution):
    def is_pure(self):
        return False


Options.docstrings = False  # remove comments

compiled = cythonize(files,
    exclude=cython_excludes,
    build_dir="_build",
    force=True,
    compiler_directives={'language_level': "3"})


setup(
    author="Eulitha AG",
    packages=find_packages(),
    # include_package_data=True,
    name="eulitha",
    version="0.0.1",
    entry_points={
        'console_scripts': [
            'eulitha = gui:main'
        ]
    },
    distclass=BinDist,
    ext_modules=compiled)
