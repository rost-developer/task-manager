## Introduction

This project deals with balancing tasks between employees.

Object Employee have attributes:
- nick_name - name employee
- personal_point - numb of task point
- total_ point - load level employee
- list_task - employee tasks

Object Task have attributes:
- task_name
- task_point

## Project Interpreter
* python 3.5 (virtualenv)

## Prerequisites
* [names](https://pypi.python.org/pypi/names/)
* [nose](http://code.google.com/p/python-nose/)

### Installation on Ubuntu
    sudo pip install names
    sudo pip install nose

## Running the Application
    bin/task_manager [-p] [-t] [-h]
    * -p - number employees state (default 10)
    * -t - number of task (default 30)
    * -h - help

## Testing
        cd project
        nosetests

## Example
    bin/task_manager -p 12 -t 35
### or
    bin/task_manager --numb_person 12 --numb_tasks 35





