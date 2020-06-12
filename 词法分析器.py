from rply import LexerGenerator
import rply, re

规则 = [
    '小数',
    '整数',
    '加',
    '減',
    '星号',
    '除',
    '标识符',
    '(',
    ')',
    '===',
    '!==',
    '==',
    '!=',
    '>',
    '<',
    '>=',
    '<=',
    '换行',
    '=',
    ',',
    '前括号',
    '后括号',
    '连词_如果',
    '连词_否则如果',
    '连词_否则',
    '连词_或',
    '连词_且',
    '连词_每当',
    '动词_终止',
    '动词_跳过',
    '名词_函数',
    '动词_返回',
    '?',
    ':',
    '动词_引用',
    '点',
    '连词_于',
    '名词_空',
    '非',
    '名词_类型',
    '名词_操作符',
    '形容词_外部',
    '名词_真',
    '名词_假',
    '字符串字面量',
    '连词_对',
]

分词器母机 = LexerGenerator()

分词器母机.add('小数', '\\d+\\.\\d+')
分词器母机.add('整数', '\\d+')
分词器母机.add('字符串字面量', '(\\").*?\\1')
分词器母机.add('前括号', '{\\r*\\n*') # TODO: 何用？ , flags=(re.DOTALL)
分词器母机.add('后括号', '\\r*\\n*}') # , flags=(re.DOTALL)
分词器母机.add('名词_空', '\\bnil\\b')
分词器母机.add('名词_真', '\\btrue\\b')
分词器母机.add('名词_假', '\\bfalse\\b')
分词器母机.add('连词_且', '\\band\\b')
分词器母机.add('连词_或', '\\bor\\b')
分词器母机.add('连词_如果', '\\bif\\b')
分词器母机.add('连词_否则如果', '\\r*\\n*\\s*elif\\s*\\r*\\n*') # TODO: 何用？ , flags=(re.DOTALL)
分词器母机.add('连词_否则', '\\r*\\n*\\s*else\\s*\\r*\\n*') # , flags=(re.DOTALL)
分词器母机.add('连词_每当', '\\bwhile\\b')
分词器母机.add('连词_对', '\\bfor\\b')
分词器母机.add('动词_返回', '\\breturn\\b')
分词器母机.add('动词_终止', '\\bbreak\\b')
分词器母机.add('动词_跳过', '\\bcontinue\\b')
分词器母机.add('名词_函数', '\\bfunc\\b')
分词器母机.add('名词_类型', '\\btype\\b')
分词器母机.add('动词_引用', '\\busing\\b')
分词器母机.add('连词_于', '\\bin\\b')
分词器母机.add('名词_操作符', '\\boperator\\b')
分词器母机.add('形容词_外部', '\\bextern\\b')
分词器母机.add('标识符', '\\$?[_a-zA-Z\u4e00-\u9fa5][_a-zA-Z0-9\u4e00-\u9fa5]*')
分词器母机.add('点', '\\.')
分词器母机.add('(', '\\(')
分词器母机.add(')', '\\)')
分词器母机.add('===', '===')
分词器母机.add('!==', '!==')
分词器母机.add('==', '==')
分词器母机.add('!=', '!=')
分词器母机.add('>=', '>=')
分词器母机.add('<=', '<=')
分词器母机.add('>', '>')
分词器母机.add('<', '<')
分词器母机.add('=', '=')
分词器母机.add(',', ',')
分词器母机.add('加', '\\+')
分词器母机.add('減', '-')
分词器母机.add('星号', '\\*')
分词器母机.add('除', '/')
分词器母机.add('非', '!')
分词器母机.add('?', '\\?')
分词器母机.add(':', ':')
分词器母机.add('换行', '\n')
分词器母机.ignore('[ \t]+') # TODO: \r 何用? 也许和 windows 换行有关
分词器母机.ignore('/\\*.*?\\*/', flags=(re.DOTALL))

分词器 = 分词器母机.build()
