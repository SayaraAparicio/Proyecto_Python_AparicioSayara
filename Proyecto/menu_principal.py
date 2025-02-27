import json
from conectores import *
from conectores import abrirMEDICAMENTOS

continuar = True


while continuar:
    
    comando = input("Escribe 'salir' para terminar el ciclo: ")

    
    if comando == "salir":
        continuar = False
        print("Saliendo del ciclo...")
    else:
        print(f"Comando ingresado: {comando}")
    print("Bienvenido a la Farmacia")
    print("¿Que deseas hacer hoy?")
    print("----------------------------------")
    print("      1. Ver medicamentos         ")
    print("----------------------------------")
    print("      2. Ver ventas               ")
    print("----------------------------------")
    print("      3. Ver compras              ") 
    print("----------------------------------")
    print("      4. Ver proveedores          ")
    print("----------------------------------")
    print("      5. Ver pacientes            ")
    print("----------------------------------")
    print("      6. Ver empleados            ")
    print("----------------------------------")
    opc = input("Ingrese una opcion: ")

    if opc == "1":
        MEDICAMENTOS = abrirMEDICAMENTOS()
        for i in range(len(MEDICAMENTOS["medicamentos"])):
            print("\nMedicamento: ", i+1)
            print("nombre", MEDICAMENTOS["medicamentos"][i]["nombre"])
            print("precio: ",MEDICAMENTOS["medicamentos"][i]["precio"])
            print("stock: ", MEDICAMENTOS["medicamentos"][i]["stock"])
            print("fecha de expiracion: ", MEDICAMENTOS["medicamentos"][i]["fechaExpiracion"])

    if opc == "2":
        VENTAS = abrirVENTAS()
        for i in range(len(VENTAS["ventas"])):
            print("\nVenta: ", i+1)
            print("fechaVenta", VENTAS["ventas"][i]["fechaVenta"])
            print("paciente: ",VENTAS["ventas"][i]["paciente"])
            print("empleado: ", VENTAS["ventas"][i]["empleado"])
            print("medicamentosVendidos: ", VENTAS["ventas"][i]["medicamentosVendidos"])

    if opc == "3":
        COMPRAS = abrirCOMPRAS()
        for i in range(len(COMPRAS["compras"])):
            print("\nCompra: ", i+1)
            print("fechaCompra", COMPRAS["compras"][i]["fechaCompra"])
            print("proveedor: ",COMPRAS["compras"][i]["proveedor"])
            print("medicamentosComprados: ", COMPRAS["compras"][i]["medicamentosComprados"])

    if opc == "4":
        PROVEEDORES = abrirPROVEEDORES()
        for i in range(len(PROVEEDORES["proveedores"])):
            print("\nProveedor: ", i+1)
            print("nombre", PROVEEDORES["proveedores"][i]["nombre"])
            print("contacto: ",PROVEEDORES["proveedores"][i]["contacto"])
            print("direccion: ", PROVEEDORES["proveedores"][i]["direccion"])

    if opc == "5":
        PACIENTES = abrirPACIENTES()
        for i in range(len(PACIENTES["pacientes"])):
            print("\nPaciente: ", i+1)
            print("nombre", PACIENTES["pacientes"][i]["nombre"])
            print("direccion: ",PACIENTES["pacientes"][i]["direccion"])
            print("telefono: ", PACIENTES["pacientes"][i]["telefono"])

    if opc == "6":
        EMPLEADOS = abrirEMPLEADOS()
        for i in range(len(EMPLEADOS["empleados"])):
            print("\nEmpleado: ", i+1)
            print("nombre", EMPLEADOS["empleados"][i]["nombre"])
            print("cargo: ",EMPLEADOS["empleados"][i]["cargo"])
            print("fechaContratacion: ", EMPLEADOS["empleados"][i]["fechaContratacion"])
         
