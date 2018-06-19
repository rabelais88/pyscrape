#web scraping with python

### basic howto with virtual environment

1. establish virtual environment

```python3 venv -m [projectname]``` creates a new project

2. activate virtual environment script from folder

```[projectname]/Scripts/activate.bat``` or ```activate```(Linux)

Under virtual environment, python must be referred as ```python``` instead of any custom names(```py, python3```).

3. after project, freeze the requirements

```pip freeze > requirements.txt```

4. when downloaded from git, install all requirements

```pip install -r requirements.txt```

*note* if it doesn't install, consider using ```pip3``` instead of ```pip```. 

*note* unlike node repository, python virtual env is dedicated to a single OS. It's either for POSIX(Mac, Linux) or Windows. once it's created for Windows, it cannot be installed/run from Linux and vice versa. as you may have noticed, this example is created entirely from windows environment.

5. add custom setup for python linting(to disable unncessary VScode no linter errors)

 - E501, E111, E114: indentation related errors(for custom 2 spaced indentation)

under ```./vscode/settings.json```:
```
{
  "python.pythonPath": "${workspaceFolder}\\scraping1\\Scripts\\python.exe",
  "python.linting.pylintPath":"${workspaceFolder}\\scraping1\\Scripts\\pylint.exe",
  "python.linting.pep8Enabled": true,
    "python.linting.pep8Args": [
        "--ignore=E501,E111,E114" 
    ],
    "python.linting.enabled": true
  }
```