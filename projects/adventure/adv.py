from room import Room
from player import Player
from world import World
import random
from ast import literal_eval
from typing import List

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()
# instantiate a player 
player = Player(world.starting_room)

""" UPER 
Use the room and player APIs to traverse the entire maze
Have to construct the graph as we walk around in the
form:
{ 
room_id : {'n': '?', 's': '?', 'w': '?', 'e': '?'}
}

Can move to a room with player.travel(direction key)



"""

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

def traverse_maze(player) -> List[str]:
    start = player.current_room
    print(start)
    print(start.get_exits())


traversal_path = ['n','n']



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    print("CURRENT ROOM", player.current_room)
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
