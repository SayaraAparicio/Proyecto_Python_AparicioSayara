import json

def abrirMEDICAMENTOS():
    dicFinal={}
    with open("./medicamentos.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarMEDICAMENTOS(dic):
    with open("./medicamentos.json",'w') as outFile:
        json.dump(dic,outFile)

def abrirVENTAS():
    dicFinal={}
    with open("./ventas.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def abrirCOMPRAS():
    dicFinal={}
    with open("./compras.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def abrirPROVEEDORES():
    dicFinal={}
    with open("./proveedores.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def abrirPACIENTES():
    dicFinal={}
    with open("./pacientes.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def abrirEMPLEADOS():
    dicFinal={}
    with open("./empleados.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal