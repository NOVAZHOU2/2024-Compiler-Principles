import re

map = {
    'if': 'IFTK', 'else': 'ELSETK', 'do': 'DOTK', 'while': 'WHILETK',
    'for': 'FORTK', 'return': 'RETURNTK', 'scanf': 'SCANFTK', 'printf': 'PRINTFTK',
    'int': 'INTTK', 'char': 'CHARTK', 'void': 'VOIDTK', 'const': 'CONSTTK',
    'main': 'MAINTK',
    '=': 'ASSIGN', ';': 'SEMICN', ',': 'COMMA', '(': 'LPARENT', ')': 'RPARENT',
    '{': 'LBRACE', '}': 'RBRACE', '[': 'LBRACK', ']': 'RBRACK',
    '<': 'LSS', '<=': 'LEQ', '>': 'GRE', '>=': 'GEQ', '==': 'EQL', '!=': 'NEQ',
    '+': 'PLUS', '-': 'MINU', '*': 'MULT', '/': 'DIV'
}

patten = [
    (r'"[^"]*"', 'STRCON'),
    (r"'.'", 'CHARCON'),
    (r'\bif\b|\belse\b|\bdo\b|\bwhile\b|\bfor\b|\breturn\b|\bscanf\b|\bprintf\b', 'KEYWORD'),
    (r'\bint\b|\bchar\b|\bvoid\b|\bconst\b|\bmain\b', 'KEYWORD'),
    (r'[a-zA-Z_]\w*', 'IDENFR'),
    (r'\d+', 'INTCON'),
    (r'==|!=|<=|>=|<|>', 'OPERATOR'),
    (r'\+|\-|\*|/', 'OPERATOR'),
    (r'\(', 'LPARENT'), (r'\)', 'RPARENT'),
    (r'\{', 'LBRACE'), (r'\}', 'RBRACE'),
    (r'\[', 'LBRACK'), (r'\]', 'RBRACK'),
    (r',', 'COMMA'), (r';', 'SEMICN'),
    (r'=', 'ASSIGN')
]


def lexer(input_file, output_file):
    with open(input_file, 'r') as f:
        code = f.read()
    results = []
    tokens = re.findall(r'"[^"]*"|\'.\'|==|!=|<=|>=|<|>|\+|-|\*|/|[a-zA-Z_]\w*|\d+|[,;=(){}\[\]]', code)

    for token in tokens:
        if token in map:
            results.append(f"{map[token]} {token}")
        elif re.fullmatch(r'"[^"]*"', token):
            results.append(f"STRCON {token[1:-1]}")
        elif re.fullmatch(r"'.'", token):
            results.append(f"CHARCON {token[1:-1]}")
        else:
            matched = False
            for pattern, token_type in patten:
                if re.fullmatch(pattern, token):
                    category = map.get(token, token_type)
                    results.append(f"{category} {token}")
                    matched = True
                    break
            if not matched:
                results.append(f"UNKNOWN {token}")

    with open(output_file, 'w') as f:
        f.write("\n".join(results))


if __name__ == "__main__":
    input_file = "testfile.txt"
    output_file = "output.txt"
    lexer(input_file, output_file)
