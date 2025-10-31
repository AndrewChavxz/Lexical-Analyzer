import re   #importing regex

#creating sets of keywords.
KEYWORDS = {'#', 'asm', 'auto', 'bool', 'break', 'case', 
'catch', 'char', 'class', 'const', 'const_cast',
'continue', 'default', 'delete', 'do', 'double',
'dynamic_cast', 'else', 'enum', 'explicit', 'export',
'extern', 'false', 'float', 'for', 'friend',
'goto', 'if', 'inline', 'int', 'long',
'mutable', 'namespace', 'new', 'operator', 'private',
'protected', 'public', 'register', 'reinterpret_cast',
'return', 'short', 'signed', 'sizeof', 'static',
'static_cast', 'struct', 'switch', 'template', 'this',
'throw', 'true', 'try', 'typedef', 'typeid',
'typename', 'union', 'unsigned', 'using', 'virtual',
'void', 'volatile', 'wchar_t', 'while'
}
#creating a set of operators
OPERATORS = {
    '+', '-', '*', '/', '%', '++', '--',
'=', '+=', '-=', '*=', '/=', '%=', '<<=', '>>=', '&=', '^=', '|=',
'==', '!=', '>', '<', '>=', '<=',
'&&', '||', '!',
'&', '|', '^', '~', '<<', '>>',
'.', '->', '*', '&', '::', 'sizeof', 'typeid',
'?', ':', ',', 
'new', 'delete', 'new[]', 'delete[]',
'throw', 'dynamic_cast', 'static_cast', 'const_cast', 'reinterpret_cast',
'and', 'and_eq', 'bitand', 'bitor',
'compl', 'not', 'not_eq', 'or', 'or_eq', 'xor', 'xor_eq'
}
#creating a set of operators
SEPARATORS = {'(', ')', '[', ']', '{', '}', ',', ';'}

#this opens the file 
with open('C:/Users/Greg/Desktop/CSUF FALL 2025/COMPILER/c_code.txt', 'r') as file:
    content = file.read()  # reads the entire content of the file

#using regex to create patters in which will be used to extract from the file
number_pattern = r'\d+(\.\d+)?$'
identifier_pattern = r'^[A-Za-z_]\w*'
string_pattern = r'"[^"]*"|\'[^\']*\''
operator_pattern = '|'.join(re.escape(op) for op in OPERATORS)

#this is done to sort the operators, so that for example when combing through, '+=' will be identified as opposed to '+' and '=' seperately. 
OPERATORS = sorted(OPERATORS, key=len, reverse=True)
#using the regex, the file is combed through. the findall function finds anything in there that fits the criteria given.
#first, it is gone thru and comments such as // and /* and */ are removed.
content = re.sub(r'//.*|/\*.*?\*/', '', content, flags=re.DOTALL)
#this creates the set of tokens
tokens = re.findall(rf'"[^"]*"|\'[^\']*\'|[A-Za-z_]\w*|\d+\.\d+|\d+|{operator_pattern}|[^\s]', content)


#then, this set is gone through and compared to various criteria. 
for token in tokens:
    if token in KEYWORDS:
        print(f"{token} → KEYWORD")
    elif token in OPERATORS:
         print(f"{token} → OPERATOR")
    elif token in SEPARATORS:
        print(f"{token} -> SEPARATOR")
    elif re.match(number_pattern, token):
        print(f"{token} → LITERAL")
    elif re.match(identifier_pattern, token):
        print(f"{token} -> IDENTIFIER")
    elif re.match(string_pattern, token):
        print(f"{token} → STRING")
    
    else:
        print('Unrecognized Output')

