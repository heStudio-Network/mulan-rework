from rply import LexerGenerator
import rply, re

# 顺序与词法规则添加顺序一致. 值不为中文的是关键词.

小数 = '小数'
整数 = '整数'
双引号字符串 = '双引号字符串'
单引号字符串 = '单引号字符串'
前大括号 = '前大括号'
后大括号 = '后大括号'
名词_空 = 'nil'
名词_真 = 'true'
名词_假 = 'false'
连词_且 = 'and'
连词_或 = 'or'
连词_如果 = 'if'
连词_否则如果 = 'elif'
连词_否则 = 'else'
连词_每当 = 'while'
动词_循环 = 'loop'
连词_对 = 'for'
动词_返回 = 'return'
动词_终止 = 'break'
动词_跳过 = 'continue'
名词_函数 = 'func'
名词_类型 = 'type'
动词_引用 = 'using'
连词_于 = 'in'
动词_试试 = 'try'
名词_操作符 = 'operator'
连词_每隔 = 'by'
形容词_外部 = 'extern'
名词_应变属性 = 'attr'
标识符 = '标识符'
点点小于 = '..<'
点点 = '..'
点 = '.'
名词_自身 = '$'
前中括号 = '['
后中括号 = ']'
前小括号 = '('
后小括号 = ')'
严格等于 = '==='
严格不等于 = '!=='
等于 = '=='
不等于 = '!='
大于等于 = '>='
小于等于 = '<='
箭头 = '->'
大于 = '>'
小于 = '<'
符号_赋值 = '='
逗号 = ','
增量赋值 = '+='
减量赋值 = '-='
加 = '+'
减 = '-'
星号 = '*'
除 = '/'
乘方 = '^'
分号 = ';'
非 = '!'
问号 = '?'
冒号 = ':'
换行 = '换行'

规则 = [
    小数,
    整数,
    加,
    减,
    星号,
    除,
    标识符,
    前小括号,
    后小括号,
    严格等于,
    严格不等于,
    等于,
    不等于,
    大于,
    小于,
    大于等于,
    小于等于,
    换行,
    符号_赋值,
    逗号,
    前大括号,
    后大括号,
    连词_如果,
    连词_否则如果,
    连词_否则,
    连词_或,
    连词_且,
    连词_每当,
    动词_终止,
    动词_跳过,
    名词_函数,
    动词_返回,
    问号,
    冒号,
    动词_引用,
    点,
    连词_于,
    名词_空,
    非,
    名词_类型,
    名词_操作符,
    形容词_外部,
    名词_真,
    名词_假,
    双引号字符串,
    单引号字符串,
    连词_对,
    点点,
    点点小于,
    分号,
    增量赋值,
    减量赋值,
    动词_循环,
    前中括号,
    后中括号,
    连词_每隔,
    箭头,
    乘方,
    名词_自身,
    名词_应变属性,
    动词_试试,
]

分词器母机 = LexerGenerator()

分词器母机.add(小数, '\\d+\\.\\d+')
分词器母机.add(整数, '\\d+')
分词器母机.add(双引号字符串, '(\\").*?\\1')
分词器母机.add(单引号字符串, "(\\').*?\\1")
分词器母机.add(前大括号, '{\\r*\\n*') # TODO: 何用？ , flags=(re.DOTALL)
# TODO: 参考[rply 测试用例](https://github.com/alex/rply/blob/19a9e08c486b2723a2e2378df6edb6a26e2df4a5/tests/test_lexer.py#L106)
# 不知在正则表达式中无`.`时此 flag 有何用
分词器母机.add(后大括号, '\\r*\\n*}') # , flags=(re.DOTALL)
分词器母机.add(名词_空, '\\bnil\\b')
分词器母机.add(名词_真, '\\btrue\\b')
分词器母机.add(名词_假, '\\bfalse\\b')
分词器母机.add(连词_且, '\\band\\b')
分词器母机.add(连词_或, '\\bor\\b')
分词器母机.add(连词_如果, '\\bif\\b')
分词器母机.add(连词_否则如果, '\\r*\\n*\\s*elif\\s*\\r*\\n*') # TODO: 何用？ , flags=(re.DOTALL)
分词器母机.add(连词_否则, '\\r*\\n*\\s*else\\s*\\r*\\n*') # , flags=(re.DOTALL)
分词器母机.add(连词_每当, '\\bwhile\\b')
分词器母机.add(动词_循环, '\\bloop\\b')
分词器母机.add(连词_对, '\\bfor\\b')
分词器母机.add(动词_返回, '\\breturn\\b')
分词器母机.add(动词_终止, '\\bbreak\\b')
分词器母机.add(动词_跳过, '\\bcontinue\\b')
分词器母机.add(名词_函数, '\\bfunc\\b')
分词器母机.add(名词_类型, '\\btype\\b')
分词器母机.add(动词_引用, '\\busing\\b')
分词器母机.add(连词_于, '\\bin\\b')
分词器母机.add(动词_试试, '\\btry\\b')
分词器母机.add(名词_操作符, '\\boperator\\b')
分词器母机.add(连词_每隔, '\\bby\\b')
分词器母机.add(形容词_外部, '\\bextern\\b')
分词器母机.add(名词_应变属性, '\\battr\\b')
分词器母机.add(标识符, '\\$?[_a-zA-Z\u4e00-\u9fa5][_a-zA-Z0-9\u4e00-\u9fa5]*')
分词器母机.add(点点小于, '\\.\\.<')
分词器母机.add(点点, '\\.\\.')
分词器母机.add(点, '\\.')
分词器母机.add(名词_自身, '\\$')
分词器母机.add(前中括号, '\\[')
分词器母机.add(后中括号, '\\]')
分词器母机.add(前小括号, '\\(')
分词器母机.add(后小括号, '\\)')
分词器母机.add(严格等于, '===')
分词器母机.add(严格不等于, '!==')
分词器母机.add(等于, '==')
分词器母机.add(不等于, '!=')
分词器母机.add(大于等于, '>=')
分词器母机.add(小于等于, '<=')
分词器母机.add(箭头, '->')
分词器母机.add(大于, '>')
分词器母机.add(小于, '<')
分词器母机.add(符号_赋值, '=')
分词器母机.add(逗号, ',')
分词器母机.add(增量赋值, '\\+=')
分词器母机.add(减量赋值, '-=')
分词器母机.add(加, '\\+')
分词器母机.add(减, '-')
分词器母机.add(星号, '\\*')
分词器母机.add(除, '/')
分词器母机.add(乘方, '\\^')
分词器母机.add(分号, ';')
分词器母机.add(非, '!')
分词器母机.add(问号, '\\?')
分词器母机.add(冒号, ':')
分词器母机.add(换行, '\n')
分词器母机.ignore('[ \t]+') # TODO: \r 何用? 也许和 windows 换行有关
分词器母机.ignore('//[^\n]*')
分词器母机.ignore('/\\*.*?\\*/', flags=(re.DOTALL))

分词器 = 分词器母机.build()
