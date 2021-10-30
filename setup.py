import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["app", "question_generation", "jinja2"],
    "include_files":["lists", "tests", "topics"]
}

setup(
    name="Study Help",
    version="0.1.4",
    author="Joshua Clark",
    options = {"build_exe": build_exe_options},
    executables = [Executable("website.py")]
)

# [windows] ```python setup.py build```
# [mac] ```python3 setup.py build```
# ???[windows]```python setup.py bdist_msi``` or 
# ???[mac]```python3 setup.py bdist_msi```

# if there is an error due to ...:
# module not being recognized: add it to packages
# files not being found: add it to include_files

# licenses can be figured out with ```pip-licenses```