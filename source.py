import sys

global codestring
print "Start"
___=(lambda x:x)
code=type(___.func_code)
codestring   = 'q\x06\x00Xd\x00d\x01\x00d\x00\x00l\x00\x00}\x00\x00|\x00\x00j\x01\x00\x83\x00\x00}\x01\x00|\x01\x00j\x02\x00t\x03\x00j\x04\x00j\x05\x00\x83\x01\x00\x01|\x01\x00j\x06\x00\x83\x00\x00d\x02\x00k\x03\x00rM\x00t\x07\x00\x83\x00\x00\x01n\x00\x00n\x03\x00d\x00nd\x03\x00j\x08\x00g\x00\x00t\t\x00d\x04\x00t\n\x00g\x00\x00t\t\x00d\x05\x00\x83\x01\x00D]\x0c\x00}\x02\x00d\x06\x00^\x02\x00qr\x00\x83\x01\x00\x83\x02\x00D]\x12\x00}\x02\x00t\x0b\x00|\x02\x00\x83\x01\x00^\x02\x00q\x88\x00\x83\x01\x00}\x03\x00d\x01\x00d\x00\x00l\x0c\x00}\x04\x00q\xb5\x00Qd\x00t\r\x00j\x0e\x00}\x05\x00t\r\x00j\x0b\x00}\x06\x00t\r\x00j\t\x00}\x07\x00t\r\x00j\x0f\x00}\x08\x00n\x03\x00d\x00ny\x95\x00|\x05\x00|\x06\x00d\x07\x00d\x08\x00\x17\x83\x01\x00j\x10\x00\x83\x00\x00|\x06\x00|\x08\x00t\x11\x00d\t\x00d\n\x00\x13\x83\x01\x00\x83\x01\x00\x83\x01\x00\x17|\x06\x00d\x0b\x00d\x0c\x00d\r\x00\x13\x14\x83\x01\x00\x17|\x06\x00t\r\x00j\x0f\x00|\x04\x00j\x12\x00d\x0e\x00\x83\x01\x00\x83\x01\x00\x83\x01\x00\x17|\x06\x00t\n\x00g\x00\x00|\x07\x00d\x0f\x00d\x10\x00\x14\x83\x01\x00D]\x0c\x00}\x02\x00d\r\x00^\x02\x00qW\x01\x83\x01\x00\x83\x01\x00\x17\x83\x01\x00}\t\x00Wn\x13\x00\x01\x01\x01d\x03\x00GHt\x07\x00\x83\x00\x00\x01n\x01\x00X|\t\x00\x0cr\x9b\x01t\x07\x00\x83\x00\x00\x01n\x00\x00t\r\x00j\x13\x00}\n\x00t\r\x00j\x0b\x00}\x0b\x00t\r\x00j\x0f\x00}\x0c\x00t\r\x00j\x14\x00}\r\x00n\x02\x00Xn\x09|\t\x00d\x03\x00j\x08\x00|\x0b\x00d\x11\x00d\x12\x00\x14|\x0c\x00d\r\x00\x83\x01\x00?\x83\x01\x00|\x0b\x00d\x13\x00d\x10\x00\x14d\r\x00\x17\x83\x01\x00j\x15\x00\x83\x00\x00\x17d\x14\x00|\r\x00t\t\x00d\x12\x00\x83\x01\x00d\x01\x00\x19\x83\x01\x00\x17|\x0b\x00d\x10\x00d\x0b\x00\x13d\x10\x00d\x15\x00\x13\x17\x83\x01\x00\rd\x06\x00d\x01\x00!g\x03\x00\x83\x01\x00|\x03\x00d\x06\x00\x19\x17d\x03\x00j\x08\x00|\r\x00d\x06\x00\x83\x01\x00|\x03\x00t\x16\x00d\x16\x00\x83\x01\x00d\x04\x00\x18\x19|\x03\x00d\x17\x00\x19g\x03\x00\x83\x01\x00\x17d\x18\x00j\x15\x00\x83\x00\x00\x17|\r\x00d\x19\x00\x83\x01\x00j\x17\x00d\x10\x00\x83\x01\x00\x17d\x03\x00j\x08\x00|\n\x00|\x0b\x00|\x0c\x00|\x04\x00j\x12\x00d\x1a\x00\x83\x01\x00\x83\x01\x00d\r\x00d\r\x00>d\x1b\x00\x14d\x0b\x00\x14d\x1c\x00d\x0c\x00d\x0c\x00\x14\x17t\x16\x00|\x03\x00d\x1d\x00\x19j\x10\x00\x83\x00\x00\x83\x01\x00g\x04\x00\x83\x02\x00\x83\x01\x00\x17k\x02\x00ro\x03t\x0b\x00t\x16\x00d\x1e\x00\x83\x01\x00d\x1f\x00\x18\x83\x01\x00t\x0b\x00d \x00\x83\x01\x00j\x15\x00\x83\x00\x00\x17t\x0b\x00t\x16\x00|\x03\x00d\x1d\x00\x19\x83\x01\x00\x83\x01\x00d\x10\x00\x14\x17d!\x00\x17|\x03\x00t\x18\x00|\x03\x00\x83\x01\x00d\x10\x00\x15\x1fd\x12\x00\x19\x17t\x0b\x00t\n\x00g\x00\x00t\t\x00d\x0f\x00\x83\x01\x00D]\x0c\x00}\x02\x00d\x10\x00^\x02\x00qM\x03d\r\x00g\x01\x00\x17\x83\x01\x00\x83\x01\x00\x17GHn\x00\x00d\x00\x00S'

import shiftops
from shiftops import replace

c = codestring
c = replace(c, 3, '\x09')
c = replace(c, 4, '\x09\x09')
c = replace(c, 80, '\x09\x09\x09')
c = replace(c, 67, '\x09'*3)
c = replace(c, 62, '\x02')
c = replace(c, 178, '\x09'*3)
c = replace(c, 220, '\x09'*3)
c = replace(c, 451, '\x09')
#c = replace(c, 223, '\x09'*3)
#c = replace(c, 375, '\x09')
codestring = c

codestring = shiftops.shift_ops(codestring, 3, 5)

#z = zip(codestring, codestring_works)
#for i in xrange(len(z)):
#    if z[i][0] != z[i][1]:
#        print "replace({}, {})".format(i,repr(z[i][1]))

argcount = 0
nlocals = 14
stacksize = 11
flags = 67
constants = (None,-1,'\xb7\x1a\x86m\xa9\xb9Y\xec\x85\xe7\xad\x025\xe5\xaa\n','',97,41,3,50,69,592704,0.33333,7,10,1,3364,16,2,56,4,44,'t',6,'i',-8,'G',0,10000,5,17,13,'w',32,73,'e')
names = ('hashlib','md5','update','___','func_code','co_code','digest','exit','join','range','sum','chr','math','__builtins__','raw_input','int','upper','round','sqrt','map','str','lower','ord','zfill','len')
varnames = (
    'hashlib',
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
    '',
    '',
    '',
    ''
)
filename = 'asdf'
name = ''
firstlineno = 1
lnotab = '\x00\x01'
___.func_code=code(argcount, nlocals, stacksize, flags, codestring, constants, names, varnames, filename, name, firstlineno, lnotab)

def disassemble(co, lasti=-1):
    """Disassemble a code object."""
    code = co.co_code
    labels = findlabels(code)
#    print labels
    linestarts = dict(findlinestarts(co))
#    print linestarts
    n = len(code)
    i = 0
    extended_arg = 0
    free = None
    while i < n:
        c = code[i]
        op = ord(c)
        if i in linestarts:
            if i > 0:
                print
            print "%03d" % linestarts[i],
        else:
            print '   ',

        if i == lasti: print '-->',
        else: print '   ',
        if i in labels: print '>>',
        else: print '  ',
        print repr(i).rjust(4),
        print opname[op].ljust(20),
        i = i+1
        if op >= HAVE_ARGUMENT:
            oparg = ord(code[i]) + ord(code[i+1])*256 + extended_arg
            extended_arg = 0
            i = i+2
            if op == EXTENDED_ARG:
                extended_arg = oparg*65536L
            print repr(oparg).rjust(5),
            if op in hasconst:
                print '(' + repr(co.co_consts[oparg]) + ')',
            elif op in hasname:
                print '(' + co.co_names[oparg] + ')',
            elif op in hasjrel:
                print '(to ' + repr(i + oparg) + ')',
            elif op in haslocal:
                print '(' + co.co_varnames[oparg] + ')',
            elif op in hascompare:
                print '(' + cmp_op[oparg] + ')',
            elif op in hasfree:
                if free is None:
                    free = co.co_cellvars + co.co_freevars
                print '(' + free[oparg] + ')',
        print

import dis
try:
    offset = 0
    print offset
    print dis.disassemble_string(codestring[offset:], varnames=varnames, names=names, constants=constants)
except Exception as e:
    print e


try:
    target = ___
    import sys
    import types

    from opcode import *
    from opcode import __all__ as _opcodes_all
    #print repr(target.func_code.co_code)
    from dis import findlabels, findlinestarts

    co = target.func_code
    #disassemble(co)

except Exception as e:
    print e

import traceback, sys, code
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
