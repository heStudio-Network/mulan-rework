## 已实现语法
```
模块 : 声明列表

声明列表 : 表达式声明
        | 声明列表 换行 表达式声明

表达式声明 : 表达式

表达式 : 二元表达式
      | 数
      | 调用

数 : 整数

二元表达式 : 表达式 加 表达式
          | 表达式 減 表达式
          | 表达式 乘 表达式
          | 表达式 除 表达式

调用 : 变量 参数部分

参数部分 : ( 各参数 )

# TODO: 暂仅支持单参数
各参数 : 参数

变量 : 名称

名称 : 标识符

参数 : 表达式
```

## 开发环境

Python 3.7.4. 如使用 3.8, 语法树测试将失败.

## 运行

```
$ python 中.py 测试/四则运算.ul 
4
```

## 测试

```
$ chmod +x 中.py
$ python 测试.py
$ python test*
```