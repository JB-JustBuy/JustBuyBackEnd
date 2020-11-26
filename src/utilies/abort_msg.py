import sys
import traceback
def abort_msg(e):
    error_class = e.__class__.__name__
    detail = e.args[0]
    cl, exc, tb = sys.exc_info()
    last_call_stack = traceback.extract_tb(tb)[-1]
    file_name = last_call_stack[0]
    line_num = last_call_stack[1]
    func_name = last_call_stack[2]
    # generate the error message
    err_msg = {error_class: [detail]}
    return err_msg