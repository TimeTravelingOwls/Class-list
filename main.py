class Pirate:
  instances = []

  def __init__(self, name):
    self.name = name
    self.__class__.instances.append(self)

hook = Pirate('Captain Hook')
smee = Pirate('Mr Smee')
jack = Pirate('Capn Jack Swallow')

for capn in Pirate.instances:
  print(capn.name) 

swashbuckler = jack

if swashbuckler in Pirate.instances:
  print('\nFound', swashbuckler.name)
