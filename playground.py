from shiftops import *

def target():
    import sys
    sys.exit(100)

import dis

co_code = target.func_code.co_code

code = type(target.func_code)

c = target.func_code.co_code
print repr(c)
codestring = c

target.func_code = code(
target.func_code.co_argcount, target.func_code.co_nlocals, target.func_code.co_stacksize, target.func_code.co_flags, codestring, target.func_code.co_consts, target.func_code.co_names, target.func_code.co_varnames, target.func_code.co_filename, target.func_code.co_name, target.func_code.co_firstlineno, target.func_code.co_lnotab
    )

dis.dis(target)
target()
