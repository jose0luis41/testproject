#Operating Systems www.icesi.edu.co/facultad_ingenieria/

##Flask - Jenkins
Flask testing with jenkins

### Install Jenkins
Install jenkins in a CentOS machine and configure a virtualenv in the folder with the
required dependencies (A guide will be provided in class)

Take into account to check your sources for the appropiate permissions:

```sh
$ git ls-files --stage
$ git ls-tree HEAD
```

If you find that run_tests.sh does not have execution permissions you can set the appropiated permissions using the
following command

```sh
$ git update-index --chmod=+x run_tests.sh
```

### Setup environment variables
set an environment variable named USERMGT_SETTINGS and check if the variable was created

```sh
$ export USERMGT_SETTINGS=settings/production.py
$ echo $USERMGT_SETTINGS
```

### Useful commands

Export package requirements list

```sh
$ pip freeze > requeriments.txt
```

Install package requirements list

```sh
$ pip install -r requeriments.txt
```

Run test with pytest

```sh
$ py.test
```

Run test with pytest and export unit tests xml format

```sh
$ py.test --junitxml=python-tests.xml
```

### References

[**Test Redirection**][test-redirection]
[test-redirection]: http://stackoverflow.com/questions/23146253/test-redirection-in-flask-with-python-unittest



