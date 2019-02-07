# /etc/jupyterhub/jupyterhub_config.py
# Simple PAM Authenticator Configuration

c = get_config()
c.JupyterHub.log_level = 10
c.Spawner.cmd = '/opt/miniconda3/envs/jupyterhub/bin/jupyterhub-singleuser'

# Cookie Secret Files
c.JupyterHub.cookie_secret_file = '/srv/jupyterhub/jupyterhub_cookie_secret'
c.ConfigurableHTTPProxy.auth_token = '/srv/jupyterhub/proxy_auth_token'

# Users
c.Authenticator.whitelist = {'peter'}
c.Authenticator.admin_users = {'peter'}