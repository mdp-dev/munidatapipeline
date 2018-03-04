
# Municipal Data Pipeline (MDP)

MDP is intended to enble resource constrained developers (e.g. students) to make use of open data platforms, especially GiS portals, where wrangling data may involve multiple computationally expensive spatial joins

# How it Works 

For each chunk of data, MDP schedules user defined functions and passes them to a child process, ensuring all system resources are released at the end of an operation.

The user is free to define their own data wrangling functions and include them in the pipeline, but MDP ships with built-ins intended to help you work with municipal data. These include functions that can pull data into the pipeline from open data portals, and typical operations like joins and groupbys. 

# Installation

Use pip:

    pip install munidatapipeline

# Quickstart
Here we run through a quick implementation of a data wrangling procedure. (In a real situation you would never use mdp on such a tiny amount of data.)

Begin by importing mdp (and pandas for the actual munging):
```
import munidatapipeline as mdp
import pandas as pd
```

If you're also going to use some of our built in functions, then we want to also call:

    from munidatapipeline import *

Create an instance of mdp with an empty schedule:
```
pipe = mdp.muni_data_pipe()
pipe.opts.schedule = []
```

Now we'll create a tiny dataframe of arbitrary data and assign it to the data attribute for our instance. This data can be passed back and forth between the parent and child process.
```
i = {'a': [a for a in range(10)], 'b': [b for b in range(10, 20)],
        'c': ['dog', 'cat', 'spam', 'egg', 'dog', 
              'cat', 'spam', 'egg', 'dog', 'spam']}
pipe.data = pd.DataFrame(i)
```

Now we define some functions and decorate them with the built in `err_to_parent` function, which just ensures that errors in the child process are raised in the parent.
```
@err_to_parent
def adder(connection, load, message):
    load['d'] = load['a'] + load['b']
    connection.send(load)
```
Note: functions always take these three arguments `(connection, load, message)` - the connection is to the parent process, the load is `pipe.data` by default, and `message` is a dict containing all your parameters. If you schedule a function which does not call `connection.send` or define `pipe.opts.timeouts` then your scheduler can hang.

Next we define another function, this time using the reserved `'chunk'` key from the `message` parameter to select which slice of data to group the dataframe by.
```
@err_to_parent
def grouping_and_save(connection, load, message):
    load = load.groupby(message['chunk']).sum()
    load.to_csv('./grouped_by_' + message['chunk'] + '.csv')
    connection.send("nada")
```
Also note that we're sending an arbitrary string back up the connection. Since we're using this function to save data to disk, we're going set the reserved key `'pandas_to_data'` to "none" when we schedule that function. In other words, regardless of what we send back to the parent, it won't be added to `pipe.data`.


Finally lets append our two functions to our schedule. We want to overwrite our `pipe.data` with the `adder` function and then nothing with our `grouping_and_save` function (we could also use 'concat' or 'append):
```
pipe.opts.schedule.append([adder, {'pandas_to_data':'overwrite'}])
pipe.opts.schedule.append([grouping, {'pandas_to_data':'none'}])
pipe.opts.chunk = "b"

pipe.scheduler()
```

And if we wanted to group by a different column, such as `'c'` then we would just call our scheduler as:
```
pipe.scheduler(chunk= 'c')
``` 

# What's Next for MDP 
* More API Queries 
* MySQL 
* Data from more cities! 
* PostGIS 
* Dask 

Plus: 
* Documentation Improvements 
* Docker Images 

# Get In Touch 
<munidatapipelinedevelopment@gmail.com>

# Contribute 

All countributions are welcome as we continue to report and fix bugs, improve documentation, and look to improve overall usuability. 

If you have any suggestions, we strongly encourage you to get in touch via email or: 
1. Clone the repository (git clone https://github.com/munidatadevelopmentpipeline)
2. Raise an issue or create a new branch with your issue request and changes 
3. Submit a pull request with your issue name and date 
