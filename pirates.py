class Pirate:
  instances = []

  def __init__(self, name):
    self.name = name
    self.__class__.instances.append(self)

hook = Pirate('Captain Hook')
smee = Pirate('Mr Smee')
jack = Pirate('Capn Jack Swallow')

