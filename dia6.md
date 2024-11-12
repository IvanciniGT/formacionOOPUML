# Sistema de control de Versiones:

SCM - Source Code Management

- CVS           ARCHIOBSOLETO
- Subversion    MUY OBSOLETO (En Indra aún se sigue usando en pocos proyectos - legacy)
- GIT           ESTE ES EL BUENO (En Indra esto se usa en muchos proyectos.. y lo que estaba en svn se está migrando a git)

Estas herramientas nos permiten:
- Tener controladas multiples versiones de mi proyecto, incluso versiones paralelas entre si.
    v1.0.1
        v1.0.2
    v2.0.0
- Me sirven de copia de seguridad (servidor)
- Nos ayudan a a trabajar en equipo, donde varios desarrolladores pueden trabajar en el mismo proyecto:
  - CVS y SVN lo que me permiten es solicitar al servidor que guarda el proyecto el BLOQUEO de un fichero, de forma que nadie más pueda modificarlo.
  - GIT permite a varias personas trabajar sobre el mismo fichero... pero al hacerlo pueden pisarse uno al otro: GENERAR CONFLICTOS... que luego hay que arreglar.

## Diagrama entidad relación:


```mermaid

classDiagram
    direction LR
    class Idioma {
        <<entity>>
        + id: Entero
        + nombre: Cadena texto
        + icono: Carácter
    }
    class Diccionario {
        <<entity>>
        + id: Entero
        + idioma: Idioma
        + nombre: Cadena texto
    }
    class Palabra {
        <<entity>>
        + id: Entero
        + diccionario: Diccionario
        + palabra: Cadena texto
    }
    class Contexto {
        <<entity>>
        + id: Entero
        + contexto: Cadena texto
        + siglas: Cadena texto
    }
    class Significado {
        <<entity>>
        + id: Entero
        + palabra: Palabra
        + definición: Cadena texto
        + contexto: Contexto
    }
    class Ejemplo {
        <<entity>>
        + id: Entero
        + significado: Significado
        + ejemplo: Cadena texto
    }
    class Sinonimo {
        <<entity>>
        + id: Entero
        + significado1: Significado
        + significado2: Significado
    }

    Idioma "1" -- "n" Diccionario
    Diccionario "1" -- "n" Palabra
    Palabra "1" -- "n" Significado
    Significado "n" -- "1" Contexto
    Significado "1" -- "n" Ejemplo
    Significado "n" -- "n" Sinonimo
    Significado "n" -- "n" Sinonimo

   
```

# Diagrama de Clases que ayude a identificar Componentes



```mermaid

classDiagram
    direction TD

    class SERVICIO_DE_BUSQUEDA {
        <<interface>>
        + buscarPalabra(palabra: texto, idioma: texto) : Lista~Significado~
    }


    class CONTROLADOR_DE_SALIDA {
        <<interface>>
        + mostrarSignificadosDeUnaPalabra(Significado: Lista~Significado~) : Nada
        + mostrarPalabraNoEncontradaEnDiccionario(palabra: string, idioma: string): Nada
        + mostrarIdiomaNoExistente(idioma: string): Nada
    }

    class CONTROLADOR_DE_ENTRADA {
        <<interface>>
        + capturarIdioma() : texto
        + capturarPalabra() : texto
    }

    class MiPrograma {
        + main() : Nada
    }



    SERVICIO_DE_BUSQUEDA --> Significado: Provee

    MiPrograma ..> CONTROLADOR_DE_ENTRADA : usa
    MiPrograma ..> CONTROLADOR_DE_SALIDA : usa
    MiPrograma ..> SERVICIO_DE_BUSQUEDA : usa
    CONTROLADOR_DE_SALIDA --> Significado: Imprime


    class Significado {
        <<entity>>
        + id: Entero
        + palabra: Palabra
        + definición: Cadena texto
        + contexto: Contexto
    }

```


```mermaid

classDiagram
    direction TD
    class REPOSITORIO_DE_DICCIONARIOS {
        <<interface>>
        + obtenerPalabras(idioma: texto) : Lista~Palabra~
    }
    class REPOSITORIO_DE_DICCIONARIOS_DE_FICHEROS {
        <<repository>>
        + obtenerPalabras(idioma: texto) : Lista~Palabra~
        - existeElFichero(idiom: texto) : boolean
        - abreUnFichero(idiom: texto) : ReferenciaAlFichero
        - leeFicheroCompleto(fichero: ReferenciaAlFichero) : Lista~Palabra~
        - cierraFichero(fichero: ReferenciaAlFichero) : Nada
    }

    class SERVICIO_DE_BUSQUEDA {
        <<interface>>
        + buscarPalabra(palabra: texto, idioma: texto) : Lista~Significado~
    }


    class CONTROLADOR_DE_SALIDA {
        <<interface>>
        + mostrarSignificadosDeUnaPalabra(Significado: Lista~Significado~) : Nada
        + mostrarPalabraNoEncontradaEnDiccionario(palabra: string, idioma: string): Nada
        + mostrarIdiomaNoExistente(idioma: string): Nada
    }

    class CONTROLADOR_DE_ENTRADA {
        <<interface>>
        + capturarIdioma() : texto
        + capturarPalabra() : texto
    }


    class SERVICIO_DE_BUSQUEDA_BINARIA {
        <<service>>
        - REPOSITORIO_DE_DICCIONARIOS repositorioConcreto
        + buscarPalabra(palabra: texto, idioma: texto) : Lista~Significado~
    }


    class CONTROLADOR_DE_SALIDA_POR_CONSOLA {
        <<controller>>
        + mostrarSignificadosDeUnaPalabra(Significado: Lista~Significado~) : Nada
        + mostrarPalabraNoEncontradaEnDiccionario(palabra: string, idioma: string): Nada
        + mostrarIdiomaNoExistente(idioma: string): Nada
    }

    class CONTROLADOR_DE_ENTRADA_POR_CONSOLA {
        <<controller>>
        + capturarIdioma() : texto
        + capturarPalabra() : texto
    }

    class MiPrograma {
        + main() : Nada
    }


    REPOSITORIO_DE_DICCIONARIOS <|.. REPOSITORIO_DE_DICCIONARIOS_DE_FICHEROS : implementa
    SERVICIO_DE_BUSQUEDA_BINARIA ..> REPOSITORIO_DE_DICCIONARIOS : utiliza

    REPOSITORIO_DE_DICCIONARIOS --> Palabra: Provee
    REPOSITORIO_DE_DICCIONARIOS_DE_FICHEROS --> Palabra: Provee
    SERVICIO_DE_BUSQUEDA --> Significado: Provee

    MiPrograma ..> CONTROLADOR_DE_ENTRADA : usa
    MiPrograma ..> CONTROLADOR_DE_SALIDA : usa
    MiPrograma ..> SERVICIO_DE_BUSQUEDA : usa

    CONTROLADOR_DE_ENTRADA <|.. CONTROLADOR_DE_ENTRADA_POR_CONSOLA : implementa
    CONTROLADOR_DE_SALIDA <|.. CONTROLADOR_DE_SALIDA_POR_CONSOLA : implementa
    SERVICIO_DE_BUSQUEDA_BINARIA ..|>  SERVICIO_DE_BUSQUEDA : implementa


    class Palabra {
        <<entity>>
        + id: Entero
        + diccionario: Diccionario
        + palabra: Cadena texto
    }
    class Significado {
        <<entity>>
        + id: Entero
        + palabra: Palabra
        + definición: Cadena texto
        + contexto: Contexto
    }
    Palabra "1" -- "n" Significado

```

## Enterprise Architect

- Herramienta de modelado UML de sistemas (software y hardware)

UML es un estándar ISO para crear diagramas de modelos de software:
- Diagramas estáticos o estructurales
    - Diagramas de clases
    - Diagramas de componentes
    - Diagramas de objetos
- Diagramas dinámicos o de comportamiento
  - Diagramas de secuencia
  - Diagramas de casos de uso
  - Diagramas de estados
  - Diagramas de actividades

Hay extensiones de UML:
- SysML: Para modelar sistemas de hardware
  Recogen muchos de los diagramas de UML (no todos) y añaden sus propios nuevos tipos de diagramas:
    - Diagramas de requerimientos
- BPMN: Para modelar procesos de negocio