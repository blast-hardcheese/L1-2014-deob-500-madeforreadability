import sys

from shiftops import replace, shift_ops
from mydis import disassemble

import hashlib

def build(codestring):
    retval=(lambda x:x)
    code=type(retval.func_code)

    argcount = 0
    nlocals = 14
    stacksize = 11
    flags = 67

    code_md5 = hashlib.md5()
    code_md5.update(codestring)
    codehash = code_md5.digest()

    constants = (None,-1,codehash,'',97,41,3,50,69,592704,0.33333,7,10,1,3364,16,2,56,4,44,'t',6,'i',-8,'G',0,10000,5,17,13,'w',32,73,'e')
    names = ('hashlib','md5','update','___','func_code','co_code','digest','exit','join','range','sum','chr','math','__builtins__','raw_input','int','upper','round','sqrt','map','str','lower','ord','zfill','len','sys')
    varnames = (
    'hashlib',
    '',
    '',
    '',
    'math',
    '',
    '',
    '',
    '',
    '',
    'map',
    'str',
    'eval',
    'int'
    )
    filename = 'asdf'
    name = 'module name?'
    firstlineno = 1
    lnotab = '\x00\x01'

    retval.func_code=code(argcount, nlocals, stacksize, flags, codestring, constants, names, varnames, filename, name, firstlineno, lnotab)

    return retval

codestring = open('co_code').read().strip()

c = codestring
c = replace(c,   4, '\x09'*2)  # Jump fix
c = replace(c,  80, '\x09'*3)  # Jump fix
c = replace(c, 178, '\x09'*3)  # Jump fix
c = replace(c, 220, '\x09'*3)  # Jump fix
codestring = c

#codestring = shift_ops(codestring, 375, 10)

___ = build(codestring)

try:
    co = ___.func_code
    disassemble(co)
except Exception as e:
    print e

import traceback, code
try:
    pass
    ___()
except Exception as e:
    type, value, tb = sys.exc_info()
    traceback.print_exc()
    last_frame = lambda tb=tb: last_frame(tb.tb_next) if tb.tb_next else tb
    frame = last_frame().tb_frame
    ns = dict(frame.f_globals)
    ns.update(frame.f_locals)
    ns['EX'] = e
    #code.interact(local=ns)
