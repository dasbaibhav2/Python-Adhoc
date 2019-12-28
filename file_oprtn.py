#!/usr/bin/python3

import sys
file_name=sys.argv[1:]

for i in file_name:
    f=open(i,'w')
    f.close()

for i in file_name:
    with open(i, 'w') as f:
        f.write("hey python ")
