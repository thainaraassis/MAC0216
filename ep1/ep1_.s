;****************************************************************************** 
; MAC0216 - Técnicas de Programação I (2024)
; EP1 - Linguagem de Montagem
;
; Nome do(a) aluno(a): Thainara de Assis Goulart
; NUSP: 13874413
;****************************************************************************** 

global _start 

;****************************************************************************** 
; Seção de declaração de variáveis inicializadas e constantes
;****************************************************************************** 
section .data				

;*************************************************
; Constantes
;*************************************************

; Funções das syscalls
READ			equ 0
WRITE			equ 1

; Descritores dos arquivos de entrada e saída padrão   
STDIN  			equ 0
STDOUT 			equ 1

; Modos de abertura de arquivo (segundo parâmetro da syscall sys_open)
RDONLY 			equ 0                 		; somente leitura
WRONLY 			equ 1                 		; somente escrita
RDWR  			equ 2                 		; leitura + escrita
WRONLY_CREAT_TRUNC  	equ 577  	  		; somente escrita + cria se não existe + trunca se existe

; Modo de permissão de acesso a arquivo (terceiro parâmetro da syscall sys_open)
PERMISSION_MODE		equ 438          		; permissões de leitura e escrita 

; Deslocamentos para os parâmetros e variáveis locais das funções


;*************************************************
; Variáveis
;*************************************************
msg_arq_entrada  	db "Digite o nome do arquivo de entrada: ",0x0
msg_arq_saida	  	db "Digite o nome do arquivo de saida: ",0x0


;****************************************************************************** 
; Seção de declaração de variáveis não inicializadas
;****************************************************************************** 
section .bss

hexadecimal		resb 10
tam_hex			equ $ - hexadecimal
inverte			resb 10

nome_entrada		resb 256
tam_max_nome_IN   	equ $ - nome_entrada
nome_saida		resb 256
tam_max_nome_OUT   	equ $ - nome_saida

char_lidos_IN 		resq 1
char_lidos_OUT		resq 1

file_desc_IN 		resb 256
file_desc_OUT		resb 256

byte_arq   		resb 8
byte_lidos 		resb 8

code_point		resd 1

	
;****************************************************************************** 
; Seção de texto (código do corpo do programa)
;******************************************************************************    
section .text

;******************************************************************************
; FUNÇÃO: le_string(char* buffer, int tam_max)
; Lê da entrada padrão (STDIN) uma sequência de caracteres finalizada por ENTER 
; (caracter 0xA) e armazena-a na memória, finalizando com '\0' (caractere 0x0).
; Usa a sys_read.  
; ENTRADAS:
; - char* buffer: endereço inicial do espaço de memória onde a função 
;                 armazenará a string lida.
; - int tam_max: a quantidade máxima de caracteres a serem lidos. Usado para 
;                evitar 'estouro' do buffer caso o usuário digite mais 
;                caracteres do que o espaço disponível para armazenamento.
; SAÍDA: 
; - Devolve no registrador RAX a quantidade de caracteres lidos.
;******************************************************************************
le_string: 

	; salva o valor de RBP e define uma nova base
	push rbp
        mov rbp, rsp
     
        ; funcao
        ; sys_read 
        mov rax, READ
        mov rdi, STDIN  			
        mov rsi, [rbp + 16]
        mov rdx, [rbp + 24]		
        syscall
        
        mov [rsi+rax-1], byte 0 			; removemos o "enter" do final da string lida e colocamos o caracter nulo '\0'
         
        ; restaurar RBP
        pop rbp
    
    	ret

;******************************************************************************
; FUNÇÃO: escreve_string(char* buffer)
; Escreva uma string na saída padrão (STDOUT). A função supõe que a string é 
; finalizada com '\0' (código 0x0). Usa a sys_write.
; ENTRADA:
; - char* buffer: ponteiro para a string (ou seja, o endereço da sua posição de 
;                 memória inicial).
;******************************************************************************
escreve_string:

	; salva o valor de RBP e define uma nova base
        push rbp
        mov rbp, rsp

        ; funcao 
        ; fazemos o loop a seguir para podermos achar o tamanho da string e passar essa informação como parâmetro na sys_write
        
        mov rcx, [rbp + 16]				; rcx é o registrador que irá salvar esse tamanho
        
loop_null:

	mov al, [rcx]                  
	cmp al, 0             				; comparamos com o caracter nulo, por ser o último caracater de uma string            
	je end_count                         
	inc rcx                              
	jmp loop_null                     

end_count:

	inc rcx
	sub rcx, [rbp+16] 
	
	; sys_write
	mov rax, WRITE
	mov rdi, STDOUT            
	mov rsi, [rbp + 16]                       
	mov rdx, rcx                 
	syscall
                         
    	; restaurar RBP
    	pop rbp
    
    	ret

;******************************************************************************
; FUNÇÃO:  abre_arquivo(char* nome_arquivo, int modo_abertura)
; Abre um arquivo. 
; Usa a sys_open (const char *pathname, int flags, mode_t mode).
; Obs.: No parâmetro mode da sys_open, passa o valor 438 (constante 
;       PERMISSION_MODE) como modo de permissão de acesso (que corresponde à
;       permissão de leitura e escrita).
; ENTRADAS: 
; - char* nome_arquivo: endereço inicial da string do nome (ou do caminho+nome)
; - int modo_abertura: valor 0 (constante RDONLY) para indicar abertura para 
;                      leitura ou valor 577 (constante WRONLY_CREAT_TRUNC) para 
;                      indicar abertura para escrita e criando o arquivo caso
;                      ele não exista ainda ou sobreescrevendo o conteúdo dele
;                      caso ele já exista.  
; SAÍDA: 
; - Devolve no registrador RAX o descritor do arquivo aberto.
;******************************************************************************
abre_arquivo: 

	; salva o valor de RBP e define uma nova base
        push rbp
        mov rbp, rsp
     	  	
        ; funcao 
        ; sys_open
        mov rax, 2
	mov rdi, [rbp + 16]
	mov rsi, [rbp + 24]
	mov rdx, PERMISSION_MODE
	syscall		
              
        ; restaurar RBP
        pop rbp
    
    	ret

;******************************************************************************
; FUNÇÃO: fecha_arquivo(int descritor_arquivo)
; Fecha um arquivo aberto previamente. Usa a sys_close.
; ENTRADA:
; - int  descritor_arquivo: descritor do arquivo a ser fechado.
;******************************************************************************
fecha_arquivo:

    	; salva o valor de RBP e define uma nova base
        push rbp
        mov rbp, rsp
     	   	
        ; funcao 
        ; sys_close
	mov rax, 3
	mov rdi, [rbp + 16]
	syscall	
             
        ; restaurar RBP
        pop rbp

   	ret

;******************************************************************************
; FUNÇÃO: le_byte_arquivo(int descritor_arquivo, char* byte_arq) 
; Lê um byte de um arquivo aberto previamente para leitura. Usa a sys_read.
; ENTRADAS:
; - int descritor_arquivo: descritor do arquivo aberto para leitura.
; - char* byte_arq: endereço da posição de memória onde será armazenado o byte
;                   lido do arquivo.
; SAÍDA: 
; - Devolve em RAX o número de bytes lidos (ou seja, o valor devolvido pela 
;   chamada à sys_read). 
;******************************************************************************
le_byte_arquivo:    

    	; salva o valor de RBP e define uma nova base
        push rbp
        mov rbp, rsp
     	   	
        ; funcao 
        ; sys_read
	mov rax, READ
	mov rdi, [rbp + 16]
	mov rsi, [rbp + 24]
	mov rdx, 1					; usamos '1' como tamanho, pois sempre iremos ler apenas um byte
	syscall
             
        ; restaurar RBP
        pop rbp

    	ret

;******************************************************************************
; FUNÇÃO: grava_string_arquivo(int descritor_arquivo, char* buffer)
; Grava string em um arquivo previamente aberto para escrita. A função supõe 
; que a string é finalizada com '\n' (código 0xA) e com '\0' (código 0x0). 
; Usa a sys_write.
; ENTRADAS:
; - int descritor_arquivo: descritor do arquivo aberto para escrita.
; - char* buffer: ponteiro para a string (ou seja, o endereço da sua posição de 
;                 memória inicial).
;******************************************************************************
grava_string_arquivo:

    	; salva o valor de RBP e define uma nova base
        push rbp
        mov rbp, rsp
        
	; funcao 
	; fazemos o loop a seguir para podermos achar o tamanho da string e passar essa informação como parâmetro na sys_write
        
        mov rcx, [rbp+24]				; rcx é o registrador que irá salvar esse tamanho
        
loop_grava:

	mov al, [rcx]                  
	cmp al, 0   				; comparamos com o caracter nulo, por ser o último caracater de uma string                     
	je end_grava                         
	inc rcx                              
	jmp loop_grava                     

end_grava:
	
	sub rcx, [rbp+24] 

	; sys_write
	mov rax, WRITE
	mov rdi, [rbp + 16]
	mov rsi, [rbp + 24]
	mov rdx, rcx
	syscall
                         
    	; restaurar RBP
    	pop rbp
    	
    	ret

;******************************************************************************
; FUNÇÃO: gera_string_hexadecimal(int valor, char* buffer)
; Converte um número em uma string com a representação em hexadecimal dele. Por
; ex., para o inteiro 128526 (11111011000001110b), a string em hexadecimal é 
; '0x1F60E'. A função finaliza a string gerada com um caractere de quebra de 
; linha '\n' (código 0xA) e com o '\0' (código 0x0).
; ENTRADAS:
; - int valor: o número inteiro a ser convertido.
; - char* buffer: endereço da posição inicial da região de memória previamente  
;                 alocada que receberá a string gerada na conversão. 
;******************************************************************************
gera_string_hexadecimal:

    	; salva o valor de RBP e define uma nova base
        push rbp
        mov rbp, rsp

        ; funcao 
        
        mov rax, [rbp+16]				; rax guarda o valor a ser convertido
        mov r11, [rbp+24]				; r11 guarda o endereço para "hexadecimal", que receberá a string
        mov rcx, 16					; rcx guarda a constante 16
        xor rsi, rsi					; rsi será o contador
        xor r10, r10 					; r10 será o contador para auxiliar na inversão dos caracteres
        
loop:
	cmp rax, 0					; se o valor inteiro for 0, podemos partir para sua finalização
	je add_ini
	xor rdx, rdx					; garantimos que todos registradores terão o valor correto após a divisão
	div rcx						; divide o valor por 16
	
	cmp dl, 10					; se o resto < 10, temos um dígito que pode ser transformado em um caracter
	jl transf_char
	
	; se resto for 10, 11, 12, 13, 14 ou 15, apenas os substituiremos pelo seu caracter equivalente, sendo A, B, C, D, E ou F, respectivamente
	cmp dl, 10
	je dez
	cmp dl, 11
	je onze
	cmp dl, 12
	je doze
	cmp dl, 13
	je treze
	cmp dl, 14
	je catorze
	cmp dl, 15
	je quinze
	jmp incr
	
transf_char:	
	add dl, '0' 					; caracter '0', transforma o resto em ASCII 
							; dl é parte do RDX onde está o resto e sabemos que um digito tem um byte	
incr: 
	mov [inverte+rsi], dl				; salvamos o caracter no endereço "inverte" e incrementamos o loop
	inc rsi
	jmp loop 

dez:       mov dl, 'A'
	   jmp incr
onze:      mov dl, 'B'
	   jmp incr
doze:	   mov dl, 'C'
	   jmp incr
treze:	   mov dl, 'D'
	   jmp incr
catorze:   mov dl, 'E'
	   jmp incr
quinze:    mov dl, 'F'
	   jmp incr

add_ini:
	mov [r11], byte '0'				; adicionamos manualmente o formato do hexadecimal '0x'
	inc r10
	mov [r11+r10], byte 'x'
	inc r10
	jmp invertido
	
invertido: 
	
	; aqui iremos inverter os caracteres, pois em "inverte" obtemos a notação hexadecimal invertida, e salvaremos essa inversão em 
	; "hexadecimal" (r11)
	
	dec rsi
	cmp rsi, 0
	jl end_loop
	
	mov al, [inverte+rsi]
	mov [r11+r10], al
	inc r10
	jmp invertido

end_loop:
	
	mov [r11 + r10], byte 0xA			; adicionamos manualmente a quebra de linha e o caracter nulo
	inc r10
	mov [r11 + r10], byte 0
	
    	; restaurar RBP
    	pop rbp
    	
    	ret


;******************************************************************************
; Início do Programa
;****************************************************************************** 
_start:
	
	; escreve_string(msg_arq_entrada)  
	mov rbx, msg_arq_entrada					
	push rbx
	
	call escreve_string
	add rsp, 8					; libera espaço dos parâmetros/limpa a pilha (8 bytes do registrador)
	
	;
	; le_string(nome_entrada, tam_max_nome_IN)
	mov rbx, tam_max_nome_IN                             	       
	push rbx
	mov rbx, nome_entrada					
	push rbx
	
	call le_string
	mov [char_lidos_IN], rax				        								
	add rsp, 16					; libera espaço dos parâmetros/limpa a pilha (16 bytes = 2 * 8 bytes, de cada registrador)
	
	;
	; escreve_string(msg_arq_saida)  
	mov rbx, msg_arq_saida					
	push rbx
	
	call escreve_string
	add rsp, 8
	
	;
	; le_string(nome_saida, tam_max_nome_OUT)
	mov rbx, tam_max_nome_OUT                             	       
	push rbx
	mov rbx, nome_saida					
	push rbx
	
	call le_string
	mov [char_lidos_OUT], rax				      								
	add rsp, 16
    
    	;
    	; abre_arquivo(nome_entrada, RDONLY)
        mov rbx, RDONLY
        push rbx
        mov rbx, nome_entrada
        push rbx
        
        call abre_arquivo
        mov [file_desc_IN], rax
        add rsp, 16
        
	;
        ; abre_arquivo(nome_saida, WRONLY_CREAT_TRUNC)
        mov rbx, WRONLY_CREAT_TRUNC
        push rbx
        mov rbx, nome_saida
        push rbx
        
        call abre_arquivo
        mov [file_desc_OUT], rax
        add rsp, 16
    
    	;
    	;
    	
loop_le_byte: 
     	
     	;
        ; le_byte_arquivo(file_desc_IN, byte_arq)
        mov rbx, byte_arq
        push rbx
        mov rbx, [file_desc_IN]
        push rbx
        
        call le_byte_arquivo
        mov [byte_lidos], rax
        add rsp, 16
       
        ;
        ; com o byte lido, iremos verificar se ele de fato leu 1 byte ou então se leu 0, caso tenha lido 0, sabemos que ele já leu todo nosso
        ; texto e podemos finalizar o programa
        
        cmp [byte_lidos], byte 0
        je leu_tudo
      	
      	xor rax, rax
      	xor rcx, rcx
      	mov [code_point], eax				; garantimos que "code_point" está xerado, assim como al e cl
      
      	mov al, [byte_arq] 				; copiamos o byte lido para al
      	
      	  	
      	; copiamos o byte lido para cl várias vezes, já que irá se modificar a cada "and" que fizermos
      	; o "and" é realizado para verificar qual será o formato do "code_point", se será composto por 1, 2, 3 ou 4 bytes
      	
      	; verificamos se o bit mais significativo é zero, se sim, o "code_ point" será formado por 1 byte
	mov cl, [byte_arq]
	and cl, 10000000b				
	jz code_point_1
	
	; verificamos se o terceiro bit mais significativo é zero, se sim, o "code_ point" será formado por 2 bytes
	mov cl, [byte_arq]
	and cl, 00100000b
	jz code_point_2
	
	; verificamos se o quarto bit mais significativo é zero, se sim, o "code_ point" será formado por 3 bytes
	mov cl, [byte_arq]
	and cl, 00010000b
	jz code_point_3
	
	; verificamos se o quinto bit mais significativo é zero, se sim, o "code_ point" será formado por 4 bytes	
	mov cl, [byte_arq]
	and cl, 00001000b
	jz code_point_4
	
	
code_point_1:
	
	; para o "code_point" formado por apenas 1 byte, basta pegar seus 7 bits menos significativos e transformá-lo em hexadecimal
	
	and al, 01111111b
	xor rdx, rdx
    	mov dl, al
    	mov [code_point], edx
    	jmp transforma_hexa
	
code_point_2:
        
        ; para o "code_point" formado por 2 bytes, pegamos seus 5 bits menos significativos do primeiro byte e então precisamos 
        ; ler seu segundo byte.
        ; como precisamos ler somente mais UM byte após o primeiro já analisado, temos r10 = 1, ou seja, ler mais UM byte
        
	and al, 00011111b
    	xor rdx, rdx
    	mov dl, al
    	mov [code_point], edx
    	mov r10, 1
	jmp loop_le_another_byte
	
code_point_3:
	
	; para o "code_point" formado por 3 bytes, pegamos seus 4 bits menos significativos do primeiro byte e então precisamos 
        ; ler seu segundo e terceiro bytes.
        ; como precisamos ler mais DOIS bytes após o primeiro já analisado, temos r10 = 2, ou seja, ler mais DOIS bytes
        
	and al, 00001111b
    	xor rdx, rdx
    	mov dl, al
    	mov [code_point], edx
    	mov r10, 2	
	jmp loop_le_another_byte
	
code_point_4:
	
	; para o "code_point" formado por 4 bytes, pegamos seus 3 bits menos significativos do primeiro byte e então precisamos 
        ; ler seu segundo, terceiro e quarto bytes.
        ; como precisamos ler mais TRÊS bytes após o primeiro já analisado, temos r10 = 3, ou seja, ler mais TRÊS bytes
        
	and al, 00000111b
    	xor rdx, rdx
    	mov dl, al
    	mov [code_point], edx
    	mov r10, 3
	jmp loop_le_another_byte

loop_le_another_byte:

	; irá ler os próximos bytes necessários para cada tipo de "code_point" 
	
	;
	; le_byte_arquivo(file_desc_IN, byte_arq)
       	mov rbx, byte_arq
    	push rbx
    	mov rbx, [file_desc_IN]
    	push rbx
    	
    	call le_byte_arquivo
    	mov [byte_lidos], rax
    	add rsp, 16
	
	;
        ; com o byte lido, iremos verificar se ele de fato leu 1 byte ou então se leu 0, caso tenha lido 0, sabemos que ele já leu todo nosso
        ; texto e podemos finalizar o programa
        
    	cmp [byte_lidos], byte 0
    	je leu_tudo

    	mov al, [byte_arq]
	
	; para os segundo, terceiro e quarto bytes, precisamos pegar seus 6 bits menos significativos
    	and al, 00111111b				
    
    	xor rdx, rdx
    	mov dl, al  
    	shl dword [code_point], 6  		; desloca os 6 bits menos significativos do "code_point" atual
    	or dword [code_point], edx  		; combina o "code_point" atual com o byte recem lido, gerando um novo valor para o "code_point" 

    	dec r10 				; decrementamos o número de bytes que precisamos ler
    	jnz loop_le_another_byte		; caso ainda tenha bytes a serem lidos, permanecemos no loop
	jz  transforma_hexa			; caso contrário, podemos obter seu valor hexadecimal

transforma_hexa:
	
	;
	; gera_string_hexadecimal([code_point], hexadecimal)
        mov rbx, hexadecimal
        push rbx
        mov rbx, [code_point]
        push rbx
        
        call gera_string_hexadecimal
        add rsp, 16
         
     	;
	; grava_string_arquivo(file_desc_OUT, hexadecimal)
	mov rbx, hexadecimal
	push rbx
	mov rbx, [file_desc_OUT]
	push rbx
		
	call grava_string_arquivo
	add rsp, 16
	
	;
	; após gravar o primeiro code_point, repete o processo até que todos "code_point" tenham sido gravados
    	jmp loop_le_byte				
	
leu_tudo:
        
        ; quando não lemos nenhum byte (0), sabemos que o texto acabou e podemos então finalizar o programa, pois já lemos todos bytes
        
        ;
        ; fecha_arquivo(file_desc_IN)
        mov rbx, [file_desc_IN]
        push rbx
        
        call fecha_arquivo
        add rsp, 8
        
        ;
        ; fecha_arquivo(file_desc_OUT)
        mov rbx, [file_desc_OUT]
        push rbx
        
        call fecha_arquivo
        add rsp, 8
    
    	;
        ; sys_exit(int status)
        mov rax,60					; numero da chamada ao sistema (sys_exit)
        mov rdi,0					; primeiro argumento: código de saída (0 = sucesso)
        syscall
