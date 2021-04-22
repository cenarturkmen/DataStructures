# https://runestone.academy/runestone/books/published/pythonds3/Trees/BinaryHeapImplementation.html
"""
Another interesting property of a complete tree is that we can represent it using a single list.
We do not need to use nodes and references or even lists of lists.
Because the tree is complete, the left child of a parent (at position p) 
is the node that is found in position 2p+1 in the list. 
Similarly, the right child of the parent is at position 2p+2 in the list.
Given that a node is at position n in the list, the parent is at position (n−1)//2.
"""
class BinaryHeap():
    def __init__(self):
        self._heap = []
    
    def insert(self, item):
        self._heap.append(item)
        self._perc_up(len(self._heap)-1)

    def _perc_up(self, cur_idx):
        while (cur_idx - 1) // 2 >= 0:
            parent_idx = (cur_idx - 1) // 2
            if self._heap[cur_idx] < self._heap[parent_idx]:
                self._heap[cur_idx], self._heap[parent_idx] = self._heap[parent_idx], self._heap[cur_idx]
            cur_idx = parent_idx

    def get_min(self):
        return self._heap[0]

    def delete(self):
        self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
        result = self._heap.pop()
        self._perc_down(0)
        return result

    def _perc_down(self, cur_idx):
        while 2 * cur_idx + 1 < len(self._heap):
                min_child_idx = self._get_min_child(cur_idx)
                if self._heap[cur_idx] > self._heap[min_child_idx]:
                    self._heap[cur_idx], self._heap[min_child_idx] = self._heap[min_child_idx], self._heap[cur_idx]

                else:
                    return
                cur_idx = min_child_idx
                
    def _get_min_child(self, parent_idx):
        if 2 * parent_idx + 2 > len(self._heap) - 1:
            return 2 * parent_idx + 1        

        if self._heap[2 * parent_idx + 1] < self._heap[2 * parent_idx + 2]:
            return 2 * parent_idx + 1

        return 2 * parent_idx + 2


    def is_empty(self):
        return not bool(self._heap)

    def size(self):
        return len(self._heap)
   

heap = BinaryHeap()

heap.insert(1)
heap.insert(2)
heap.insert(3)
heap.insert(4)
heap.insert(5)
print(heap._heap)

heap.delete()
print(heap._heap)

print(heap.is_empty())
print(heap.size())
print(heap.get_min())