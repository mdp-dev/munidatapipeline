
# Municipal Data Pipeline (MDP)

MDP is intended to enble resource constrained developers (e.g. students) to make use of open data platforms, especially GiS portals, where wrangling data may involve multiple computationally expensive spatial joins

# How it Works 

For each chunk of data, MPD schedules user defined functions and passes them to a child process, ensuring all system resources are released at the end of an operation.

The user is free to define their own data wrangling functions and include them in the pipeline, but MDP ships with built-ins intended to help you work with municipal data. These include functions that can pull data into the pipeline from open data portals, and typical operations like joins and groupbys. 
 

# What's Next for MDP 
* More API Queries 
* MySQL 
* Data from more cities! 
* PostGIS 
* Dask 

Plus: 
* Documentation Imporvements 
* Docker Images 

# Get In Touch 
<munidatapipelinedevelopment@gmail.com>

# Contribute 

All countributions are welcome as we continue to report and fix bugs, improve documentation, and look to improve overall usuability. 

If you have any suggestions, we strongly encourage you to get in touch via email or: 
1. Clone the repository (git clone <https://github.com/mdp-dev/munidatapipeline>)
2. Raise an issue or create a new branch with your issue request and changes 
3. Submit a pull request with your issue name and date 
