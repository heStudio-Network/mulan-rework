**_注：本项目的开发管理今后将在 [OSChina](https://www.oschina.net/p/mulan-rework) 继续_**

## 前言
没错，这就是那个木兰。

2020 年一月第一时间提出知乎问题[「木兰」编程语言有什么特色？](https://www.zhihu.com/question/366509495/answer/977696328)的正是本人。至于此项目的渊源，见[悬赏布告](https://github.com/MulanRevive/bounty)和[木兰编程语言专栏](https://zhuanlan.zhihu.com/ulang)。

## 项目目标

逐步实现木兰编程语言与交互环境的所有功能。

将源程序转换为 Python 的中间表示（AST），可较便利地实现各种语法设计与周边功能。这种方式值得探索和研究。

## 运行

如下运行源码（建议`.ul`后缀）。

```
$ python 中.py 测试/运算/四则运算.ul
4
```

下面[例程](测试/手工测试/草蟒_海龟.ul)调用了[草蟒](https://www.oschina.net/p/grasspy)的中文 API：
```javascript
using * in 海龟
颜色("黄色", "红色")
开始填充()
for 拐数 in 0..4 {
  前进(200)
  右转(144)
}
结束填充()
主循环()
```

更多测试用例[在此](测试)。

## 开发环境

个人使用 Mac 开发，需 Python 3.7。如使用 3.8，语法树测试将失败。

为提高开发维护效率，本项目中尽量使用中文标识符。包括语法规则、Python 代码等等。

依赖 Python 包：
- rply

## 已实现功能

随着项目推进，将同步[语法说明](文档/语法说明.md)。另外，为调试方便，报错等等反馈信息将中文化。短期内的目标细化[在此](文档/待决问题)。

## 测试

```
$ chmod +x 中.py
$ python 运行测试.py
$ python test语法树.py
```

## 许可证

GNU GPLv3
