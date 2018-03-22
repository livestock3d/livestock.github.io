Title: My First Template
Date: 22-03-2018
Modified: 22-03-2018
Status: published
Authors: Christian Kongsgaard

Now when the Grasshopper component is written, it is time to write the template and the CPython script.
Navigate to where you put the templates.py and open it.
It can easily be found by in explorer typing:
> %appdata%\McNeel\Rhinoceros\5.0\scripts\livestock3d

Python scripts can be opened and edited with a range of editors: Notepad, [Notepad++](https://notepad-plus-plus.org/download/v7.5.6.html)
or Spyder, which comes with the Anaconda installation, is among the simplest. 

The top function in templates.py is the function we used in the component: pick_template()

```python
def pick_template(template_name, path):
    """
    Writes a template given a template name and path to write it to.
    
    :param template_name: Template name.
    :param path: Path to save it to.
    """
 
    template_name = str(template_name)
 
    if template_name == 'my_first_template':
        my_first_template(path)
 
    elif template_name == 'plot_graph':
        plot_graph(path)
 
    else:
        raise NameError('Could not find template: ' + str(template_name))
 
    return True
```

pick_template is a convenient way of writing out different templates with the same function. 
You just need to give the name of the template and a path, where the template should be written.
At the moment it is possible to write out two templates. For this tutorial we will only use the first one.
When pick_template receives the template_name: "my_first_template", the function my_first_template() will be called. 
Therefore, we need to create a function called my_first_template()

```python
def my_first_template(path):
    """
    Writes a template.
 
    :param path: Path to write it to.
    :type path: str
    :return: The file name
    """
 
    file_name = r'/my_first_template.py'
    file = open(path + file_name, 'w')
 
    file.write("# Imports\n")
    file.write("import sys\n")
    file.write("sys.path.insert(0, r'C:\livestock3d')\n")
    file.write("import livestock3d as ls\n")
 
    file.write("# Run function\n")
    file.write("ls.my_function(r'" + path + "')\n")
 
    file.write("# Announce that template finished and create out file\n")
    file.write("print('Finished with template')\n")
 
    file.close()
 
    return file_name
```

The function takes a path as an input. The path specifies, where the template should be written.
We define a variable with the file name of the template and creates that file with the open statement.

To let Python know that we want to use scripts from the C:\livestock3d folder, we need to add it to the PYTHONPATH.
We do that with sys.path.insert(). After that we can import livestock3d.

After the imports we can call the function my_function from livestock3d. 
The function is not yet created, but we will do that in the next paragraph.
