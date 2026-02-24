# Imports
import os
import logging
from datetime import datetime
from colorama import Fore, Style, init

# Necessário para cores funcionarem corretamente no Windows
init(autoreset=True)


class ColorFormatter(logging.Formatter):
    COLORS = {
        "DEBUG": Fore.CYAN,
        "INFO": Fore.GREEN,
        "WARNING": Fore.YELLOW,
        "ERROR": Fore.RED,
        "CRITICAL": Fore.RED + Style.BRIGHT,
    }

    def format(self, record):
        color = self.COLORS.get(record.levelname, "")
        message = super().format(record)
        return f"{color}{message}{Style.RESET_ALL}"


def setup_logger(pasta_log="./logs"):
    os.makedirs(pasta_log, exist_ok=True)

    log_file = os.path.join(
        pasta_log,
        f"log_{datetime.now().strftime('%Y%m%d_%H%M')}.log"
    )

    logger = logging.getLogger()       # root logger
    logger.setLevel(logging.INFO)

    # Evita handlers duplicados ao importar múltiplas vezes
    if logger.handlers:
        return logger

    # ========================================
    # Handler de LOG EM ARQUIVO (sem cores)
    # ========================================
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(
        logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s",
            "%Y-%m-%d %H:%M:%S"
        )
    )

    # ========================================
    # Handler de LOG NO CONSOLE (com cores)
    # ========================================
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(
        ColorFormatter("%(asctime)s | %(levelname)s | %(message)s")
    )

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
