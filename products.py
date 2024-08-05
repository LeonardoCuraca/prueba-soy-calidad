products 	= { 1: 'Pantalones', 	2: 'Camisas', 	3: 'Corbatas', 	4: 'Casacas' 	}
prices 		= { 1: 200.00, 			2: 120.00, 		3: 50.00, 		4: 350.00 		}
stock 		= { 1: 50, 				2: 45, 			3: 30, 			4: 15 			}

def show_products():
	if len(products) == 0:
		print('\nNo hay productos\n')
		return
	
	# Extra: Se calculará cuantas tabulaciones usar entre los nombres de los productos y sus precios
	max_length = len(max(products.values(), key=len))
	max_used_tabs = int(max_length / 8)

	for k, v in products.items():
		length = len(v)
		used_tabs = int(length / 8)

		times = 1 if used_tabs > max_used_tabs else max_used_tabs - used_tabs + 1
		
		print(f'{ k }\t{ v }', end = times * '\t')
		print(f'{ prices[k] }\t{ stock[k] }')

def input_type_validation(name, type, blank=False):
	while True:
		try:
			value = input(f'{ name }: ')
			if value == '' and blank:
				return None
			return type(value)
		except ValueError:
			print('\nNo se pudo procesar el valor ingresado. Por favor, intente de nuevo.\n')

def confirm(text):
	confirm = input(f'\n{ text } [s/n]: ')
	return confirm == 's' or confirm == 'S'

def add_product():
	print('\n\033[94mCrear un nuevo producto\033[0m')

	id = list(products)[-1] + 1

	n = input('Nombre: ')
	p = input_type_validation('Precio', float)
	s = input_type_validation('Existencias', int)

	if confirm('¿Desea continuar?'):
		products[id] = n
		prices[id] = p
		stock[id] = s

		print('\nSe ha agregado el producto.\n')
	else:
		print('Bye!\n')

def delete_product():
	print('\n\033[94mEliminar un producto\033[0m')

	while True:
		id = input_type_validation('ID', int)

		if id in products:
			print('\n\033[91mSe eliminará el siguiente registro:\033[0m\n')

			print(f'Nombre: { products[id] }')
			print(f'Precio: { prices[id] }')
			print(f'Existencias: { stock[id] }')

			if confirm('¿Desea continuar?'):
				products.pop(id)
				prices.pop(id)
				stock.pop(id)

				print('\nSe ha eliminado el producto.\n')

				if not confirm('¿Desea eliminar otro producto?'):
					print('Bye!\n')
					break

			else:
				print('Bye!\n')
				break

		else:
			print('\nNo se ha encontrado el producto indicado.')

			if not confirm('¿Desea ingresar otro ID?'):
				print('Bye!\n')
				break

def update_product():
	print('\n\033[94mActualizar un producto\033[0m')

	while True:
		id = input_type_validation('ID', int)

		if id in products:

			print('\nSe actualizará el siguiente registro \033[93m(Dejar en blanco si no desea modificar)\033[0m:\n')

			print(f'Nombre: { products[id] }')
			print(f'Precio: { prices[id] }')
			print(f'Existencias: { stock[id] }')

			n = input('\nNombre: ')
			p = input_type_validation('Precio', float, blank=True)
			s = input_type_validation('Existencias', int, blank=True)

			if confirm('¿Desea continuar?'):
				products[id] = n if n else products[id]
				prices[id] = p if p else prices[id]
				stock[id] = s if s else stock[id]

				print('\nSe ha actualizado el producto.')

				if not confirm('¿Desea actualizar otro producto?'):
					print('Bye!\n')
					break
			else:
				print('Bye!\n')

		else:
			print('\nNo se ha encontrado el producto indicado.')

			if not confirm('¿Desea ingresar otro ID?'):
				print('Bye!\n')
				break

def main():
	again = False
	while True:
		if not again:
			again = False
			print('========================================')
			print('Lista de Productos:')
			print('========================================')

			show_products()
			
			print('========================================')
			print('[1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir')
		option = input('Elija opción: ')

		if option == '1': add_product()

		elif option == '2': delete_product()

		elif option == '3': update_product()

		elif option == '4':
			print('Bye!')
			break
		
		else:
			again = True
			print('\nLa opción no es válida. Por favor, intente de nuevo.\n')

main()