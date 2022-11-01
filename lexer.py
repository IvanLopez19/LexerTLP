import re
from tkinter.ttk import tclobjs_to_py

f = open('ejemplo.cc','r')

#Lista de tipos de tokens
#Cada uno de estos diccionarios representa un token
operadores = { '=': 'Asignacion','+': 'Operador suma', '-' : 'Operador resta', '/' : 'Division Operador', '*': 'Multiplicacion Operador', '++' : 'Operador incremente', '--' : 'Operador decremento'}
optr_keys = operadores.keys()

comentarios = {r'//' : 'Comentario de línea',r'/*' : 'Inicia comentario multilinea', r'*/' : 'Termina comentario multilinea', '/**/' : 'Comentario vacio'}
comentarios_keys = comentarios.keys()

tiposDeDatos = {'int': 'Integer','float' : 'Floating Point', 'char': 'Character','long': 'long int'}
tiposDeDatos_keys = tiposDeDatos.keys()

identificadores ={r'[a-z]([a-z]+|[0-9]+)*': 'variables', r'[a-z]([a-z]+|[0-9]+)*()': 'funciones'}
identificadores_keys = identificadores.keys()

palabrasReservada = {'return' : 'Palabra clave que retorna al SO', 'true':'verdadero', 'false':'falso', 'if':'condicional', 'else':'condicional', 'for':'bucle','while':'bucle','public':'publico','private':'privado'}
palabrasReservada_keys = palabrasReservada.keys()

delimitador = {';':'Fin de instruccion'}
delimitador_keys = delimitador.keys()

bloques = {'{' : 'Inicia bloque de instrucciones', '}':'Fin de bloque de instrucciones'}
bloque_keys = bloques.keys()

valores = {r'[0-9]+': 'numeros enteros', r'[0-9]+.[0-9]+': 'numeros decimales'}
valores_keys = valores.keys()

#Estos ya no son tokens
non_identifiers = ['_','-','+','/','*','`','~','!','@','#','$','%','^','&','*','(',')','=','|','"',':',';','{'
,'}','[',']','<','>','?','/']

numerals = ['0','1','2','3','4','5','6','7','8','9','10']

# Banderas
dataFlag = False

#Leemos el archivo de c++
i = f.read()

#Esta variables para conocer por cual fila del codigo vamos
count = 0
#Aqui dividimos el programa completo en un arreglo con un elemento por cada fila
program =  i.split('\n')

#En este arreglo se guardan todos los elementos de la tabla de simbolos
tablaSimbolos = []
#Aqui se guardan unicamente los indicadores de la tabla de simbolos
tablaSimbolos_keys=[]

#Hacemos un loop for por cada linea del programa
for line in program:
    tipo=''
    identificador=''
    valor=''

    count = count+1
    print ("Line #",count,"\n",line)
    
    fila=count 
    #Dividimos una linea separando los tokens por cada espacio vacio que encontremos
    tokens = line.split(' ')
    print ("Tokens son",tokens)
    print ("Linea #",count,'propiedades \n')
    
    #Hacemos loop for por cada token de la linea
    for token in tokens:
         
        if '\r' in token:
            position = token.find('\r')
            token=token[:position]
        # print 1
        
        if token in bloque_keys:
            print (bloques[token])

        elif token in optr_keys:
            print ("Operador es: ", operadores[token])

        elif token in comentarios_keys:
            print ("Comentario: ", comentarios[token])

        elif token in tiposDeDatos_keys:
            print("tipo de dato: ",token)
            tipo = token

        elif token in palabrasReservada_keys:
            print ("palabra reservada es: ", palabrasReservada[token])
        
        elif token in delimitador:
            print ("Delimitador" , delimitador[token])

        else:
            #Comparamos el token con cada una de las expresiones regulares que estan en el diccionario de identificadores
            for identificador1 in identificadores_keys:
                #Si coincide con una y el identificador no a sido agregado al arreglo de tablaSimbolos_keys entonces el
                #token se agrega a la variable identificador
                if(re.search(identificador1, token) and (token not in tablaSimbolos_keys)):
                    print ("Identificador: ",token)
                    identificador = token

                    break
            #Comparamos el token con cada una de las expresiones regulares que estan en el diccionario de valores
            for valor1 in valores_keys:
                #Si coincide entonces se agrega a la variable valor
                if(re.search(valor1, token)):
                    print ("Valor: ",token)
                    valor = token
                    break

  
    dataFlag = False   
    print ("________________________")

    print(identificador)
    #Si se ha encontrado un identificador en esa linea entonces se envia a la tabla de simbolos
    if(identificador is not ''):
        tablaSimbolos.append({'tipo':tipo, 'identificador':identificador, 'valor':valor, 'fila':fila}) 

#Imprimimos la tabla de simbolos
print("TABLA DE SIMBOLOS")       
for simbolo in tablaSimbolos:
    print("---------------------")
    print("tipo de dato: ", simbolo['tipo'])
    print("identificador: ", simbolo['identificador'])
    print("valor: ", simbolo['valor'])
    print("fila: ", str(simbolo['fila']))
    


f.close()