class Item:
   def __init__(self, item_name):
       self.name = item_name
       self.description = None


   #method to get the description of the item:
   def get_description(self):
       return self.description


   #method to set the description of the item:
   def set_description(self, item_description):
       self.description = item_description


   #method to get the name of the item:
   def get_name(self):
       return self.name


   #method to set the name of the item:
   def set_name(self, item_name):
       self.name = item_name


   def describe(self):
       print("The [" + self.name + "] is here - " + self.description)