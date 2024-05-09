''' example of using an ini configuration file'''

import configparser

config = configparser.ConfigParser()
# case in attributes are mereely for visual effect. Attributes in an ini file are case insensitive. 
# option values must bee strings
config['DEFAULT'] = {'FullName': 'Programmer',
                     'Experience': 'none',
                     'CurrentLanguage': 'python'}

config['team.prog1'] = {}
config['team.prog1']['FullName'] = 'Donnie Bryson'
config['team.prog1']['Experience'] = '30+'
config['team.prog1']['CurrentLanguage'] = 'python'
config['team.prog1']['age'] = '66'
config['team.prog1']['pay'] = '45'



config['team.prog2'] = {}
config['team.prog2']['FullName'] = 'Sam Smith'
config['team.prog2']['Experience'] = '2'
config['team.prog2']['CurrentLanguage'] = 'java'
config['team.prog2']['age'] = '24'
config['team.prog2']['pay'] = '35'



with open('sample_config.ini', 'w') as configfile:
  config.write(configfile)

readback_config = configparser.ConfigParser()
readback_config.read('sample_config.ini')

for key in readback_config['team.prog2']:  
    print(key, readback_config['team.prog2'][key])

