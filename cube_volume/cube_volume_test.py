import unittest

from cube_volume.cube_volume import cub_volume


class TestCube(unittest.TestCase):

    def test_volume(self):
        self.assertAlmostEqual(cub_volume(2), 8)
        self.assertAlmostEqual(cub_volume(1), 1)
        self.assertAlmostEqual(cub_volume(0), 0)
        self.assertAlmostEqual(cub_volume(5.5), 166.375)