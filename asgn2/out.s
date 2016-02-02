[0, 16]
[]
*********************************************************************************
{'v_a': 3, '1line': 1, 'v_k': 8}
{'1line': 2, 'v_a': 3, 'v_b': 3, 'v_k': 8}
{'v_a': 9, '1line': 3, 'v_k': 8}
{'v_l': 6, 'v_a': 9, '1line': 4, 'v_k': 8}
{'v_l': 6, 'v_j': 6, 'v_a': 9, '1line': 5, 'v_k': 8}
{'v_l': 7, 'v_j': 12, 'v_a': 9, '1line': 6, 'v_k': 8}
{'v_l': 8, 'v_j': 12, 'v_a': 9, '1line': 7, 'v_k': 8}
{'1line': 8, 'v_a': 9, 'v_j': 12, 'v_k': 9}
{'1line': 9, 'v_a': 16, 'v_j': 12}
{'1line': 10, 'v_h': 13, 'v_a': 16, 'v_j': 12}
{'1line': 11, 'v_h': 13, 'v_a': 16, 'v_j': 12}
{'v_h': 13, 'v_a': 16, '1line': 12}
{'v_a': 16, '1line': 13}
{'v_p': 15, 'v_a': 16, '1line': 14}
{'v_a': 16, '1line': 15}
{'1line': 16}
*********************************************************************************
.section .data
v_p:
	.long 0
v_f:
	.long 0
v_a:
	.long 0
v_b:
	.long 0
v_l:
	.long 0
v_k:
	.long 0
v_h:
	.long 0
v_j:
	.long 0
v_q:
	.long 0
.section .data
 
.section .text
 
.global _start


movl $2 , %ebx
movl $7 , %ecx
addl %ecx , %ebx
movl $8 , %esi
movl $9 , %edi
addl %esi , %edi
movl %esi , %eax
addl %esi , %edx
addl %ebx , %edx
movl %ecx , v_b
movl $2 , %ecx
movl %esi , v_l
movl $4 , %esi
movl %edi , %edi
addl $9 , %edi
movl %ecx , %ecx
subl $3 , %ecx
movl %ecx , v_h
movl $6 , %ecx
movl %ecx , %ecx
addl $7 , %ecx
movl %ebx , %ebx
addl $8 , %ebx
