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

    def find_enhanced(self, array, number):
        i = len(array) / 2

        if (number == array[i]):
            return True

        elif (len(array) == 1):
            return False

        elif (number < array[i]):
            if (i - 1 >= 0 and i + 1 < len(array)
                           and array[i - 1] < array[i]
                           and array[i + 1] < array[i]):
                return self.find_enhanced(array[0:i], number) or self.find_enhanced(array[i + 1: len(array)], number)
            else:
                return self.find_enhanced(array[0:i], number)

        else:
            if (i - 1 >= 0 and i + 1 < len(array)
                           and array[i - 1] > array[i]
                           and array[i + 1] > array[i]):

                return self.find_enhanced(array[0:i], number) or self.find_enhanced(array[i + 1: len(array)], number)

        return self.find_enhanced(array[i + 1:len(array)], number)




