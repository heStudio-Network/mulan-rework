import unittest

from 编辑器.运行木兰 import 运行木兰代码
from 木兰.分析器.错误 import 语法错误
from 木兰.功用.反馈信息 import *
from 测试.unittest.功用 import *

class test所有(unittest.TestCase):

    def test_运行前报错(self):
        对应报错 = {
            "测试/错误处理/2.ul": "没认出这个词 \"整数\"",

            # TODO：如果是用错关键词，如 throw 用错为 raise（原 py 用户）则应提示
            "测试/错误处理/不识关键词.ul": "没认出这个词 \"标识符\"",

            "测试/错误处理/列表内容末尾逗号.ul": "没认出这个词 \"]\"",
            "测试/错误处理/属性为关键词self.ul": "没认出这个词 \"while\"",
        }
        for 文件 in 对应报错:
            try:
                读源码生成树(文件)
                self.fail("不该到这")
            except 语法错误 as e:
                self.assertEqual(e.信息, 对应报错[文件], 文件)

    def test_运行时报错(self):
        对应报错 = {
            "测试/错误处理/下标越界.ul": 报错_列表索引,

            # TODO: catch 的类型指定尚无实际作用
            "测试/错误处理/catch类型错误.ul": 报错_列表索引,
            "测试/错误处理/try随意.ul": "需要添加此属性：__enter__" + 参考_enter,
            "测试/错误处理/全局.ul": "请先对本地变量‘x’赋值再引用",
            "测试/错误处理/调用错误函数.ul": "请先定义‘b’再使用",
            "测试/错误处理/多行除零.ul": "请勿除以零",
            "测试/错误处理/字典无键.ul": "字典中不存在此键：4",
            "测试/错误处理/字符串拼接.ul": "字符串只能拼接字符串，请将“int”先用 str() 转换",
            "测试/错误处理/属性被静态调用.ul": "需要添加此属性：'function' object has no attribute 'var'",

            # TODO:
            # 测试/错误处理/不可见字符.ul
        }
        for 文件 in 对应报错:
            报错 = 运行木兰代码(文件)
            self.assertEqual(报错[0], 对应报错[文件], 文件)

        单层报错 = {
            "测试/错误处理/catch2.ul": "语法错误: default 'except:' must be last (catch2.ul, line 2)\n",
            "测试/错误处理/函数外return.ul": "语法错误: 'return' outside function (函数外return.ul, line 2)\n",
        }
        for 文件 in 单层报错:
            self.assertEqual(运行木兰代码(文件), 单层报错[文件], 文件)

    def test_行号(self):
        try:
            读源码生成树("测试/错误处理/属性为关键词引用.ul")
            self.fail("不该到这")
        except 语法错误 as e:
            self.assertEqual(e.信息, "没认出这个词 \"while\"")
            self.assertEqual(e.行号, 7)  # 第三行定义可以, 第七行引用时报错

    def test_列号(self):
        try:
            节点 = 生成语法树("using func")
            self.fail("不该到这")
        except 语法错误 as e:
            self.assertEqual(e.列号, 7)

    def test_行列号(self):
        try:
            读源码生成树("测试/错误处理/词不识.ul")
        except 语法错误 as e:
            self.assertEqual(e.信息, "分词时没认出这个词 \"#\"")
            self.assertEqual(e.行号, 3)
            self.assertEqual(e.列号, 6) # 应该为 1, 在rply 提问: https://github.com/alex/rply/pull/95#issuecomment-729513800
