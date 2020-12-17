# CS 331 Programming #1:
# Uninformed and Informed Search
# Name: Hao Jia

# Print out the states along the solution path from the start state to the goal state
# If no path exists, print out a no solution found message
# Print out the number of search nodes expanded


import sys
import copy
from queue import PriorityQueue


def readfile(name):
    readfile = open(name, "r")
    arr = []

    for i in range(0,2):
        line = readfile.readline()[:-1]
        temp = []
        for x in line.split(','):
            temp.append(int(x))
        arr.append(temp)
    readfile.close()

    return arr


def check_chicken_GT_wolf(list):
    if list[0][0] >= list[0][1] and list[1][0] >= list[1][1]:
        return True
    else:
        if list[0][0] == 0 or list[1][0] == 0:
            return True
        else:
            return False


def less_zero(list):
    count = 0
    for i in range (0, 2):
        for j in range (0, 2):
            if list[i][j] < 0:
                count+=1
    if count > 0:
        return False
    else:
        return True


def action_1(list):
    if list[0][2] == 1:
        list[0][0] = list[0][0] - 1
        list[1][0] = list[1][0] + 1

        list[0][2] = list[0][2] - 1
        list[1][2] = list[1][2] + 1

    elif list[1][2] == 1:
        list[0][0] = list[0][0] + 1
        list[1][0] = list[1][0] - 1

        list[0][2] = list[0][2] + 1
        list[1][2] = list[1][2] - 1


def action_2(list):
    if list[0][2] == 1:
        list[0][0] = list[0][0] - 2
        list[1][0] = list[1][0] + 2

        list[0][2] = list[0][2] - 1
        list[1][2] = list[1][2] + 1

    elif list[1][2] == 1:
        list[0][0] = list[0][0] + 2
        list[1][0] = list[1][0] - 2

        list[0][2] = list[0][2] + 1
        list[1][2] = list[1][2] - 1


def action_3(list):
    if list[0][2] == 1:
        list[0][1] = list[0][1] - 1
        list[1][1] = list[1][1] + 1

        list[0][2] = list[0][2] - 1
        list[1][2] = list[1][2] + 1

    elif list[1][2] == 1:
        list[0][1] = list[0][1] + 1
        list[1][1] = list[1][1] - 1

        list[0][2] = list[0][2] + 1
        list[1][2] = list[1][2] - 1


def action_4(list):
    if list[0][2] == 1:
        list[0][0] = list[0][0] - 1
        list[1][0] = list[1][0] + 1

        list[0][1] = list[0][1] - 1
        list[1][1] = list[1][1] + 1

        list[0][2] = list[0][2] - 1
        list[1][2] = list[1][2] + 1

    elif list[1][2] == 1:
        list[0][0] = list[0][0] + 1
        list[1][0] = list[1][0] - 1

        list[0][1] = list[0][1] + 1
        list[1][1] = list[1][1] - 1

        list[0][2] = list[0][2] + 1
        list[1][2] = list[1][2] - 1


def action_5(list):
    if list[0][2] == 1:
        list[0][1] = list[0][1] - 2
        list[1][1] = list[1][1] + 2

        list[0][2] = list[0][2] - 1
        list[1][2] = list[1][2] + 1

    elif list[1][2] == 1:
        list[0][1] = list[0][1] + 2
        list[1][1] = list[1][1] - 2

        list[0][2] = list[0][2] + 1
        list[1][2] = list[1][2] - 1


def solution_node(temp, s):
    if temp[0][2] != s[0][2]:
        return 1
    else:
        return 0


def BFS(start, goal, visited, queue, output_txt):
    visited.append(start)
    queue.append(start)
    node = 0
    s_node = 0
    writefile = open(output_txt,'a')

    while queue:
        s = queue.pop(0)
        node+=1
        print(s, end=" ")
        print()

        output = str(s) + "\n"
        writefile.write(output)

        if s != goal:
            for i in range(1, 6):
                temp = copy.deepcopy(s)
                if i == 1:
                    action_1(temp)
                elif i == 2:
                    action_2(temp)
                elif i == 3:
                    action_3(temp)
                elif i == 4:
                    action_4(temp)
                elif i == 5:
                    action_5(temp)

                if check_chicken_GT_wolf(temp) and less_zero(temp):
                    if temp not in visited:
                        visited.append(temp)
                        queue.append(temp)
                        s_node += solution_node(temp, visited[-2])
        else:
            print("Path fund")
            print("Solution node: ", s_node + 1)
            print("Expanded node: ", node)


            output = "Path fund\n""Solution node: " + str(s_node + 1) + "\nExpanded node: " + str(node)
            writefile.write(output)
            writefile.close()

            exit()
    print("No solution")


def DFS(start, goal, visited, queue, output_txt):
    writefile = open(output_txt,'a')
    visited.append(start)
    queue.insert(0, start)
    node = 0
    s_node = 0

    while queue:
        s = queue.pop(0)
        node+=1
        print(s, end=" ")
        print()

        output = str(s) + "\n"
        writefile.write(output)

        if s != goal:
            for i in range(1, 6):
                temp = copy.deepcopy(s)
                if i == 1:
                    action_1(temp)
                elif i == 2:
                    action_2(temp)
                elif i == 3:
                    action_3(temp)
                elif i == 4:
                    action_4(temp)
                elif i == 5:
                    action_5(temp)

                if check_chicken_GT_wolf(temp) and less_zero(temp):
                    if temp not in visited:
                        visited.append(temp)
                        queue.insert(0, temp)
                        s_node += solution_node(temp, visited[-2])
        else:
            print("Path fund")
            print("Solution node: ", s_node + 1)
            print("Expanded node: ", node)

            output = "Path fund\n""Solution node: " + str(s_node + 1) + "\nExpanded node: " + str(node)
            writefile.write(output)
            writefile.close()

            exit()
    print("No solution")


def IDDFS(start, goal, output_txt):
    writefile = open(output_txt,'a')
    node = 0
    deepth = 0
    s_node = 0

    for limit in range(0, 10000):
        queue = []
        visited = []
        queue.insert(0, start)
        visited.append(start)
        print("limit: ", limit)

        while queue and len(queue) <= limit:
            s = queue.pop(0)
            node+=1
            print(s, end=" ")
            print()

            output = str(s) + "\n"
            writefile.write(output)

            if s != goal:
                for i in range(1, 6):
                    temp = copy.deepcopy(s)
                    if i == 1:
                        action_1(temp)
                    elif i == 2:
                        action_2(temp)
                    elif i == 3:
                        action_3(temp)
                    elif i == 4:
                        action_4(temp)
                    elif i == 5:
                        action_5(temp)

                    if check_chicken_GT_wolf(temp) and less_zero(temp):
                        if temp not in visited:
                            visited.append(temp)
                            queue.insert(0, temp)
                            s_node += solution_node(temp, visited[-2])
            else:
                print("Path fund")
                print("Solution node: ", s_node + 1)
                print("Expanded node: ", node)

                output = "Path fund\n""Solution node: " + str(s_node + 1) + "\nExpanded node: " + str(node)
                writefile.write(output)
                writefile.close()

                exit()
        print("No solution")


def heuristic(current, goal):
    heur = 0
    for i in range(0,3):
        heur += abs(goal[0][i] - current[0][i])
    return heur


def ASTAR(start, goal, visited, queue, output_txt):
    writefile = open(output_txt,'a')
    visited.append(start)
    cost = heuristic(start, goal)
    queue_pq = []
    queue_pq = PriorityQueue()
    queue_pq.put((cost, start))
    node = 0
    s_node = 0

    while queue_pq:
        queue = queue_pq.get()
        s = queue[1]
        node+=1
        print(s, end=" ")
        print()

        output = str(s) + "\n"
        writefile.write(output)

        if s != goal:
            for i in range(1, 6):
                temp = copy.deepcopy(s)
                if i == 1:
                    action_1(temp)
                elif i == 2:
                    action_2(temp)
                elif i == 3:
                    action_3(temp)
                elif i == 4:
                    action_4(temp)
                elif i == 5:
                    action_5(temp)

                if check_chicken_GT_wolf(temp) and less_zero(temp):
                    if temp not in visited:
                        visited.append(temp)
                        pre_cost = node + heuristic(temp, goal)
                        queue_pq.put((pre_cost, temp))
                        s_node += solution_node(temp, visited[-2])
        else:
            print("Path fund")
            print("Solution node: ", s_node + 1)
            print("Expanded node: ", node)

            output = "Path fund\n""Solution node: " + str(s_node + 1) + "\nExpanded node: " + str(node)
            writefile.write(output)
            writefile.close()

            exit()
    print("No solution")


def main():
    n = len(sys.argv)
    if n != 5:
        print("Enter wrong number of files")
        exit()

    start = readfile(sys.argv[1])
    goal = readfile(sys.argv[2])
    model_name = sys.argv[3]
    output_txt = sys.argv[4]

    visited = []
    queue = []

    if model_name == 'BFS':
        BFS(start, goal, visited, queue, output_txt)
    elif model_name == 'DFS':
        DFS(start, goal, visited, queue, output_txt)
    elif model_name == 'IDDFS':
        IDDFS(start, goal, output_txt)
    elif model_name == 'ASTAR':
        ASTAR(start, goal, visited, queue, output_txt)
    else:
        print("Enter an error model name")
        exit()


if __name__=="__main__":
    main()
