from myClasses import log_file, delimeter_file

log = log_file('log.txt')
csv = delimeter_file('text.csv', ', ')

log.write('Registering a random log message')
log.write('Now registering another new random log message')

csv.write(['a','b','c','d'])
csv.write(['1','2','3','4'])

import os
with open(os.path.join('..','files', 'log.txt'), 'r') as f:
    for l in f:
        print(l, end='')
