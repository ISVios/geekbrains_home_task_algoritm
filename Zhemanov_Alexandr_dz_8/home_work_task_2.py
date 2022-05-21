#!/bin/env python
#2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
from collections import Counter, deque
################################################################################
class Node:
    ###
    def __init__(self, mass, value, left = None, right = None):
        self.mass  = mass
        self.value = value
        self.left  = left
        self.right = right
    ###
    def __gt__(self, other):
        return self.mass < other.mass
    ###
################################################################################
class Haffman: 
    def __init__(self):
        self.code = dict()
    def encode(self, in_str: str):

        lst_feq = [Node(count, char) for (char, count) in Counter(in_str).most_common()]
        
        while(len(lst_feq) > 1):
            b_node = lst_feq.pop()
            a_node = lst_feq.pop()
            c_node = Node(b_node.mass + a_node.mass, None, b_node, a_node)
            lst_feq.append(c_node)
            lst_feq.sort()

        lst_feq = lst_feq[0]
        self._gen_bit(lst_feq, [False])


        for ch in in_str:
            print(self.code[ch], end="")
        print()

    ###
    def _gen_bit(self, node, set_bit):
        
        if(node.value):
            self.code[node.value] = "".join([ "1" if bools else "0" for bools in set_bit])

        bit = set_bit[len(set_bit) - 1]
        
        if node.left:
            self._gen_bit(node.left, set_bit + [not bit])
            node.left = (set_bit, node.left)
        
        if node.right:
            self._gen_bit(node.right, set_bit + [bit])
            node.right = (not set_bit, node.left)
    ###
################################################################################

str_ = input("input text to Haffman encode: ")

haff = Haffman()
haff.encode(str_)
print(haff.code)
