import random
import math
import time
import sys

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value) -> None:
        self.queue.append((value))
    
    def dequeue(self):
        if (self.size()) > 0:
            return self.queue.pop(0)
        else:
            return None
    
    def size(self):
        return len(self.queue)

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id) -> bool:
        if user_id == friend_id:
            print("You are not allowed to be your own friend.")         
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("You are already friends")
            return False
        else:
            self.friendships[user_id].add(friend_id), self.friendships[friend_id].add(user_id)
            return True

    def addUser(self, name):
        self.last_id += 1 
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()


    def populate_graph(self, num_users, avg_friendships):
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for i in range(0, num_users):
            self.addUser(f"User {i}")

        # Create Frienships
        # Generate all possible friendship combinations
        possible_friendships = []

        # Avoid duplicates by ensuring the first number is smaller than the second
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        # Shuffle the possible friendships
        random.shuffle(possible_friendships)

        # Create friendships for the first X pairs of the list
        # X is determined by the formula: num_users * avg_friendships // 2
        # Need to divide by 2 since each add_friendship() creates 2 friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def populate_graph_2(self, num_users, avg_friendships):
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        for i in range(0, num_users):
            self.addUser(f"User {i}")

        target_friendships = (num_users * avg_friendships) // 2
        total_friendships = 0
        collisions = 0 

        while total_friendships < target_friendships:
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)
            if self.add_friendship(user_id, friend_id):
                total_friendships += 1
            else:
                collisions += 1 
        print(f"collisions: {collisions}")

    def get_all_social_paths(self, user_id):
        q = Queue()

        visited = {} # k, v are user and path to user

        q.enqueue([user_id])

        while q.size() > 0:
            path = q.dequeue()

            v = path[-1]

            if v not in visited:

                visited[v] = path # mark as visited, cache path so far

                for neighbor in self.friendships[v]:

                    #path_copy = list(path)  # Make a copy
                    #path_copy.append(neighbor)
                    #q.enqueue(path_copy)
                    q.enqueue(path + [neighbor])
        return visited

if __name__ == '__main__':
    n = 100
    a = 3 
    sg = SocialGraph()
    start_time = time.time()
    sg.populate_graph(n, a)
    end_time = time.time()
    print (f"runtime: {end_time - start_time} seconds")
    print(sg.friendships)
    start_time = time.time()
    sg.populate_graph_2(n, a)
    end_time = time.time()
    print (f"runtime: {end_time - start_time} seconds")


