import os 
# Getting the ent working Directory 
print(os.getcwd())
path = os.getcwd()

names = sorted([name for name in os.listdir() if name.endswith('py')])
print(names)

