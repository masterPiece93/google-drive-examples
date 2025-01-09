# Google Drive Examples
Package for examples on operations that can be performed with google drive

### [Documentation](./doc.md)

### [How to Install](https://github.com/masterPiece93/google-drive-examples/wiki/Package-Installation-From-Git)

---

#### Help on Python Packaging 

[link](https://www.mssqltips.com/sqlservertip/6802/create-wheel-file-python-package-distribute-custom-code/)

```sh
# to build pkg
python setup.py bdist_wheel 
```

```sh
# to check if build created is not having any issues 
check-wheel-contents <path-to-dist-folder>
```

##### everything about python packaging in short :

[link](https://xebia.com/blog/a-practical-guide-to-using-setup-py/)


##### How to include the static/additional/non-python-file pkg data :

[link-1](https://sixty-north.com/blog/including-package-data-in-python-packages.html#:~:text=Broadly%2C%20package%20data%20is%20any,included%20in%20a%20Python%20package.)

link-1 > link2

[link-2 : manifest file](https://setuptools.pypa.io/en/latest/userguide/miscellaneous.html)

[accessing pkg data in python file of pkg code .](https://docs.python.org/3/library/importlib.resources.html)

