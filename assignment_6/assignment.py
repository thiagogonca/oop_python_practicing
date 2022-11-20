import os

class ConfigKeyError(Exception):
    
    def __init__(self, this, key):
        self.key = key
        self.keys = this.keys()

    def __str__(self):
        dlm = ", "
        return f"Key '{self.key}' not found. Available keys: [" + dlm.join(self.keys) + "]"

class ConfigFile(object):
    
    @staticmethod
    def verify_file(filename):
        if not os.path.isfile(filename):
            try:
                open(filename, 'w').close()
            except IOError:
                raise IOError('ConfigDict arg must be a valid pathname')


class ConfigDict(dict,ConfigFile):

    def __init__(self, filename):
        self.__filename = filename
        self.verify_file(filename)
        self.__set_dict_key_val()
        
    def __set_dict_key_val(self):
        with open(self.__filename) as f: 
            for line in f:
                line = line.strip()
                key, val = line.split('=',1)
                dict.__setitem__(self, key, val)
                
    def __setitem__(self, key, val):
        dict.__setitem__(self, key, val)        
        with open(self.__filename, 'w') as f:
            for key, val in self.items():
                f.write(f'{key}={val}\n')

    def __getitem__(self,key):
        if key not in self:
            # raise -> creates and prints the object at the same time!!!!
            raise ConfigKeyError(self,key) 
        return dict.__getitem__(self,key)



cc = ConfigDict('config06.txt')
cc['oi'] = 3
print(cc['oisg'])