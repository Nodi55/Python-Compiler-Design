
from re import Match

import symbol
import emitter
import lexer
from emitter import file_output

file_input  = open('file.exp', 'r')
file_error  = open('file.err', 'w')

input_text0 = file_input.read()

lookahead = ''


def error():
    file_error.write('line:' + str(lexer.lineno) + ' syntax error')


def match(token):
    global lookahead
    if lookahead == token:
        lookahead = lexer.lexan()
    else:
        error()


def parse():
    global lookahead
    symbol.initialize()
    lookahead = lexer.lexan()

    while lookahead != 'EOF':
        stmt()
        match(';')





def stmt():
    global lookahead


    if lookahead == 'ID':
        tok = lexer.tokenval
        match('ID')
        match('=')
        expr()
        emitter.emit('ASSIGN', tok)


    elif lookahead == 'IF':
        match('IF')
        match('(')
        expr()
        match(')')
        emitter.emit('IF')
        match('THEN')
        stmt()
        emitter.emit('ELSE')

    # ------------------------------------
    # while (expr) do stmt
    # ------------------------------------
    elif lookahead == 'WHILE':
        match('WHILE')
        emitter.emit('WHILE')
        match('(')
        expr()
        match(')')
        emitter.emit('WHILE2')
        match('DO')
        stmt()
        emitter.emit('WHILE3')

    elif lookahead == 'FOR':
        tok = lexer.tokenval
        match('FOR')
        emitter.emit("loop1" ,tok )
        match('ID')
        match('IN')
        match('[')
        loob2(tok, lexer.tokenval)
        match('NUM')
        match(',')
        emitter.emit('loop3', (tok,lexer.tokenval))
        match('NUM')
        match(']')
        match('EXECUTE')
        stmt()
        emitter.emit("loop4")

    # ------------------------------------
    # begin ... end
    # ------------------------------------
    elif lookahead == 'BEGIN':
        match('BEGIN')
        CS()
        match('END')

    else:
        error()


def CS():
    global lookahead
    while lookahead != 'END':
        stmt()
        match(';')


def expr():
    term()
    moreterms()


def term():
    factor()
    morefactors()


def morefactors():
    if lookahead == '*':
        match('*')
        factor()
        emitter.emit('*')
        morefactors()

    elif lookahead == '/':
        match('/')
        factor()
        emitter.emit('/')
        morefactors()

    elif lookahead == 'DIV':
        match('DIV')
        factor()
        emitter.emit('DIV')
        morefactors()

    elif lookahead == 'MOD':
        match('MOD')
        factor()
        emitter.emit('MOD')
        morefactors()


def moreterms():
    if lookahead == '+':
        match('+')
        term()
        emitter.emit('+')
        moreterms()

    elif lookahead == '-':
        match('-')
        term()
        emitter.emit('-')
        moreterms()


def factor():
    global lookahead

    match lookahead:
        case '(':
            match('(')
            expr()
            match(')')

        case 'NUM':
            emitter.emit('NUM', lexer.tokenval)
            match('NUM')

        case 'ID':
            emitter.emit('ID', lexer.tokenval)
            match('ID')

        case _:
            error()

def loob2(tok,value):
    emitter.emit("loob2")