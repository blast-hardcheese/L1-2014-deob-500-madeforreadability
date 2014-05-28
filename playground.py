from shiftops import *

#from uncompyle2 import uncompyle

from mydis import disassemble

from StringIO import StringIO

def target():
    print "Hey"

import dis

co_code = target.func_code.co_code

out = StringIO()

code = type(target.func_code)

c = target.func_code.co_code
codestring = c

consts = target.func_code.co_consts
varnames = target.func_code.co_varnames
names = target.func_code.co_names

#print consts
#consts = ('?', 'why')
#names = ('what',)
#varnames = ('woo',)

target.func_code = code(
    target.func_code.co_argcount,
    target.func_code.co_nlocals,
    target.func_code.co_stacksize,
    target.func_code.co_flags,
    codestring,
    consts,
    names,
    varnames,
    target.func_code.co_filename,
    target.func_code.co_name,
    target.func_code.co_firstlineno,
    target.func_code.co_lnotab,
)

#uncompyle('2.7', target.func_code, out=out)

#out.seek(0)
#print out.read()

dis.dis(target)
#target()
