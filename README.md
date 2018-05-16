# Primer on Python Decorators #

## About ##

This is a set of working examples from the [Primer on Python Decorators] by [Real Python]. Some of the examples (mostly the Flask ones) are editted to actually work and not just show out the use of decorators.

Although the tutorial uses Python 3, this examples are actually in Python 3. The differences are only in the `print` syntax and a use of `xrange` instead of `range` in some cases.

## Usage ##

To run the Flask examples:

1. Install [Flask]:
   * `pip install flask`
2. Run the app:
   * `FLASK_APP=login_required.py flask run`
   * `FLASK_APP=validate_json.py flask run`

## Credit ##

* [Real Python] website


[Primer on Python Decorators]: https://realpython.com/primer-on-python-decorators/
[Real Python]: https://realpython.com/primer-on-python-decorators/
[Flask]: http://flask.pocoo.org/