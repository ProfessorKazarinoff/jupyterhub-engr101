# Google Authentication

Now that the JupyterHub deployment works and we have two users set up on the server, we are going to get into the weeds of getting the Google authenticator to work. 

Why Google authenticator instead of just setting up users one by one at the command line? Our college uses the Gmail suite for both staff and students. When students log onto their college email, they are logging into Gmail. Students can use Google calendar and Google drive with their college email account as well. Instead of emailing students individual user names and passwords (and having students remember another set of usernames and passwords), students could log into JuypterHub using the same Google login that they use to access their college email, Google drive and calendar. It's just going to take a bit of work to get there.

[TOC]

## Google OAuth Instance

To allow students to use Google usernames and passwords to log into JupyterHub, the first thing we need to do is set up a Google OAuth instance. I set up the Google OAuth instance using my personal Gmail account, rather than my college Gmail account. Some parts of Google suite are not available in my college profile, like YouTube and developer tabs. 

To obtain the Google OAuth credentials, we need to log into the Google API console [https://console.developers.google.com/](https://console.developers.google.com/) and select [Credentials] on the lefthand menu.

![Google oauth credentials](images/google_oauth_credentials.png)

Next we'll create a new OAuth credential under [Credentials] --> [Create Credentials] --> [OAuth client ID]:

![Google create credentials](images/google_oauth_create_credentials.png)

To create a set of Google OAuth credentials we need to input:

 * Authorized JavaScript origins: ```https://mydomain.org```
 * Authorized redirect URIs: ```https://mydomain.org/hub/oauth_callback```

![Google js origins and callback url](images/google_oauth_javascript_origins_redirect_uri.png)

After clicking [Create] a problem surfaced. The Google OAuth dashboard noted that:

 > Invalid Origin: domain must be added to the authorized domains list before submitting

![Google OAuth Dashboard Resistrictions](images/google_oauth_restrictions.png)

So click the [authorized domains list] link and enter the domain name for the JupyterHub server in the text box under [Authorized domains].

![Google OAuth add scope](images/google_oauth_add_scope.png)

Then click [Submit for verification] and [Save]. For some reason the authorize domains submit for verification step and save step took a couple tries and more than a couple minutes. I don't know if Google is going a DNS lookup or what kind of verification steps they do - either way it took some time for the domain to be "verified".

![Google OAuth submit for verification](images/google_oauth_submit_for_verification.png)

Once the domain is verified, go back to the [Credentials] --> [Create Credentials] --> [OAuth client ID] screen and try entering in the [Authorized JavaScript origins] and [Authorized redirect URIs] again.

![Google OAuth re_enter domain](images/google_oauth_re_enter_domain.png)

The scary red [Invalid Origin] should be absent as long as the domain has been verified.

After creating a new set of Google OAuth credentials, note the:

 * client ID
 * client secret
 
![Google client ID and secret](images/google_oauth_client_id_and_secret.png)
 
 The client ID and client secret strings will be included in our revised JupyterHub configuration.

For this JupyterHub Deployment, I also downloaded the json file that contains the client ID and client secret. You can access the json file containing the client ID and client secret by clicking the [Credentials] tab and find the credential you just created. On the right hand side is a download icon. Clicking this icon downloads the json file.

![Google OAuth Credentials Tab](images/google_oauth_credentials_tab.png)

![Google OAuth Credentials Tab](images/google_oauth_credentials_tab_download_json.png)

Download the json file. It has a structure that looks kind of like this:

```text
{"web":
    {"client_id":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.apps.googleusercontent.com",
    "project_id":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "auth_uri":"https://accounts.google.com/o/oauth2/auth",
    "token_uri":"https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs",
    "client_secret":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "redirect_uris":["https:XXXXXXXXXXXXXXX/hub/oauth_callback"],
    "javascript_origins":["https://eXXXXXXXXXXXX.org"]
    }
 }
```

On a local computer, rename the json file to ```google_oauth_credentials.json```. Then we can use Python and the ```json``` module to pull out the ```"client_id"``` and ```"client_secret"```. Make sure the json file is in the same directory on your local computer where the code is run. Try the following Python code on your local computer:

```python
with open('google_oauth_credentials.json') as f:
    google_oauth = json.load(f)

print(google_oauth['web']['client_id'])
print(google_oauth['web']['client_secret']
```

The output will be the ```'client_id'``` and ```'client_secret'``` from the json file.

Now we need to move the ```google_oauth_credentials.json``` to the sever and **MAKE SURE TO ADD THE FILE TO .gitignore** we **DON'T WANT CREDENTIALS STORED ON GITHUB**.

In ```.gitignore``` on my local machine, I added the following lines at the end. Note that locally this file is saved at ```projectroot/etc/jupyterhub/google_oauth_credentials.json```

```text
# .gitignore

...

## Config files

/etc/jupyterhub/config.json
/etc/jupyterhub/google_oauth_credentials.json

...

```

Now move the json file over to the server and save it in the ```/etc/jupyterhub/``` directory. I used FileZilla for this instead of copy-paste into PuTTY and the nano code editor.

Open FileZilla and select [File] --> [Sites]. Enter in the server's IP address and select the SSH key used to log into the server.
![]()

Move both file browsers to ```/etc/jupyterhub```. On the local computer, the json file is present. On the server, only the jupyterhub config file is present.

![]()

Drag the json file over to the server side of the window.

![]()

Now you can close the FileZilla window.

After the json file is saved on the server, the contents of ```/etc/jupyterhub``` should be:

```text
/etc/jupyterhub/
├── google_oauth_credentials.json
└── jupyterhub_config.py
```

## Modify jupyterhub_config.py

Once we get our Google OAuth credentials, we need to edit ```jupyterhub_conf.py``` again. Note your Google OAuth credentials are replaced by the credentials from the ```google_oauth_credentials.json``` file. .

```python
# /etc/jupyterhub/jupyterhub_conf.py

import json # used to read the json google oauth config file

# For Google OAuth
from oauthenticator.google import LocalGoogleOAuthenticator
c.JupyterHub.authenticator_class = LocalGoogleOAuthenticator

# Set up config
c = get_config()
c.JupyterHub.log_level = 10
c.Spawner.cmd = '/opt/miniconda3/envs/jupyterhubenv/bin/jupyterhub-singleuser'

# Cookie Secret and Proxy Auth Token Files
c.JupyterHub.cookie_secret_file = '/srv/jupyterhub/jupyterhub_cookie_secret'
c.ConfigurableHTTPProxy.auth_token = '/srv/jupyterhub/proxy_auth_token'

# Google OAuth Login
with open('google_oauth_credentials.json') as f:
    google_oauth = json.load(f)

c.LocalGoogleOAuthenticator.client_id = google_oauth['web']['client_id']
c.LocalGoogleOAuthenticator.client_secret = google_oauth['web']['client_secret']

c.LocalGoogleOAuthenticator.oauth_callback_url = 'https://engr101lab.org/hub/oauth_callback' # replace with your domain
c.LocalGoogleOAuthenticator.create_system_users = True
c.Authenticator.add_user_cmd = ['adduser', '-q', '--gecos', '""', '--disabled-password', '--force-badname']
c.LocalGoogleOAuthenticator.hosted_domain = 'pcc.edu'   # replace with collegedomain.edu
c.LocalGoogleOAuthenticator.login_service = 'Portland Community College'  # replace with 'College Name'

``` 

This little line:

```python
c.Authenticator.add_user_cmd = ['adduser', '-q', '--gecos', '""', '--disabled-password', '--force-badname']
```

was a real gottacha. Our college email addresses are in the form:

```firstname.lastname@college.edu```

When a student logs in, JupyterHub tries to create a new Linux user with a dot ```.``` in their username. Usernames with ```.``` doesn't work on Linux. I tried to create a new Linux user with a dot in their username, and the terminal asked me to use the ```--force-badname``` flag. So ```--force-badname``` is what we'll add to the ```c.Authenticator.add_user_cmd``` list. Otherwise, users (students) will be able to authenticate with Google, but they won't get a new user account on the server, and they won't be able to run notebooks or Python code.

## Restart JupyterHub and Login

Restart JupyterHub and browse to the web address attached to the server.

```
$ sudo systemctl stop jupyterhub
$ sudo systemctl start jupyterhub
$ sudo systemctl status jupyterhub
# [Ctrl + c] to exit
```

The login window should now look something like:

![Sign in with Google](images/sign_in_with_google.png)

We can log in with our Google user name and password (college username and password). 

Pretty sweet!

After we log in using our college username and password, we can see if JupyterHub created a new user (with our college username) on the server. The command below produces a long list of users. This long list contains the non-root sudo user ```peter``` and the Google authenticated user (college username).

```text
$ awk -F':' '{ print $1}' /etc/passwd
....
uuidd
dnsmasq
landscape
sshd
pollinate
peter
peter.lastname
githubusername
```

<br>

## Next Steps

The next step is to use the JupyterLab interface as the default interface. This means when students log into JupyterHub, they see JupyterLab instead of the typical Jupyter notebook file browser.

<br>
