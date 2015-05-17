"""
Diff between Python2 and Python3 -> http://spartanideas.msu.edu/2014/06/01/the-key-differences-between-python-2-7-x-and-python-3-x-with-examples/

Package manager:
  - pip (more supported than setuptools)
  - setuptools (Old)

Environment:
  - pyenv (new from 3.3)
  - virtualenv

Create virtual env with pyenv:
  1. pyvenv myenv (create new virtual environment named myenv)
  2. source myenv/bin/activate (activate environment)
  3. python (don't need to use the command python3 to open Python 3)

Create virtual env with Virtualenvwrapper:
  1. pip install virtualenv
  2. pip install virtualenvwrapper
  3. mkdir ~/.virtualenvs
  4. open .bashrc
    a. export WORKON_HOME=~/.virtualenvs
    b. source /usr/local/bin/virtualenvwrapper.sh
  5. source .bashrc
  6. mkvirtualenv --python=/usr/local/bin/python3 myenv
  7. deactivate (disable the virtual env)
  8. workon myenv (activate virtual env)
  9. python (don't need to use the command python3 to open Python 3)

"""
