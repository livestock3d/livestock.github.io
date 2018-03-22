Title: Graph Plotter Component
Date: 22-03-2018
Modified: 22-03-2018
Status: published
Authors: Christian Kongsgaard
Tags: python, grasshopper, tutorial

Welcome to the second tutorial! In this tutorial we will create a component that can plot a graph with 
[Matplotlib](https://matplotlib.org/) and [NumPy](http://www.numpy.org/).
If you heard of Python, you have probably heard of NumPy as well. NumPy is a library that can handle numerical operations in Python.
NumPy is super fast and is relying heavily on C code, which makes it very hard (if not impossible) to use in IronPython.
Matplotlib is a plotting library, which works very well together with NumPy. The syntax of Matplotlib resemble Matlab's, 
which makes it easy to use. 

We will use the image viewer from Ladybug Tools to view the plot when finished, so make sure to download it first. 
Ladybug Tools can be found [here](http://www.food4rhino.com/app/ladybug-tools). Important is not download the [+] version, be get the legacy plugins.
If you are not going to use Ladybug Tools again, you can also just download the viewer [here](https://github.com/mostaphaRoudsari/ladybug/raw/master/userObjects/Ladybug_ImageViewer.gha)

We will make the Graph Plotter component, by modifying the component from the first tutorial.
We just need to modify the component a little bit. You can start by opening the "1 - My First Component.gh" and save it as:
"Graph Plotter.gh". There we can start changing the component. We do not need the y input on the component, so you can start removing that.
Thereafter, double click the component and change the write_file function to:

```python
def write_file(file_path, x):
    file = open(file_path, 'w')
    
    for value in x:
        file.write(str(value) + '\n')
 
    file.close()
```

Here we loop over the input and saves each value on a new line in the data file.
We should change the file locations and the stuff inside the if statement:

```python
# Specify paths 
txt_file = folder + '/data_file.txt'
template_file = folder + '/plot_graph_template.py'
result_file = folder + '/plot.png'
 
# Run functions
if run:
    write_file(txt_file, x)
    write_template('plot_graph', folder)
    run_template(py, template_file)
```

We are done coding the component now. The only thing missing is to change the x input to a list. By default all inputs to the
Grasshopper Python Scripts Component is set to "item". We do not want that, in this case. You change it by right-clicking the 
x and a menu will appear. In the bottom you can see "List Access". Click on that.
![alt text]({filename}/images/graph_plotter_1.png)

The full script in the component, looks like this:

```python
#------------------------------------------------------------------------------#
# Imports
import os
import scriptcontext as sc
import subprocess
import livestock3d
  
#------------------------------------------------------------------------------#
# Functions
 
def write_file(file_path, x):
    file = open(file_path, 'w')
    
    for value in x:
        file.write(str(value) + '\n')
 
    file.close()
 
def write_template(template, path):
    livestock3d.pick_template(template, path)
 
def run_template(py_exe, template_to_run):
    thread = subprocess.Popen([py_exe, template_to_run])
    thread.wait()
    thread.kill()
    
def load_file(file):
    file = open(file, 'r')
    lines = file.readlines()
    file.close()
    
    return lines
 
def print_lines(lines):
    for line in lines:
        print(line.strip())
        
        
#------------------------------------------------------------------------------#
# Execution
 
# Get CPython path from the other component
py = str(sc.sticky["PythonExe"])
 
# Make folder
folder = r'C:/livestock3d/data'
if not os.path.exists(folder):
    os.mkdir(folder)
 
# Specify paths 
txt_file = folder + '/data_file.txt'
template_file = folder + '/plot_graph_template.py'
result_file = folder + '/plot.png'
 
# Run functions
if run:
    write_file(txt_file, x)
    write_template('plot_graph', folder)
    run_template(py, template_file)
```