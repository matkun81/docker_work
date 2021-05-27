import logging


class Logger:
    logger = logging.getLogger("Logger")

    @staticmethod
    def info(str_):
        logging.info(str_)

    @staticmethod
    def error(str_):
        logging.error(str_)

    @staticmethod
    def list_log_output(object_list):
        for i in object_list:
            Logger.info(i.__dict__)
