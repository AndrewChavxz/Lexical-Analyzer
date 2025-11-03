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

String_pattern = r'"(?:\\.|[^"\\])*"'  # accepts any string within (""), accepts special and normal characters
Char_pattern   = r"'(?:\\.|[^'\\])'"   # accepts any string within (''), accepts escape char(\n)

Multi_operator = "|".join(re.escape(op) for op in sorted(Opreators, key=len, reverse=True))  # longest-first
Identifier_pattern = r'[A-Za-z_]\w*'   # variable names, first char must be a letter or _
Int_pattern   = r'\d+'                 # any int, no decimals
Single_separators  = "[" + re.escape("".join(Separators)) + "]"  # single-char separators
Single_operator   = r'[+\-*/=><!&|^~?]'                          # single-char operators

# Create one big regex that matches all token types
# The pattern checks for the most specific matches first (like strings or multi-character operators)

# re.compile(...):  builds the regex so it runs faster later.
# rf""" ... """: lets you insert other regex variables
# re.VERBOSE:  lets you write the regex neatly across multiple lines with comments.
MASTER = re.compile(
    rf"""(
        {String_pattern}        |  # 1: string
        {Char_pattern}          |  # 2: char
        {Multi_operator}        |  # 3: multi-char op
        {Identifier_pattern}    |  # 4: identifier
        {Int_pattern}           |  # 5: int
        {Single_separators}     |  # 6: single char separator
        {Single_operator}          # 7: single char operator
    )""",
    re.VERBOSE # Makes the regex easier to read by allowing spaces and comments
)

def classify(lexeme: str) -> str:
    if lexeme in Keywords:
        return "keyword"
    if lexeme in Opreators:
        return "operator"
    if len(lexeme) == 1 and lexeme in Separators:
        return "separator"
    if re.fullmatch(Int_pattern, lexeme):
        return "integer"
    if re.fullmatch(String_pattern, lexeme):
        return "string"
    if re.fullmatch(Char_pattern, lexeme):
        return "char"
    return "identifier"

def main():
    filename = input("Enter the path to your .txt file: ").strip().strip('"')
    try:
        with open(filename, "r", encoding="utf-8") as f:
            code = f.read()
    except OSError as e:
        print(f"Could not open file: {e}")
        return

    code = re.sub(r'//.*', '', code)              # remove // line comments
    code = re.sub(r'/\*[\s\S]*?\*/', '', code)    # remove /* ... */ block comments

    # Scan and print tokens
    i, n = 0, len(code)

    while i < n: # Skip spaces, tabs, and newlines
        if code[i].isspace():
            i += 1
            continue

        m = MASTER.match(code, i) # Try to match a token using the MASTER regular expression
        if m:
            lex = m.group(1)  # Get the matched text
            print(f"\"{lex}\" = {classify(lex)}")
            i = m.end()
        else:
            print(f"\"{code[i]}\" = unknown") #if we dont know we dont know
            i += 1

if __name__ == "__main__":
    main()
