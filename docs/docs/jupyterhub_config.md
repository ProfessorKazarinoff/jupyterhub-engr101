# JupyterHub Configuration

Next, we'll create a ```jupyterhub_config.py``` file and modify it to include our cookie secret and proxy auth token. 

[TOC]

## Create jupyterhub_config.py

We'll create the JupyterHub config file in the ```/etc/jupyterhub``` directory. After the directory is created, we need to modify the directory permissions. Then ```cd``` into it create the config file with the command ```jupyterhub --generate-config```. Make sure you are in the ```(jupyterhub)``` virtual environment when you run the command.  

```text
$ cd /etc
$ sudo mkdir jupyterhub
$ sudo chown -R root:peter jupyterhub/
$ sudo chmod -R g+rwx jupyterhub/
$ cd jupyterhub
$ conda activate jupyterhub
(jupyterhub)$ jupyterhub --generate-config
(jupyterhub)$ ls

jupyterhub_config.py
```

## Modify jupyterhub_config.py

Now we'll modify the ```jupyterhub_config.py``` file to allow local spawners and include our user ```peter``` as an admin user:

```text
$ nano jupyterhub_config.py
```

There will be a lot of commented out text in the ```jupyterhub_config.py``` file. At the top of the file, add the following:

```python
# /etc/jupyterhub/jupyterhub_config.py
# PAM Authenticator

c = get_config()
c.JupyterHub.log_level = 10
c.Spawner.cmd = '/opt/miniconda3/envs/jupyterhub/bin/jupyterhub-singleuser'

# Cookie Secret Files
c.JupyterHub.cookie_secret_file = '/srv/jupyterhub/jupyterhub_cookie_secret'
c.ConfigurableHTTPProxy.auth_token = '/srv/jupyterhub/proxy_auth_token'

# Users
c.Authenticator.whitelist = {'peter'}
c.Authenticator.admin_users = {'peter'}

...
```

<br>

## Restart Nginx and start Jupyterhub, see if we can login

Now we'll restart Nginx.

If it seems like Nginx isn't working, try ```$ sudo systemctl status nginx``` and see if Nginx really started. If it didn't, try the command ```nginx -t```. This command prints out any error messages if Nginx failed to start. I had to trouble shoot the Nginx configuration many a lot before I got Nginx and JupyterHub working together.

```text
$ sudo systemctl stop nginx
$ sudo systemctl start nginx
$ sudo systemctl status nginx
# [Ctrl]+[c] to exit
```

Once Nginx is running, try to restart JupyterHub without the ```--no-ssl``` flag. Make sure the ```(jupyterhubenv)``` virtual environment is active before running the ```jupyterhub``` command.

```text
$ cd /etc/jupyterhub
$ conda activate jupyterhub
(jupyterhub)$ jupyterhub
```

Expect to get an error at this point due to the permissions we set for our ```cookie_secret``` and ```proxy_auth_token``` files. Since these files are set to permissions that only the sudo owner can read and write, running JupyterHub as the user ```peter``` won't work. When JupyterHub starts up, it won't be able to access the ```cookie_secret``` and ```proxy_auth_token``` files.

We will remedy this situation in the next step: running JupyterHub as a system service. The system service will run as root and the permissions we set for the ```cookie_secret``` and ```proxy_auth_token``` files will not be a problem.

## Summary

In this section we created a ```jupyterhub_config.py``` file and included a minimal configuration to use the local PAM authenticator (Linux login usernames and passwords). We restarted Nginx, but could not run JupyterHub because of the permissions set to the ```cookie_secret``` and ```proxy_auth_token``` files.

## Next Steps

The next step is to run JupyterHub as a system service. This allows JupyterHub to run continuously even if we aren't logged into the server. It also allows us to work on our JupyterHub deployment while it is still running.

<br>
