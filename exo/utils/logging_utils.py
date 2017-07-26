import logging

def setup_logger(logger, level=logging.DEBUG):
    logger.setLevel(level)
    ch = logging.StreamHandler()
    ch.setLevel(level)
    formatter = logging.Formatter('%(levelname)s [%(name)s] - %(asctime)s : %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger
