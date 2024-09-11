# CSC 510: Software Engineering Homework2

![GitHub](https://img.shields.io/badge/Language-Python-blue.svg)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat&logo=linux&logoColor=black) 
![MIT License](https://img.shields.io/badge/License-MIT-red.svg) 
![GitHub repo size](https://img.shields.io/github/repo-size/CSC510-SE-HW/hw2) 
[![Build Status](https://github.com/CSC510-SE-HW/hw2/actions/workflows/main.yml/badge.svg)](https://github.com/CSC510-SE-HW/hw2/actions)
![GitHub Pull Requests](https://img.shields.io/github/issues-pr/CSC510-SE-HW/hw2) 
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/CSC510-SE-HW/hw2) 
![GitHub contributors](https://img.shields.io/github/contributors/CSC510-SE-HW/hw2) 
![GitHub forks](https://img.shields.io/github/forks/CSC510-SE-HW/hw2)
![Closed issues](https://img.shields.io/github/issues-closed-raw/CSC510-SE-HW/hw2?color=bright-green)
![Open issues](https://img.shields.io/github/issues-raw/CSC510-SE-HW/hw2)
[![Commit Acitivity](https://img.shields.io/github/commit-activity/m/CSC510-SE-HW/hw2)](https://github.com/CSC510-SE-HW/hw2)
[![Codecov](https://codecov.io/gh/CSC510-SE-HW/hw2/branch/main/graph/badge.svg)](https://codecov.io/gh/CSC510-SE-HW/hw2)
![Pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)
![Radon Complexity](https://img.shields.io/badge/code%20complexity-radon%20A-brightgreen)
![PEP8](https://img.shields.io/badge/code%20style-autopep8-blue)


This repository illustrates how to apply static analysis tools in order to create a cleaner and more readable coding format. All the badges show the essential information about the repository and how the test cases pass correctly after debugging a code that is not working.
Other than the tests that will be run after each commit, the static analysis tools will also check the new code. Moreover, the traces of how these different tools analyzed the code are also shown here, both before and after modifying the code accordingly. Having all the test cases and ensuring they run after each commit makes the repository more maintainable, and analyzing the code after each commit using the static analysis tools will ensure that the code follows specific coding patterns.


1. **`.github/workflows/main.yml`**
   - The `main.yml` file in this repository triggers on push and pull requests, setting up Python 3.x, running tests with `pytest`, generating a coverage report, and uploading it to Codecov for the `hw1` project.

2. **`LICENSE`**
   - This MIT License allows users to freely use, modify, and distribute the `CSC510-SE-HW1` software, provided they include the original copyright notice. 

3. **`README.md`**
   - This file provides an overview of the project. It includes badges that display the build status, license, and code coverage.

4. **`scripts/run_radon_metrics.sh`**
   - This script folder runs `run_radon_metrics.sh`, which generates a log file after running radon in order to show the traces of this static analysis tool.
5. **`src`**
   - This folder contains the original codes for the merge sort function, including hw2_debugging.py and rand.py.
6. **`traces`**
   - This folder has all the generated traces both before and after modification. The only important thing to pay attention to is that radon analyzes and gives information about the code's complexity, comments, and similar factors, which do not usually change after modifying the code according to the other tools.
8. **`test_sort.py`**
   - This test file uses `pytest` to verify the functionality of the merge sort function, with three different passing tests trying to cover various input arrays and see if there is any problem with the algorithm.
