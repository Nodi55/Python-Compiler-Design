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
