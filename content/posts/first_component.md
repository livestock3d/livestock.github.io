Title: My First Component
Date: 16-03-2018
Modified: 16-03-2018
Status: published
Authors: Christian Kongsgaard           

When you successfully installed the requirements for Livestock, then it is time to create your first component.
Firstly you should open the Grasshopper script called "1 - My First Component.gh"

The script should contain two panels and a component called "Python Executor".
We start by double clicking on the Grasshopper Canvas and types in "python" until the Python Scipt Component appears. 
Place it on the canvas.

Double click the component. A new window will appear.
This component should be able to take in a text string and a number, send that to CPython using the Livestock Template Method,
and return a text file, where the original text string is repeated the number of time we specified.
We start by typing in some imports:

```python
# Imports
import os
import scriptcontext as sc
import subprocess
import livestock3d
```                 

Now we will write the functions we will use. For this component we will need 5.
The first function will write a data file. It looks like this:

```python
def write_file(file_path, string, number_of_repeats):
    file = open(file_path, 'w')
    file.write(str(string) + '\n')
    file.write(str(int(number_of_repeats)) + '\n')
    file.close()
```                       

The function is simple:
* A file is created
* The text string is written to the first line of the file
* The number of copies are written to the second line of the file

The second function will write the template:

```python
def write_template(template, path):
    livestock3d.pick_template(template, path)
```             

The function calls a function in the livestock3d library, which you placed in %appdata%\McNeel\Rhinoceros\5.0\scripts\livestock3d
We will take a look on that file in a minute, but let us finish with the component.

The next function we need is a function that can run our template.
```python
def run_template(py_exe, template_to_run):
    thread = subprocess.Popen([py_exe, template_to_run])
    thread.wait()
    thread.kill()
```               

This function will call python.exe (which we specified in the Python Executor component) on the template file.

The last to functions is to load the result file and print them out.
```python
def load_file(file):
    file = open(file, 'r')
    lines = file.readlines()
    file.close()
    
    return lines

def print_lines(lines):
    for line in lines:
        print(line.strip())
```                                                                                                                                                               