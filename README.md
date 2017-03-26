# HowTo

```
$ git clone git@github.com:mashhadlug/next.git
$ cd next
$ virtualenv3 .env
$ source .env/bin/activate
$ pip install pelican
$ make devserver
```

You can open [localhost:8000](http://localhost:8000/).
To manually update your changes to be shown in
webserver running on your localhost:

```
$ pelican content -s pelicanconf.py -t template
```

Also To publish changes to github's `gh-pages` branch simply run:

```
# .. make changes
$ make github
```

# Demo

[next.mashhadlug.org](http://next.mashhadlug.org/)
