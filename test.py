from maximpact import MaxImpact

import unittest


class TestMaxImpact(unittest.TestCase):

    def setUp(self):
        self.mi = MaxImpact([{'x': 0, 'y': 0, 'r': 0}])

    def test_in_range(self):
        point1 = {'x': 10, 'y': 0, 'r': 10}  # False
        point2 = {'x': 0, 'y': 10, 'r': 0}

        point3 = {'x': 1.1, 'y': 0, 'r': 3}  # True
        point4 = {'x': 0, 'y': 7, 'r': 2}

        point5 = {'x': 3, 'y': 9, 'r': 4}  # False
        point6 = {'x': 1, 'y': 7, 'r': 0}

        self.assertEqual(self.mi.in_range(point1, point2), False)
        self.assertEqual(self.mi.in_range(point3, point4), True)
        self.assertEqual(self.mi.in_range(point5, point6), False)

    def test_get_max(self):
        """
        Experiment with different groups
        combinations.
        """

        # 0 and 1 combine
        groups1 = {
            0: [2, 1, 0],
            1: [0, 1],
            2: [],
            3: []
        }

        # mines 0 and 1 have equal impact
        valid = {0: set([0, 1, 2]), 1: set([0, 1, 2])}
        self.mi.groups = groups1
        self.assertEqual(self.mi.get_max(), valid)

        # 0 and 1 combine
        groups2 = {
            0: [2, 1, 0],
            1: [0, 1],
            2: [],
            3: [2]
        }

        # mines 0 and 1 have equal impact
        valid = {0: set([0, 1, 2]), 1: set([0, 1, 2])}
        self.mi.reset()
        self.mi.groups = groups2
        self.assertEqual(self.mi.get_max(), valid)

        # 0, 1, and 3 combine
        groups3 = {
            0: [2, 1, 0],
            1: [0, 1],
            2: [],
            3: [2, 1, 4],
            4: []
        }

        # mine 3 has greatest impact
        valid = {3: set([0, 1, 2, 4])}
        self.mi.reset()
        self.mi.groups = groups3
        self.assertEqual(self.mi.get_max(), valid)

        # 0, 1, and 3 combine
        groups4 = {
            0: [1, 0],
            1: [0, 1],
            2: [2],
            3: [3, 2, 1, 4],
            4: [4]
        }

        # mine 3 has greatest impact
        valid = {3: set([0, 1, 2, 3, 4])}
        self.mi.reset()
        self.mi.groups = groups4
        self.assertEqual(self.mi.get_max(), valid)

        # 0, 1, 3, and 4 combine
        groups5 = {
            0: [1, 0],
            1: [0, 1],
            2: [2],
            3: [3, 2, 1, 4],
            4: [4, 3]
        }

        # mine 3 and 4 have greatest impact
        valid = {3: set([0, 1, 2, 3, 4]), 4: set([0, 1, 2, 3, 4])} 
        self.mi.reset()
        self.mi.groups = groups5
        self.assertEqual(self.mi.get_max(), valid)

        # 0, 1, 3, and 4 combine
        groups6 = {
            0: [1, 0, 4],
            1: [1],
            2: [2],
            3: [3, 2, 4],
            4: [4, 3]
        }

        # mine 3 and 4 have greatest impact
        valid = {0: set([0, 1, 2, 3, 4])}
        self.mi.reset()
        self.mi.groups = groups6
        self.assertEqual(self.mi.get_max(), valid)

    def test_build_map(self):
        point1 = {'x': 1.1, 'y': 0, 'r': 3}
        point2 = {'x': 0, 'y': 7, 'r': 2}

        valid = {0: [0, 1], 1: [0, 1]}
        self.mi.graph = [point1, point2]
        self.assertEqual(self.mi.build_map(), valid)

        point3 = {'x': 1.1, 'y': 0, 'r': 0.9}
        point4 = {'x': 0, 'y': 10, 'r': 0}
        point5 = {'x': 2.2, 'y': 1.1, 'r': 4}
        point6 = {'x': 0, 'y': 0, 'r': 0}

        valid = {0: [0, 1, 3], 1: [0, 1], 2: [0, 2], 3: [0, 3]}
        self.mi.graph = [point3, point4, point5, point6]
        self.assertEqual(self.mi.build_map(), valid)
