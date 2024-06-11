# Programa que calcule la potencia de un numero

# Alejandro Ruiz

base = int(input('Dime la base de la potencia '))
expo = int(input('DIme el exponente: '))

if expo > 0:
    print(f'EL resultado de la potencia : {base**expo}')
elif expo == 0:
    print(f'EL resultado de la potencia : 1')
else:
    operation = (base**abs(expo))
    print(f'El resultado es 1/{operation} = {1/operation}')
