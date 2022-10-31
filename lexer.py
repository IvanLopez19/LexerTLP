import re

f = open('ejemplo.cc','r')

#Lista de tokens
listaTokens = {'operadores':0, 'comentarios':0, 'identificadores':0, 'palabrasreservadas':0, 'constantes':0, 'strings':0, 'iniciodebloque':0, 'findebloque':0, 'funciones':0, 'numeros':0, 'tiposdedatos':0, 'findeinstruccion':0}

#Lista de tipos de tokens
operadores = { '=': 'Asignacion','+': 'Operador suma', '-' : 'Operador resta', '/' : 'Division Operador', '*': 'Multiplicacion Operador', '++' : 'Operador incremente', '--' : 'Operador decremento'}
optr_keys = operadores.keys()

comentarios = {r'//' : 'Comentario de línea',r'/*' : 'Inicia comentario multilinea', r'*/' : 'Termina comentario multilinea', '/**/' : 'Comentario vacio'}
comment_keys = comentarios.keys()

#header = {'.h': 'archivo de encabezado'}
#header_keys = header.keys()

#sp_header_files = {'<stdio.h>':'Standard Input Output Librería','<string.h>':'String Manipulation Libreria'}

#macros = {r'#\w+' : 'macro'}
#macros_keys = macros.keys()

tiposDeDatos = {'int': 'Integer','float' : 'Floating Point', 'char': 'Character','long': 'long int'}
tiposDeDatos_keys = tiposDeDatos.keys()

palabrasReservada = {'return' : 'Palabra clave que retorna al SO', 'true':'verdadero', 'false':'falso', 'if':'condicional', 'else':'condicional', 'for':'bucle','while':'bucle','public':'publico','private':'privado'}
palabrasReservada_keys = palabrasReservada.keys()

delimiter = {';':'Fin de instruccion'}
delimiter_keys = delimiter.keys()

blocks = {'{' : 'Inicia bloque de instrucciones', '}':'Fin de bloque de instrucciones'}
block_keys = blocks.keys()

builtin_functions = {'cout':'Imprime en consola', 'cin':'lee datos'}

non_identifiers = ['_','-','+','/','*','`','~','!','@','#','$','%','^','&','*','(',')','=','|','"',':',';','{'
,'}','[',']','<','>','?','/']

numerals = ['0','1','2','3','4','5','6','7','8','9','10']

# banderas
dataFlag = False


i = f.read()

count = 0
program =  i.split('\n')

for line in program:
    count = count+1
    print ("Line #",count,"\n",line)
    
     
    tokens = line.split(' ')#asumiendo el espacio //no deberia ser
    print ("Tokens son",tokens)
    print ("Linea #",count,'propiedades \n')
    for token in tokens:
        
        if '\r' in token:
            position = token.find('\r')
            token=token[:position]
        # print 1
        
        if token in block_keys:
            print (blocks[token])
            if token == '{':
                listaTokens['iniciodebloque'] = listaTokens['iniciodebloque'] +1
            else:
                listaTokens['findebloque'] = listaTokens['findebloque'] +1
        if token in optr_keys:
            print ("Operador es: ", operadores[token])
            listaTokens['operadores'] = listaTokens['operadores'] + 1
        if token in comment_keys:
            print ("Comentario: ", comentarios[token])
            listaTokens['comentarios'] = listaTokens['comentarios'] + 1
        #if token in macros_keys:
            #print ("Macro es: ", macros[token])
        #if '.h' in token:
            #print ("Archivo de encabezado: ",token, sp_header_files[token])
        if ('()' in token) or (token in builtin_functions):
            print ("Función:", token)
            listaTokens['funciones'] = listaTokens['funciones'] + 1
        
        if dataFlag == True and (token not in non_identifiers) and ('()' not in token):
            print ("Identificador: ",token)
            listaTokens['identificadores'] = listaTokens['identificadores'] + 1
        if token in tiposDeDatos_keys:
            print ("Tipo es: ", tiposDeDatos[token])
            dataFlag = True
            listaTokens['tiposdedatos'] = listaTokens['tiposdedatos'] + 1
        
        if token in palabrasReservada_keys:
            print (palabrasReservada[token])
            listaTokens['palabrasreservadas'] = listaTokens['palabrasreservadas'] + 1
            
        if token in delimiter:
            print ("Delimitador" , delimiter[token])
            listaTokens['findeinstruccion'] = listaTokens['findeinstruccion'] + 1
        #if '#' in token:
            #match = re.search(r'#\w+', token)
            #print ("Encabezado", match.group())
        if token in numerals:
            print (token,type(int(token)))
            listaTokens['numeros'] = listaTokens['numeros'] + 1
            
    dataFlag = False   
            
    
    print ("________________________")

    print (listaTokens)
    

f.close()