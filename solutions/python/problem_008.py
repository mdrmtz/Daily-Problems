import unittest


def two_sum(numbers, k):
    for n in numbers:
        if k - n in numbers:
            return True

    return False


# True
print(two_sum([4, 7, 1, -3, 2], 5))


class Test(unittest.TestCase):
    def test_two_sum(self):
        self.assertEqual(two_sum([], 17), False)
        assert not two_sum([], 17)
        assert two_sum([10, 15, 3, 7], 17)
        assert not two_sum([10, 15, 3, 4], 17)


if __name__ == '__main__':
    unittest.main()
