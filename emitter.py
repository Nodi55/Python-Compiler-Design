import lexer
from symbol import *
file_output = None
file_output2 = None

def emit(token, attribute=None):
    match token:

        case '+':
            file_output2.write('+ ')
            file_output.write('pop r1\npop r2\nadd r2, r1\npush r2\n')

        case '-':
            file_output2.write('- ')
            file_output.write('pop r1\npop r2\nsub r2, r1\npush r2\n')

        case '*':
            file_output2.write('* ')
            file_output.write('pop r1\npop r2\nmul r2, r1\npush r2\n')

        case '/':
            file_output2.write('/ ')
            file_output.write('pop r1\npop r2\ndiv r2, r1\npush r2\n')

        case 'MOD':
            file_output2.write('mod ')
            file_output.write('pop r1\npop r2\nmod r2, r1\npush r2\n')

        case 'DIV':
            file_output2.write('idiv ')
            file_output.write('pop r1\npop r2\nidiv r2, r1\npush r2\n')

        # ---------------------------------------
        # NUM and ID
        # ---------------------------------------

        case 'NUM':
            file_output2.write(str(attribute) + ' ')
            file_output.write('push ' + str(attribute) + '\n')

        case 'ID':
            file_output2.write(symbol_table[attribute].string + ' ')
            file_output.write('push ' + symbol_table[attribute].string + '\n')

        # ---------------------------------------
        # ASSIGN   (pop x)
        # ---------------------------------------

        case 'ASSIGN':
            file_output.write('pop ' + symbol_table[attribute].string + '\n')

        # ---------------------------------------
        # IF
        # ---------------------------------------

        case 'IF':
            file_output.write('pop r2 \ncmp r2,0 \nbe else\n')

        case 'ELSE':
            file_output.write('else:\n')


        # WHILE

        case 'WHILE':
            file_output.write('while:\n')

        case 'WHILE2':
            file_output.write('pop r2 \ncmp r2,0 \nbe endwhile\n')

        case 'WHILE3':
            file_output.write('b while\nendwhile:\n')

        case 'loop1':
            file_output.write("loop:\n")

        case "loop2",(tok, value):
            file_output.write("cmp"+symbol_table[tok].string+','+str(value)+'\nbl endFor\n')

        case ('loop3',(tok , value)):
            file_output.write("cmp" + symbol_table[tok].string + ',' + str(value) + '\nbg endFor\n')

        case 'loop4':
            file_output.write("b loob\nendFor:\n")


        case _:
            pass