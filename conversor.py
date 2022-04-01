def exchanges (moneda, cantidad):
    result = 0
    # Moneda Chilena
    if moneda == 1:
        result = cantidad * 0.0013
        print(f'Los {cantidad} pesos chilenos equivalen a {result} dolares')
    # Moneda colombiana
    elif moneda == 2:
        result = cantidad * 0.00027
        print (f'Los {cantidad} pesos Colombianos equivalen a {result} dolares')
    # Moneda Argentina
    elif moneda == 3:
        result = cantidad * 0.014
        print (f'Los {cantidad} pesos Argentinos equivalen a {result} dolares')
    # Moneda Mexicana
    elif moneda == 4:
        result = cantidad * 0.004
        print (f'Los {cantidad} pesos Mexicanos equivalen a {result} dolares')  
    # Otro
    else:
        print("Ingresa solo un numero de la lista")
        
        
        
if __name__ == "__main__":
    try:
        moneda = int(input('''
        Ingresa el indice de la moneda que quieres convertir a dolar:
            [1] Moneda Chilena a Dolar
            [2] Moneda colombiana a Dolar
            [3] Moneda Argentina a Dolar
            [4] Moneda Mexicana a Dolar
        Selecciona: '''))
        print("*********************************************")
        cantidad = int (input("Ingresa la cantidad que quieres convertir: "))
        exchanges(moneda,cantidad)
    except:
        print("*********E R R O R***********")
        print("Por favor, Ingresa solo valores numericos")