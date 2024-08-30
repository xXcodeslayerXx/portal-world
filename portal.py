class portal:
   def __init__(self, portal_name):
       self.name = portal_name
       self.description = None
       self.linked_portals = {}
       self.character = None
       self.item = None



   def get_description(self):
       return self.description



   def set_description(self, portal_description):
       self.description = portal_description



   def describe(self):
       print(self.description)



   def get_name(self):
       return self.name



   def set_name(self, portal_name):
       self.name = portal_name


   def describe(self):
       print(self.description)



   def link_portal(self, portal_to_link, direction):
       self.linked_portals[direction] = portal_to_link


   def get_details(self):
       for direction in self.linked_portals:
           portal = self.linked_portals[direction]
           print("The " + portal.get_name() + " is " + direction)


   def move(self, direction):
       if direction in self.linked_portals:
           return self.linked_portals[direction]
       else:
           print("You can't go that way")
           return self



   def get_character(self):
       return self.character



   def set_character(self, portal_character):
       self.character = portal_character



   def get_item(self):
       return self.item



   def set_item(self, portal_item):
       self.item = portal_item

