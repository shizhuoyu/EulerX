# Copyright (c) 2014 University of California, Davis
# 
# 
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
# 
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import sys
import commands
import os

class Callable:
    def __init__(self, callable):
        self.__call__ = callable

def findkey(mapp, value):
#    tmplist = [k for k, v in mapp.iteritems() if v == value]
#    if tmplist is []:
#        return None
#    return tmplist[0]
    return mapp.keys()[mapp.values().index(value)]


class Logger(object):
    # filename may have proper path
    def __init__(self, filename):
        self.terminal = sys.stdout
        self.log = open(filename, "a")
        
    def __del__(self):
        self.log.close()
        
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

def newgetoutput(cmd):
    result = commands.getstatusoutput(cmd)
    if result[0] != 0:
        print "cmd: ", cmd
        print "exit status: ", result[0]
        return
    else:
        return result[1]

def createLastRunTimeStamp(fileName, user, host, timestamp, name):
    f = open(fileName, "w")
    s = os.path.join(user + '-' + host, timestamp + '-' + name)
    f.write(s)
    f.write('\n')
    f.write(name)
    f.close()