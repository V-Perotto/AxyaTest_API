import os
from typing import Any, Optional
from datetime import datetime
import logging

APP_NAME = os.environ.get("APP_NAME","axyatest_api")
CLIENT = os.environ.get("CLIENT","client_name")

TIMEZONE = os.environ.get("TIMEZONE","America/Sao_Paulo")
OUTPUT_LOG = "logger/output"

output_log_format = f"%(asctime)s - [%(levelname)s] - %(message)s"

class Logger:
    
    def __init__(self) -> None:
        pass
    
    def __add_kwargs_in_log(self, kwargs, args = "") -> str:
        count = 0
        for key, value in kwargs.items():
            count += 1
            if len(kwargs.items()) > 1:
                if count < len(kwargs.items()):
                    args += f"{key}={value} | "
                else:
                    args += f"{key}={value}"
            else:
                args += f"{key}={value}"
        return args
        
    def _message(self, message: str = '', traceId: Optional[str] = None, **kwargs: Any):
        msg = message
        if traceId:
            msg = f"ID: {traceId} | {message}"
        
        args = self.__add_kwargs_in_log(kwargs)
        if args == "":
            msg = args if message == '' else f'{msg}'
        else:
            msg = args if message == '' else f'{msg} | {args}'
        return msg

    def _create_file_log(self, datetime_now, log_per_day: bool = False) -> str:
        if log_per_day:
            return f"{OUTPUT_LOG}/{datetime_now.strftime('%Y-%m-%d')}.log"
        else:
            return f"{OUTPUT_LOG}/{datetime_now.strftime('%Y-%m-%d_%H-%M-%S-%f')}.log"
        
    def __verify_file_extension(self, filename: str) -> bool:
        if '.txt' in filename[-4:]:
            return f"{OUTPUT_LOG}/{filename}"                
        if '.log' in filename[-4:]:
            return f"{OUTPUT_LOG}/{filename}"
        if not '.log' in filename[-4:] or not '.txt' in filename[-4:]:
            return f"{OUTPUT_LOG}/{filename}.log"
        else:
            return f"{OUTPUT_LOG}/{filename}.txt"
           
    def _filename(self, filename: str = None, log_per_day: bool = True) -> str:
        if filename == None:
            return self._create_file_log(datetime.now(), log_per_day)
        else:
            return self.__verify_file_extension(filename)
    
    def __log(self, 
              level, 
              message: str = '', 
              traceId: Optional[str] = None, 
              log_format: str = output_log_format,
              log_per_day: bool = True,  
              **kwargs: Any) -> None:
        logging.basicConfig(filename=self._filename(log_per_day=log_per_day), level=level, format=f"{log_format}")
        msg = self._message(message, traceId=traceId, **kwargs)
        return msg
    
    def log_debug(self, message: str = '', traceId: Optional[str] = None, **kwargs: Any):
        logging.debug(self.__log(level=logging.DEBUG, message=message, traceId=traceId, **kwargs))
        
    def log_info(self, message: str = '', traceId: Optional[str] = None, **kwargs: Any):
        logging.info(self.__log(level=logging.INFO, message=message, traceId=traceId, **kwargs))
        
    def log_warn(self, message: str = '', traceId: Optional[str] = None, **kwargs: Any):
        logging.warning(self.__log(level=logging.WARNING, message=message, traceId=traceId, **kwargs))
        
    def log_error(self, message: str = '', traceId: Optional[str] = None, **kwargs: Any):
        logging.error(self.__log(level=logging.ERROR, message=message, traceId=traceId, **kwargs))
        
    def log_critical(self, message: str = '', traceId: Optional[str] = None, **kwargs: Any):
        logging.critical(self.__log(level=logging.CRITICAL, message=message, traceId=traceId, **kwargs))
            