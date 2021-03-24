import ipdb

class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self, head=None, default_node=Node):
        self.head = head
        self.ll_size = 0
        if self.head:
            self.ll_size += 1
        
        self._default_node = default_node

    def set_node_creater(self, node_cls):
        self._default_node = node_cls
        return self

    def at_begin_insert(self, data):
        new_node = self._default_node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.ll_size += 1
        return True

    def in_between_insert(self, data, exist_node):
        if not (exist_node and isinstance(exist_node, self._default_node)):
            return False

        new_node = self._default_node(data)
        new_node.next = exist_node.next
        exist_node.next = new_node
        self.ll_size += 1
        return True
    
    def at_end_insert(self, data):
        if not self.head:
            return False

        new_node = self._default_node(data)
        curr_node = self.head
        if not curr_node:
            curr_node = new_node
        else:
            while curr_node.next:
                curr_node = curr_node.next

            curr_node.next = new_node
        
        self.ll_size += 1
        return True
    
    def remove_node(self, data_key):
        if not self.head:
            return False

        curr_node = self.head
        prev_node = None
        while curr_node or prev_node:
            if curr_node.data == data_key:
                prev_node.next = curr_node.next
                del curr_node
                self.ll_size -= 1
                break
            
            prev_node = curr_node
            curr_node = curr_node.next
        
        return True

    def get_nodes(self):
        if not self.head:
            return False

        curr_node = self.head
        nodes_store = []
        while curr_node:
            nodes_store.append(curr_node.data)
            curr_node = curr_node.next
        
        return nodes_store

    def get_node(self, data_key):
        if not self.head:
            return False

        curr_node = self.head
        while curr_node:
            if curr_node.data == data_key:
                return curr_node

            curr_node = curr_node.next

        return False


if __name__ == "__main__":
    root = Node("#ROOT")
    ll = LinkedList(head=root)
    
    ll.at_begin_insert("SUB_CHILD #1")
    ll.at_begin_insert("SUB_CHILD #2")
    ll.at_begin_insert("SUB_CHILD #3")

    ll.at_end_insert("LAST_CHILD #10")
    ll.at_end_insert("LAST_CHILD #11")
    ll.at_end_insert("LAST_CHILD #12")

    nd = ll.get_node(data_key="SUB_CHILD #3")
    ll.in_between_insert(data="SUPER NODE #99", exist_node=nd)
    
    print(ll.get_nodes())
    print(ll.ll_size)

    ll.remove_node("SUB_CHILD #2")
    ll.remove_node("LAST_CHILD #12")
    ll.remove_node("LAST_CHILD #11")

    print(ll.get_nodes())
    print(ll.ll_size)

