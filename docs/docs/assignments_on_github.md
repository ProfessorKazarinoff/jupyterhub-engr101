# Assignments on GitHub

Now we'll build a set of pre-constructed assignments and notes for each JupyterHub user. We'll save these assignments and notes to a GitHub repo.

[TOC]

## Create a repo of assignments on GitHub.com

On GitHub.com, create a new repo with the notes and assignments for the quarter.

![new repo]()

![repo details]()

## Pull the repo down from GitHub.com to the local computer

On a local computer, not the server, clone the GitHub repo. This allows us to work on the notes and assignments locally.

```text
# local computer
$ mkdir ENGR101
$ cd ENGR101
$ git init
$ git remote add origin https://github.com/username/reponame.git
$ git pull origin master
```

## Create the assignments and notes

On the local computer, not the server, build the assignment and notes for the quarter. I did this using Jupyter notebooks.

## Push the completed assignments and notes up to GiHub

Then add, commit and push the changes up to GitHub.

```text
# local computer
$ git add .
$ commit -m "added assignments and notes"
$ git push origin master
```

## Summary

## Next Steps
