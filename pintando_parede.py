"""
    Crie um programa que leia a altura e largura de uma parede em metros e calcule sua area e a quantidade
    de tinta necessaria para pinta-la, sabendo que cada litro de tinta, pinta uma area de 2m²
"""
larg = float(input('Largura da sua parede em Metros:'))
alt = float(input('Altura da sua parede em Metros:'))
area = larg * alt
# print(f'sua parede tem as dimenções de {larg} x {alt} e sua área é de {area} m²')
tinta = area/2
print(f'para pintar uma parede de {area} você vai precisar de {tinta} litros de tinta')

