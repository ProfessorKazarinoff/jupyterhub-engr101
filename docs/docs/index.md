# Welcome to the JupyterHub Deployment Docs for ENGR101 2019Q1

<br>

This documentation serves as a record of the [JupyterHub](https://jupyter.org/hub) Deployment for ENGR101 Winter 2019 at Portland Community College. 

<br>

The GitHub repo for the deployment can be found here: 

 > [https://github.com/ProfessorKazarinoff/jupyterhub-engr101](https://github.com/ProfessorKazarinoff/jupyterhub-engr101)

<br>

Click the menu items on the left to view the deployment steps.

Or start [Here](what_is_jupyterhub.md) and click the arrows at the bottom of each page.

[![Next Setup Arrow](images/next_what_is_jupyterhub_arrow.png)](what_is_jupyterhub.md)

<br>

The documentation site for a previous JupyterHub deployment can be found [here](https://professorkazarinoff.github.io/jupyterhub-engr114/) 

There is also a [series of blog posts](https://pythonforundergradengineers.com/why-jupyter-hub.html) that documents my first JupyterHub deployment in Summer 2018. 

This documentation builds upon the experience from my two previous JupyterHub depoloyments.

<br>

## Main Steps

* Install PuTTY, generate SSH keys
* Create server, non-root sudo user
* Install JupyterHub and Python packages
* Aquire and link domain name to server
* Aquire SSL cirt
* Create Cooke Secret, Proxy Auth Token, and dhparam.pem
* Install and configure Nginx
* Configure JupyterHub
* JupyterHub as system service
* Google Authentication
* Create custom login page
* Pull assignments down from GitHub for each user
* Extra configuration
