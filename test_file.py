from a_star_algorithm import shortest_path

# Getting the coordinates of each point from intersections.txt and then creating a dictionary with them
coordinates_file = open("intersections.txt", "r")
coordinates = dict()
coordinates_lines = coordinates_file.readlines()
for index, line in enumerate(coordinates_lines):
    new_line = line.split(' ')
    new_line[1] = new_line[1][:len(new_line[1])-1]
    for i in range(2):
        new_line[i] = float(new_line[i])
    coordinates[index] = new_line
coordinates_file.close()


# Getting the adjacency list of each node from adjacency_list.txt
# Creating 2D list out of adjacency list of lenght 40, which is the number of nodes in the the graph
adjacency_file = open("adjacency_list.txt", "r")
adjacency_list = list()
adjacency_lines = adjacency_file.readlines()
for line in adjacency_lines:
    line = line.split(' ')
    line = line[:len(line)-1]
    for i in range(len(line)):
        line[i] = int(line[i])
    adjacency_list.append(line)
adjacency_file.close()


# Pre-made answers for your testing purposes
map_answers = [
    (5, 34, [5, 16, 37, 12, 34]),
    (5, 5,  [5]),
    (8, 24, [8, 14, 16, 37, 12, 17, 10, 24]),
    (0, 39, [0, 36, 39]),
    (6, 19, [6, 15, 17, 28, 36, 2, 19]),
    (8, 24, [8, 14, 16, 37, 12, 17, 10, 24])
]


# Test function for your test purposes
def test(shortest_path_function):
    correct = 0
    for start, goal, answer_path in map_answers:
        path = shortest_path_function(coordinates, adjacency_list, start, goal)
        if path == answer_path:
            correct += 1
        else:
            print("For start:", start,
                  "Goal:     ", goal,
                  "Your path:", path,
                  "Correct:  ", answer_path)
    if correct == len(map_answers):
        print("You passed all tests!!")
    else:
        print("You didn't pass all the tests :/")


test(shortest_path)
