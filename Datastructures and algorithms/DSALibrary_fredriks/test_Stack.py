import unittest
from Stack import Stack

class TestStack(unittest.TestCase):
    def test_01_simple_push_and_pop_and_isEmpty(self):
        stack = Stack()

        stack.push(50)
        stack.push(60)
        stack.push(70)

        val = stack.pop()
        self.assertEqual(val, 70)

        val = stack.pop()
        self.assertEqual(val, 60)

        self.assertEqual(stack.isEmpty(), False)

    def test_02_stack_peek_test(self):
        stack = Stack()

        stack.push(50)
        stack.push(60)
        stack.push(70)

        self.assertEqual(stack.peek(), 70)







if __name__ == '__main__':
    unittest.main(verbosity=2)
