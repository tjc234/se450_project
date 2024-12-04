# class to handle stacks
class Stack:
    def __init__(self):
        self.items = []  # initialize an empty list

    def push(self, item):
        # add an item to the top of the stack
        self.items.append(item)

    def pop(self):
        # remove and return the top item of the stack
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Pop from an empty stack")

    def peek(self):
        # return the top item of the stack without removing it
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Peek from an empty stack")

    def is_empty(self):
        # check if the stack is empty
        return len(self.items) == 0

    def size(self):
        # return the number of elements in the stack
        return len(self.items)

    def display(self):
        # display all elements in the stack
        return self.items

    def clear(self):
        # clear the stack
        self.items = []

# class to handle queues
class Queue:
    def __init__(self):
        self.items = []  # initialize an empty list to store queue elements

    def enqueue(self, item):
        # add an item to the rear of the queue
        self.items.append(item)

    def dequeue(self):
        # remove and return the front item of the queue
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("Dequeue from an empty queue")

    def peek(self):
        # return the front item of the queue without removing it
        if not self.is_empty():
            return self.items[0]
        raise IndexError("Peek from an empty queue")

    def is_empty(self):
        # check if the queue is empty
        return len(self.items) == 0

    def size(self):
        # return the number of elements in the queue
        return len(self.items)

    def display(self):
        # display all elements in the queue
        return self.items

    def clear(self):
        # clear the queue
        self.items = []

# node class for linked list
class Node:
    def __init__(self, value):
        self.value = value  # store the node's value
        self.next = None    # pointer to the next node

# class to handle linked lists
class LinkedList:
    def __init__(self):
        self.head = None  # initialize an empty linked list

    def insert(self, value):
        # insert a new node at the beginning of the list
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete(self, value):
        # delete the first node with the specified value
        current = self.head
        prev = None

        while current and current.value != value:
            prev = current
            current = current.next

        if current is None:
            raise ValueError("Value not found in the list")

        if prev is None:
            self.head = current.next
        else:
            prev.next = current.next

    def search(self, value):
        # search for a value in the linked list
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def display(self):
        # display all values in the linked list
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

    def clear(self):
        # clear the linked list
        self.head = None

# node class for binary search tree
class TreeNode:
    def __init__(self, key):
        self.key = key  # store the value of the node
        self.left = None  # pointer to the left child
        self.right = None  # pointer to the right child

# class to handle binary search trees
class BinarySearchTree:
    def __init__(self):
        self.root = None  # initialize an empty binary search tree

    def insert(self, key):
        # insert a new key into the tree
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return TreeNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def search(self, key):
        # search for a key in the tree
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node is not None
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def inorder(self):
        # perform an inorder traversal of the tree
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)

    def clear(self):
        # clear the binary search tree
        self.root = None

# class to handle priority queues
class PriorityQueue:
    def __init__(self):
        self.items = []  # initialize an empty list to store the queue elements

    def enqueue(self, item, priority):
        # add an item to the priority queue based on priority
        self.items.append((item, priority))
        self.items.sort(key=lambda x: x[1], reverse=True)  # Higher priority comes first

    def dequeue(self):
        # remove and return the item with the highest priority
        if not self.is_empty():
            return self.items.pop(0)[0]
        raise IndexError("Dequeue from an empty priority queue")

    def peek(self):
        # return the item with the highest priority without removing it
        if not self.is_empty():
            return self.items[0][0]
        raise IndexError("Peek from an empty priority queue")

    def is_empty(self):
        # check if the priority queue is empty
        return len(self.items) == 0

    def size(self):
        # return the number of elements in the priority queue
        return len(self.items)

    def display(self):
        # display all elements in the priority queue
        return [item[0] for item in self.items]
    
    def clear(self):
        # clear the priority queue
        self.items = []

# class to handle graphs
class Graph:
    def __init__(self):
        self.graph = {}  # store graph as a dictionary of nodes

    def add_edge(self, node1, node2):
        # add an undirected edge between node1 and node2
        if node1 not in self.graph:
            self.graph[node1] = []
        if node2 not in self.graph:
            self.graph[node2] = []
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    def remove_edge(self, node1, node2):
        # remove an edge between node1 and node2
        if node1 not in self.graph or node2 not in self.graph[node1]:
            raise ValueError(f"Edge ({node1}, {node2}) not found")
        if node2 not in self.graph or node1 not in self.graph[node2]:
            raise ValueError(f"Edge ({node2}, {node1}) not found")

        # Remove the edge in both directions
        self.graph[node1].remove(node2)
        self.graph[node2].remove(node1)

    def display(self):
        # display all nodes and their adjacent nodes
        return {node: neighbors for node, neighbors in self.graph.items()}


def main():
    # stack example use
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Stack after pushes:", stack.display())
    print("Popped from stack:", stack.pop())
    print("Stack after pop:", stack.display())
    stack.clear()
    print("Stack after clearing:", stack.display())

    # eueue example use
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print("Queue after enqueues:", queue.display())
    print("Dequeued from queue:", queue.dequeue())
    print("Queue after dequeue:", queue.display())
    queue.clear()
    print("Queue after clearing:", queue.display())

    # linked List example use
    linked_list = LinkedList()
    linked_list.insert(10)
    linked_list.insert(20)
    linked_list.insert(30)
    print("Linked list after inserts:", linked_list.display())
    linked_list.delete(20)
    print("Linked list after deletion:", linked_list.display())
    print("Search for 10 in linked list:", linked_list.search(10))
    print("Search for 50 in linked list:", linked_list.search(50))
    linked_list.clear()
    print("Linked list after clearing:", linked_list.display())

    # binary search tree example use
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)
    print("Inorder traversal of BST:", bst.inorder())
    print("Search 40 in BST:", bst.search(40))
    print("Search 90 in BST:", bst.search(90))
    bst.clear()
    print("BST after clearing:", bst.inorder())

    # priority queue example use
    pq = PriorityQueue()
    pq.enqueue("Task 1", 3)
    pq.enqueue("Task 2", 1)
    pq.enqueue("Task 3", 2)
    print("Priority queue after enqueues:", pq.display())
    print("Dequeued from priority queue:", pq.dequeue())
    print("Priority queue after dequeue:", pq.display())

    # graph example use
    graph = Graph()
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    print("Graph after adding edges:", graph.display())
    graph.remove_edge("A", "B")
    print("Graph after removing edge:", graph.display())

if __name__ == "__main__":
    main()
