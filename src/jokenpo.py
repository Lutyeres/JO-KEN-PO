import random

choices = ['PEDRA', 'PAPEL', 'TESOURA']
usuario = input('PEDRA, PAPEL OU TESOURA? \n').upper()

print('JO')
print('KEN')
print('PÔ')
x = random.choice(choices)
print(f'O computador escolheu {x}!')

if usuario not in choices:
    print ('Escolha invalida!')
elif usuario == x:
    print ('EMPATOU!')
elif usuario == 'PEDRA':
    if x == 'TESOURA':
        print('VOCÊ GANHOU!')
    else:
        print('VOCÊ PERDEU!')

elif usuario == 'PAPEL':
    if x == 'PEDRA':
        print('VOCÊ GANHOU!')
    else:
        print('VOCÊ PERDEU!')
        
elif usuario == 'TESOURA':
    if x == 'PAPEL':
        print('VOCÊ GANHOU!')
    else:
        print('VOCÊ PERDEU!')