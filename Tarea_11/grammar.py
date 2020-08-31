# -----------------------------------------------------------------------------
# Raul Xiloj - 201612113 | Tarea 11
# -----------------------------------------------------------------------------
import ply.yacc as yacc
import ply.lex as lex

# ----------------------------- Analizador lexico -----------------------------

tokens = (
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'PIZQ',
    'PDER',
    'NUMERO'
)

# Tokens
t_MAS = r'\+'
t_MENOS = r'-'
t_POR = r'\*'
t_DIVIDIDO = r'/'
t_PIZQ = r'\('
t_PDER = r'\)'


def t_NUMERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Valor del entero muy grande %d", t.value)
        t.value = 0
    return t


# Ignored characters
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Caracter invalido '%s'" % t.value[0])
    t.lexer.skip(1)


# Construyendo el analizador léxico
lexer = lex.lex()

# --------------------------- Analizador Sintactico ---------------------------


class Temp:
    ''' Clase usada para llevar los valores temporales y el CD3 '''
    tmp = ""
    c3d = ""


def new_temp():
    new_temp.counter += 1
    return "t" + str(new_temp.counter)


new_temp.counter = 0


def p_init(t):
    ''' S : E '''
    print(t[1].c3d)


def p_E(t):
    ''' E : E MAS T 
          | E MENOS T
          | T '''
    if len(t) > 2:
        if t[2] == '+':
            t[0] = Temp()
            t[0].tmp = new_temp()
            t[0].c3d = t[1].c3d + t[3].c3d + t[0].tmp + \
                "=" + t[1].tmp + "+" + t[3].tmp + "\n"
        elif t[2] == '-':
            t[0] = Temp()
            t[0].tmp = new_temp()
            t[0].c3d = t[1].c3d + t[3].c3d + t[0].tmp + \
                "=" + t[1].tmp + "-" + t[3].tmp + "\n"
    else:
        t[0] = Temp()
        t[0].tmp = t[1].tmp
        t[0].c3d = t[1].c3d


def p_T(t):
    ''' T : T POR F
          | T DIVIDIDO F
          | F '''

    if len(t) > 2:
        if t[2] == '*':
            t[0] = Temp()
            t[0].tmp = new_temp()
            t[0].c3d = t[1].c3d + t[3].c3d + t[0].tmp + \
                "=" + t[1].tmp + "*" + t[3].tmp + "\n"
        elif t[2] == '/':
            t[0] = Temp()
            t[0].tmp = new_temp()
            t[0].c3d = t[1].c3d + t[3].c3d + t[0].tmp + \
                "=" + t[1].tmp + "/" + t[3].tmp + "\n"
    else:
        t[0] = Temp()
        t[0].tmp = t[1].tmp
        t[0].c3d = t[1].c3d


def p_F(t):
    ''' F : PIZQ E PDER
          | NUMERO '''

    if t[1] == '(':
        t[0] = Temp()
        t[0].tmp = t[2].tmp
        t[0].c3d = t[2].c3d
    else:
        t[0] = Temp()
        t[0].tmp = str(t[1])
        t[0].c3d = ""


def p_error(t):
    print("Error sintactico en '%s'" % t.value)


# Construyendo el analizador sintactico
parser = yacc.yacc()

# Procedemos a probarlo
# Cadena de entrada: 1 + 5 * 7 + 4 / 2
input = "1 + 5 * 7 + 4 / 2 + (2 + 2)"
print(input)
parser.parse(input)
