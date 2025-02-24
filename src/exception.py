import sys


def error_message_detail(error, error_detail: sys):
    """
    Formats error message with file name, line number, and original error.
    """        
    _, _, exc_tb = error_detail.exc_info()  # Get traceback object
    file_name = exc_tb.tb_frame.f_code.co_filename  # Get file where error occurred
    line_number = exc_tb.tb_lineno  # Get line number
    error_message = f"Error in {file_name}, line {line_number}: {str(error)}"
    
    return error_message


class CustomException(Exception):
    """
    Custom Exception class to log detailed error messages with traceback.
    """
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)  # Pass base error message
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message

  
    