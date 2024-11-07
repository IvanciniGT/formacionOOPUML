

```mermaid
stateDiagram-v2
direction LR
  Apagado --> Encendido: Encender
  Encendido --> Apagado: Apagar
```


```mermaid
stateDiagram-v2
direction LR
  state Encendido {
    [*] --> Reposo
    Reposo --> Ocupado: INSERTAR TARJETA
    Ocupado --> Reposo: EXTRAER TARJETA
    Reposo --> [*]
  }
```

```mermaid
stateDiagram-v2
direction LR
  state Ocupado {
    state "Lectura de la Tarjeta" as Lectura
    state "Obtención del PIN" as PIN
    state "Obtención de la Cantidad" as Cantidad
    state "Entrega del dinero" as Entrega
    state condicion <<choice>>
    state condicion2 <<choice>>
    state condicion3 <<choice>>

    [*] --> Lectura
    Lectura     --> condicion
    condicion   --> Error: [Si no he leido la tarjeta]
    condicion   --> PIN: [Si he leido la tarjeta]
    PIN         --> condicion2
    condicion2  --> Error: [Si no he conseguido <br> un PIN correcto]
    condicion2  --> Cantidad: [Si he conseguido <br> un PIN correcto]
    Cantidad    --> condicion3
    condicion3  --> Error: [Si no he conseguido <br> una cantidad correcta]
    condicion3  --> Entrega: [Si he conseguido <br> una cantidad correcta]
    Error       --> [*]
    Entrega     --> [*]
  }
```

En UML, en los diagramas de estados, 
- Los EVENTOS se representan como textos en medio de una flecha.
  EL CONVENIO ES ESCRIBIRLOS EN MAYUSCULA  
- Las guardas, que son las condiciones que deben cumplirse para que se ejecute una transición se representan entre corchetes.


# Acciones y los contextos extendidos

Las máquinas de estados pueden necesitar de datos adicionales para funcionar. 
Por ejemplo, una guarda puede depender de un dato.
Esos datos los llamamos CONTEXTOS EXTENDIDOS de la máquina de estados.
En ocasiones algunas transiciones pueden alterar el contexto extendido de la máquina de estados, sus datos : ACCIONES
Eso se representa también en medio de la flecha de transición. Lo que hacemos es anteponer una BARRA / a la acción.

En esos textos que pongo en medio de las flechas, UML no se mete... más allá de estas cuestiones.
Hay 2 tendencias claras:
- Usar lenguaje humano
- Usar un pseudo-lenguaje de programación

Decidiré uno u otro en base al interlocutor al que vaya dirigido el diagrama.


```mermaid
stateDiagram-v2
    direction LR
    state Encendida {

        state Limpieza {
            state condicion <<choice>>
            state "Limpieza rápida" as rapida
            state "Limpieza exhaustiva" as exhaustiva

            [*]         --> condicion
            condicion   --> rapida: [numero_cafes % 50 != 0 && <br> NOW - ult_exhaustiva <= 1]
            condicion   --> exhaustiva: [numero_cafes % 50 == 0 || <br> NOW - ult_exhaustiva > 1]
            rapida      --> [*]
            exhaustiva  --> [*]: / ul_exhaustiva = NOW
        }

        state "En reposo" as reposo
        state "Preparando cafe" as cafe {

            state inicio_paralelo <<fork>>
            state fin_paralelo <<join>>

            state "Calentando agua" as calentando
            state "Moliendo cafe" as moliendo
            state "Sirviendo cafe" as sirviendo

            [*]         --> inicio_paralelo
            inicio_paralelo --> calentando
            inicio_paralelo --> moliendo
            calentando --> fin_paralelo
            moliendo --> fin_paralelo
            fin_paralelo --> sirviendo
            sirviendo --> [*]

        }
        
        [*]         --> reposo
        reposo      --> cafe: SOLICITAR_CAFE
        cafe        --> Limpieza: / numero_cafes++
        Limpieza    --> reposo
        reposo      --> [*] : APAGAR_MAQUINA
    }

    Apagada     --> Encendida: ENCENDER_MAQUINA
    Encendida   --> Apagada
```
