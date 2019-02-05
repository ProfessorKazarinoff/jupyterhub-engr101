# What is JupyterHub?

JupyterHub is a server-hosted distributed Jupyter notebook environment. JupyterHub allows users to log into a server and write Python code within a web browswer without any software installation on their local computer. Anywhere you have an internet connection, you can bring up a JupyterHub webpage and write/run Python code in a Jupyter notebook. The Jupyter notebook and JupyterLab interfaces that JupyterHub provides is the same Jupyter interface you run locally. Because JupyterHub runs in a web browser, it even works on tablets and phones.

Below is an image of a running JupyterHub server. The JupyterLab interface is shown.

![JupyterHub Running](images/jupyterhub_running_live.png)

## Why JupyterHub?

Why **Jupyter Hub**? I am teaching an introductory engineering course this winter. In previous quarters, our college has taught MATLAB for three of the labs in this course. But this winter, I want to try teaching **Python** and cover the same concepts and learning outcomes.

If we use Python in the class this winter, I would like to spend the class time coding and solving problems. I don't want to spend time during class downloading Python, creating virtual environments, troubleshooting installs, dealing with system vs. non-system versions of Python, installing packages, dealing with folder structure, explaining the difference between conda and pip, teaching command-line commands, going over Python on Windows compared to Python on MacOSX... The solution is to use JupyterHub.

## Summary

JupyterHub is a way to run Jupyter notebooks on a remote server. Students can log on to a JupyterHub server then write and run Python code without installing any software. Students see the same interface on JupyterHub as they see running Jupyter notebooks locally.

## Next Steps

Next, we'll review what tools need installed on our local comptuer to deploy JupterHub. We'll also review the standard locations for JupyterHub configuration and runtime files.