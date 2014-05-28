import sys
import dis
#import uncompyle2

from shiftops import replace, shift_ops, strip_nops, revmap
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
    'hobj',
    'var3',
    'var4',
    'math',
    'var6',
    'chr',
    'var8',
    'var9',
    'var10',
    'map',
    'str',
    'eval',
    'int'
    )
    filename = 'asdf'
    name = 'asdfmodule'
    firstlineno = 1
    lnotab = '\x00\x01'

    retval.func_code=code(argcount, nlocals, stacksize, flags, codestring, constants, names, varnames, filename, name, firstlineno, lnotab)

    return retval

codestring = open('co_code').read().strip()

c = codestring

c = replace(c,   3, '\x09')

c = replace(c,   4, '\x09'*2)  # Jump fix
c = replace(c,  80, '\x09'*3)  # Jump fix
c = replace(c, 178, '\x09'*3)  # Jump fix
c = replace(c, 220, '\x09'*3)  # Jump fix
c = replace(c, 451, '\x09')    # Jump fix

c = replace(c, 223, '\x09'*3)  # Disabling try: catch
c = replace(c, 371, '\x09')    # Disabling try: catch
c = replace(c, 375, '\x09'*3)  # Disabling try: catch

c = replace(c, 736, '\x03')   # Changing comparison to print "Winner"

## Cleanup
#c = replace(c,  0, '\x09'*4)
#c = replace(c, 18, '\x09'*3)
#c = replace(c, 21, '\x09'*3)
#c = replace(c, 24, '\x09'*3)
#c = replace(c, 27, '\x09'*3)
#c = replace(c, 30, '\x09'*3)
#c = replace(c, 33, '\x09'*3)
#c = replace(c, 36, '\x09'*3)
#c = replace(c, 39, '\x09'*3)
#c = replace(c, 42, '\x09'*3)
#c = replace(c, 45, '\x09'*3)
#c = replace(c, 48, '\x09')
#c = replace(c, 49, '\x09'*3)
#c = replace(c, 52, '\x09'*3)
#c = replace(c, 55, '\x09'*3)
#c = replace(c, 58, '\x09'*3)
#c = replace(c, 61, '\x09'*3)
#c = replace(c, 64, '\x09'*13)
#c = replace(c, 77, '\x09'*3)

#c = strip_nops(c)

c = shift_ops(c, 734, 20)
c = replace(c, 735, chr(dis.opmap['PRINT_ITEM']))

codestring = c

___ = build(codestring)

co = ___.func_code

print "Here"
from StringIO import StringIO
out = StringIO()

if True:
    #uncompyle2.uncompyle('2.7', co, out=out)

    out.seek(0)
    print out.read()
    print "There"

try:

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
