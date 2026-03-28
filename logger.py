import sys
from datetime import datetime
import time
import functools

class Logger:
    _instance = None

    levels = ["DEBUG","INFO", "WARNING", "ERROR", "CRITICAL"]

    def __new__(cls,level="DEBUG"):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.level = level
            cls._instance.level_index = cls._instance.levels.index(level)
        return cls._instance
    
    def _log(self, level_name,msg):
        if self.levels.index(level_name) >= self.level_index:
            time_str = datetime.now().strftime("%H:%M:%S")
            print(f"[{time_str}] [{level_name}]", {msg},file=sys.stdout)

    def debug(self, msg):
        self._log("DEBUG", msg)

    def info(self, msg):
        self._log("INFO", msg)

    def warning(self, msg):
        self._log("WARNING", msg)

    def error(self, msg):
        self._log("ERROR", msg)

    def critical(self, msg):
        self._log("CRITICAL", msg)

    def set_level(self, level):
        if level in self.LEVELS:
            self.level = level
            self.level_index = self.LEVELS.index(level)

    def calc_time(self,level="DEBUG"):

        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                start_time = time.time()
                result = func(*args, **kwargs)
                end_time = time.time()
                elapsed = (end_time - start_time) * 1000
                self._log(level, f"Function '{func.__name__}' took {elapsed:.f} ms")
                return result
            return wrapper
        return decorator