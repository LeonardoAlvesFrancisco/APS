import logging

class LogginManager:
    
    def setup_logging(self) -> object:
        logging.basicConfig(level=logging.INFO)