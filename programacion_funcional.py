
def saluda(nombre):
    print("Hola " + nombre + ", ¿cómo estás?")

saluda("Iván")
saluda("Menchu")

texto = "Adios" # Asignar a una variable el valor "Adios"    "Adios" -> texto
                # Eso sería cierto para algunos lenguajes de programación... no para todos.
                # En ADA, C, C++ sería cierto
                    # Una variable es una región en memoria donde guardo un DATO
                # En python, en js, en ts, en java NO ES CIERTO, de hecho es lo contrario:
                # Asignamos la variable al valor "Adios"      texto -> "Adios"
                   # En estos lenguajes, una variable guarda más relación con el concepto de PUNTERO en el lenguaje C
                   # En JAVA, PY, KOTLIN, una variable es una referencia a un DATO que tengo guardado en RAM

texto = "Hola"  # Ese dato "hola", que se guarda en RAM, Dónde se guarda?
                    # Sobre-escribiendo al dato "Adios" ?  C, C++, ADA
                    # En otro lugar de la RAM ?           PY, JAVA, KOTLIN, TS, JS

texto = saluda  # Hago que la variable texto referencia a la función saluda

texto("Federico")   # Ejecutando a la función saluda, a través de la variable texto


def imprimir_saludo(funcion_generadora_de_saludos, nombre):
    print( funcion_generadora_de_saludos(nombre) )

def funcion_generadora_de_saludos_informales(nombre):
    return "Ey " + nombre + ", ¿qué tal?"

def funcion_generadora_de_saludos_formales(nombre):
    return "Buenos días " + nombre + ", ¿cómo se encuentra?"

imprimir_saludo(funcion_generadora_de_saludos_informales, "Lucas")

# Esto me permite crear funciones, donde parte de la lógica de la función
# es desconocida en el momento de crear la función... 
# y esa parte de lógica se suministra como argumento/parámetro