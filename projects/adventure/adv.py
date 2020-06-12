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

Player methods:
player.travel(direction key) to travel to valid room
player.current_room.id to get the current room's id

Room get methods methods:
exits with room.get_exits()
coordinates with room.get_coords()
the name of a next room with room.get_room_in_direction(direction)

So then we start in room zero like this:
Room_0: {'n': '?', 's': '?', 'w': '?', 'e': '?'}

And we add this to the list of explored rooms:

explored_rooms: List[Room] = []

Also we need the return list of directions:

directions: List[str] = []

We start by checking exits with room.get_exits() and updating the ?s to 
which rooms they link to with get_room_in_direction(direction)

Also checking that we haven't been there already with something like:

room.get_room_in_direction(direction) in explored_rooms == False

and then we go into a random valid next room and repeating this until we can
no longer do this and are at a dead end.

SAVE THE DIRECTIONS WE WENT IN ORDER SO CAN REVERSE WHEN WE REACH A DEAD END

Then we back out until we can go to a new room.

So something like:

initialize directions, rooms graph, starting room

DFT standard boiler plate code using a stack

stack.push(starting room)
graph = {}

while stack.size > 0:
    curr = s.pop()
    if curr not in graph:
        graph add curr
        for neighbor in room.get_exits:

  """
        s = Stack()
        s.push(starting_vertex)
        visited_nodes: Set = set()
        while s.size() > 0:
            curr = s.pop()
            if curr not in visited_nodes:
                print(curr)
                visited_nodes.add(curr)
                for neighbor in self.get_neighbors(curr):
                    s.push(neighbor)

        

"""

def traverse_maze(player) -> List[str]:
    start = player.current_room
    print(start)
    print("EXIT directions")
    print(start.get_exits())
   # print("directions")
   # print(start.get_directions())
    print("coords")
    print(start.get_coords())


traverse_maze(player)

# Fill this out with directions to walk
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
