# Comunicaciones

En los sistemas podemos tener comunicaciones SINCRONAS o ASINCRONAS.

De hecho, los humanos también tenemos entre nosotros comunicaciones sincronas y asincronas.

Si llamo a mi madre por teléfono, estoy estableciendo una comunicación sincrona. Yo mando un mensaje y me quedo a la espera de respuesta (sin hacer nada mientras tanto).

Si por el contrario mando un whatsapp a mi madre, estoy estableciendo una comunicación asíncrona. Yo mando un mensaje y sigo con mi vida, sin esperar respuesta inmediata. Ella ya contestará cuando pueda.

El hecho de usar comunicaciones sincronas o asíncronas muchas veces viene determinado por el propio problema que tengo que resolver (REQUISITOS DE PARTIDA FUNCIONALES)

> Ejemplo 1. MERCADONA

Voy a Mercadona y hago mi compra... y quiero pagar.
Para ello, en el mercadona tienen un TPV (Terminal Punto de Venta) que es un ordenador, con un programa que se encarga de leer mi tarjeta, pedirme el pin, y solicitar al banco (la pasarela de pagos del banco) que haga la transacción.

PREGUNTA: Tengo una comunicación entre: 
    - El Programa instalado en el TPV de Mercadona
    - La Pasarela de Pagos del Banco
¿Esa comunicación la quiero sincrona o asíncrona? SINCRONA

El TPV espera la respuesta del banco, que puede ser:
- SI: Me voy a casa con la compra
- NO: No me voy a casa con la compra, yo me voy a casa, pero la compra se queda en el supermercado.
- PUEDE NO CONTESTAR o decir que tiene problema: Yo me voy, pero me quedo sin la compra.

> Ejemplo 2. PEAJE

Entro a un peaje en la carretera y al salir no quiero pagar, pero tengo que pagar.
Para ellos, en el peaje tienen un TPV (Terminal Punto de Venta) que es un ordenador, con un programa que se encarga de leer mi tarjeta, pedirme el pin... etc.

PREGUNTA: Esa comunicación es síncrona o asíncrona? ASINCRONA! Y DEBE SERLO, no hay alternativa

El TPV espera respuesta... que puede ser:
- SI: Abre la barrera y me voy
- NO: No abre la barrera y se acercan amablemente a pedirme los billetes en mano, ponerme una receta!
- PUEDE NO CONTESTAR o decir que tiene problema: La barrera se TIENE QUE ABRIR, no hay alternativa
- De no hacerlo están cometiendo un delito

Por eso los peajes no admiten tarjetas prepago, por que el cargo no lo hacen al momento.
Y no tratan de hacer el cargo al momento. Solo anotan que el cargo debe realizarse... Ya se realizará.

Como decía en ocasiones los requisitos me obligan a optar por comunicaciones síncronas o asíncronas.
Hay casos especiales... donde por ejemplo para establecer una comunicación SINCRONA, voy a usar un mecanismo ASINCRONO.

Una gracia grande de las comunicaciones ASINCRONAS es que suelen establecerse mediante lo que llamamos un SISTEMA DE MENSAJERIA!
    Informática:    Kafka, RabbitMQ, ActiveMQ, ZeroMQ
    Humanos:        Whatsapp, Telegram, 

    Esos sistemas actúan de garantes del envío del mensaje, y de la entrega del mensaje.

       IVAN -----> LLAMADA POR TELEFONO A SU MADRE ----> MADRE
                    ¿Qué tienes hoy de comer?
            
            Si mi madre no contesta... que hago yo? Necesito esa respuesta!
            Llamo otra vez! y otra.. y otra! hasta que lo coja!
        
        IVAN ---> WHATSAPP A   ----> Servidor de Whatsapp ----> MADRE
                    ¿Qué tienes hoy de comer?
            Si mi madre no contest... que hago yo? Necesito esa respuesta!
        Ya no mando otra vez el mensaje... el servidor de whatsapp se encarga de entregarlo cuando esté disponible. 

    Esto último tiene muchas ventajas, especialmente en el mundo de la informática:
    1. Yo me quedo libre... ya mandé el mensaje... no tengo que estar mandando el mensaje una y otra vez
    2. Y MAS IMPORTANTE: No estreso al destinatario... Si está sobrecargado, no quiero sobrecargarle más... Más tardará!