# Paradigmas de programación

Eso es un nombre un tanto hortera que en el mundo del desarrollo le damos a la forma de usar un lenguaje. En Español también lo tenemos!

- Imperativo            Cuando el lenguaje me permite ir expresando una secuencia de ORDENES 
                        que deben ejecutarse en un determinado orden.

                            print("ALGO");          // Statements / Declaración / Sentencia = Frase, Oración
                            input("DAME ALGO");     // Statements
                        En ocasiones queremos romper o alterar el orden (flujo) de operaciones (frases, sentencias) y 
                        hacemos uso de los operadores típicos de control de flujo presentes en los lenguajes imperativos:
                            FOR, WHILE, IF, CASE/SWITCH

                        Un programa podía tener 2000 / 3000 líneas.. o más! Y era un infierno de mantener y entender.

- Procedural            Cuando el lenguaje me permite agrupar frases (statements) en un concepto que denominamos:
                            Función, Método, Procedimiento, Subrutina 
                        Y posteriormente solicitar la ejecución de todas esas frases (statements) a través de esa agrupación (función, método, procedimiento, subrutina).

                        Esto surge más adelante, después de la programación imperativa, y tiene 2 ventajas grandes:
                        - Me aporte estructura (y mejor legibilidad) a mi código
                        - Me permite reutilizar código
                        Muchos lenguajes incluso permiten el escribir las funciones en diferentes archivos y luego importarlas. 

- Funcional             Una evolución de los lenguajes procedurales son los funcionales... esto es muy viejo.
                        Cuando el lenguaje me permite que una variable albergue/apunte a una función (metodo, procedimiento, subrutina) de forma que posteriormente pueda invocar (solicitar la ejecución) de esa función a través de la variable.
                        El tema con la programación funcional, no es lo que es... que es muy simple.
                        El tema es que una vez que el lenguaje me permite hacer eso, se abre un mundo de posibilidades, entre otras cosas:
                        - Podemos empezar a crear funciones que admiten funciones como argumentos (datos)
                        - Podemos empezar a crear funciones que devuelven funciones ejecutable

- Orientado a Objetos   La siguiente evolución fué la POO

                        Todo lenguaje maneja DATOS... los lenguajes ofrecen una serie de TIPOS DE DATOS por defecto. TODOS

                                    Se caracterizan por:                    Qué puedo hacer sobre ellos, por ser de un tipo concreto
                                    -------------------------------------   --------------------------------------------------------

                            Texto   Su secuencia concreta de caracteres     AMayusculas! AMinusculas! dimeTuLongitud acabasCon('ido')?

                            Fecha   - año                                   caesEnJueves?
                                    - mes                                   eseAñoEsBisiesto?
                                    - dia                                   restar2Fechas

                            Lista   Una secuencia de datos                  añadirItems, eliminarItems, ordenarItems, buscarItems
                        
                        Los lenguajes de programación OO, lo que me permiten es definir MIS PROPIOS TIPOS DE DATOS,
                        con sus propias características y operaciones.
                    
                            Usuario  - nombre                               saludar     login   enviarEmail
                                     - edad
                                     - email
                                     - ...

                        Esto me ayuda a:
                        - Estructurar aún más mi código
                        - Reutilizar aún más mi código

                        A los nuevos TIPOS DE DATOS les denominamos CLASES.
                        Los datos que generamos de esos TIPOS DE DATOS los denominamos OBJETOS.

                        TEXTO es una Clase.. "hola" es un objeto de la clase TEXTO
                        33    es un objeto de la clase NUMERO. Número es una clase (un tipo de dato) 

- Declarativo           Esta es la evolución MAXIMA. Todas las herramientas y Frameworks que hoy en día triunfan lo hacen por usar paradigmas declarativos: Spring, .net Core, Angular, Terraform, Kubernetes, Ansible...
                        Este paradigma viene a reemplazar el lenguaje IMPERATIVO... que le hemos cogido mucha manía.
                        Odiamos hoy en día los lenguajes IMPERATIVOS.. el problema es que a veces estamos tan acostumbrados a ellos
                        que no damos cuenta lo perjudiciales que son.
                        Los lenguajes imperativos nos hacen olvidar nuestro objetivo, centrándonos en el CÓMO conseguir el objetivo.
                        Los lenguajes declarativos nos permiten centrarnos en nuestro objetivo, y delegar el CÓMO conseguir el objetivo.

make directory -> mkdir
change directory -> cd

# Programación Imperativa

> Felipe: IF hay algo que no sea una silla debajo de la ventana, THEN:
    >Felipe, lo quitas                               Imperativo
> Felipe: IF(Si) no hay ya una silla debajo de la ventana, ENTONCES:
    > Felipe, IF (silla == FALSE) THEN:
        > Vete al ikea y compra una silla.           Imperativo
    > Felipe, pon una silla debajo de la ventana!    Imperativo

Felipe: debajo de la ventana debe haber una silla     Declarativo 
Le digo a Felipe lo que quiero... y DELEGO en él la responsabilidad de conseguirlo.

# Programación Orientada a Objetos