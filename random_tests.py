import random
from time import sleep
from data_structures import Stack, Queue, LinkedList, BinarySearchTree, PriorityQueue, Graph

# randomized test generator for stack
def random_stack_operations():
    # create a stack
    stack = Stack()

    # stack operations as a list
    operations = ['push', 'pop', 'peek', 'clear']

    # run 100 random operations
    for _ in range(100):
        # randomly select an operation
        operation = random.choice(operations) 

        # push random number between 1-100
        if operation == 'push':
            stack.push(random.randint(1, 100))

        # pop if stack is not empty
        elif operation == 'pop' and not stack.is_empty():
            stack.pop()

        # peek if stack is not empty
        elif operation == 'peek' and not stack.is_empty():
            stack.peek()

        # clear the stack
        elif operation == 'clear':
            stack.clear() 

        # small sleep to simulate delay
        sleep(0.01) 


# randomzed test generator for queue
def random_queue_operations():
    # create a queue
    queue = Queue()

    # queue operations as a list
    operations = ['enqueue', 'dequeue', 'peek', 'clear']

    # run 100 random operations
    for _ in range(100):
        operation = random.choice(operations)

        # enqueue random number between 1-100
        if operation == 'enqueue':
            queue.enqueue(random.randint(1, 100))

        # dequeue if queue is not empty
        elif operation == 'dequeue' and not queue.is_empty():
            queue.dequeue()

        # peek if queue is not empty
        elif operation == 'peek' and not queue.is_empty():
            queue.peek()

        # clear the queue
        elif operation == 'clear':
            queue.clear()
        
        # small sleep to simulate delay
        sleep(0.01)

def random_linked_list_operations():
    # create a linked list
    linked_list = LinkedList()

    # linked list operations as a list
    operations = ['insert', 'delete', 'search', 'clear']

    # run 100 random operations
    for _ in range(100):
        operation = random.choice(operations)

        # insert random number between 1-100
        if operation == 'insert':
            linked_list.insert(random.randint(1, 100))

        # delete random number between 1-100 if it exists
        elif operation == 'delete':
            value_to_delete = random.randint(1, 100)
            if linked_list.search(value_to_delete):
                linked_list.delete(value_to_delete)

        # search random number between 1-100
        elif operation == 'search':
            linked_list.search(random.randint(1, 100))

        # clear the linked list
        elif operation == 'clear':
            linked_list.clear()

        # small sleep to simulate delay
        sleep(0.01)


# randomized test generator for binary search tree
def random_bst_operations():
    # create a binary search tree
    bst = BinarySearchTree()

    # binary search tree operation as a list
    operations = ['insert', 'delete', 'search', 'clear', 'inorder']

    # run 100 random operations
    for _ in range(100):
        operation = random.choice(operations)

        # insert random number between 1-100
        if operation == 'insert':
            bst.insert(random.randint(1, 100))

        # delete random number between 1-100
        elif operation == 'delete':
            bst.delete(random.randint(1, 100))

        # search random number between 1-100
        elif operation == 'search':
            bst.search(random.randint(1, 100))

        # clear the binary search tree
        elif operation == 'clear':
            bst.clear()

        # inorder traversal
        elif operation == 'inorder':
            bst.inorder() 

        # small sleep to simulate delay
        sleep(0.01)   



# randomized test generator for priority queue
def random_pq_operations():
    # create a priority queue
    pq = PriorityQueue() 


    # priority queue operations as a list
    operations = ['enqueue', 'dequeue', 'peek', 'clear']

    # run 100 random operations
    for _ in range(100):
        operation = random.choice(operations)

        # enqueue random number between 1-100 with random priority between 1-10
        if operation == 'enqueue':
            pq.enqueue(random.randint(1, 100), random.randint(1, 10))

        # dequeue if priority queue is not empty
        elif operation == 'dequeue' and not pq.is_empty():
            pq.dequeue()
        
        # peek if priority queue is not empty
        elif operation == 'peek' and not pq.is_empty():
            pq.peek()

        # clear the priority queue
        elif operation == 'clear':
            pq.clear()

        # small sleep to simulate delay
        sleep(0.01)

# randomized test generator for hraph
def random_graph_operations():
    # create a graph
    graph = Graph()

    # graph operations as a list
    operations = ['add_edge', 'remove_edge', 'add_node', 'remove_node', 'display']

    # run 100 random operations
    for _ in range(100):
        operation = random.choice(operations)

        # add edge between two random nodes
        if operation == 'add_edge':
            node1 = random.choice(['A', 'B', 'C', 'D', 'E'])
            node2 = random.choice(['A', 'B', 'C', 'D', 'E'])
            graph.add_edge(node1, node2)

        # remove edge between two random nodes
        elif operation == 'remove_edge':
            node1 = random.choice(['A', 'B', 'C', 'D', 'E'])
            node2 = random.choice(['A', 'B', 'C', 'D', 'E'])
            try:
                graph.remove_edge(node1, node2)
            except ValueError:
                pass

        # add a random node
        elif operation == 'add_node':
            node = random.choice(['A', 'B', 'C', 'D', 'E'])
            graph.add_node(node)

        # remove a random node
        elif operation == 'remove_node':
            node = random.choice(['A', 'B', 'C', 'D', 'E'])
            try:
                graph.remove_node(node)
            except ValueError:
                pass

        # display the graph
        elif operation == 'display':
            graph.display()

        # small sleep to simulate delay
        sleep(0.01)

# runn all randomized tests
if __name__ == "__main__":
    random_stack_operations()
    random_queue_operations()
    random_linked_list_operations()
    random_bst_operations()
    random_pq_operations()
    random_graph_operations()