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
