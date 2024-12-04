import unittest
from random import randint
from data_structures import Stack, Queue, LinkedList, BinarySearchTree, PriorityQueue, Graph

# test class for data structures
class TestDataStructures(unittest.TestCase):

    # stack tests
    def test_stack_operations(self):
        # create a stack
        stack = Stack()

        # push elements to stack
        stack.push(10)
        stack.push(20)
        stack.push(30)

        # test stack operations
        self.assertEqual(stack.pop(), 30)
        self.assertEqual(stack.pop(), 20)
        self.assertEqual(stack.peek(), 10)
        self.assertEqual(stack.size(), 1)
        stack.clear()
        self.assertTrue(stack.is_empty())

    # test stack empty pop
    def test_stack_empty_pop(self):
        stack = Stack()
        with self.assertRaises(IndexError):
            stack.pop()

    # queue tests
    def test_queue_operations(self):
        # create a queue
        queue = Queue()

        # enqueue elements to queue
        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)

        # test queue operations
        self.assertEqual(queue.dequeue(), 10)
        self.assertEqual(queue.dequeue(), 20)
        self.assertEqual(queue.peek(), 30)
        self.assertEqual(queue.size(), 1)
        queue.clear()
        self.assertTrue(queue.is_empty())

    # test queue empty dequeue
    def test_queue_empty_dequeue(self):
        queue = Queue()
        with self.assertRaises(IndexError):
            queue.dequeue()

    # linked list tests
    def test_linked_list_operations(self):
        # create a linked list
        linked_list = LinkedList()

        # insert elements to linked list
        linked_list.insert(10)
        linked_list.insert(20)
        linked_list.insert(30)

        # test linked list operations
        self.assertTrue(linked_list.search(20))
        linked_list.delete(20)
        self.assertFalse(linked_list.search(20))
        self.assertEqual(linked_list.display(), [30, 10])

    # test linked list empty delete
    def test_linked_list_empty_delete(self):
        linked_list = LinkedList()
        with self.assertRaises(ValueError):
            linked_list.delete(10)

    # binary search tree tests
    def test_bst_operations(self):
        # create a binary search tree
        bst = BinarySearchTree()

        # insert elements to binary search tree
        bst.insert(50)
        bst.insert(30)
        bst.insert(70)

        # test binary search tree operations
        self.assertTrue(bst.search(30))
        self.assertFalse(bst.search(100))
        self.assertEqual(bst.inorder(), [30, 50, 70])

        # test binary search tree clear
        bst.clear()
        self.assertEqual(bst.inorder(), [])

    # priority queue tests
    def test_priority_queue_operations(self):
        # create a priority queue
        pq = PriorityQueue()

        # enqueue elements to priority queue
        pq.enqueue("Task 1", 3)
        pq.enqueue("Task 2", 1)
        pq.enqueue("Task 3", 2)

        # test priority queue operations
        self.assertEqual(pq.dequeue(), "Task 1")
        self.assertEqual(pq.dequeue(), "Task 3")
        self.assertEqual(pq.peek(), "Task 2")

        # test priority queue empty dequeue
        pq.clear()
        self.assertTrue(pq.is_empty())

    # graph tests
    def test_graph_operations(self):
        # create a graph
        graph = Graph()

        # add vertices to graph
        graph.add_edge("A", "B")
        graph.add_edge("A", "C")
        graph.add_edge("B", "D")

        # test graph operations
        self.assertIn("B", graph.graph["A"])
        graph.remove_edge("A", "B")
        self.assertNotIn("B", graph.graph["A"])

    # test graph empty remove edge
    def test_graph_empty_remove_edge(self):
        graph = Graph()
        graph.add_edge("A", "B")
        with self.assertRaises(ValueError):
            graph.remove_edge("A", "C")

if __name__ == "__main__":
    unittest.main()