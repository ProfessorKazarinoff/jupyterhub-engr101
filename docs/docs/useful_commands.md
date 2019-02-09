# Useful Commands

Below are some useful commands for setting up and running JupyterHub 

### kill configurable-http-proxy

```
ps aux | grep configurable-http-proxy
kill ####                
```

### nginx

```
sudo service nginx stop
sudo service nginx start
sudo service nginx restart
nginx -t
```

### Shutdown and restart server

```
sudo shutdown -r now
```

### Start JupyterHub with sudo (need to do this to allow other users to logon)

```
sudo /home/peter/anaconda3/bin/jupyterhub
```

### Start jupyterhub as service, will run continuously

```
sudo systemctl start jupyterhub
sudo systemctl <start|stop|status> jupyterhub
```

### Add environmental variables:

```
$ export OAUTH_CLIENT_SECRET=xxxxxxxxxxx
```

### Gitpuller extension URLs

```
https://domain.org/hub/user-redirect/git-pull?repo=GitHubUserName%2FRepoName&branch=master&app=lab
```

### change the systemctl start jupyterhub configurations

If changes are made to ```/etc/systemd/system/jupyterhub.service``` needs to reload:

```
sudo systemctl daemon-reload
sudo systemctl start jupyterhub
```
