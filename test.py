""" """

import math
import random
from typing import *
from dataclasses import dataclass, field

class Heap:
    def __init__(self, data: List[Union[int, float]], heap_type: Callable = max) -> None:   
        self.heap_type = heap_type
        self._data = self._build_heap(data)

    def _build_heap(self, method: Callable) -> List:
        """ 
            Private method used to convert self._data
            to a valid heap-structure
        """

        i = len(self._data)
        while math.floor(i // 2) >= 1:
            self.heapify(self._data, i // 2, self.heap_type)
            i = math.floor(i // 2)

    @staticmethod
    def heapify(array: List, index: int, method: Callable) -> None:
        largest: int = index
        left: int = 2 * index + 1
        right: int = 2 * index + 2

        if left < len(array) and method(array[left], array[largest]) == array[left]:
            largest = left

        if left < len(array) and method(array[right], array[largest]) == array[right]:
            largest = right

        if largest != index:
            array[index], array[largest] = array[largest], array[index]
            heapify(array, largest, method)

    @classmethod
    def to_array(cls) -> List:
        """ """
        return cls._data

    def __get__(self, key) -> Any:
        """ Returns the element of index _key_
            in the heap structure.

            Raises KeyError if no value 
            exists at that index.
        """
        try:
            return self._data[key]
        except KeyError:
            raise

if __name__ == "__main__":

    heap_size: int = 100
    arbitrary_data: List[int] = [random.int(0, heap_size - 1) for _ in range(heap_size)]


    print(arbitrary_data)
    data_heap = Heap(arbitrary_data)
    print(Heap.to_array())