import logging
from logging import StreamHandler


def get_logger(name):
    log_format = "%(asctime)s %(name)s : %(levelname)s : %(message)s"

    loggers = [logging.getLogger()]  # get the root logger
    loggers = loggers + [logging.getLogger(name) for name in logging.root.manager.loggerDict]
    for l in loggers:
        l.handlers.clear()

    logging.basicConfig(
        level='INFO',
        format=log_format,
        datefmt='[%X]',
        handlers=[StreamHandler()],
        force=True
    )

    logger = logging.getLogger(name, )
    logger.info(f"initialized logger for {name}")
    return logger
