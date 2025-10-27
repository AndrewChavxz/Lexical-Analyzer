import re

Keywords = {
    "int", "return", "if", "else", "while", "for", "void", "char", "float", "double"
}

Opreators = [
    ">>=", "<<=", "==", "!=", ">=", "<=", "&&", "||", "->", "::", "+=", "-=", "*=", "/=", "%=",
    "<<", ">>",
    "+", "-", "*", "/", "%", "=", ">", "<", "!", "&", "|", "^", "~", "?"
]

Separators = set("(){}[],;.:#")

String_pattern = r'"(?:\\.|[^"\\])*"' # accepts any sting within (""), accepts special and normal characters

Char_pattern   = r"'(?:\\.|[^'\\])'" # accepts any strinf within (''), accepts escape char(\n)

Multi_operator = "|".join(re.escape(op) for op in sorted(Opreators, key=len, reverse=True)) # sorts the opreators from longest to shortest and allows symbols

Identifier_pattern = r'[A-Za-z_]\w*' # accepts variable names, first char must be a letter or _. 

Int_pattern   = r'\d+' # any int, no decimals

Single_separators  = "[" + re.escape("".join(Separators)) + "]" # takes all separators, re.escape() to make sure special symbols like . or [ are treated literally 

Single_operator   = r'[+\-*/=><!&|^~?]' # takes any symbol in the []

