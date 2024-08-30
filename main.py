from portal import portal
from character import Enemy, Friend
from character import Character
from item import Item


portal1 = portal("portal 1")
portal1.set_description("takes you back to portalworld ")


portalworld = portal("portalworld")
portalworld.set_description("The world of all portals")


portal2 = portal("portal 2")
portal2.set_description("A small portal")

portal1.link_portal(portalworld, "south")
portal2.link_portal(portalworld, "east")
portalworld.link_portal(portal2, "west")
portalworld.link_portal(portal1, "north")

portalmonster = Enemy("portalmonster", "Don't let him get away!!!")
portalmonster.set_conversation("PORTAL WORLD WILL BE MINE!!!")
portalmonster.set_weakness("portalbomb")
portalworld.set_character(portalmonster)


harry = Friend("harry", "A friendly dwarf")
harry.set_conversation("hello portal boy")
portal2.set_character(harry)


portalbomb = Item("portalbomb")
portalbomb.set_description("Portal monsters worst nightmare")
portal2.set_item(portalbomb)
portalgun = Item("portalgun")
portalgun.set_description("Opens up portals to get to the monster")
portalworld.set_item(portalgun)
bag = []




current_portal = portal1
dead = False
while dead == False:
   print("\n")


   item = current_portal.get_item()
   if item is not None:
       item.describe()


   current_portal.get_details()
   inhabitant = current_portal.get_character()
   if inhabitant is not None:
       inhabitant.describe()


   command = input("> ")


   if command in ["north", "south", "east", "west"]:
       current_portal = current_portal.move(command)


   elif command == "talk":
       if inhabitant is not None:
           inhabitant.talk()


   elif command == "fight":
       if inhabitant is not None and isinstance(inhabitant, Enemy):
           print("What will you fight with?")
           fight_with = input()
           if fight_with in bag:
               if inhabitant.fight(fight_with) == True:
                   print("PORTAL MONSTER IS DEAD, YOU WON!")
                   current_portal.set_character(None)
                   if Enemy.enemies_to_defeat == 0:
                       print("YOU SAVED PORTAL WORLD!")
                       dead = True
               else:
                   print("Scurry home, you lost the fight.")
                   print("That's the end of the game")
                   dead = True
           else:
               print("You don't have a " + fight_with)
       else:
           print("There is no one here to fight with")


   elif command == "hug":
       if inhabitant is not None:
           if isinstance(inhabitant, Enemy):
               print("hug me and your dead...")
           else:
               inhabitant.pat()
       else:
           print("There is no one here to hug :(")


   elif command == "take":
       if item is not None:
           print("You put the " + item.get_name() + " in your bag")
           bag.append(item.get_name())
           current_portal.set_item(None)