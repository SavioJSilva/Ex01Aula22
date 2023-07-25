import Moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de R${p} é R${Moeda.metade(p)}')
print(f'O dobro de R${p} é R${Moeda.dobro(p)}')
print(f'Aumentando 10%, temos R${Moeda.aumentar(p, 10)}')