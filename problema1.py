"""
	@ricardoifc
	Problema 1
"""

file = open("promedios.txt")
promedio = (file.split(","))
resultado = filter(lambda x: x <= 16.5, promedio)
print(resultado)
print(list(resultado))