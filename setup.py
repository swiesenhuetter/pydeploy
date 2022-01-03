from setuptools import setup, find_packages
from distutils.command.build_ext import build_ext
from setuptools.command.build_py import build_py
from Cython.Build import cythonize
from Cython.Compiler import Options
import sys


with open("README.md", 'r') as f:
    long_description = f.read()

Options.docstrings = False  # remove comments

class skip_py(build_py):
    """
    overwrites distutils code to skip py source installation
    without this we would distribute *.py sources
    """
    def find_package_modules(self, package, package_dir):
        return []


class build_ext_with_init(build_ext):
    """
    overwrite distutils code to fix the "__init__.py" issue
    see https://bugs.python.org/issue35893
    and 
    https://stackoverflow.com/questions/58797673/how-to-compile-init-py-file-using-cython-on-windows    
    """
    def get_export_symbols(self, ext):
        return []


"""
no cythonize when cleaning
cythonize creates the *.c-sources
"""
if 'clean' in sys.argv:
    compiled = []
else:
    files = ["**/*.py"]
    cython_excludes = ["setup.py"]
    compiled = cythonize(files,
        exclude=cython_excludes,
        build_dir="build",
        language="c++",
        force=True,
        compiler_directives={'language_level': "3"})

setup(
    author="Eulitha AG",
    packages=find_packages(),
    include_package_data=True,
    name="eulitha",
    version="0.0.3",
    description="Eulitha Phabler GUI",
    long_description=long_description,
    install_requires=["PySide6"],
    setup_requires=["setuptools", "cython", "wheel"],
    ext_modules=compiled,
    cmdclass={'build_ext': build_ext_with_init, 'build_py': skip_py},
    entry_points={
        'console_scripts': [
            'eulitha = gui:main'
        ]
    },
    )
