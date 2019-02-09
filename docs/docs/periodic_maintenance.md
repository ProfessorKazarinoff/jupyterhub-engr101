# Periodic Maintenance

After running JupyterHub for two quarters there are a couple lessons I've learned about maintenance. 

## Restart server once a week

The Hub has seemed to get sluggish when it has been running for a long time continously. Shutting the down JupyterHub, Nginx, then restarting the server once each week is a good idea. To restart the server, first log into JupyterHub and shut down all the servers. The from the command line, run :

```text
$ sudo systemctl stop jupyterhub
$ sudo systemctl stop nginx
$ reboot #?
# shutdown -h now ?
```

Then go to the Digital Ocean dashboard and restart the server. After the server restarts, restart nginx then JupyterHub.

```text
$ sudo systemctl start nginx
$ sudo systemctl status nginx
$ sudo systemctl start jupyterhub
$ sudo systemctl status jupyterhub
```

## Increase server size before class starts

Right at the start of class, when everyone logs in, the server can get overloaded. So during only those class times when 24 students plus 1 instructor will all be on the Hub at the same time, boost the server size to a $40/month or maybe even up to an $80/month server. You can update the server size at the Digital Ocean Dashboard. 

Then remeber to drop the server size back down after class. Don't want to rack up a huge bill with Digital Ocean.

## Extras

There are a couple extra docs pages. Browse through these if you want to use the JupyterLab interface, include a GitHub in the JupyterLab interface or try and make the regular domain name go to the nbgitpuller domain name.

<br>
 