"""
Q2. Consider a binary tree, with its structure(in C, but please feel free to redefine it as a class/object) given below,
 struct treeNode{
     int myData;
     treeNode * leftKid;
     treeNode * rightKid;
 };
 where each node stores a positive integer value. We define the distance of two nodes A and B in the tree as the sum of the values stored by the nodes in the path between them(including both A and B).
 Write a program to compute the maximum distance between any two nodes in a given tree.
 For example: given a tree as below,
  3
 / \
 2  5
   / \
   2 1
The program returns 12 as the answer.
"""


class Node(object):
    def __init__(self, value):
        self.left_node = None
        self.right_node = None
        self.value = value

        self.array = []

    def __str__(self):
        return '{}({})'.format(self.array, self.value)


class Tree:
    def __init__(self, value):
        self.root = Node(value)

    def _add(self, node, value):
        if node.value >= value:
            if node.left_node is None:
                node.left_node = Node(value)
            else:
                self._add(node.left_node, value)
        else:
            if node.right_node is None:
                node.right_node = Node(value)
            else:
                self._add(node.right_node, value)

    def insert(self, value):
        self._add(self.root, value)


class Solution(object):
    # Look to left and right
    # Pick subtree with highest sum
    # Join subtree
    @staticmethod
    def find_max_distance_with_path(root, container):
        if root is None:
            return Node(0)

        l = Solution.find_max_distance_with_path(root.left_node, container)
        r = Solution.find_max_distance_with_path(root.right_node, container)

        container[0] = (l.array + r.array + [root.value])

        if sum(l.array) >= sum(r.array):
            root.array = l.array
        else:
            root.array = r.array

        root.array.append(root.value)

        return root

    @staticmethod
    def find_max_distance_sum(root, container):
        if root is None:
            return 0

        # look to left, look to right
        l = Solution.find_max_distance_sum(root.left_node, container)
        r = Solution.find_max_distance_sum(root.right_node, container)
        # join paths
        container[0] = l + r + root.value
        # return the subtree max sum
        return max(l, r) + root.value

    # Return maximum path sum in tree with given root

    @staticmethod
    def find_max_with_paths(root):
        container = [[]]
        Solution.find_max_distance_with_path(root, container)
        print("paths", container[0])
        return sum(container[0])

    @staticmethod
    def find_max(root):
        container = [0]
        Solution.find_max_distance_sum(root, container)
        return container[0]


def result(tree):
    # Find both path and max
    # max_distance = Solution.find_max_with_paths(tree)
    max_distance = Solution.find_max(tree)
    print('Max distance', max_distance)


def example_one():
    #    3
    #   / \
    #  2   5
    #     / \
    #    2   1
    root = Node(3)
    node_one = Node(2)
    node_three = Node(5)
    node_four = Node(2)
    node_five = Node(1)

    root.left_node = node_one
    node_three.left_node = node_four
    node_three.right_node = node_five
    root.left_node = node_one
    root.right_node = node_three

    result(root)


def example_two():
    #          4
    #         / \
    #        3   5
    myTree = Tree(4)
    myTree.insert(3)
    myTree.insert(5)

    result(myTree.root)


def example_three():
    #           4
    #         /   \
    #        3     5
    #       / \     \
    #      1   4    12
    #     / \
    #    1   3
    myTree = Tree(4)
    myTree.insert(3)
    myTree.insert(5)
    myTree.insert(1)
    myTree.insert(1)
    myTree.insert(3)
    myTree.insert(12)
    myTree.insert(4)

    result(myTree.root)


example_one()
example_two()
example_three()
