import logging
import os

# Log Level - note: This is the only env setting that is consumed outside the config class due to the circular import
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")


def get_log_level(log_level_str: str) -> int:
    """Retrieves the logging level numeric value based on a string
    representation.

    This function takes a string that represents a logging level ("CRITICAL", "ERROR",
    "WARNING", "INFO", "DEBUG") and returns the corresponding numeric value defined in
    the logging module. If the provided string does not match any of the predefined
    levels, it defaults to returning the numeric value for "INFO".

    Args:
        log_level_str (str): The string representation of the desired logging level.
                             It is case-insensitive.

    Returns:
        int: The numeric value of the logging level from the logging module. Defaults to
             logging.INFO if the `log_level_str` is not recognized.
    """
    level_dict = {
        "CRITICAL": logging.CRITICAL,
        "ERROR": logging.ERROR,
        "WARNING": logging.WARNING,
        "INFO": logging.INFO,
        "DEBUG": logging.DEBUG,
    }
    return level_dict.get(log_level_str.upper(), logging.INFO)


def configure_logging():
    """Configures the basic settings for the logging system.

    This function sets up the logging configuration for the application, including the log level and format. It is designed to be called once at the start of the application. If the logging system is already configured, indicated by a custom attribute on the logging module, this function will not reconfigure it.

    The configuration sets the logging level based on the `LOG_LEVEL` environment variable and specifies a format for log messages that includes the timestamp, log level, logger name, and function name.

    Note:
        This function uses a custom attribute `_configured` on the `logging` module to ensure that the logging configuration is only applied once, even if the function is called multiple times.
    """
    if not getattr(logging, "_configured", False):
        logging.basicConfig(
            level=get_log_level(LOG_LEVEL),
            format="%(asctime)s - %(levelname)s - %(name)s - %(funcName)s: %(message)s",
        )
        setattr(logging, "_configured", True)


def get_logger(name: str) -> logging.Logger:
    """Creates and returns a logger with a specified name.

    This function creates a logger instance using the provided name. If the name starts
    with "azure", the logger's level is set to WARNING, otherwise, it retains the default
    logging level. This is particularly useful for controlling log output verbosity on a
    per-logger basis.

    Args:
        name (str): The name of the logger. This name identifies the logger and can be
                    used to retrieve the same logger instance from anywhere in the
                    application.

    Returns:
        logging.Logger: The logger instance with the specified name. If the name starts
                        with "azure", the logger's level is set to WARNING.
    """
    logger = logging.getLogger(name)

    if name.startswith("azure"):
        logger.setLevel(logging.WARNING)

    return logger
