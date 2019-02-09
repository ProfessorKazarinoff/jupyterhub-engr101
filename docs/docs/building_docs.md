# Building Docs

The documentation for this JupyterHub deployment was completed using **mkdocs**, the **mkdocs-material** theme and deployed on GitHub pages.

The directory structure of the GitHub repo that house the deployment files and docs looks like this:

```text


```


To build the docs locally, make sure you have Python installed (I use Anaconda) start out by cloning the repo:

```test
git clone https://github.com/ProfessorKazarinoff/jupyterhub-engr101.git
```

Cd into the cloned repo, and create a virtual environment. Install the Python packages needed to build the docs.

```text
cd jupyterhub-engr101.git
conda create -n jupyterhub python=3.7
conda activate jupyterhub
(jupyterhub) pip install requirements.txt
```

Cd into the docs dir, and run ```mkdocs build``` and ```mkdocs serve```

```text
cd docs
ls
# mkdocs.yml

mkdocs build
mkdocs serve
```

Look at the built site on local host:

 > [http://lcoalhost:8000](http://lcoalhost:8000)
 
Deploy to GitHub pages

```text
mkdocs gh-deploy
```





