# Building Docs

The documentation for this JupyterHub deployment was completed using **mkdocs**, the **mkdocs-material** theme and deployed on GitHub pages.

The directory structure of the GitHub repo that house the deployment files and docs looks like this:

```text
.
├── LICENSE
├── README.md
├── docs
│   ├── docs
│   ├── mkdocs.yml
│   └── theme
├── etc
│   ├── jupyterhub
│   ├── nginx
│   └── systemd
└── opt
    └── miniconda3
```


Inside the ```docs/``` directory is another ```docs/``` subdirectory with all of markdown files that make up the documentation. There is also a mkdocs yaml file in the ```docs``` directory. When calling mkdocs commands from the command line, you need to be in the folder with the ```mkdocs.yml``` file.

```text
./docs/
├── mkdocs.yml
├── docs/
│   ├── images/
│   ├── add_users.md
│   ├── assignments_on_github.md
│   ├── building_docs.md
│   ├── cookie_secret_proxy_auth_token.md
│   ├── custom_login_page.md
│   ├── dns_routing.md
│   ├── extra_configuration.md
│   ├── google_oauth.md
│   ├── index.md
│   ├── install_jupyterhub.md
│   ├── jupyterhub_config.md
│   ├── nbgitpuller_defaut_url.md
│   ├── nbgitpuller_plugin.md
│   ├── nginx_config.md
│   ├── nginx_install.md
│   ├── periodic_maintenance.md
│   ├── server_setup.md
│   ├── setup_and_tools.md
│   ├── slides
│   ├── ssh_keys.md
│   ├── ssl_cirtificates.md
│   ├── static
│   ├── systemd.md
│   ├── useful_commands.md
│   └── what_is_jupyterhub.md
└── theme
    ├── assets
    └── partials
```

To build the docs locally, make sure you have Python installed (I use [Anaconda](https://anaconda.com/downloads)) start out by cloning the repo:

```text
git clone https://github.com/ProfessorKazarinoff/jupyterhub-engr101.git
```

```cd``` into the cloned repo, and create a virtual environment. Install the Python packages needed to build the docs.

```text
cd jupyterhub-engr101.git
conda create -n jupyterhub python=3.7
conda activate jupyterhub
(jupyterhub) pip install -r requirements.txt
```

```cd``` into the docs dir, and run ```mkdocs build``` and ```mkdocs serve```

```text
cd docs
ls
# mkdocs.yml

mkdocs build
mkdocs serve
```

Look at the built site on local host:

 > [http://localhost:8000/](http://localhost:8000/)
 
Deploy to GitHub pages

```text
mkdocs gh-deploy
```

