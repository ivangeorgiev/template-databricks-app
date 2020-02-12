# Databricks Template Application
Databricks Template Application



## Getting Started

You need to have Python 3.7 installed. Using Python `py`  launcher to create a virtual environment.

```bash
py -3.7 -m venv .venv
```





## Build

```
pip install -U setuptools wheel
python setup.py sdist bdist_wheel
```

To automatically tag with version number:

```
git tag -a v$(python setup.py --version) -m "Tag v$(python setup.py --version)"
```



See also:

* https://setuptools.readthedocs.io/en/latest/setuptools.html
* https://docs.python.org/3/distutils/setupscript.html

## Misc

### Supress Deprecation Warnings

Add option:

```bash
pytest -W ignore::DeprecationWarning
```



### Import Directory

* http://nightlyclosures.com/2019/06/07/import-a-directory-into-databricks-using-the-workspace-api/