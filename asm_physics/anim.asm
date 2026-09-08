section .data
	c db "*"
	c_len equ $ - c

	cn db " "
	cn_len equ $ - cn

	nl db 10
	nl_len equ $ - nl

	go_home db `\033[H`, 0
	go_home_len equ $ - go_home

	delay_time:
		dq 0
		dq 50000000

section .text
	global _start

%macro Print 2
	mov rax, 1
	mov rdi, 1
	mov rsi, %1
	mov rdx, %2
	syscall
%endmacro

%macro Exit 0
	mov rax, 60
	mov rdi, 0
	syscall
%endmacro

%macro time 0
	mov rax, 35
	mov rdi, delay_time
	xor rsi, rsi
	syscall
%endmacro

; r12 is the counter to parse x
; rbx is the counter to parse y
; r15 is the y coord of the circle
; r13 is used as a temp ((a-40)**2)
; r14 is used as a temp ((b-r15)**2)
; rbp is the y velocity
; r8 is the x coord of the circle
; r9 is the x velocity

_start:
	;mov r12, 40
	;mov rbx, 40
	mov r15, 20
	mov rbp, 0
	mov r8, 20
	mov r9, 10

animation:
	mov rbx, 40
	time

	; calculating y vel
	add rbp, 1 ; considering g*t = 10 * 0.1 approx.

	; calculating y coord
	mov r13, 1
	imul r13, rbp

	mov rax, r13
	mov r14, 10
	cqo ; prep rdx for div, interesting...
	idiv r14
	sub r15, rax
	;imul r13, 

	; calculating x coord
	;r9/10
	mov r13, 1
	mov r13, r9

	mov rax, r13
	mov r14, 10
	cqo
	idiv r14
	sub r8, rax


	; check collision with ground
	mov r14, r15
	sub r14, 5
	jge next_thing
true:
	neg rbp
	mov r15, 5

next_thing:
	; check collision with right wall
	mov r14, r8
	sub r14, 5
	jg next_thing2
true2:
	neg r9
	mov r8, 5

next_thing2:
	; check collision with left wall
	mov r14, r8
	sub r14, 35
	jl next_thing3
true3:
	neg r9
	mov r8, 35


next_thing3:
	Print go_home, go_home_len

outer_loop:
	mov r12, 40

inner_loop:
	; check condition
	
	mov r13, r12
	sub r13, r8
	imul r13, r13
	;imul r13, 3

	mov r14, rbx
	sub r14, r15
	imul r14, r14
	imul r14, 2

	add r13, r14

	; mov r14, r15
	; imul r14, r15
	
	sub r13, 25 ; 25 is radius squared
	jg f

t:
	; true
	Print c, c_len
	jmp next

f:
	; false
	Print cn, cn_len

next:
	dec r12
	jnz inner_loop
	
	Print nl, nl_len
	dec rbx
	jnz outer_loop

	jmp animation

	Exit
