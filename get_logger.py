import logging

import sys


def get_module_logger(name):
    """Get a logger for the name module

    Parameters
    ----------
    name : str
        the name of the module. Can be the builtin `__name__`

    Returns
    -------
    TYPE
        (logger)[https://docs.python.org/2/library/logging.html#logging.Logger]\
         instance.
    """
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    return logging.getLogger(name)
