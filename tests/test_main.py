import unittest
from keras.datasets import mnist


class TestKondaraStudy(unittest.TestCase):
    def test_main(self):
        (train_images, train_labels), (test_images, test_labels) = mnist.load_data()

        self.assertEqual("foo".upper(), "FOO")


if __name__ == "__main__":
    unittest.main()
