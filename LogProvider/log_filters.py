import logging


@DeprecationWarning
# Create own contextual information
class ContextFilter(logging.Filter):
    def filter(self, record):
        pass
        record.module = module
        return True
