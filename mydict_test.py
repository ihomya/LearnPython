import unittest

from mydict import Dict


# 编写一个测试类，从unittest.TestCase继承
class TestDict(unittest.TestCase):
    # 以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法
    def test_init(self):
        d = Dict(a=1, b='test')
        # self.assertEqual(abs(-1), 1) # 断言函数返回的结果与1相等
        self.assertEqual(d.a, 1)  # 最常用的断言就是assertEqual()
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        # 另一种重要的断言就是期待抛出指定类型的Error，
        # 比如通过d['empty']访问不存在的key时，断言会抛出KeyError
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        # 而通过d.empty访问不存在的key时，我们期待抛出AttributeError
        with self.assertRaises(AttributeError):
            value = d.empty

    # 这两个方法会分别在每调用一个测试方法的前后分别被执行
    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')


# 运行单元测试
if __name__ == '__main__':
    unittest.main()
