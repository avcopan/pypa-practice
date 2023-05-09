# pypa-practice

Steps:

1. `conda create -n pypa-env python=3.10`

2. `conda activate pypa-env`

3. Created `pyproject.toml` as described [here](https://setuptools.pypa.io/en/latest/userguide/quickstart.html), but added in the following section to exclude one directory and include another:
```
[tool.setuptools.packages.find]
include = ["greetme"]
exclude = ["old"]
```

4. `python -m build` -- used to build

5. `python -m pip install dist/greetme-0.0.1-py3-none-any.whl` -- used to install

6. `python -m pip uninstall greetme` if you want to uninstall

