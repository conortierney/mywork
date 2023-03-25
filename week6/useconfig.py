# show how you would use a configuration file 
# you would push this to github but not "config.py" file as it is sensitive info.
# messing with config.


import config as cfg

password = cfg.gmail['password']

print (password)

