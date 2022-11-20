import abc
from datetime import datetime
import os

class write_file(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractclassmethod
    def write(self):
        pass

    def __init__(self,filename):
        self.filename = filename
    
    def write_line(self, text):
        # with / as -> internally calls the close() method
        with open(os.path.join('..','files', self.filename), 'a') as f:
            f.write(text+'\n')

class delimeter_file(write_file):

    def __init__(self,filename,delim):
        super(delimeter_file,self).__init__(filename)
        self.delim = delim

    def write(self, g_list):
        line = self.delim.join(g_list)
        self.write_line(line)

class log_file(write_file):

    def write(self, msg):
        dt = datetime.now()
        date_str = dt.strftime('%m/%d/%Y - %H:%M')
        self.write_line(date_str+'\t'+msg)
        