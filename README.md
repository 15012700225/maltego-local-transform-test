# maltego-local-transform-test

Very basic local transform for Maltego, useful as an example.

To install it, you need to go in Maltego `Transform > New Local Transform` and set the following fields:

* Display Name: whatever name you want for this script
* Input Entity Type: `Domain`
* Command-line: address of your python binary (be careful if you are using virtualenv to give the virtualenv python binary)
* Command parameters: the name of your script
* Working directory: the path of your toolkit folder

`Maltego.py` in this directory is a Maltego python library provided by [Paterva](https://docs.paterva.com/en/developer-portal/local-transforms/python-local-transforms-examples/).

## References

* [Paterva Python Local Transform Example](https://docs.paterva.com/en/developer-portal/local-transforms/python-local-transforms-examples/)
* [Maltego Transforms for the Lazy by Scott J Roberts](https://medium.com/@sroberts/maltego-transforms-for-the-lazy-31c067d7b79)
