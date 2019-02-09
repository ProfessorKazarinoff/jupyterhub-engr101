# Extra Configuration

In this section, we will go over some extra configuration settings we can set in ```jupyterhub_config.py``` to help our JupyterHub deployment hum along and help if students forget to logout or too many student try and log in at the same time. 



## Summary

In this section we installed the nbgitpuller plugin for JupyterHub. Then we created a custom URL. When we browse to the custom URL, we enter our JupyterHub environment with all the files contained on GitHub placed in our user directory. 

This is a great plugin to have with JupyterHub. Now when we make changes to the Labs or Assignments in the GitHub Repo, those changes are reflected when students log into JupyterHub with the special URL.

## Next Steps

Next, we'll configure JupyterHub to automatically go the the URL we setup with the nbgitpuller plugin. So when students go to ```domain.org``` they get the same files as if they went to the custom plugin URL ```https://mydomain.org/hub/user-redirect/git-pull?repo=GitHubUserName%2FRepoName&branch=master&app=lab```

