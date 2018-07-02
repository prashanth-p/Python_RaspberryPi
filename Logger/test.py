import log
import time

LOG_FILE_ONE = "Log_json_2.log"
log.setup_logger(logger_name='log_id', log_file=LOG_FILE_ONE)
i = 1

while True:
    msg_to_be_saved = 'Test Messages we want to pass ' + str(i)
    log.log_data(logger_name='log_id', msg=msg_to_be_saved)
    print "Logging ... %d" %(i)
    i = i + 1
    time.sleep(0.5)
