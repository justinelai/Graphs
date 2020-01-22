from graph import Graph
#from typing import List, Tuple
from util import Queue


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for item in ancestors:
        graph.add_vertex(item[1])
        graph.add_vertex(item[0])
    for item in ancestors:
        graph.add_edge(item[1], item[0])
    
    longest_path = 1
    earliest_ancestor = -1
    
    queue: Queue = Queue()
    queue.enqueue([starting_node])
    
    while queue.size() > 0:
        path = queue.dequeue()
        vertex = path[-1]

        for ancestor in graph.vertices[vertex]:
            path_copy = list(path)
            path_copy.append(ancestor)
            queue.enqueue(path_copy) # Enqueue the new path that includes ancestor

        if (len(path) == longest_path and vertex < earliest_ancestor):
            earliest_ancestor = vertex
            longest_path = len(path)
        if len(path) > longest_path:
            earliest_ancestor = vertex
            longest_path = len(path)

    return earliest_ancestor

if __name__ == '__main__':
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    earliest_ancestor(test_ancestors, 3)

"""

Attempted to write from scratch (failing tests)
    # Prepare solution tracker.
    longest_path = []
    # Instructions specify a particular return for a condition. We'll use this to check
    has_parent = False
    # Initialize the path.
    queue.enqueue([starting_node])
    # Make a set to keep track of where we've been
    visited = set()
    # While there queue is not empty
    while queue.size() > 0:
    #   get first path from queue
        current_path = queue.dequeue()
        child_vertex = current_path[-1] # get the last node of the path. we will check if this vertex is a child
    #    If not visited
        if child_vertex not in visited:
            visited.add(child_vertex) # add the vertex to visited/mark as visited
    #       we're checking each of the ancestors to determine if they have a parent. "having a parent" is the path
    #       doing this as range to make reference to tuple possible - check each pair so we ensure we'd catch 2 parents
            for i in range(0, len(ancestors) - 1):
                if ancestors[i][1] == child_vertex: # if the current vertex exists in the data, is indeed child
                    has_parent = True # mark condition
                    new_path = list(current_path)
                    new_path.append(ancestors[i][0]) #add the parent ID to the path
                    queue.enqueue(new_path) # Enqueue the new path that includes ancestor
                    print(new_path)
                    i += 1
            if has_parent is False:
                return -1 # edge case response according to spec
        if len(new_path) > len(longest_path):
            longest_path = new_path
        elif len(new_path) == len(longest_path):
            if new_path[-1] < longest_path[-1]:
                longest_path = new_path
    return longest_path[-1]
"""