from utils import mount_from_file
from counters import Counters


def count_inversions():
    array = mount_from_file("data/IntegerArray.txt")
    return Counters(array).count_inversions()

print count_inversions()