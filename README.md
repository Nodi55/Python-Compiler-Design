# Custom Python Compiler Design

A highly structured, custom language compiler written in **Python**. The compiler processes source code through formal compilation phases, manages scoping via a symbol table, and emits low-level, stack-based **Intermediate Language (IL)** commands (such as `push`, `pop`, `loop`, `sub`, and conditional jumps).

This project demonstrates core computer science principles in language design, syntax parsing, and code generation.

---

## 🏗️ Compiler Architecture & Components

The compilation pipeline is divided into five modular compiler subsystems:

1.  **Lexer (`lexer.py`):** Performs lexical analysis, stripping comments and whitespaces, while converting raw characters into semantic tokens (keywords, identifiers, operators, and literals).
2.  **Parser (`parser.py`):** Executes syntax and grammar validation. It constructs the parsing hierarchy based on language rules and ensures proper syntax structure.
3.  **Symbol Table (`symbol.py`):** Manages variable declarations, tracking identifier types and scoping rules to ensure safe compile-time variables allocation.
4.  **Emitter (`emitter.py`):** The code generation phase. It translates validated syntactic structures into low-level stack-based assembly-like Intermediate Language (IL).
5.  **Main Entry (`main.py`):** Coordinates the execution, piping source code input into the compiler and outputting the compiled program.

---

## 📄 Target Output Sample (Stack-Based IL)
The compiler successfully compiles logic files into stack instructions (saved as `.il` extension):

```assembly
push 9
pop x
loop:
push x
push 1
pop r1
pop r2
sub r2, r1
push r2
pop x
b loob
endFor:
