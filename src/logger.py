import logging
import sys

# Configura o logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Configura o formato das mensagens de log
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Configura o handler para enviar logs para a saída padrão (console)
stream_handler = logging.StreamHandler(stream=sys.stdout)

# Define as cores para cada nível de log
COLORS = {
    logging.DEBUG: '\033[94m',  # Azul
    logging.INFO: '\033[92m',   # Verde
    logging.WARNING: '\033[93m',  # Amarelo
    logging.ERROR: '\033[91m',    # Vermelho
    logging.CRITICAL: '\033[91m',  # Vermelho
}
RESET_COLOR = '\033[0m'  # Reseta a cor

class ColoredFormatter(logging.Formatter):
    def format(self, record):
        log_color = COLORS.get(record.levelno, '')
        message = super().format(record)
        return f"{log_color}{message}{RESET_COLOR}"

stream_handler.setFormatter(ColoredFormatter(formatter._fmt, datefmt=formatter.datefmt))

# Adiciona o handler ao logger
logger.addHandler(stream_handler)

