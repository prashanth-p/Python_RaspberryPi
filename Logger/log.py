import logging
from logging.handlers import RotatingFileHandler

# func setup_logger: logger_name, log_file, level
# Logger Name --> Name of your logger
# Logger file --> .\to\your\logger\yourFileName.log
# Level --> level of your data to be logged, either INFO/DEBUG INFO/..
# Change MaxBytes to the value you want the logger to roll


def setup_logger(logger_name, log_file,maxBytes_file=10*1000*1000, level=logging.INFO):
    # Create a logger and set the logging level
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)

    # Create a file handler from our new FileHandlerWithHeader class
    # and set the logging level

    handler = RotatingFileHandler(filename=log_file, maxBytes = maxBytes_file, backupCount=7)
    handler.setLevel(logging.INFO)

    # Add formatter to the file handler.
    formatter = logging.Formatter("%(asctime)s, %(message)s", datefmt='%m/%d/%Y, %I:%M:%S')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)


# func log_data: logger_name, msg
# logger_name: Name of your logger
# msg: msg to be logged. Type String.


def log_data(logger_name, msg):
    try:
        logger = logging.getLogger(logger_name)

    except:
        print "Call setup_logger function first"

    else:
        logger.info(msg)
