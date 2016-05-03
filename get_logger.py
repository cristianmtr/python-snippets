import logging


# Python's logging framework creates a single instance
# for each 'name' logger
# we need to make sure to return the same
# instance for the same 'name'
# e.g. Runnable class instances use the same logger
# see http://stackoverflow.com/questions/7173033/duplicate-log-output-when-using-python-logging-module
loggers = {}

def get_module_logger(name):
    """Get a logger for the module name

    Args:
        name (string): name of the module

    Returns:
        TYPE: (logger)[https://docs.python.org/2/library/logging.html#logging.Logger]\
             instance.

    """
    global loggers
    if loggers.get(name):
        return loggers.get(name)
    else:
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
        loggers[name] = return_logger
        return return_logger
