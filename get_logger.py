import logging


def get_module_logger(name):
    """Get a logger for the module name

    Args:
        name (string): name of the module

    Returns:
        TYPE: (logger)[https://docs.python.org/2/library/logging.html#logging.Logger]\
             instance.

    """
    return_logger = logging.getLogger(name)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M')
    handler.setFormatter(formatter)
    return_logger.addHandler(handler)
    # set to DEBUG to make sure all messages get logged
    # https://docs.python.org/2/library/logging.html#logging.Logger.setLevel
    return_logger.setLevel(logging.DEBUG)
    return return_logger
