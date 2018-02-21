# gnc_geosat

This repo contains Python code written at Astranis for simulating GEO-Sat 
environments 

## Quickstart For Running Binaries

```
$ ./bootstrap.sh
$ source venv/bin/activate
$ # Run your binary of choice, e.g.:
```

## Python Compatibility

Generally we only aim to be compatible with Python 3.5+. If any library is
required to be compatible with both Python 2 and 3, make it obvious in the
comments.

## Organization

The `geosat` package in this repo is a
["namespace package"](https://packaging.python.org/guides/packaging-namespace-packages/).
If you add any packages (subdirectories) under `geosat/`, you will have to
update `packages` list in `setup.py`.

## Style, tests, formatting

TODO
