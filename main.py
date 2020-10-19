from pirates import *


for capn in Pirate.instances:
  print(capn.name) 

swashbuckler = jack

if swashbuckler in Pirate.instances:
  print('\nFound', swashbuckler.name)
