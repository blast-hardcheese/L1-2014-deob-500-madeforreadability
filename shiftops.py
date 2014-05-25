import dis
from pprint import pprint

revmap = {dis.opmap[x]: x for x in dis.opmap}

def log(*args):
    #print args
    pass

def shift_ops(codestring, start, count, limit=True):
    i = 0
    r = codestring

    while i < len(codestring) and (limit or i < start):
        op = ord(codestring[i])
        opi = i
        log(opi, revmap.get(op, '<%d>' % op))
        i += 1

        if op in dis.hasjabs:
            replrange = codestring[i:i+2]
            oparg = ord(replrange[0]) + ord(replrange[1]) * 256
            if oparg >= start:
                newtarget = oparg + count
                newtargethex = chr(newtarget % 256) + chr(newtarget / 256)
                codestring = codestring[:i] + newtargethex + codestring[i+2:]
            i += 2
        elif op > dis.HAVE_ARGUMENT:
            i += 2

    if limit is True:
        munge = 0
        r = codestring[:start+1-munge] + '\x09' * (count + munge) + codestring[start+1:]
    return r

def replace(c, i, s):
    return c[:i] + s + c[i + len(s):]
