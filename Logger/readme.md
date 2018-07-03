# Log Module:

- Func setup_logger: logger_name, log_file, level
  * Logger Name --> Name of your logger
  * Logger file --> .\to\your\logger\yourFileName.log
  * Level --> level of your data to be logged, either INFO/DEBUG INFO/..
  * Change MaxBytes to the value you want the logger to roll
  
- Func log_data: logger_name, msg
  * logger_name: Name of your logger
  * msg: msg to be logged. Type String.
  
 ## Use Case:
 - import log
 - log.setup_logger(logger_name='log_id', log_file= "/path/to/logFiles/myLog.log")
 - log.log_data(logger_name='log_id', msg=msg_to_be_saved)
