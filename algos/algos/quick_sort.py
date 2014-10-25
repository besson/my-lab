class QuickSort:

    def __init__(self, array):
        self._array = array

    def sort(self):
        self._sort(self._array, 0, len(self._array) - 1)
        return self._array

    def _sort(self, array, start, end):
        if start < end:
            p = self.partition(array, start, end)
            self._sort(array, start, p - 1)
            self._sort(array, p + 1, end)

    def partition(self, array, i, j):
        pos = i
        i = i + 1

        while (i <= j):
            if (array[i] < array[pos]):
                i = i + 1
            elif (array[j] > array[pos]):
                j = j - 1
            else:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
                i = i + 1
                j = j - 1

        pivot = array[pos]
        array[pos] = array[i - 1]
        array[i - 1] = pivot

        return i - 1