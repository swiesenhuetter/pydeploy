from setuptools import setup, find_packages
from setuptools.command.build_py import build_py
from Cython.Build import cythonize
from Cython.Compiler import Options

with open("README.md", 'r') as f:
    long_description = f.read()

files = ["main.py", "gui/gui.py"]
cython_excludes = ["**/__init__.py"]

Options.docstrings = False  # remove comments


class skip_py(build_py):
    def find_package_modules(self, package, package_dir):
        modules = super().find_package_modules(package, package_dir)
        init_files = list(filter(lambda x: "__init__.py" == x[1], modules))
        return init_files


compiled = cythonize(files,
    exclude=cython_excludes,
    build_dir="build",
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
    cmdclass={'build_py': skip_py},
    entry_points={
        'console_scripts': [
            'eulitha = gui:main'
        ]
    },
    )
