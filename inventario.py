# Diccionario lista de Productos

productos = [ 
            {"Nombre":"BARBA ROJA","Cantidad":7,"precio":3000},
            {"Nombre":"SIR LUPULO","Cantidad":8,"precio":3000}, 
            {"Nombre":"BOUSON","Cantidad":12,"precio":4000}, 
            {"Nombre":"PATAGONIA","Cantidad":12,"precio":4000},
            {"Nombre":"STRANGE","Cantidad":5,"precio":2000}
            ]

opcion="" 
while opcion != 6:    
    print("-" * 50)                             
    print("Bienvenidos a 'La Birra es Bella'\n")
    print("-" * 50)
    print("Control de Inventario")
    print("1. Agregar un nuevo producto")
    print("2. Mostrar lista de productos")
    print("3. Modificar stock de un producto.")
    print("4. Eliminar un producto (Proximamente).")
    print("5. Mostrar productos con bajo stock (Proximamente).")
    print("6. Salir del sistema.")
    print("-" * 50)
    opcion = int(input("Ingrese la opcion que desea usar: "))
    print("-" * 50)

# Opción 1: Agregar producto

    if opcion == 1:
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad del producto: "))
        precio = float(input("Ingrese el precio del producto: "))
        productos.append({"Nombre":nombre,"Cantidad":cantidad,"precio":precio})
        print("Producto agregado con exito")


# Opción 2: Mostrar producto

    elif opcion == 2:
        print("Lista de productos:")
        for producto in productos:
            print(producto)
            print("")

# Opción 3 : Modificar stock

    elif opcion == 3:
        nombre = input("Ingrese el nombre del producto que desea modificar: ")
        for producto in productos:
            if producto["Nombre"] == nombre:
                cantidad = int(input("Ingrese la nueva cantidad del producto: "))
                producto["Cantidad"] = cantidad
                precio = float(input("actualice el precio si es necesario: "))
                producto["precio"] = precio
                print("")
                print("Producto modificado con exito")
                break

            else:
                print("")
                print("el producto no se encuentra en stock todavia.")    
                

# Opción 4 : Eliminar Producto

    elif opcion == 4:
        pass

# Opción 5 : Mostrar producto con bajo Stock


    elif opcion == 5:   #mostrar bajo stock
        pass

# Opción 6 : salir

    elif opcion ==6:   
        
        print("Gracias por usar nuestro sistema!! VUELVAS PRONTOS")

# solicitud 

    else :
        print("Elija una opcion correcta por favor.")