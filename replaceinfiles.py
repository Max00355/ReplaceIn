#!/usr/bin/python

import os
import sys

pattern = raw_input("Word to replace: ")                                                                                                                                                             
replaceWith = raw_input("What to replace it with: ")
confirm = raw_input("Are you sure you want me to replace everything that matches the pattern {} in this directory and every sub directory with {}? [y/n] ".format(pattern, replaceWith))

if confirm.lower() not in ['y', 'yes', 'yeah', 'yea', 'yup']:
    print "Okay, I won't do it."
else:
    for x, _, y in os.walk(os.getcwd()):
        for y in y:
            if y == sys.argv[0]:
                continue
            with open(x+"/"+y) as file:
                data = file.read()
                with open(x+"/"+y, 'w') as fout:
                    data = data.replace(pattern, replaceWith)
                    fout.write(data)



