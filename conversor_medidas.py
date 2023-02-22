medida = float(input("Digite uma distancia em metros: \n256"))
dm = medida * 10
cm = medida * 100
mm = medida * 1000
dam = medida / 10
hm = medida / 100
km = medida / 1000

print(f"""
{medida} Metros são:
{dm} decimetro,
{cm} Centrimetro,
{mm} Melimetro,
{dam} Decametro,
{hm} Hectometro,
{km} kilometro

""")