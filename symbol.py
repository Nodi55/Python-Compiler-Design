class Entry:
    def __init__(self, string, token):
        self.string = string
        self.token = token


symbol_table = []


def lookup(string):
    for i, elm in enumerate(symbol_table):
        if elm.string == string:
            return i
    return None


def insert(string, token):
    symbol_table.append(Entry(string, token))
    return len(symbol_table) - 1


keywords = [
    Entry('div', 'DIV'),
    Entry('mod', 'MOD'),
    Entry('if', 'IF'),
    Entry('then', 'THEN'),
    Entry('while', 'WHILE'),
    Entry('do', 'DO'),
    Entry('begin', 'BEGIN'),
    Entry('end', 'END'),
    Entry('for', 'FOR'),
    Entry('in', 'IN'),
    Entry('execute', 'EXECUTE'),
]


def initialize():
    for elm in keywords:
        insert(elm.string, elm.token)