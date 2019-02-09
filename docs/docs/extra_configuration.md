# Extra Configuration

In this section, we will go over some extra configuration settings we can set in ```jupyterhub_config.py``` to help our JupyterHub deployment hum along and help if students forget to logout or too many student try and log in at the same time. 

[TOC]

## Configuration Options

In the JupyterHub docs, there is a list of configuration options and descriptions:

 > [https://jupyterhub.readthedocs.io/en/stable/api/app.html](https://jupyterhub.readthedocs.io/en/stable/api/app.html)

A couple configuration options in the list seem like good ideas:

The class has 24 students, plus one instructor. In case I think 26 is a good number for the maximum that can use JupyterHub the same time. 

```text
config c.JupyterHub.active_server_limit = Int(0)
# Maximum number of concurrent servers that can be active at a time.
```

Having too many users log in all at the same time can overload the server. Let's set this as 13, so half of the class can log in at a time.

```text
config c.JupyterHub.concurrent_spawn_limit = Int(100)
Maximum number of concurrent users that can be spawning at a time.
```

A couple settings relate to shutting down the hub and if user servers shut down too. I want it set so that if I shut down the hub all the user servers are shut down too.

```text
config c.JupyterHub.cleanup_proxy = Bool(True)
# Whether to shutdown the proxy when the Hub shuts down.
```

```text
config c.JupyterHub.cleanup_servers = Bool(True)
# Whether to shutdown single-user servers when the Hub shuts down.
```

## Cull Idle Servers

A problem with the first two JupyterHub deployments was that some students would not shut down their server when they were done working. Then twenty or so servers would all run all the time. This script from the JupyterHub Examples repo looks like it might help:

 > [https://github.com/jupyterhub/jupyterhub/tree/master/examples/cull-idle](https://github.com/jupyterhub/jupyterhub/tree/master/examples/cull-idle)
 
To get it to work, it looks like you need to add the following to ```jupyterhub_config.py```

```text
c.JupyterHub.services = [
    {
        'name': 'cull-idle',
        'admin': True,
        'command': [sys.executable, 'cull_idle_servers.py', '--timeout=3600'],
    }
]
```

I don't know if the ```cull_idle_servers.py``` script has to be placed somewhere, or if that script is already part of the JupyterHub package. Maybe sticking it in the same directory as the ```jupyterhub_config.py``` file is how to do it? 

## Modify 

## Summary

In this section we installed the nbgitpuller plugin for JupyterHub. Then we created a custom URL. When we browse to the custom URL, we enter our JupyterHub environment with all the files contained on GitHub placed in our user directory. 

This is a great plugin to have with JupyterHub. Now when we make changes to the Labs or Assignments in the GitHub Repo, those changes are reflected when students log into JupyterHub with the special URL.

## Additional Extras

That's it for the main JupyterHub deployment. The next section is about periodic maintenance. After running JupyterHub for two quarters there are a couple lessons learned.

