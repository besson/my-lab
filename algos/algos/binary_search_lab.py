class BinarySearchLab:

    def find(self, array, number):
        i = len(array) / 2

        if (number == array[i]):
            return True
        elif (len(array) == 1):
            return False
        elif (number < array[i]):
            return self.find(array[0:i], number)

        return self.find(array[i + 1:len(array)], number)
