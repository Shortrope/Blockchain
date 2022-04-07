# Testing
Generic test module
```python
from unittest import TestCase
from MODULE import CLASS_NAME, FUNC_NAME
# or
# import MODULE as INITIALS

Class PostTest(TestCase):
    def test_thing_I_am_testing(self):      #test case name starts w test_
        # setup
        self.assertTrue(booleanExpression)
        self.assertFalse(booleanExpression)
        self.assertEqual(expected result, actual result from method)
        self.assertListEqual(expected list, result_from_func_call)
        self.assertDictEqual(expected dict, actual result)
```

blog/tests/unit/test_post.py    # files starting w test_ will be automatically found by unittest
```python
from unittest import TestCase
form post import Post

Class PostTest(TestCase):
    def test_create_post(self)              
        p = Post('Test', 'Test Content')
        self.assertEqual('Test', p.title)   
        self.assertEqual('Test Content', p.content)
        
    def test_json_method(self):
        p = Post('Test', 'Test Content')
        expected = {'title': 'Test', 'content': 'Test Content'}
        self.assertDictEqual(expected, p.json())
        
```

Test __repr__ method