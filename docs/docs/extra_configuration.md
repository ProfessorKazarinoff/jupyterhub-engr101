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
 
To get the ```cull_idle_servers.py``` script to run as a JupyterHub service, it looks like you need to add the following to ```jupyterhub_config.py```. (Based on [this page](https://github.com/jupyterhub/jupyterhub/tree/master/examples/cull-idle) in the JupyterHub docs)

```text
# /etc/jupyterhub/jupyterhub_config.py

import sys

...
# Cull Idle Servers
# place cull_idle_servers.py in /etc/jupyterhub
c.JupyterHub.services = [
        {
            'name': 'cull-idle',
            'admin': True,
            'command': [sys.executable,
                        '/etc/jupyterhub/cull_idle_servers.py',
                        '--timeout=3000',
                        '--url=http://127.0.0.1:8081/hub/api'
                        ],
        }
    ]
```

Put ```cull_idle_servers.py``` (found [here](https://github.com/jupyterhub/jupyterhub/blob/master/examples/cull-idle/cull_idle_servers.py)) in ```/etc/jupyterhub/```. Make sure **dateutil** is intalled in the jupyterhub virtual env. Try ```>>> import dateutil  >>> dateutil.__version__``` (using the ```(jupyterhub)``` virtual env. Make sure to add ```import sys``` to the top of ```jupyterhub_config.py```. Restart JupyterHub. Check for errors.

```text
$ sudo systemctl stop jupyterhub
$ sudo systemctl start jupyterhub
$ sudo systemctl status jupyterhub
# [Ctrl]+[c] to exit
```

If it seems like the ```cull_idle_servers.py``` script isn't working, try running ```cull_idle_servers.py``` from the command line to see if there are any errors. Make sure you are in the ```(jupyterhub)``` virtual environment when you run the script. The script will look for the ```JUPYTERHUB_API_TOKEN``` environment variable. An API token can be aquired by logging into JupyterHub (like a regular student) and clicking the [Token] menu from the home page that has the [Stop My Server] and [My Server] buttons. Click [Request new API token] and copy the API token. Then run the lines below (replace ```XXXX```` with your actual API token):

```text
$ export JUPYTERHUB_API_TOKEN='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
$ echo $JUPYTERHUB_API_TOKEN
# API token is printed

$ cd /etc/jupyterhub
$ conda activate jupyterhub
(jupyterhub)$ python cull_idle_servers.py --timeout=60 --url=http://127.0.0.1:8081/hub/api
# check for errors
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
# place cull_idle_servers.py in /etc/jupyterhub
c.JupyterHub.services = [
        {
            'name': 'cull-idle',
            'admin': True,
            'command': [sys.executable,
                        '/etc/jupyterhub/cull_idle_servers.py',
                        '--timeout=3000',
                        '--url=http://127.0.0.1:8081/hub/api'
                        ],
        }
    ]
...
```

I made these changes in ```jupyterhub_config.py``` locally and then used FileZilla to upload the modified config file to the server.

After the modified ```jupyterhub_config.py``` file is uploaded to the server, restart JupyterHub and make sure there no errors.

```text
$ sudo systemctl start jupyterhub
$ sudo systemctl status jupyterhub
# [Ctrl]+[c] to exit
```

## Summary

In this section we added a few extra configuration options to the ```jupyterhub_config.py``` file. A few extra configuration options we included were to limit the number of servers that can run at the same time and limit the amount of servers that can spawn at the same time.

We also added a ```cull_idle_servers.py``` script to the server which will shut down idle servers if a student has not used them in a while. This involved copying the script locally from GitHub, then uploading the script on the server in the ```/etc/jupyterhub/``` directory. The ```jupyterhub_config.py``` file has to be modified so that ```sys``` is imported and the ```cull_idle_servers.py``` script runs and a JupyterHub service

Finally we uploaded the modified ```jupyterhubconfig.py``` configuration file and restarted JupyterHub.

## Additional Extras

That's it for the main JupyterHub deployment! The next section is about periodic maintenance. After running JupyterHub for two quarters there are a couple lessons learned server regarding maintenance.

<br>
