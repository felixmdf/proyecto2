import requests
import io
import os
import numbers
from collections import Counter
import matplotlib.pyplot as plt
import sys
import math
import json


response = requests.get('https://saman-caribbean.vercel.app/api/cruise-ships')


data = response.json()


def abrir_datos(jsonfile):
    #'funcion para leer un archivo json'
    f=open(jsonfile)
    print(f)
    dato=json.load(f)
    return(dato)

def abrir_json(jsonfile):
    #funcion para leer datos de json y convertirlos en lista
    #jsonfile='datos.json' # Archivo de almacenamiento de datos
    datos_vacio=None    
    verificar_archivo(jsonfile,datos_vacio) #verificar la existencia del archivo json, o creacion de uno
    dato_json=abrir_datos(jsonfile)
    return(dato_json)
    
def guardar_datos(jsonfile, datos):
    #'funcion para guardar un archivo json'
    with open(jsonfile, 'w') as f:
        json.dump(datos, f)

def agregar_datos(jsonfile, datos):
    #'funcion para agregar datos a un archivo json'
    dato=abrir_datos(jsonfile)
    
    data=isinstance(dato, numbers.Integral)
    if data is True:
        dato=[datos]
    else:
        dato.append(datos)
    return(dato)

class modulo():
    

    def modulo_2(self):
        c=Aplicacion()

        print('1.Visualizar Habitaciones🛌🏿'
                 '\n2.Vender Habitacion🛌🏿'
                 '\n3.Desocupar Habitacion🛌🏿'
                 '\n4.Buscar Habitacion🛌🏿')

        mod2=numero_valido(4) 

        if mod2==1: 
            print('Visualizar Habitaciones')
            info=''
            while info !='NO':
                opcion=c.barco(data)
                info=c.elegir_habitacion(opcion,data)
                if info=='NO':
                    main()

        elif mod2==2:
            jsonfile='datos.json'
            datos_vacio=None    
            verificar_archivo(jsonfile,datos_vacio) 
            dato_json=abrir_datos(jsonfile)
        
            print('\nVender Habitaciones\n')
            print('Compra de Boletos:\n'
                  '1.Por Destino\n'
                  '2.Por Barco\n'
                  '0. Menú Principal')

            boleto=numero_valido(2)
            if boleto==1:
                destino=c.destino(data)
                print('Destino elegido:', destino)
                barco=c.destino_en_barco(data,destino)
                print('Barcos Disponibles: ', barco)
                print('Seleccione un Barco')
                opcion_barco=c.barco(data)
            elif boleto==2:
                opcion_barco=c.barco(data)
            else:
                main()
                
            barco=data[opcion_barco-1]['name']
            print('Tipo de Habitacion')
            tipo_hab=c.tipo_habitacion()
            print('Numero de Personas')
            num_personas=lee_numero()

            lista_hab=data[opcion_barco-1]['rooms'] #accede a la informacion de habitaciones de un barco desde base de datos principal
            hab=c.id_habitacion(lista_hab, tipo_hab) #se obtiene la identificacion de todas las habitaciones del barco escogido
            capacidad=c.capacidad_habitacion(data, opcion_barco, tipo_hab) #se obtiene la capacidad del tipo de habitacion escogido
            asig_habitaciones=c.selec_habitacion(hab, num_personas, capacidad,dato_json,barco)#se obtiene el numero de habitaciones asignadas al cliente y los id de las habitaciones
            print('capacidad:', capacidad ,'\nnumero:',asig_habitaciones)
            personas=c.formulario(num_personas)
            costo=c.costos(data, opcion_barco, tipo_hab, asig_habitaciones, personas)

            a_bordo=c.cliente_a_bordo()
            registro=c.registro_id(opcion_barco, num_personas, asig_habitaciones)

            datos={'barco':data[opcion_barco-1]['name'],'Tipo Hab':tipo_hab,'Capacidad Hab':capacidad,
                   'Numero de Personas':num_personas,'Habitaciones':asig_habitaciones,
                   'Datos de Pasajeros':personas, 'Costos': costo,
                   'Cliente a Bordo': a_bordo, 'Boleto_id':registro}
            
            print(datos,)

            y=agregar_datos(jsonfile, datos)
            guardar_datos(jsonfile, y)
            main()

        elif mod2==3:
            
            jsonfile='datos.json' # Archivo de almacenamiento de datos
            datos_vacio=None    
            verificar_archivo(jsonfile,datos_vacio) #verificar la existencia del archivo json, o creacion de uno
            dato_json=abrir_datos(jsonfile)

            print('\nMódulo 3\n')
            print('Desocupar Habitación')
            
        
            opcion=''
            while opcion!='NO':
                print('Buscar Habitación')
                encontrado=c.buscar_id(dato_json)
                
                print(encontrado)
                registro=encontrado[0]['Boleto_id']
                
                
                print('Desea Desocupar?')
                des=lee_entrada()
                if des=='SI':
                    encontrado[0]['Cliente a Bordo']='NO'
                    dato=c.borrar_registro(registro, jsonfile)
                    dato.append(encontrado[0])
        
                    guardar_datos(jsonfile, dato)
                print(encontrado)
                print('\nDesea Buscar Otro?')
                opcion=lee_entrada()
                if opcion=='NO':
                    main()
        
        elif mod2==4:
            print('\nMódulo 4\n')
            opcion=''
            while opcion!='NO':
                print('Buscar Habitación')
                encontrado=c.buscar()
                print(encontrado)
                
                print('\nDesea Buscar Otro?')
                opcion=lee_entrada()
                if opcion=='NO':
                    main()
    def modulo_1(self):
        c=Aplicacion()

        info=''
        while info !='NO':
            opcion=c.barco(data)
            info=c.info_barco(opcion,data)
            if info=='NO':
                main()

    def modulo_3(self):
        c=Aplicacion()
        jsonfile='datos_tour.json' # Archivo de almacenamiento de datos
        datos_vacio=None    
        verificar_archivo(jsonfile,datos_vacio) #verificar la existencia del archivo json, o creacion de uno
        dato_json=abrir_datos(jsonfile)

        Num_tour=[]
        dato_true=isinstance(dato_json, numbers.Integral)
        if dato_true is True:
            pass
        else:
            for i in range(len(dato_json)):
                num_cli=dato_json[i]['Cliente']['Numero de Personas']
                num_tour=dato_json[i]['Datos Tour']['Tour']
                Num_tour.append([num_tour,num_cli])
            
        opcion=''
        while opcion!='NO':
            print('......................\n'
                '\n   Modulo 3\n'
                  'Venta de Tour\n')
            formulario=c.formulario_tour()
            tour_barco=c.tour(formulario['Numero de Personas'], Num_tour)

            dato={'Cliente':formulario, 'Datos Tour':tour_barco}

            y=agregar_datos(jsonfile, dato)
            guardar_datos(jsonfile, y)

            print(dato)

            print('\nDesea Agregar Otro?')
            opcion=lee_entrada()
            if opcion=='NO':
                main()


    def modulo_4(self):
        d=Aplicacion_rest()
        print('\nModulo 4'
              '\nGestion de Restaurante\n')
        jsonfile='datos_rest.json' # Archivo de almacenamiento de datos
        datos_vacio=None    
        verificar_archivo(jsonfile,datos_vacio) #verificar la existencia del archivo json, o creacion de uno
        dato_json=abrir_datos(jsonfile)

        opcion=''
        while opcion!='NO':
            print('.........................................\n'
                'GESTION DE RESTAURANTE\n'
                '\nSeleccione Opcion\n'
                  '1.Buscar Producto o Combo \n'
                  '2.Agregar Producto\n'
                  '3.Eliminar Producto \n'
                  '4.Modificar Producto\n'
                  '5.Agregar Combo \n'
                  '6.Eliminar Combo \n'
                  '7.Modificar Combo \n'
                  '8.Ir al Menú Principal')
            menu=numero_valido(8)
            
            if menu==1:
                print('Buscar Producto o Combo?')
                clase=d.lee_clase()
                resultado=d.buscar_rest(dato_json,clase)
                print(resultado)
                
            elif menu==2:
                print('Agregar Producto')
                producto=d.agregar()
                print(producto)
                y=agregar_datos(jsonfile, producto)
                guardar_datos(jsonfile, y)
                main()
       
            elif menu==3:
                print('Eliminar Producto')
                clase='P'
                eliminar=d.eliminar_prod_comb(dato_json, clase)
                guardar_datos(jsonfile, eliminar)
                main()

            elif menu==4:
                print('Modificar Producto')
                clase='P'
                print('Buscar Producto')
                resultado=d.buscar_rest(dato_json,clase)
                print(resultado)
                id_colect=resultado[0]['cod']
                print('Desea Modificar?')
                opcion=lee_entrada()
                if opcion=='SI':
                    producto=d.agregar()
                    eliminar=d.eliminar_prod(dato_json, clase, id_colect)
                    guardar_datos(jsonfile, eliminar)
                    y=agregar_datos(jsonfile, producto)
                    guardar_datos(jsonfile, y)
                else:
                    main()
                
            elif menu==5:
                print('Agregar Combo')
                combo=d.agregar_combo()
                print(combo)
                y=agregar_datos(jsonfile, combo)
                guardar_datos(jsonfile, y)
                main()

                
            elif menu==6:
                print('Eliminar Combo')
                clase='C'
                eliminar=d.eliminar_prod(dato_json, clase)
                guardar_datos(jsonfile, eliminar)
                main()
                
            elif menu==7:
                print('Modificar Combo')
                clase='C'
                print('Buscar Producto')
                resultado=d.buscar_rest(dato_json,clase)
                print(resultado)
                id_colect=resultado[0]['cod']
                print('Desea Modificar?')
                opcion=lee_entrada()
                if opcion=='SI':
                    producto=d.agregar_combo()
                    eliminar=d.eliminar_prod(dato_json, clase, id_colect)
                    guardar_datos(jsonfile, eliminar)
                    y=agregar_datos(jsonfile, producto)
                    guardar_datos(jsonfile, y)
                else:
                    main()               
                
            elif menu==8:
                print('..............')
                main()

            print('\nCotinuar en Gestion de Restaurant?')
            opcion=lee_entrada()
            if opcion=='NO':
                main()

    def modulo_5(self):
        a=estadistica()

        jsonfile1='datos.json' # Archivo de almacenamiento de datos
        jsonfile2='datos_tour.json'

        datos_vacio=None    
        verificar_archivo(jsonfile1,datos_vacio) #verificar la existencia del archivo json, o creacion de uno
        dato_json1=abrir_datos(jsonfile1)

        verificar_archivo(jsonfile2,datos_vacio) #verificar la existencia del archivo json, o creacion de uno
        dato_json2=abrir_datos(jsonfile2)

        print('\nModulo 5'
              '\Estadísticas')
        print('\n1.Gasto por cliente (Ticket+Tour)'
              '\n2.Porcentaje de Clientes que no Compran Tour'
              '\n3.Clientes (primeros 3)de mayor fidelidad (que gastan más dinero)'
              '\n4.Top 3 Cruceros con más ventas en Tickets'
              '\n5.Top 5 Productos más vendidos en Restaurant'
              '\n6. Volver al menú principal')
        menu=numero_valido(6)

        if menu==1:
            print('\nPromedio de gasto de un cliente en el crucero  (Ticket+Tour)')
            gasto=a.gasto_cliente(dato_json1,dato_json2)
            monto=[]
            for i in range(len(gasto)):
                monto_cliente=gasto[i][1]
                monto.append(monto_cliente)

            personas=[]
            for i in range(len(gasto)):
                persona_cliente=gasto[i][0]
                personas.append(persona_cliente)

            monto_suma=sum(monto)
            promedio=monto_suma/len(gasto)
            print('Promedio de Gasto: ',round(promedio,2))
            main()
            
        elif menu==2:
            print('\nPorcentaje de Clientes que no Compran Tour')
            notour=a.no_tour(dato_json1,dato_json2)
            print(notour)
            main()
            
        elif menu==3:
            print('\nClientes (primeros 3)de mayor fidelidad')
            gasto=a.gasto_cliente(dato_json1,dato_json2)
            top3=a.top(gasto)
            for i in range(len(top3)):
                print(i+1,'.Nombre: ',top3[i][0],'   Monto: ',top3[i][1])
            main()
        elif menu==4:
            print('\nTop 3 Cruceros con más ventas en Tickets')
            crtop=a.crucero_top(dato_json1)
            for i in range(3):
                print(i+1,'.Crucero: ',crtop[i][0],'   Tickets:',crtop[i][1])
            main()
        elif menu==5:
            print('\nTop 5 Productos más vendidos en Restaurant')
            venta=a.p_vendidos(data)
            for i in range(5):
                print(i+1,'...',venta[i][0],'   Ventas:',venta[i][1])
            main()
            
        elif menu==6:
            main()

class estadistica():
    
    def gasto_cliente(self,dato_json1,dato_json2):
        data1=isinstance(dato_json1, numbers.Integral)
        data2=isinstance(dato_json2, numbers.Integral)
        
        clientes=[]
        if data1 is True:
            pass
        else:
            for i in range(len(dato_json1)):
                cliente_principal=dato_json1[i]["Datos de Pasajeros"][0]['Nombre']
                costo=dato_json1[i]["Costos"]["Total"]
                cliente=[cliente_principal, costo]
                clientes.append(cliente)

        clientes2=[]
        if data2 is True:
            pass
        else:
            for i in range(len(dato_json2)):
                cliente_principal=dato_json2[i]["Cliente"]["Nombre"]
                costo=dato_json2[i]["Datos Tour"]["Total"]
                cliente=[cliente_principal, costo]
                clientes2.append(cliente)

        gasto=[]

        if (data1 and data2) is True:
            print('Sin Datos*')
            return 0

        elif data1 is True:
            print('Sin Datos de Crucero')
            return clientes2
            
        elif data2 is True:
            print('Sin Datos de Tour')
            return clientes
        
        elif (data1 and data2) is False:
            list_a=[]
            for i in range(len(clientes)):
                for j in range(len(clientes2)):
                    if clientes[i][0] in clientes2[j][0]:
                        gasto_sum=clientes[i][1]+clientes2[j][1]
                        gastos_client=[clientes[i][0],round(gasto_sum,2)]
                        gasto.append(gastos_client)          
            return gasto

    def no_tour(self, dato_json1,dato_json2):
        data1=isinstance(dato_json1, numbers.Integral)
        data2=isinstance(dato_json2, numbers.Integral)
        
        clientes=[]
        if data1 is True:
            pass
        else:
            for i in range(len(dato_json1)):
                cliente_principal=dato_json1[i]["Datos de Pasajeros"][0]['Nombre']
                clientes.append(cliente_principal)

        clientes2=[]
        if data2 is True:
            pass
        else:
            for i in range(len(dato_json2)):
                cliente_principal=dato_json2[i]["Cliente"]["Nombre"]
                clientes2.append(cliente_principal)

        if (data1 and data2) is False:
            list_a=[]
            for i in range(len(clientes)):
                if clientes[i] in clientes2:
                    list_a.append(clientes[i])

            porcentaje=(1-len(list_a)/len(clientes))*100
            return (str(round(porcentaje,1))+'%')
        
        elif (data1 and data2) is True:
            return ('Sin datos')
        elif data1 is True:
            return ('Sin datos de Pasajeros')
        else:
            return ('Sin datos de Venta de Tour')


    def top(self, gasto):
        
        lista=gasto
        top3=[]
        for i in range(3):
            x, y = zip(*gasto)
            maximo = [[gasto[i],i] for i,a in enumerate(y) if a == max(y)]
            lista.pop(maximo[0][1])
            top3.append(maximo[0][0])
            
        return top3

    def crucero_top(self, dato_json):
        data=isinstance(dato_json, numbers.Integral)
        cruceros=[]
        if data is True:
            print('Sin datos')
            return (0)
        else:
            for i in range(len(dato_json)):
                crucero=dato_json[i]["barco"]
                cruceros.append(crucero)

        cuenta=dict((x,cruceros.count(x)) for x in set(cruceros))
        order=[[k,v] for k, v in sorted(cuenta.items(), key=lambda item:item[1])]
        top=order[::-1]
        
        return top

    def p_vendidos(self, data):

        productos=[]
        cantidad=[]
        for i in range(len(data)):
            for j in range(len(data[i]["sells"])):
                venta=data[i]["sells"][j]["name"]
                cant=data[i]["sells"][j]["amount"]
                
                productos.append(venta)
                cantidad.append([venta,cant])

        cuenta=[[x,productos.count(x)] for x in set(productos)]

        lista=[]
        for i in range(len(cuenta)):
            producto1=cuenta[i][0]
            a=0
            for j in range(len(cantidad)):
                producto2=cantidad[j][0]
                if producto1==producto2:
                    cant=cantidad[j][1]
                    a=cant+a
            lista.append([producto1,a])

        gasto=lista
        top5=[]
        for i in range(5):
            x, y = zip(*lista)
            maximo = [[gasto[i],i] for i,a in enumerate(y) if a == max(y)]
            lista.pop(maximo[0][1])
            top5.append(maximo[0][0])

        return top5

class Aplicacion_rest():
    #'Apliccion secundaria que controla las opciones sobre un restaurant'
    
    def agregar(self):
        nombre=input('Nombre de Alimento o Bebida :')
        print('Clasificacion (alimento/bebida)')
        clasif=Aplicacion_rest.lee_clasificacion(self)
        if clasif=='A':
            tipo=Aplicacion_rest.lee_clas_A(self)
        elif clasif=='B':
            tipo=Aplicacion_rest.lee_clas_B(self)
        print('Ingrese el precio')
        precio=lee_numero()
        precio=precio+precio*.16

        cod_id='P'+nombre+clasif+tipo
        alimento={'CLASE':'P','Nombre':nombre,'Clasificacion':clasif,'Tipo':tipo,'Precio':precio,'cod':cod_id}
        return(alimento)

    def agregar_combo(self):
        nombre=input('Nombre del Combo')
        num_prod=0
        productos=[]
        opcion=''
        while opcion!='NO':

            producto=input('Agregue un producto')
            productos.append(producto)
            num_prod=num_prod+1

            if num_prod<2:
                print('Agregue Otro')
                continue
            else:
                print('\nAgregar otro producto?')
                opcion=lee_entrada()
                if opcion=='NO':
                    break
        print('Indique precio del combo')
        precio_a=lee_numero()
        precio=precio_a+precio_a*.16
        cod_id='C'+nombre+str(precio_a)

        combo={'CLASE':'C', 'Nombre':nombre, 'Productos': productos, 'Precio':precio,'cod':cod_id }
        return(combo)


    def lee_clase(self):
    #'funcion para pedir al usuario una clasificacion de alimento/bebida'
    #'devuelve los carateres  alimento o bebida, en mayusculas'
        while True: 
            print("Ingrese P (producto) o C (combo)")
            opcion = input().upper()
            if opcion in ["P", "C"]:
                return opcion
            
    def lee_clasificacion(self):
    #'funcion para pedir al usuario una clasificacion de alimento/bebida'
    #'devuelve los carateres  alimento o bebida, en mayusculas'
        while True: 
            print("Ingrese A (Alimento) o B (bebida)")
            opcion = input().upper()
            if opcion in ["A", "B"]:
                return opcion
            
    def lee_clas_A(self):
    #'funcion para pedir al usuario una clasificacion de alimento'
        while True: 
            print("Ingrese E (empaque) o P (preparacion)")
            opcion = input().upper()
            if opcion in ["E", "P"]:
                return opcion
            
    def lee_clas_B(self):
    #'funcion para pedir al usuario una clasificacion de bebida''
        while True: 
            print("Ingrese S (prqueño), M (mediano) o G (grande)")
            opcion = input().upper()
            if opcion in ["S", "M", "G"]:
                return (opcion)

    def buscar_rest(self, dato_json, clase):
        print('\nBuscar por:\n'
            '1.Nombre\n'
            '2.Rango de Precio\n'
            '3.Volver')
        buscar_op=numero_valido(3)
        
        if buscar_op==1:
          resultado=Aplicacion_rest.buscar_nombre_rest(self,dato_json, clase)
        elif buscar_op==2:
          resultado=Aplicacion_rest.buscar_rango_rest(self,dato_json, clase)
          
        return resultado
      
    def buscar_nombre_rest(self, dato_json, clase):
        print('Buscar por nombre')
        nombre=input('Nombre: ')

        data=isinstance(dato_json, numbers.Integral)
        if data is True:
            Resultado='Sin datos'

        else:
            Resultado=[]
            for i in range(len(dato_json)):
                if clase==dato_json[i]['CLASE']:
                    if nombre in dato_json[i]['Nombre']:
                        resultado=dato_json[i]
                        Resultado.append(resultado)

        return(Resultado)
        
    def buscar_rango_rest(self, dato_json, clase):
        rango_val=rango()
        rango_min=rango_val[0]
        rango_max=rango_val[1]

        data=isinstance(dato_json, numbers.Integral)
        if data is True:
            Resultado='Sin datos'
            
        else:
            Resultado=[]
            for i in range(len(dato_json)):
                if clase==dato_json[i]['CLASE']:
                    if (dato_json[i]['Precio']>=rango_min and dato_json[i]['Precio']<=rango_max):
                        resultado=dato_json[i]
                        Resultado.append(resultado)
        return(Resultado)

    def eliminar_prod_comb(self, dato_json, clase):
        
        buscar=Aplicacion_rest.buscar_rest(self, dato_json, clase)
        colect=[]
        id_colect=[]
        for i in range(len(buscar)):
            if clase==buscar[i]["CLASE"]:
                colect.append(buscar[i])
                id_colect.append(buscar[i]['cod'])
                
        data=isinstance(colect, numbers.Integral)
        if data is True:
            print('Sin datos')
            main()
        else:
            print('Reultados:\n',colect)
            print('Desea Eliminar?')
            opcion=lee_entrada()
            if opcion=='SI':
                for i in range(len(dato_json)):
                    if dato_json[i]["cod"] in id_colect:
                        print('ID: ',id_colect)
                        del dato_json[i]
                        print('....\n',dato_json)
                        return(dato_json)

    def eliminar_prod(self, dato_json, clase, id_colect):
        data=isinstance(dato_json, numbers.Integral)
        if data is True:
            print('Sin datos')
            main()
        else:
            for i in range(len(dato_json)):
                if dato_json[i]["cod"]==id_colect:
                    print('Eliminar ID: ',id_colect)
                    del dato_json[i]
                    print('....\n',dato_json)
                    return(dato_json)
        
class Aplicacion():

    def barco(self,db):
    #'Mostrar los barcos disponibles en base de datos""
        len_db=len(db)
        print()
        print('\nCruceros\n')
        for i in range(len_db):
            print(i+1,'.',db[i]['name'])

        opcion=numero_valido(len_db)

        return(opcion)
    
    def destino(self,db):
    #'Mostrar los destinos disponibles en base de datos.Devuelve un destino'
        len_db=len(db)      
        destinos=[]
        print('')
        print('\nDestinos Disponibles\n')
        for i in range(len_db):
            destino=db[i]['route']
            for j in range(len(destino)):
                destinos.append(destino[j])

        destinos=list(set(destinos))

        for i in range(len(destinos)):
            print(i+1,'.',destinos[i])

        print('Seleccione un Destino:\n')
        opcion=lee_numero()
        salida=destinos[opcion-1] #la salida es el destino escogido
        return(salida)

    def destino_en_barco(self, db, destino):
                                 
        busqueda=[]                         
        for i in range(len(db)):
            if destino in db[i]['route']:
                busqueda.append(db[i]['name'])
        return(busqueda)
         
    def info_barco(self, opcion,db):
    #'Mostrar la informacion de los barcos'
        print('\nBarco ',db[opcion-1]['name'])  #disponibles en base de datos
        print('\nRuta: \n')
        for i in range(len(db[opcion-1]['route'])):
            print('--->',db[opcion-1]['route'][i])
        
        print('\nFecha de Salida: ', db[opcion-1]['departure'] )
        print('\nPrecio de Boletos: ', db[opcion-1]['cost'] )
        print('\nCapacidad de Habitaciones: ', db[opcion-1]['capacity'] )
        print('\nPiso,Pasillo: ', db[opcion-1]['rooms'])
        
        salida=ver_otro_barco()
        return(salida)

    def tipo_habitacion(self):
    
        print("Seleccione el tipo de Habitacion:\n"
              '1.Simple\n'
              '2.Premium\n'
              '3.VIP\n')
        tipo=numero_valido(3) #mod2=5 #loop para solictar numero correcto de las opciones

        if tipo==1:
            return('simple')
        elif tipo==2:
            return('premium')
        else:
            return('vip')

    def elegir_habitacion(self, opcion, db):
    #'Muestra las habitaciones disponibles en un barco'
        tipos=db[opcion-1]['rooms'] #accede al diccionario 'rooms' del barco seleccionado
        tipo=Aplicacion.tipo_habitacion(self) #Solicita el tipo de habitacion que se mostrará

        capacidad=Aplicacion.capacidad_habitacion(self,db,opcion, tipo)
        id_habitaciones=Aplicacion.id_habitacion(self,tipos, tipo) #Solicta los id del tipo de habitacion seleccionado

        print('\nBarco ',db[opcion-1]['name'])
        print('Habitaciones de clase: ', tipo)
        print('Capacidad de: ',capacidad,' personas')
        print(Aplicacion.servicio_hab(tipo))

        print('ID de habitaciones:\n', id_habitaciones)
        salida=ver_otro_barco()
        return(salida)

    def capacidad_habitacion(self, db,opcion, tipo): #mustra la capacidad de personas en una habitacion
        capac=db[opcion-1]['capacity'][tipo]
        return(capac)

    def servicio_hab(tipo):
    #'Muestra los servicios disponibles para cada tipo de habitacion'
        if tipo=='simple':
            return('Con Servicio de habitacion')
        elif tipo=='premium':
            return('Con Servicio de habitacion y vista al mar')
        elif tipo=='vip':
            return('Con Servicio de habitacion, vista al mar, espacio para fiestas privadas')

    def id_habitacion(self,tipos, tipo):
        
        pasillos=tipos[tipo][0] #numero de pasillos del buque y tipo de habitacion seleccionado
        pasillos_id=['A','B','C','D','E','F','G'] #id de pasillos permitidos
        pasillo=pasillos_id[0:pasillos] #id de pasillos del buque y tipo de habitacion seleccionado
        habitaciones=tipos[tipo][1] ##numero de habitaciones del buque y tipo de habitacion seleccionado

        if tipo=='simple':
            id_t='S'
        elif tipo=='premium':
            id_t='P'
        elif tipo=='vip':
            id_t='V'

        habitacion=[]
        for j in pasillo:
            for i in range(habitaciones):
                habitacion.append(id_t+j+str(i+1))
        return(habitacion)

    def selec_habitacion(self, hab, num_personas, capacidad, dato_json, barco):
        
        a=isinstance(dato_json, numbers.Integral) #verifica que el archivo json es nuevo (contiene integer)
        if a is True:
            len_dato=1
        else:
            len_dato=len(dato_json)

        hab_ocup=[]
        for i in range(len_dato):
            if a is True: 
                continue
            elif barco in dato_json[i]["barco"]:
                for j in range(len(dato_json[i]["Habitaciones"][1])):
                    data2=dato_json[i]["Habitaciones"][1][j]
                    hab_ocup.append(data2)

        hab_disp=[]
        for i in range(len(hab)):
            if hab[i] in hab_ocup:
                continue
            else:
                hab_disp.append(hab[i])

        num_hab_disp=len(hab_disp)
        a=num_personas/capacidad #segun el numero de personas
        num_hab=math.ceil(a)     #tambien devuelve el id de las habitaciones          

        if num_hab>num_hab_disp:
            print('Numero de Habitaciones Insuficientes\n'
                  'Seleccione otro tipo de habitación, '
                  'o número menor de pasajeros')
            print('Habitaciones Disponibles: ', num_hab_disp,
                  '\nNúmero máximo de personas: ', num_hab_disp*capacidad)
            main()
        else:
            id_hab=hab_disp[0:num_hab]
            return(num_hab, id_hab)

    def formulario(self, num_personas):
        #'funcion para llenar un formulario con los datos de cada pasajero'
        personas=[]
        for i in range(num_personas):
            nombre=input('Nombre: ')
            print('Documento de identidad')
            doc=lee_numero()
            print('Edad: ')
            edad=lee_numero()
            print('Discapacidad?')
            disc=lee_entrada()

            doc_primo=esPrimo(doc)
            doc_abun=esAbundante(doc)
            upgrade=0

            descuento=0
            if doc_primo is True:
                descuento=descuento+0.1
            if doc_abun is True:
                descuento=descuento+0.15

            if edad>64:
                upgrade=1

            if disc=='SI':
                descuento=descuento+0.3

            personas.append({'Nombre':nombre,'ID':doc,'Edad':edad,'Discapacidad':disc,'Upgrade':upgrade, 'Descuento':descuento})
        return(personas)

    def registro_id(self, opcion_barco, num_personas, asig_habitaciones):
        id_client=str(opcion_barco)+str(num_personas)+str(asig_habitaciones[1][0])
        return(id_client)
        

    def costos(self, datos, barco, tipo_hab, asig_habitaciones, personas):
        #'funcion para calcular el costo total del viaje'
        costo_hab=datos[barco-1]['cost'][tipo_hab]
        num_hab=asig_habitaciones[0]
        monto_total=costo_hab*num_hab
        desc=[]
        for i in range(len(personas)):
            descuentos=personas[i]['Descuento']
            desc.append(descuentos)
            
        desc=sum(desc)
        impuesto=monto_total*0.16
        monto_desc=monto_total-monto_total*desc
        total=monto_desc+impuesto
        costo={'Monto_Total': monto_total, 'Monto_Con_Descuento':monto_desc, 'Impuesto':impuesto,'Total':total}
        return(costo)

    def cliente_a_bordo(self):
        print('¿El pasajero se encuentr a bordo?')
        abordo=lee_entrada()
        return(abordo)

    def buscar(self):
        print('Desea buscar habitacion por:\n'
              '1. Tipo\n2.Capacidad\n3.Id de Habitación',
                '\n4.Volver')
        opcion=numero_valido(4)

        jsonfile='datos.json' # Archivo de almacenamiento de datos
        datos_vacio=None    
        verificar_archivo(jsonfile,datos_vacio) #verificar la existencia del archivo json, o creacion de uno
        dato_json=abrir_datos(jsonfile)
        
        if opcion==1:
            encontrado=Aplicacion.buscar_tipo(self,dato_json)
            return(encontrado)
        elif opcion==2:
            encontrado=Aplicacion.buscar_capacidad(self,dato_json)
            return(encontrado)
        elif opcion==3:
            encontrado=Aplicacion.buscar_id(self,dato_json)
            return(encontrado)
        else:
            main()

    def buscar_tipo(self,dato_json):
        tipo=Aplicacion.tipo_habitacion(self)
        encontrados=[]
        for i in range(len(dato_json)):
            if tipo==dato_json[i]["Tipo Hab"]:
                encontrados.append(dato_json[i])
        return(encontrados)

    def buscar_capacidad(self,dato_json):
        a=lee_numero()
        encontrados=[]
        for i in range(len(dato_json)):
            if a==dato_json[i]["Capacidad Hab"]:
                encontrados.append(dato_json[i])
        return(encontrados)

    def buscar_id(self,dato_json):
        print('\nEscriba el id de la habitacion: ')
        a=input().upper()
        encontrados=[]
        for i in range(len(dato_json)):
            if a in dato_json[i]["Habitaciones"][1]:
                encontrados.append(dato_json[i])
            else:
                print('No encontrado')
                main()
        return(encontrados)

    def borrar_registro(self, registro,jsonfile):
        datos=abrir_json(jsonfile)
        for i in range(len(datos)):
            if registro==datos[i]["Boleto_id"]:
                del datos[i]
        print('....\n',datos)     
        return(datos)

    def formulario_tour(self):
        print('Ingrese datos de pasajero')
        nombre=input('Nombre: ')
        print('Documento de identidad')
        doc=lee_numero()
        print('Número de Personas: ')
        num_per=lee_numero()
        formulario={'Nombre':nombre,'ID':doc,'Numero de Personas':num_per}
        return(formulario)
        

    def tour(self, num_per, Num_tour):
        a='Tour en el Puerto'
        b='Degustacion de comida local'
        c='Trotar por el pueblo/ciudad'
        d='Visita a lugares Históricos'
        Num_cli_a=[0]
        Num_cli_b=[0]
        Num_cli_c=[0]
        Num_cli_d=[0]
              
        data=isinstance(Num_tour, numbers.Integral)
        if data is True:
            pass
        else:
            for i in range(len(Num_tour)):
                if Num_tour[i][0]==a:
                    num_cli_a=Num_tour[i][1]
                    Num_cli_a.append(num_cli_a)
                elif Num_tour[i][0]==b:
                    num_cli_b=Num_tour[i][1]
                    Num_cli_b.append(num_cli_b)
                elif Num_tour[i][0]==c:
                    num_cli_c=Num_tour[i][1]
                    Num_cli_c.append(num_cli_c)
                elif Num_tour[i][0]==d:
                    num_cli_d=Num_tour[i][1]
                    Num_cli_d.append(num_cli_d)
        Num_cli_a=sum(Num_cli_a)
        Num_cli_b=sum(Num_cli_b)
        Num_cli_c=sum(Num_cli_c)
        Num_cli_d=sum(Num_cli_d)

        print('Seleecione El Tour\n'
              ' 1.Tour en el Puerto (Vendidos ',Num_cli_a,'/10)\n',
              '2.Degustacion de comida local (Vendidos',Num_cli_b,'/100)\n',
              '3.Trotar por el pueblo/ciudad(sin cupo maximo)\n',
              '4.Visita a lugares Históricos (Vendidos',Num_cli_c,'/15)\n',
              '5.Volver al menu principal')
                     
        opcion=numero_valido(4)
        if opcion==1:
            tour='Tour en el Puerto'
            precio=30
            hora='7 A.M.'
            max_per=4
            cupo_total=10
            disponible=(cupo_total-Num_cli_a)

    
            if num_per>max_per:
                print('Máximo 4 Personas')
                print('\nCupos Disponibles:',disponible)
                modulo.modulo_3(self)
                
            if num_per>disponible:
                print('Sin cupos sufientes')
                print('\nCupos Disponibles:',disponible,
                  '\nPersonas Maximas:', max_per)
                modulo.modulo_3(self)
                
            desc=0
            if num_per==3:
                desc=0.1
            if num_per==4:
                desc=0.2

            total=(num_per*precio)-((num_per-2)*precio*desc)
            
  
        elif opcion==2:
            max_per=2
            tour='Degustacion de comida local'
            precio=100
            hora='12 P.M'
            cupo_total=100
            disponible=cupo_total-Num_cli_b
    
            if num_per>max_per:
                print('Máximo 2 Personas')
                print('\nCupos Disponibles:',disponible)
                modulo.modulo_3(self)
            if num_per>disponible:
                print('Sin cupos sufientes')
                print('\nCupos Disponibles:',disponible,
                  '\nPersonas Maximas:', max_per)
                modulo.modulo_3(self)

            
            total=num_per*precio
            
        elif opcion==3:
            tour='Trotar por el pueblo/ciudad'
            precio=0
            max_per=None
            hora='6 A.M.'
            cupo_total=None
            total=0
            
        elif opcion==4:
            tour='Visita a lugares Históricos'
            precio=40
            max_per=4
            hora='10 A.M.'
            cupo_total=15
            disponible=cupo_total-Num_cli_d
            
            if num_per>max_per:
                print('Máximo 4 Personas')
                print('\nCupos Disponibles:',disponible)
                modulo.modulo_3(self)
            if num_per>disponible:
                print('Sin cupos sufientes')
                print('\nCupos Disponibles:',disponible,
                  '\nPersonas Maximas:', max_per)
                modulo.modulo_3(self)

            desc=0
            if num_per>2:
                desc=0.1
            
            total=(num_per*precio)-(precio*desc)
            
        elif opcion==5:
            main()

        datos_tour={'Tour':tour,'Precio':precio,'MaxPersona':max_per,'Hora':hora,'Cupo Total':cupo_total, 'Total':total}
        return(datos_tour)
    
def ver_otro_barco():
    #'pregunta al usuario si desea repetir el proceso de visualizar un barco'
    print('\nDesea ver otro barco?')
    salida=lee_entrada()
    return(salida)

def lee_numero():
    #'Se pide un valor entero y lo devuelve.'
    #'Mientras el valor ingresado no sea entero, vuelve a solicitarlo'
    while True:
        valor = input("> ")
        try:
            valor = int(valor)
            return valor
        except ValueError:
            print("ATENCIÓN: Debe ingresar un número entero sin decimales .")

def rango():
    while True:
        print("\nIngrese número minimo\n")
        valor_min=lee_numero()
        print("\nIngrese número maximo\n")
        valor_max=lee_numero()
        if valor_max>valor_min:
            return([valor_min,valor_max])
        else:
            print("Error. Introduzca de Nuevo el Rango")

def numero_valido(numero_max):
    #'devuelve un numero válido dado una serie de opciones numeradas'
    opcion=numero_max+1
    while opcion>numero_max:
        opcion=lee_numero()
        print('\n')
        if opcion>numero_max:
            print('Ingrese un numero válido')
    return(opcion)
    
def lee_entrada():
    #'funcion para pedir al usuario si desea realizar accion'
    #'devuelve los carateres  SI O NO, en mayusculas'
        while True: 
            print("Ingrese SI o NO")
            opcion = input().upper()
            if opcion in ["SI", "NO"]:
                return opcion

def verificar_archivo(archivo, datos):
    #'funcion para verificar la existencia de un archivo json'
    if os.path.isfile(archivo) and os.access(archivo, os.R_OK):
        print ("")
    else:
        print ("No se encontró base de datos\nCreando archivo json...")
        guardar_datos(archivo, 0)
        
def esPrimo(num):
    #'funcion para saber si un numero es primo'
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

def esAbundante(num):
    #'funcion para saber si un numero es abundante'
    count =  1
    suma = 0
    while (count<num):
      if (num%count==0):
        suma+=count
      count = count + 1
    
    if (suma>(num)):
      return True
    else:
      return False

def main():


    print('\nBienvenido a SAMAN CARIBEAN🛳️')
    print('1. Gestion de Cruceros \n2. Gestion de Habitaciones🛌\n'
          '3. Venta de Tour \n4. Gestion de Restaurante🍽️ '
          '\n5. Estadísticas \n6. para salir')
    

    opcion=numero_valido(6)
    mod=modulo()
    
    if opcion==1:
        mod.modulo_1()
    elif opcion==2:
        mod.modulo_2()
    elif opcion==3:
        mod.modulo_3()
    elif opcion==4:
        mod.modulo_4()
    elif opcion==5:
        mod.modulo_5()
    else:
        print('Hasta Luego')
        sys.exit()


main()
