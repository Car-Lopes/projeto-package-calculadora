

def operacao(operador):
    
    operador = input('Digite um Operador: ')
    #operador = ' '

    while operador != '*' and operador != '/'  and operador != '-' and operador != '+':
    
        print('Operador não encontrado 1')
        operador = str(input('Digite um operador valido: '))
    
    return operador






""" #input('Digite entre 1 e 0 - 1 para continuar e 0 para encerrar: ')
calcular = 1;
a = 0
b = 0
total = 0


while calcular != 0 :
    operador = input('Digite um Operador: ')

    while operador != 'x' and operador != '/'  and operador != '-' and operador != '+':
    
        print('Operador não encontrado')
        operador = str(input('Digite um operador valido: '))
    

      
    a = int(input('Digite um numero: ')) 
    b = int(input('Digite outro numero: ')) 
  
    

    if operador == 'x' :
        total = a * b;
        print(f'{a} {operador} {b} = {total}')  

    elif operador == '/' :
        if a < b:
            print('a é menor que b - não da para dividir');
        elif b == 0:
            print('Não existe divisivel por zero');
        else:        
            total = a / b;
            print(f'{a} {operador} {b} = {total}')  

    elif operador == '+' :
        total = a + b;
        print(f'{a} {operador} {b} = {total}')  

    elif operador == '-' :
        total = a - b
        print(f'{a} {operador} {b} = {total}')  

    else :
        'Operador não encontrado'

    calcular = int(input('Digite entre (1 e 0) - 1 para continuar e 0 para encerrar: '))
   
"""
