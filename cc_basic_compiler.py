file = open("read.txt")

keywords = {'to':'keyword','next':'keyword','sleep':'keyword','as':'keyword','else':'keyword','end':'keyword','elseif':'keyword','input':'keyword','dim': 'keyword','sub': 'keyword','for':'keyword', 'do' : 'keyword' , 'until' : 'keyword', 'if' : 'keyword', 'then' : 'keyword', 'print' :'keyword'}
keywords_key = keywords.keys()

operators = {'=' : 'Assignment operator','+' : 'Addition operator','-' : 'Subtraction operator','/' : 'Division operator','*' : 'Multiplication operator','<' : 'Lessthan operator','>' : 'Greaterthan operator' }
operators_key = operators.keys()

data_type = {'integer' : 'integer type', 'float': 'Floating point' , 'char' : 'Character type', 'long' : 'long int','string':'string type' }
data_type_key = data_type.keys()

punctuation_symbol = { ':' : 'colon', ';' : 'semi-colon', '.' : 'dot' , ',' : 'comma'}
punctuation_symbol_key = punctuation_symbol.keys()

identifier = {}
identifier_key = identifier.keys()

a=file.read()

count=0
program = a.split("\n")
for line in program:
    count = count + 1
    print("line#" , count, "\n" , line)

    tokens=line.split(' ')
    print("Tokens are " , tokens)
    print("Line#", count, "properties \n")
    
    in_string = False
    for token in tokens:
        if token == '':
            continue
        if in_string:
            print(token, " =>> ", data_type['string'])
            continue
        
        if token.startswith('"') or token.startswith("'"):
            in_string = True
            print(token, " =>> ", data_type['string'])
            continue
        
        if token.endswith('"') or token.endswith("'"):
            in_string = False
            print(token, " =>> ", data_type['string'])
            continue
            
        if token in keywords_key:
            print(token," =>> ", keywords[token])
        elif token in operators_key:
            print(token," =>> ", operators[token])
        elif token in data_type_key:
            print(token," =>> ", data_type[token])
        elif token in punctuation_symbol_key:
            print (token, " =>> " , punctuation_symbol[token])
        elif token in identifier_key:
            if identifier[token] != 'out of scope' and identifier[token] != 'id':
                print('Error: identifier', token, 'already declared with type', identifier[token])
            else:
                print(token, " =>> ", identifier[token])
        else:
            if token.isdigit():
                if '.' in token:
                    if token.replace('.', '').isdigit():
                        print(token, " =>> ", data_type['float'])
                    else:
                        print(token, " =>> ", data_type['string'])
                else:
                    print(token, " =>> ", data_type['integer'])
            else:
                identifier[token] = 'id'
                print (token, " =>> " , identifier[token])

    print("_ _ _ _ _ _")
