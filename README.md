# pytemplate
a simple template python project

## To make your own
1. make a new repo on [github](https://github.com), then clone it locally
2. `sudo apt-get install git-flow`
    * see [the github](https://jeffkreeftmeijer.com/git-flow/)
    * for an existing project: `$ git flow init`
3. make a directory with the same name as the repo, put an `__init__.py` in there
4. write your functions in this directory
5. make the setup.py
    * use `$ python setup.py register sdist upload` to upload to PyPI
    * Nice PyPI [tutorial](http://peterdowns.com/posts/first-time-with-pypi.html)
    * I had to follow [this thread](https://github.com/pypa/setuptools/issues/941) to get it working
    * now anyone can install the  pachage with `$ pip install andyofmelbourne-pytemplate` 
    * to test locally try `$ pip install -e .` (you may need to chown a file)



