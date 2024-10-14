import logging

# ANSI escape codes for formatting log output in the terminal
GREEN = '\033[92m'  # Green text formatting
RED = '\033[91m'  # Red text formatting
YELLOW = '\033[93m'  # Yellow text formatting
BOLD = '\033[1m'  # Bold text formatting
RESET = '\033[0m'  # Reset formatting to default

# Custom logging format with color and bold style
LOG_FORMAT = '%(asctime)s - %(name)s - ' + BOLD + '%(levelname)s' + RESET + ' - ' + BOLD + '%(message)s' + RESET


class CustomFormatter(logging.Formatter):
    """Custom formatter to apply color to logs based on their log level."""
    
    def format(self, record):
        # Apply color based on the log level
        if record.levelname == 'INFO':
            record.levelname = GREEN + record.levelname + RESET
        elif record.levelname == 'WARNING':
            record.levelname = YELLOW + record.levelname + RESET
        elif record.levelname == 'ERROR':
            record.msg = RED + record.msg + RESET
        return super().format(record)


def configure_logging(level=logging.INFO):
    """
    Configures the logging settings with custom colors and styles.
    
    :param level: Logging level to set (default: INFO).
    """
    # Set up the logger
    logger = logging.getLogger()
    logger.setLevel(level)

    # Create a stream handler for console output
    handler = logging.StreamHandler()

    # Set a custom formatter with color coding
    handler.setFormatter(CustomFormatter(LOG_FORMAT))

    # Add the handler to the logger
    logger.addHandler(handler)

    # Optional: Display a startup log message
    logger.info("Logging has been configured.")


