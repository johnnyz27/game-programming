import pygame

pygame.init()
WIDTH, HEIGHT = 1200, 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = true

locations = {
    "HOME": (450, 500),
    "A": (150, 320),
    "B": (330, 130),
    "C": (620, 150),
    "D": (760, 330),
    "E": (650, 480),
    "F": (250, 500)
}

route = ["HOME"]

def distance(a, b):
    return ((locations[a][0] - locations[b][0]) ** 2 + (locations[a][1] - locations[b][1]) ** 2) ** 0.5

def route_distance(route):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance(route[i], route[i + 1])
    return total_distance

def nearest_neighbor(start, locations):
    unvisited = set(locations.keys())
    unvisited.remove(start)
    route = [start]
    
    current_location = start
    while unvisited:
        next_location = min(unvisited, key=lambda loc: distance(current_location, loc))
        route.append(next_location)
        unvisited.remove(next_location)
        current_location = next_location
    
    route.append(start)
    return route


while running:
    


