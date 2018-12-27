# Mashhadlug Website

The repository of mashhadlug website, located at [mashhadlug.com](mashhadlug.com).

# How to Contribute

Mashhadlug website is made using [pelican static site genrator](getpelican.com).  

## Cloning and Installing

We recommend installing `pelican` and the required libraries inside a virtual environment as follows:

```bash
$ git clone git@github.com:mashhadlug/www.git
$ cd www
$ git checkout master
$ python -m venv .env
$ source .env/bin/activate
$ pip install pelican markdown ghp-import
```

## Running a Development Web Server

to create a development server run the following command

```bash
$ make devserver
```

You can open [localhost:8000](http://localhost:8000/) to view the website.

## Making Changes in the Development Environment

First make sure that your repository is updated and the virtual environment is activated:

```bash
$ git pull
$ git checkout master
$ source .env/bin/activate
```

To change the content of the website you need to edit the markdown files located inside different folders in  `contents` folder.

#### Editing the index

edit the `contents/pages/index.md` file to change the index of the website.

#### Making a new session report

Session reports are placed inside the `contents/reports` directory. you need to create a folder for each new session. **Note that any files related to the session should be placed inside that session's directory**.

#### Preview the changes in the web server.

To manually update your changes to be shown in web server running on your localhost run

```bash
$ pelican content -s pelicanconf.py
```

## Publish the Website

to update the master branch run

```bash
$ git push origin master
```

To publish the changes to github's `gh-pages` branch simply run

```bash
$ make github
```

When you're done, you can deactivate the virtual environment

```bash
$ deactivate
```



