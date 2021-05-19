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
动词_接手 = 'catch'
动词_抛出 = 'throw'
名词_操作符 = 'operator'
连词_每隔 = 'by'
形容词_外部 = 'extern'
名词_超类 = 'super'
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
左移 = '<<'
右移 = '>>'
与 = '&'
或 = '|'
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
求余 = '%'
乘方 = '^'
分号 = ';'
非 = '!'
问号 = '?'
冒号 = ':'
取反 = '~'
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
    左移,
    右移,
    与,
    或,
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
    求余,
    名词_超类,
    取反,
    动词_抛出,
    动词_接手,
]

分词器母机 = LexerGenerator()

分词器母机.add(小数, r'\d+\.\d+')
分词器母机.add(整数, r'\d+')
分词器母机.add(双引号字符串, r'(")((?<!\\)\\\1|.)*?\1')
分词器母机.add(单引号字符串, r"(')((?<!\\)\\\1|.)*?\1")  # \' 之前不能有 \
分词器母机.add(前大括号, r'{\r*\n*')  # TODO: 何用？ , flags=(re.DOTALL)
# TODO: 参考[rply 测试用例](https://github.com/alex/rply/blob/19a9e08c486b2723a2e2378df6edb6a26e2df4a5/tests/test_lexer.py#L106)
# 不知在正则表达式中无`.`时此 flag 有何用
分词器母机.add(后大括号, r'\r*\n*}')  # , flags=(re.DOTALL)
分词器母机.add(名词_空, r'\bnil\b')
分词器母机.add(名词_真, r'\btrue\b')
分词器母机.add(名词_假, r'\bfalse\b')
分词器母机.add(连词_且, r'\band\b')
分词器母机.add(连词_或, r'\bor\b')
分词器母机.add(连词_如果, r'\bif\b')
分词器母机.add(连词_否则如果, r'\r*\n*\s*elif\s*\r*\n*')  # TODO: 何用？ , flags=(re.DOTALL)
分词器母机.add(连词_否则, r'\r*\n*\s*else\s*\r*\n*')  # , flags=(re.DOTALL)
分词器母机.add(连词_每当, r'\bwhile\b')
分词器母机.add(动词_循环, r'\bloop\b')
分词器母机.add(连词_对, r'\bfor\b')
分词器母机.add(动词_返回, r'\breturn\b')
分词器母机.add(动词_终止, r'\bbreak\b')
分词器母机.add(动词_跳过, r'\bcontinue\b')
分词器母机.add(名词_函数, r'\bfunc\b')
分词器母机.add(名词_类型, r'\btype\b')
分词器母机.add(动词_引用, r'\busing\b')
分词器母机.add(连词_于, r'\bin\b')
分词器母机.add(动词_试试, r'\btry\b')
分词器母机.add(动词_接手, r'\r*\n*\s*catch\s*\r*\n*')  # , flags=(re.DOTALL)
分词器母机.add(动词_抛出, r'\bthrow\b')
分词器母机.add(名词_操作符, r'\boperator\b')
分词器母机.add(连词_每隔, r'\bby\b')
分词器母机.add(形容词_外部, r'\bextern\b')
分词器母机.add(名词_超类, r'\bsuper\b')
分词器母机.add(名词_应变属性, r'\battr\b')
分词器母机.add(标识符, r'\$?[_a-zA-Z\u4e00-\u9fa5][_a-zA-Z0-9\u4e00-\u9fa5]*')
分词器母机.add(点点小于, r'\.\.<')
分词器母机.add(点点, r'\.\.')
分词器母机.add(点, r'\.')
分词器母机.add(名词_自身, r'\$')
分词器母机.add(前中括号, r'\[')
分词器母机.add(后中括号, r'\]')
分词器母机.add(前小括号, r'\(')
分词器母机.add(后小括号, r'\)')
分词器母机.add(严格等于, '===')
分词器母机.add(严格不等于, '!==')
分词器母机.add(等于, '==')
分词器母机.add(不等于, '!=')
分词器母机.add(大于等于, '>=')
分词器母机.add(小于等于, '<=')
分词器母机.add(箭头, '->')
分词器母机.add(左移, '<<')
分词器母机.add(右移, '>>')
分词器母机.add(与, r'&')
分词器母机.add(或, r'\|')
分词器母机.add(大于, '>')
分词器母机.add(小于, '<')
分词器母机.add(符号_赋值, '=')
分词器母机.add(逗号, ',')
分词器母机.add(增量赋值, r'\+=')
分词器母机.add(减量赋值, '-=')
分词器母机.add(加, '\+')
分词器母机.add(减, '-')
分词器母机.add(星号, '\*')
分词器母机.add(除, '/')
分词器母机.add(求余, '%')
分词器母机.add(乘方, r'\^')
分词器母机.add(分号, ';')
分词器母机.add(非, '!')
分词器母机.add(问号, r'\?')
分词器母机.add(冒号, ':')
分词器母机.add(取反, '~')
分词器母机.add(换行, r'\n')
分词器母机.ignore('[ \t]+')  # TODO: \r 何用? 也许和 windows 换行有关
分词器母机.ignore('//[^\n]*')
分词器母机.ignore('/\\*.*?\\*/', flags=(re.DOTALL))

分词器 = 分词器母机.build()
