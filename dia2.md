
# Diagramas de secuencia

Y voy a tratar de explicar las interacciones (comunicaciones) que tiene lugar cuando una persona se presentar en un cajero y quiere sacar dinero.

En estos diagramas representamos otros a conceptos distintos a los que representamos en los diagramas de casos de uso:

- Actores: Siguen apareciendo, de la misma forma que en los diagramas de casos de uso.
- Participantes: Siguen apareciendo, de la misma forma que en los diagramas de casos de uso.
Pero... ambos 2 se representan en la misma linea horizontal. Y esa linea horizontal se pone por duplicado, donde cada actor/participante se une consigo mismo mediante lineas discontinuas verticales:
- Comunicaciones: Flechas que indican la comunicación entre actores/participantes. Las flechas se ponen entre las lineas verticales. El orden de las flechas (de arriba a abajo) indica el orden de las comunicaciones.
  - Flechas solidas con cabeza rellena      = Comunicaciones síncronas 
  - Flechas discontinuas con cabeza rellena = Respuestas a comunicaciones síncronas

---

El siguiente paso natural, cuando ya tengo definidos los casos de uso -> requisitos (en UML no hay diagramas de requisitos) es empezar a bajar el nivel en el análisis/modelización de mi sistema.
A la hora de trabajar, normalmente elegimos lo que llamamos el HAPPY PATH (el camino feliz).

Vamos a plantear un caso de uso... pensando en que todo va a ir ESTUPENDAMENTE BIEN. Y vamos a ver cómo se comunican los actores/participantes en ese caso de uso.

Empezaremos sin entrar en mucho detalle. Al fin y al cabo estos diagramas iniciales los usamos para comunicarnos con el "cliente".
Más adelante, cuando quiera comunicarme con mi equipo de desarrollo, necesitaré entrar en más nivel de detalle.

Para crear estos diagramas, y dado que PowerPoint es insufrible! vamos a usar un lenguaje llamado mermaid. Ese lenguaje igual que plantUML nos permite ESCRIBIR diagramas, que posteriormente algunas herramientas nos permitirán renderizar gráficamente, convertir en un diagrama visual.

Una de las herramientas que nosotros vamos a usar en la formación se llama: Visual Studio Code.