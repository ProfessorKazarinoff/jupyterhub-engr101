# Draw.IO Extension

In my ENGR114 class, students learn how to construct flow charts that describe the way a program runs. Students also use flowcharts to plan how a program will run. We can provide students access to a flow chart drawing program right in JupyterHub called [**Draw.IO**](https://www.draw.io/). Draw.IO will can added to our JuptyerHub deployment as a JupyterLab extension.

[TOC]

## Install nodejs

Ensure that nodejs is intalled in the ```(jupyterhub)``` virtual environment. Nodejs is needed to install the Draw.IO JupyterLab extension.

```
$ sudo systemctl stop jupyterhub
$ conda activate jupyterhube
(jupyterhub)$ conda install -c conda-forge nodejs
```

## Install Draw.IO extension for JupyterLub

Type another conda install line to install the Draw.IO extension for
JupyterLab.

```
(jupyterhubenv)$ jupyter labextension install jupyterlab-drawio
```

## Restart JupyterHub and test it out

```
$ sudo systemctl start jupyterhub
$ sudo systemctl status jupyterhub
[Ctrl]-[c] to exit
```

Below are some screen captures of the Draw.io extension in action. Students need to click the [Diagram] icon in the JupyterLab [Launcher] window to open a new Draw.IO drawing.

![Draw.IO Extension Launcher Tile](images/jupyterlab_add_launcher.png)

![Draw.IO Window](images/jupyterlab_add_diagram_block.png)

![Draw.IO Flow Chart](images/draw_dot_io_flow_chart.png)

## Summary

Draw.io is a drawing program students can use to create flow charts. Draw.io can be installed as a JupyterLab extension in our JupyterHub deployment. To install Draw.io into JupyterHub, first install nodejs and then install the Draw.io extension.

<br>
