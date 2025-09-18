#!/usr/bin/python3
"""Defines classes for a singly linked list."""


class Node:
    """Class defines a node of a singly linked list."""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter for private data attribute"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter for data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Defines a SinglyLInkedList class.
    This class supportes inserting vlaues in sorted ascending order,
    and provides a string representation of a list, one number per line.
    """

    def __init__(self):
        self.__head = None

    def __str__(self):
        """
        Special method to represent the object as a string
        and make the print() work
        """

        node = self.__head
        values = []

        while node is not None:
            values.append(str(node.data))
            node = node.next_node

        return "\n".join(values)    

    def sorted_insert(self, value):
        """Method inserts a new Node into a singly linked list"""
        new_node = Node(value)

        if self.__head is None:
            self.__head = new_node
            return

        if value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while (
            current.next_node is not None and
            current.next_node.data < value
            ):
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node
