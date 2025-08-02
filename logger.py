import logging

def _setup_logging(level=logging.INFO):
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

def _get_logger(name=None):
    return logging.getLogger(name)

def init_logger(name="weather_logger", level=logging.INFO):
    _setup_logging(level)
    return _get_logger(name)