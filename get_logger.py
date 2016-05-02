import logging

import sys


def get_module_logger(name):
    """Get a logger for the module name

    Args:
        name (string): name of the module

    Returns:
        TYPE: (logger)[https://docs.python.org/2/library/logging.html#logging.Logger]\
             instance.

    """
    logger = logging.getLogger(name)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M')
    logger.addHandler(handler)
    # set to DEBUG to make sure all messages get logged
    # https://docs.python.org/2/library/logging.html#logging.Logger.setLevel
    logger.setLevel(logging.DEBUG)
    return logger
