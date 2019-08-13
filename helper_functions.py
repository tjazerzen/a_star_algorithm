from math import sqrt


def calculate_distance(x1, y1, x2, y2):
    d1 = (x1 - x2)**2
    d2 = (y1 - y2)**2
    distance = sqrt(d1 + d2)
    return distance


def heuristic_value(point, coordinates):
    x1 = coordinates[point][0]
    y1 = coordinates[point][1]
    lst = []
    for i in range(len(coordinates)):
        x2 = coordinates[i][0]
        y2 = coordinates[i][1]
        distance = calculate_distance(x1, y1, x2, y2)
        lst.append(distance)
    return lst


def calculate_connections(coordinates, connection_list):
    lst = connection_list
    for i in range(len(connection_list)):
        for j in range(len(connection_list[i])):
            point1 = i
            point2 = connection_list[i][j]
            x1 = coordinates[point1][0]
            y1 = coordinates[point1][1]
            x2 = coordinates[point2][0]
            y2 = coordinates[point2][1]
            distance = calculate_distance(x1, y1, x2, y2)
            lst[i][j] = distance
    return lst