#Create a text-based game using everything learned, including classes.

class Character:
	def __init__(self, name, roomindex, inventory):
		self.name = name
		self.roomindex = roomindex
		self.inventory = inventory
		
	
class Room:
	def	__init__(self, doors, items, monsters, description):
		self.doors = doors
		self.description = description
		self.items = items
		self.monsters = monsters
				 
class Item:
	def __init__(self, description):
		self.description = description

class Monster:
	def __init__(self, description):
		self.description = description

"""

	def generate(self, roomindex):
		Character("Steve")

"""	
	
#Is Npc name redundant? Did not use names for Items. Should Npcs be a dictionary?
 


inputtext = input("What's your character's name? ")  

player = Character(inputtext, 0, [])
print("Your character's name is", inputtext)

itemtype =  { 
	"Rusty Spoon": Item("A Rusty Spoon. A capable and efficient tool for the working class cannibal!")
}

monstertype = { 
	"A Hapless Manatee": Monster("A defenseless beast. Incapable - weak.. Most easy prey for the wroth of the most roitous Patroit!")
}

#"Beaten and battered! The beast flees before your might!"

rooms = [
	Room({"Forward":1}, ["Rusty Spoon"], ["Manatee", "Manatee"],

"You find yourself in a rectangular undulating moist room. A large neon sign infront of you is stapled to the organic pulsating walls reads: 'Welcome to the Jungle, baby!'"

	),
 
	Room({"Backward":0, "Forward": 2}, [], [], "This is a dry dusty dank room"),
	Room({"Backward":1, "DOOM": 3}, [], ["A Hapless Manatee"], "Frothy clam room")
]  

while True:
	print("")
	print(rooms[player.roomindex].description)
	print(list(rooms[player.roomindex].doors.keys()))
	print(rooms[player.roomindex].items)
	print(rooms[player.roomindex].monsters)
	

	resolved = False 
	while not resolved: 
		action = input("What do you do? ")
		if " " in action:
			idx = action.index(" ")
			cmd = action[0:idx]
			sel = action[idx + 1:]
		else:
			cmd = action 
			sel = ""
		
		
		if cmd == "go": 
			if sel in rooms[player.roomindex].doors:
				player.roomindex = rooms[player.roomindex].doors[sel]
				resolved = True
			else:
				print(list(rooms[player.roomindex].doors.keys()))
		elif cmd == "get":
			if sel in rooms[player.roomindex].items:
				player.inventory.append(sel)
				rooms[player.roomindex].items.remove(sel)
				resolved = True
			else:
				print(list(rooms[player.roomindex].items))
		elif cmd == "drop":
			if sel in player.inventory:
				player.inventory.remove(sel)
				rooms[player.roomindex].items.append(sel)
				resolved = True
			else:
				print(list(rooms[player.roomindex].items))
		elif cmd == "list": 
			for itemname in player.inventory:
				print(itemtype[itemname].description)
		elif cmd == "greet":
			if sel in rooms[player.roomindex].monsters:
				print(sel)
				print(monstertype[sel].description)
		elif cmd == "slay":
			if sel in rooms[player.roomindex].monsters:
					rooms[player.roomindex].monsters.remove(sel)
					resolved = True
			else:
				print("What or whom shall meet your fury??!") 
				print(list(rooms[player.roomindex].monsters))
				print("???")
								
# 		print(npcs[npcname].description)
#			print(npcs[player.roomindex].npcs.description)
			
			# itemname is our Rusty Spoon
			# items is our dictionary of item definitions
			# items[itemname] is Item class that we looked up with name itemname
 
		elif cmd == "help":
			print("go ---; Move player to another room.")
			print("get ---; Get item into inventory.")
			print("drop ---; Drop item from inventory into the current room.")
			print("greet ---; Engage NPC.")
			print("slay ---; Slay NPC.")
			print("list ---; List items and descriptions in inventory.")
			print("help; Display this message.")
		else:
			print("Huh???")

# Homework
# When player enters a room give a monster a chance to move into a random direction or X door. "Inform the player." 
# Careful of DOOM room
# Not capital 
# More rooms 
# Multiple doors 
# Monster that takes your items



