import unittest
import watchhandle

class MyTestCase(unittest.TestCase):
    def test(self):
        watchhandle.process_handle_output("svchost")


if __name__ == '__main__':
    unittest.main()
