from unittest import TestCase
from algos.utils import mount_from_file


class TestUtils(TestCase):

    def test_should_mount_an_array_from_file(self):
        result = mount_from_file("data/array.txt")

        self.assertEquals(3, len(result))
        self.assertEquals(64, result[1])