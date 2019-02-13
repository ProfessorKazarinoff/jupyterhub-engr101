# Extra Configuration

In this section, we will go over some extra configuration settings we can set in ```jupyterhub_config.py``` to help our JupyterHub deployment hum along and help if students forget to logout or too many student try and log in at the same time. 

[TOC]

## Configuration Options

In the JupyterHub docs, there is a list of configuration options and descriptions:

 > [https://jupyterhub.readthedocs.io/en/stable/api/app.html](https://jupyterhub.readthedocs.io/en/stable/api/app.html)

A couple configuration options in the list seem like good ideas:

The class has 24 students, plus one instructor. Given that class size, I think 26 is a good number for the maximum that can use JupyterHub the same time. 

```text
config c.JupyterHub.active_server_limit = Int(0)
# Maximum number of concurrent servers that can be active at a time.
```

Having too many users log in all at the same time can overload the server. Let's set this as 13, so half of the class can log in at the same time.

```text
config c.JupyterHub.concurrent_spawn_limit = Int(100)
Maximum number of concurrent users that can be spawning at a time.
```

A couple settings relate to shutting down the hub and if user servers shut down too. I want it set so that if I shut down the hub, all the user servers are shut down too.

```text
config c.JupyterHub.cleanup_proxy = Bool(True)
# Whether to shutdown the proxy when the Hub shuts down.
```

```text
config c.JupyterHub.cleanup_servers = Bool(True)
# Whether to shutdown single-user servers when the Hub shuts down.
```

## Cull Idle Servers

A problem with the first two JupyterHub deployments was that some students would not shut down their server when they were done working. Then twenty or so servers would all keep running all the time. 

This script from the JupyterHub Examples repo looks like it might help:

 > [https://github.com/jupyterhub/jupyterhub/tree/master/examples/cull-idle](https://github.com/jupyterhub/jupyterhub/tree/master/examples/cull-idle)
 
To get it to work, it looks like you need to add the following to ```jupyterhub_config.py```

```text
# /etc/jupyterhub/jupyterhub_config.py

import sys

...
c.JupyterHub.services = [
        {
            'name': 'cull-idle',
            'admin': True,
            'command': [sys.executable, '/etc/jupyterhub/cull_idle_servers.py', '--timeout=3600'],
        }
    ]
```

#### Update

put ```cull_idle_servers.py``` in ```/etc/jupyterhub/```. Make sure **dateutil** is intalled in the jupyterhub virtual env. Try ```>>> import dateutil  >>>dateutil.__version__``` Add ```import sys``` to the top of ```jupyterhub_config.py```. Restart JupyterHub. Check for errors.

#### What I tried before is below and I don't think it worked

I don't know if the ```cull_idle_servers.py``` script has to be placed somewhere, or if that script is already part of the JupyterHub package. It looks like according to this repo [jupyterhub-deploy-teaching](https://github.com/jupyterhub/jupyterhub-deploy-teaching), deep in the ```/roles/cull_idle/tasks/main.yml``` [(link)](https://github.com/jupyterhub/jupyterhub-deploy-teaching/blob/master/roles/cull_idle/tasks/main.yml), there is a line that copies the ```cull_idle.py``` file [(link)](https://github.com/jupyterhub/jupyterhub-deploy-teaching/blob/master/roles/cull_idle/files/cull_idle_servers.py) into the ```/svr/jupyterhub/``` directory.

```text
# from https://github.com/jupyterhub/jupyterhub-deploy-teaching/blob/master/roles/cull_idle/tasks/main.yml

- name: install cull_idle_servers dependencies
  pip: name=python-dateutil state=present executable=pip

- name: install cull_idle_servers.py into {{jupyterhub_srv_dir}}
  copy: src=cull_idle_servers.py dest={{jupyterhub_srv_dir}} owner=root group=root mode=0700
```

So let's use FileZilla to copy the ```cull_idle.py``` script onto the server into the ```/srv/jupyterhub/``` directory. A problem I had was that FileZilla would not copy the file to ```/srv/jupyterhub``` because of what I think were permission issues. The way I got around it was to use FileZilla to copy the ```cull_idle_servers.py``` script into the user ```peter``` home directory, and then use the command line to ```cp``` the script into ```/srv/jupyterhub```. Then a couple commands were needed to modify the permissions of the script. I think these permission changes are needed to allow the script to be run by JupyterHub.

```text
$ ls
$ sudo chown :sudo cull_idle_servers.py
$ sudo chmod g+x cull_idle_servers.py
$ sudo chmod u+x cull_idle_servers.py
$ ls -la
```

It also looks like the Python package **python-dateutil** needs to be installed to run the ```cull_idle_servers.py``` script. We can see in the ```cull_idle_servers.py``` script there is an import for **python-dateutil**.

```text
# /srv/jupyterhub/cull_idle.py

...
import datetime
import json
import os

from dateutil.parser import parse as parse_date
...
```

The **python-dateutil** package can be installed with **conda**. Make sure to activate the ```(jupypterhub)``` virtual environment first.

```text
$ sudo systemctl stop jupyterhub
$ sudo systemctl status jupyterhub
# [Ctrl]+[c] to exit

$ conda activate jupyterhub
(jupyterhub)$ conda install python-dateutil
(jupyterhub)$ conda deactivate

$ sudo systemctl start jupyterhub
$ sudo systemctl status jupyterhub
# [Ctrl]+[c] to exit
```

## Modify jupyterhub_config.py and upload to server

The additions made to ```jupyterhub_config.py``` are shown below:

```text
# /etc/jupyterhub/jupyterhub_config.py

...
## Extra Configuration

# Maximum number of concurrent servers that can be active at a time
c.JupyterHub.active_server_limit = 26

# Maximum number of concurrent users that can be spawning at a time
c.JupyterHub.concurrent_spawn_limit = 13

# Whether to shutdown the proxy when the Hub shuts down.
c.JupyterHub.cleanup_proxy = True

# Whether to shutdown single-user servers when the Hub shuts down.
c.JupyterHub.cleanup_servers = True

# Cull Idle Servers
# place cull_idle_servers.py in /srv/jupyterhub
c.JupyterHub.services = [
        {
            'name': 'cull-idle',
            'admin': True,
            'command': 'python cull_idle_servers.py --timeout=3600'.split(),
        }
    ]

...
```

I made these changes in ```jupyterhub_config.py``` locally and then used FileZilla to upload the modified config file to the server.

After the the modified ```jupyterhub_config.py``` file is added to the server, restart JupyterHub and make sure there are not any erros.

```text
$ sudo systemctl start jupyterhub
$ sudo systemctl status jupyterhub
# [Ctrl]+[c] to exit
```

## Summary

In this section we added a few extra configuration options to the ```jupyterhub_config.py``` file. A few extra configuration options we included were to limit the number of servers that can run at the same time and limit the amount of servers that can spawn at the same time.

We also added a ```cull_idle_servers.py``` script to the server which will shut down idle servers if a student has not used them in a while. This involved copying the script to the users home directory, then copying it over to the ```/srv/jupyterhub/``` directory and modifying permissions. 

Finally we uploaded the modified ```jupyterhubconfig.py``` configuration file and restarted JupyterHub.

## Additional Extras

That's it for the main JupyterHub deployment. The next section is about periodic maintenance. After running JupyterHub for two quarters there are a couple lessons learned.

<br>
