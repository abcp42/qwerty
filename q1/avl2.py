# -*- coding: UTF-8 -*-
"""
This script implements an AVL tree, ie. a self-balancing binary search tree.

This module contains 2 classes:

- Node, which has the following methods:
update_height, balance, search_unbalanced, in_order, pre_order, post_order

- Tree, which has the following methods:
find, insert, delete, get_min, get_max, inorder_traversal, preorder_traversal,
postorder_traversal

"""


class Node(object):
    """Class whose instances are part of a Tree instance."""
    def __init__(self, value,key):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
        self.height = 0
        self.key = key

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return str(self.value)

    def update_height(self):
        """Return the height of the tree root after updating all the node's
        (node=self) ancestors heights."""
        if self.left: left_height = self.left.height
        else: left_height = -1
        if self.right: right_height = self.right.height
        else: right_height = -1

        self.height = max(left_height, right_height) + 1
        if self.parent:
            self.parent.update_height()
        return self.height

    def balance(self):
        """Return self.parent after rotating self to balance the tree."""
        if not self.left: left_height = -1
        else: left_height = self.left.height
        if not self.right: right_height = -1
        else: right_height = self.right.height

        if left_height - right_height > 1: # if the left tree is higher
            if not self.left.left: left_height = -1
            else: left_height = self.left.left.height
            if not self.left.right: right_height = -1
            else: right_height = self.left.right.height

            if left_height < right_height: # left-right case
                # first : left_rotation(self.left)
                pivot = self.left.right
                pivot.parent = self
                if pivot.left:
                    new_subright = pivot.left
                    new_subright.parent = self.left
                else: new_subright = None
                self.left.right = new_subright # instead of pivot ; self.left.left doesn't change
                self.left.parent = pivot
                pivot.left = self.left # pivot.right doesn't change
                self.left = pivot
                self.left.left.update_height()
                # second (below): right_rotation(self)

            # left-left case = right_rotation(self)
            pivot = self.left
            pivot.parent = self.parent
            if pivot.parent != None:
                if pivot.value < pivot.parent.value:
                    pivot.parent.left = pivot
                else:
                    pivot.parent.right = pivot
            if pivot.right:
                new_subleft = pivot.right
                new_subleft.parent = self
            else: new_subleft = None
            pivot.right = self
            self.parent = pivot
            self.left = new_subleft

        elif left_height - right_height < -1: # if the right tree is higher
            if not self.right.left: left_height = -1
            else: left_height = self.right.left.height
            if not self.right.right: right_height = -1
            else: right_height = self.right.right.height

            if left_height > right_height: # right-left case
                # first : right_rotation(self.right)
                pivot = self.right.left
                pivot.parent = self
                if pivot.right:
                    new_subleft = pivot.right
                    new_subleft.parent = self.right
                else: new_subleft = None
                self.right.left = new_subleft # instead of pivot ; self.right.right doesn't change
                self.right.parent = pivot
                pivot.right = self.right # pivot.left doesn't change
                self.right = pivot
                self.right.right.update_height()
                # second (below): left_rotation(self)

            # right-right case = left_rotation(self)
            pivot = self.right
            pivot.parent = self.parent
            if pivot.parent != None:
                if pivot.value < pivot.parent.value:
                    pivot.parent.left = pivot
                else:
                    pivot.parent.right = pivot
            if pivot.left:
                new_subright = pivot.left
                new_subright.parent = self
            else: new_subright = None
            pivot.left = self
            self.parent = pivot
            self.right = new_subright

        self.update_height()

        return self.parent

    def search_unbalanced(self):
        """Recursively look for any unbalanced node by going up the tree and
        return the lowest unbalanced node.
        An unbalanced node is a node whose children's heights differ by more than 1."""
        if self.left: left_height = self.left.height
        else: left_height = -1
        if self.right: right_height = self.right.height
        else: right_height = -1

        if abs(left_height - right_height) > 1:
            return self
        else: # the current node is balanced
            if self.parent: return self.parent.search_unbalanced()
            else: return None

    def get_successor(self):
        """Return the node whose value is the minimum of the right subtree."""
        current = self.right
        while current.left:
            current = current.left
        return current

    def get_predecessor(self):
        """Return the node whose value is the maximum of the left subtree."""
        current = self.left
        while current.right:
            current = current.right
        return current

    def in_order(self):
        """Return a sorted list of all the values of the subtrees (including the
        root value). Return [None] if the tree in empty."""
        in_order_list = []
        if self.left:
            in_order_list.extend(self.left.in_order())
        in_order_list.append(self.value)
        if self.right:
            in_order_list.extend(self.right.in_order())
        return in_order_list

    def pre_order(self):
        """Return the pre-order list of all the nodes of the subtrees (including
        the root node)."""
        pre_order_list = []
        pre_order_list.append(self)
        if self.left:
            pre_order_list.extend(self.left.pre_order())
        if self.right:
            pre_order_list.extend(self.right.pre_order())
        return pre_order_list

    def post_order(self):
        """Return the post-order list of all the nodes of the subtrees (including
        the root node)."""
        post_order_list = []
        if self.left:
            post_order_list.extend(self.left.post_order())
        if self.right:
            post_order_list.extend(self.right.post_order())
        post_order_list.append(self)
        return post_order_list

class Tree(object):
    """Class whose instances are height-balanced binary search trees."""
    def __init__(self):
        self.root = None
        self.size = 0

    def find(self, val):
        """Return the node whose value is val if it is in the tree. Otherwise return False."""
        current = self.root
        # as long as the current node has 2 children
        while current.left and current.right:
            if val == current.value: return current
            elif val < current.value:
                current = current.left
            else:
                current = current.right

        if val == current.value: return current
        elif not current.left and not current.right: return False
        elif current.left: # if the current node has only a left child
            if val == current.left.value: return current
        elif current.right: # if the current node has only a right child
            if val == current.right.value: return current
        else: return False

    def insert(self, val,key):
        """Return the value of the tree root if the value passed as a parameter
        could be inserted and (if necessary) if the tree was re-balanced.
        If the value couldn't be inserted, return False."""
        if self.root is None: # if the tree is empty
            self.root = Node(val,key)
            self.size += 1
            return self.root

        current = self.root
        node_to_add = Node(val,key)
        #print('node_to_add',node_to_add.value)
        # if the current node has a left and a right child, go down the tree
        while current.left and current.right:
            if node_to_add.value == current.value: return False
            elif node_to_add.value < current.value:
                current = current.left
            else:
                current = current.right

        # cannot insert a value that's already in the tree
        if node_to_add.value == current.value: return False

        if not current.left and not current.right: # if the current node has no child
            if node_to_add.value < current.value:
                current.left = node_to_add
            else:
                current.right = node_to_add
            node_to_add.parent = current
            current.update_height()

        elif current.left: # if the current node has only a left child
            if node_to_add.value == current.left.value: return False

            elif node_to_add.value > current.value: # height of the tree unchanged
                current.right = node_to_add
                node_to_add.parent = current

            else: # need to update the height of the tree
                if node_to_add.value < current.left.value:
                    current.left.left = node_to_add
                    node_to_add.parent = current.left
                    current.left.update_height()
                else:
                    current.left.right = node_to_add
                    node_to_add.parent = current.left
                    current.left.update_height()

        else: # if the current node has only a right child
            if node_to_add.value == current.right.value: return False

            elif node_to_add.value < current.value: # height of the tree unchanged
                current.left = node_to_add
                node_to_add.parent = current

            else: # need to update the height of the tree
                if node_to_add.value > current.right.value:
                    current.right.right = node_to_add
                    node_to_add.parent = current.right
                    current.right.update_height()
                else:
                    current.right.left = node_to_add
                    node_to_add.parent = current.right
                    current.right.update_height()

        self.size += 1
        # check if the tree is unbalanced after inserting the new node
        unbalanced = node_to_add.search_unbalanced()
        if unbalanced:
            unbalanced_new_parent = unbalanced.balance()
            if unbalanced_new_parent.parent == None:
                self.root = unbalanced_new_parent
        return self.root # node successfully added and tree updated if needed

    def delete(self, val):
        """Return the root of the tree after deleting val and rebalancing the
        tree if necessary."""
        target = self.find(val)

        if not target: return False

        if not target.left and not target.right: # if deleting a leaf
            if not target.parent: # if target is the root of the tree and has no child
                #target.value = None
                #target.key = None
                self.size = 0
                self.root = target
                return self.root
            else: # if target isn't the root of the tree
                to_update = target.parent
                if target.value < target.parent.value:
                    target.parent.left = None
                else:
                    target.parent.right = None

        elif target.left and not target.right: # if the target has only a left child
            target.value = target.left.value
            target.key = target.left.key
            target.left = None
            to_update = target

        elif not target.left and target.right: # if the target has only a right child
            target.value = target.right.value
            target.key = target.right.key
            target.right = None
            to_update = target

        else: # if the target node has 2 children
            if target.left.height > target.right.height: # the left subtree is higher
                predecessor = target.get_predecessor() # successor has no left child
                target.value = predecessor.value # target value is updated but now we have a duplicate (successor) that we need to delete
                target.key = predecessor.key
                if predecessor.left: # deleting a node with only a left child
                    predecessor.value = predecessor.left.value
                    predecessor.key = predecessor.left.key
                    predecessor.left = None
                    to_update = predecessor
                else: # deleting a leaf
                    to_update = predecessor.parent
                    if to_update == target:
                        to_update.left = None
                    else:
                        to_update.right = None

            else: # if the right subtree is higher or at the same height than the left tree
                successor = target.get_successor() # successor has no left child
                target.value = successor.value # target value is updated but now we have a duplicate (successor) that we need to delete
                target.key = successor.key # target value is updated but now we have a duplicate (successor) that we need to delete
                
                if successor.right: # deleting a node with only a right child
                    successor.value = successor.right.value
                    successor.key = successor.right.key
                    successor.right = None
                    to_update = successor
                else: # deleting a leaf
                    to_update = successor.parent
                    if to_update == target:
                        to_update.right = None
                    else:
                        to_update.left = None

        self.size -= 1 # decrement the tree size by 1
        to_update.update_height()
        unbalanced = to_update.search_unbalanced()
        if unbalanced:
            unbalanced_new_parent = unbalanced.balance()
            if unbalanced_new_parent.parent == None:
                self.root = unbalanced_new_parent
        return self.root # node successfully added and tree re-balanced if needed

    def get_min(self):
        """Return the minimum value of the tree."""
        current = self.root
        while current.left:
            current = current.left
        return current

    def get_max(self):
        """Return the maximum value of the tree."""
        current = self.root
        while current.right:
            current = current.right
        return current.value

    def empty(self):
        """Return the root of the tree after it's emptied."""
        post_order = self.root.post_order()
        for node in post_order:
            if node.parent:
                if node == node.parent.left:
                    node.parent.left = None
                else:
                    node.parent.right = None
            else: # we've reached the tree root node
                self.root.value = None
                self.root.key = None
                self.root.height = 0
        self.size = 0
        return self.root

    def inorder_traversal(self):
        """Return a sorted list of all the values in the tree."""
        return self.root.in_order()

    def preorder_traversal(self):
        """Used to make a copy of the tree."""
        return self.root.pre_order()

    def postorder_traversal(self):
        """Used to delete the tree."""
        return self.root.post_order()
