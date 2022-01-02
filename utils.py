import logging
import colorlog
import coloredlogs

def get_logger(module, file_name):
    logger = logging.getLogger(module)
    logger.setLevel(logging.INFO)

    # stream_handler = logging.StreamHandler()
    # stream_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(module)s %(message)s'))
    file_handler = logging.FileHandler(file_name)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(module)s %(message)s'))

    # logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

    coloredlogs.install()
    coloredlogs.BasicFormatter('%(asctime)s %(levelname)s %(module)s %(message)s')
    return logger

