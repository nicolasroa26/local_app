class Computador():
	def __init__(self, numero_equipo, sistema_operativo):
		self.numero_equipo = numero_equipo
		self.sistema_operativo = sistema_operativo
		
	def memoria(self, ram, disco_duro, numero_equipo):
		self.ram = ram
		self.disco_duro = disco_duro
		self.numero_equipo = numero_equipo

equipo1 = Computador('equipo1 ', 'windows ')
equipo2 = Computador('equipo2 ', 'mac ')
equipo1.memoria( '16 gb ', '1000 gb ', 'equipo 1 ')
equipo2.memoria( '12 gb ', '2000 gb ', 'equipo 2 ')

print('el '+str(equipo1.numero_equipo)+'tiene sistema operativo '+equipo1.sistema_operativo)
print('el '+str(equipo1.numero_equipo)+'tiene '+equipo1.ram, 'de memoria ram y su capacidad de disco es de '+equipo1.disco_duro)


print('el '+str(equipo2.numero_equipo)+ 'tiene sistema operativo '+equipo2.sistema_operativo)
print('el '+str(equipo2.numero_equipo)+'tiene '+equipo2.ram, 'de memoria ram y su capacidad de disco es de '+equipo2.disco_duro)