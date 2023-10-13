import random


class Queues:
    def __init__(self):
        self.items = []

    def encolar(self, x):
        self.items.append(x)

    def desencolar(self):
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        return len(self.items) == 0

    def imprimir(self):
        for paciente in self.items:
            print('Paciente', paciente.id)


class Nodo:
    def __init__(self, paciente): #Método Constructor
        self.paciente = paciente
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.head = None

    def adicionar(self, paciente): #Adicionar es apuntar a otro (nuevo_nodo)
        nuevo_nodo = Nodo(paciente)
        if self.head is None:
            self.head = nuevo_nodo
        else:
            actual = self.head
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def insertarCabeza(self, paciente): #Método para insertar al inicio
        nuevo_nodo = Nodo(paciente)
        nuevo_nodo.siguiente = self.head
        self.head = nuevo_nodo

    def insertar_en_segundo_lugar(self, paciente):
        nuevo_nodo = Nodo(paciente)
        if self.head is None:
            self.head = nuevo_nodo
        else:
            actual = self.head
            # Verificar si el paciente tiene estado "Código azul"
            if paciente.estado == 'Código azul':
                nuevo_nodo.siguiente = self.head
                self.head = nuevo_nodo
            else:
                # Definir las prioridades de estados
                prioridades = {'Estabilidad urgente': 0, 'Urgencias normales': 1, 'Urgencias leves': 2}
                while actual.siguiente and actual.siguiente.paciente.estado != 'Código azul':
                    # Comparar la prioridad del paciente con la prioridad del siguiente
                    if prioridades.get(paciente.estado, 3) < prioridades.get(actual.siguiente.paciente.estado, 3):
                        break
                    actual = actual.siguiente
                nuevo_nodo.siguiente = actual.siguiente
                actual.siguiente = nuevo_nodo

    def getUltimo(self): #Método para obtener el último elemento
        actual = self.head
        while actual.siguiente:
            actual = actual.siguiente
        return actual.paciente

    def insertarUltimo(self, paciente): #Método para insertar al final
        nuevo_nodo = Nodo(paciente)
        if self.head is None:
            self.head = nuevo_nodo
        else:
            actual = self.head
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo


    def buscar(self, paciente): #Método para buscar  elemento
        actual = self.head
        while actual:
            if actual.paciente == paciente:
                return True
            actual = actual.siguiente
        return False

    def modificar(self, dato_viejo, dato_nuevo): #Método para borrar elemento
        actual = self.head
        while actual:
            if actual.dato == dato_viejo:
                actual.dato = dato_nuevo
                return True
            actual = actual.siguiente
        return False

    def is_empty(self):
        return self.head == None

    def eliminar(self, paciente): #Método para eliminar elemento
        if self.head is None:
            return
        if self.head.paciente == paciente:
            self.head = self.head.siguiente
            return
        actual = self.head
        while actual.siguiente:
            if actual.siguiente.paciente == paciente:
                actual.siguiente = actual.siguiente.siguiente
                return

    def mostrar(self): #Método de visualización de la lista
        actual = self.head
        while actual:
            print(actual.paciente, end=" -> ")
            actual = actual.siguiente
        print("None")


class Persona:
    def __init__(self):
        self.nombre = None
        self.edad = None
        self.id = None
        self.estado = None
        self.enfermedad = None
        self.hora = None
        self.horaAtencion = None
        self.turnoAtencion = None
        self.horaSalida = None

    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad

    def getId(self):
        return self.id

    def getEstado(self):
        return self.estado

    def getEnfermedad(self):
        return self.enfermedad

    def getHora(self):
        return self.hora

    def getHoraAtencion(self):
        return self.horaAtencion

    def getTurnoAtencion(self):
        return self.turnoAtencion

    def setNombre(self, nombre):
        self.nombre = nombre

    def setEdad(self, edad):
        self.edad = edad

    def setId(self, id):
        self.id = id

    def setEstado(self, estado):
        self.estado = estado

    def setEnfermedad(self, enfermedad):
        self.enfermedad = enfermedad

    def setHora(self, hora):
        self.hora = hora

    def setHoraAtencion(self, horaAtencion):
        self.horaAtencion = horaAtencion

    def setTurnoAtencion(self, turnoAtencion):
        self.turnoAtencion = turnoAtencion


class Doctores:
    def __init__(self):
        self.estaLibre = True   # True = Libre, False = Ocupado


prioridades = {'Código azul': 0, 'Estabilidad urgente': 1, 'Urgencias normales': 2, 'Urgencias leves': 3}

def generarEstado():
    numero = random.randint(1, 4)
    if numero == 1:
        estadito = 'Código azul'
    elif numero == 2:
        estadito = 'Estabilidad urgente'
    elif numero == 3:
        estadito = 'Urgencias normales'
    elif numero == 4:
        estadito = 'Urgencias leves'
    return estadito

def generarSalidaAzul():
    numero = random.randint(1, 3)
    if numero == 1:
        salida = 'Remitido a hospitalización'
    elif numero == 2:
        salida = 'Remitido a especialista'
    elif numero == 3:
        salida = 'Morgue'
    return salida

def generarSalida():
    numero = random.randint(1, 5)
    if numero == 1:
        salida = 'Alta'
    elif numero == 2:
        salida = 'Alta Voluntaria'
    elif numero == 3:
        salida = 'Remitido a hospitalización'
    elif numero == 4:
        salida = 'Remitido a especialista'
    elif numero == 5:
        salida = 'Morgue'
    return salida

def main():
    pacientes = {}
    cola_pacientes = Queues()
    lista_pacientes = ListaEnlazada()

    opcion = None
    contador = 0
    turno = 1

    numeroPacientes = int(input('Ingrese el número de pacientes: '))
    horaLlegada = float(input('Ingrese la hora de llegada: '))
    medicos = [Doctores() for _ in range(2)]  # Dos médicos
    tiempo_transcurrido = 0

    while len(pacientes) != numeroPacientes:
        print('\n¿La vida del paciente está en riesgo?')
        print('1. Si')
        print('2. No')
        opcion = int(input('Ingrese una opción: '))

        if opcion == 1:
            print('\nEl paciente debe ser atendido de inmediato, estado: código azul')
            estado = 'Código azul'
            paciente = Persona()
            paciente.hora = horaLlegada
            paciente.id = contador + 1
            contador += 1
            paciente.turnoAtencion = turno
            turno += 1
            paciente.estado = estado
            paciente.salida = generarSalidaAzul()
            paciente.horaSalida = tiempo_transcurrido + 10  # Cada atención se demora 10 unidades de tiempo
            tiempo_transcurrido = paciente.horaSalida
            pacientes[paciente.id] = paciente
            cola_pacientes.encolar(paciente)

        elif opcion == 2:
            print('\nEl paciente debe continuar con la admisión y posterior triage...')
            paciente = Persona()
            print('Bienvenido a la admisión de pacientes...')
            paciente.id = contador + 1
            contador += 1
            paciente.nombre = input('Ingrese el nombre del paciente: ')
            paciente.edad = int(input('Ingrese la edad del paciente: '))
            paciente.enfermedad = input('Ingrese la enfermedad del paciente: ')
            paciente.hora = horaLlegada
            paciente.turnoAtencion = turno
            turno += 1
            paciente.estado = generarEstado()
            paciente.salida = generarSalida()
            paciente.horaSalida = None  # Inicialmente no sabemos la hora de salida
            pacientes[paciente.id] = paciente
            cola_pacientes.encolar(paciente)

    print('\nLos pacientes en la cola son:')
    for paciente in cola_pacientes.items:
        print(f'Paciente {paciente.id} - Estado: {paciente.estado}')

    pacientes_ordenados = sorted(cola_pacientes.items, key=lambda p: prioridades[p.estado])  # Ordenar por prioridad de estados

    tiempo_medico = [horaLlegada, horaLlegada]  # Lleva un registro de cuánto tiempo ha trabajado cada médico

    ordenLista = 1
    print('\nLos pacientes ordenados, luego de ser atendidos, son:')
    for paciente in pacientes_ordenados:
        tiempo_medico.sort()  # Ordena los tiempos de trabajo de los médicos
        medico_disponible = tiempo_medico[0]
        tiempo_medico[0] += 10  # Cada atención se demora 10 unidades de tiempo
        paciente.horaSalida = medico_disponible + 10
        print(f'{ordenLista}. Paciente {paciente.id} - Estado: {paciente.estado} - Estado de salida: {paciente.salida} - Hora de llegada: {paciente.hora} - Hora de salida: {paciente.horaSalida}')
        ordenLista += 1

if __name__ == "__main__":
    main()