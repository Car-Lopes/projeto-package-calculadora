import operacao

repetir = 1
#op = '+'
a = 0
b = 0
total = 0 


def calcular(a,b):  

    op = ''
    op = operacao.operacao('op') 
    if op == '*' :
        total = a * b;
        return print(f'{a} {op} {b} = {total}')  

    elif op == '/' :
        if a < b:
            return print('a é menor que b - não da para dividir');
        elif b == 0:
            return print('Não existe divisivel por zero');
        else:        
            total = a / b;
            return print(f'{a} {op} {b} = {total}')  

    elif op == '+' :
        total = a + b;
        return print(f'{a} {op} {b} = {total}')  

    elif op == '-' :
        total = a - b
        return print(f'{a} {op} {b} = {total}')  

    else :
        return 'Operador não encontrado 2'

       
       
    
