# CLI App Template for Python

This is a simple template for creating CLI applications in Python.

You can build your console application in [app/app.py](app/app.py)

This template uses the `argparse` module. (For details see the [official documentation](https://docs.python.org/2.7/library/argparse.html).)

## Recieving Inputs
In app.py is a function called `main`:

``` python
def main(args, options):
```

All input arguments are passed into `args` as an array.
If you want to use optional arguments, add them using `argparse`'s `parser.add_argument` in [cli.py](cli.py)

## Outputting Results
Use the `print` method to return results.

``` python
def main(args, options):
  results = do_something(args)
  print(results)
```

## Installing External Libraries
If you want to use external libraries, do the following:

- Write the library name and version in `requirements.txt`
- Add the following to `codecheck.yml`:

``` yaml
build:
  - pip install -r requirements.txt
```
