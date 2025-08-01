import logging

# Configuration directe de logging
def _setup_logging(level=logging.INFO):
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

# Pour récupérer un logger par nom
def _get_logger(name=None):
    return logging.getLogger(name)

def init_logger(name="mon_logger"):
    _setup_logging()
    log = _get_logger(name)
    return log
