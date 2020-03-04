'''
Q3. Consider a binary tree, with its structure (in C, but please feel free to redefine it as a class/object) given below,
struct treeNode{
    int myData;
    treeNode* leftKid;
    treeNode* rightKid;
};
where each node stores a positive integer value. Write a program to print out all the leaf nodes in the tree, whose value is smaller than all of its ancestors.
For example: given a tree as below,

  3
 / \
2   5
   / \
  2   4
The program prints: 2 2
'''


class Node:
    def __init__(self, value):
        self.left_node = None
        self.right_node = None
        self.value = value


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


class Solution:
    @staticmethod
    def find_leaf(node, smallest, collection):
        if node is None:
            return
        # Compare at leaf node
        if node.left_node is None and node.right_node is None and smallest > node.value:
            collection.append(node.value)

        smallest_left = min(node.value, smallest)
        Solution.find_leaf(node.left_node, smallest_left, collection)

        smallest_right = min(node.value, smallest)
        Solution.find_leaf(node.right_node, smallest_right, collection)


def result(root, seed):
    answers = []
    Solution.find_leaf(root, seed, answers)
    print('Smallest leaves are:', answers)


def example_one():
    #   3
    #  / \
    # 2   5
    #    / \
    #   2   4
    nodeThree = Node(5)
    nodeThree.left_node = Node(2)
    nodeThree.right_node = Node(4)

    root = Node(3)
    root.left_node = Node(2)
    root.right_node = nodeThree
    result(root, 5)


def example_two():
    #          11
    #         / \
    #        8   12
    myTree = Tree(11)
    myTree.insert(8)
    myTree.insert(12)
    result(myTree.root, float("inf"))


def example_three():
    #           11
    #         /   \
    #        8     12
    #       /  \     \
    #      1    9    12
    #     / \
    #    1   7
    #       /
    #      3
    myTree = Tree(11)
    myTree.insert(8)
    myTree.insert(12)
    # change this to 2
    myTree.insert(1)
    myTree.insert(7)
    myTree.insert(3)
    myTree.insert(1)
    myTree.insert(12)
    myTree.insert(9)

    result(myTree.root, float("inf"))


example_one()
example_two()
example_three()
