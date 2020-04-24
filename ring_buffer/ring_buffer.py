from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

# Check to see if at capacity
# if so move to tail
# set the value to the item being passed in
# if prev state set current to prev and assign current to tail
# otherwise if not at capacity add to the head of the list
    def append(self, item):
        if len(self.storage) == self.capacity:
            if self.current is None:
                self.current = self.storage.tail

            self.current.value = item

            if self.current.prev:
                self.current = self.current.prev

            else:
                self.current = self.storage.tail

        elif self.capacity > len(self.storage):
            self.storage.add_to_head(item)

    def get(self):
        list_buffer_contents = []
        selected_node = self.storage.tail

        while selected_node:
            if selected_node.value is not None:
                list_buffer_contents.append(selected_node.value)
            selected_node = selected_node.prev
        return list_buffer_contents


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
