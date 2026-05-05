import sys
from networksecurity.logging import logger

def error_mess_detail(error,error_detail:sys):
  _,_,exc_tb=error_detail.exc_info()
  filename=exc_tb.tb_frame.f_code.co_filename
  error_message="error occured in py script name [{0}] linenumber [{1}] errormessage [{2}]".format(filename,exc_tb.tb_lineno,str(error))
  return error_message

class NetworkSecurityException(Exception):
  def __init__(self, error_message,error_detail:sys):
    super().__init__(error_message)
    self.error_message=error_mess_detail(error_message,error_detail=error_detail)

  def __str__(self):
    return self.error_message
  

if __name__=="__main__":
  try:
    logger.logging.info("enter the try block")
    a=1/0
    print("this will not be printed",a)
  except Exception as e:
    raise NetworkSecurityException(e,sys)