
from configparser import ConfigParser
import ast

configur = ConfigParser()
configur.read('config.ini')
#%%

print (configur.read('config.ini'))
for section in configur.sections():
    print(section)
    for name, value in configur.items(section):
        print('  {} = {!r}'.format(name, value))




#%%
print (configur.read('config.ini'))
districts = ast.literal_eval(configur.get("selection", "districts"))
age_limit = ast.literal_eval(configur.get("selection", "age_limit"))
fee_type = ast.literal_eval(configur.get("selection", "fee_type"))
vaccine = ast.literal_eval(configur.get("selection", "vaccine"))