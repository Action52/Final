Proyecto final Gráficas computacionales
Semestre Agosto - Diciembre 2016

Crear una escena 3D usando WebGL y three.js donde el usuario controle un auto con partes móviles
La escena debe contener un parque de diversiones y una construcción interesante


El auto debe poder:

        04 avanzar                 (en la dirección a la que apuntan las ruedas)                      <T> 84
        04 retroceder              (en la dirección a la que apuntan las ruedas)                      <G> 71
        las llantas deben rotar
        04 rotar ruedas a la derecha      las llantas delanteras deben rotar como en un auto real     <H> 72
        04 rotar ruedas a la izquierda    las llantas delanteras deben rotar como en un auto real     <F> 70
        04 abrir las puertas delanteras                                                               <U> 85
        04 cerrar las puertas delanteras                                                              <J> 74
        04 abrir el cofre                                                                             <Y> 89
        04 cerrar el cofre                                                                            <R> 82
        04 abrir la cajuela                                                                           <V> 86
        04 cerrar la cajuela                                                                          <B> 66
        10 mostrar diferentes materiales(metal, plastico, vidrios), y tener una estructura bien definida

    IMPORTANTE: NO CAMBIAR LOS CONTROLES

El parque de diversiones debe tener atracciones en movimiento:

    una rueda de la fortuna
        crear las sillas/canastas, la estructura, deben girar
        las sillas deben "obedecer a la gravedad"
        mínimo 16 sillitas (sugerencias .clone())
    un carrusel
        más simple, solo rota, mínimo 16 caballitos
        deben girar y además deben suir y bajar
        (si no, no es divertido)
    otra atracción rotatoria
        pueden ser sillas voladoras, tazas locas, etc.
        mínimo 16 "plazas"

Todas las atracciones deben tener materiales y/o texturas  - 25

(ejemplos de la construcción Interesante: el estadio azteca, el castillo de Disney, S.T.A.R. labs, la torre STARK,nuestro campus, propuestas ) - 25 

La construcción debe tener :

    estructuras computacionales que generen los cuerpos
    al menos 3 geometrías definidas en three.js (no primitivas)
    materiales y texturas
       
ES INDISPENSABLE QUE EL CONTROL DE LA CAMARA FUNCIONE AL 100 % usando flechas de direccion y WASD

    avanzar (en la dirección a la que apunta la camara)     <Flecha Arriba>
    retroceder (en la dirección a la que apunta la camara)  <Flecha abajo>
    rotar camara a la izquierda                             <Flecha Izquierda>
    rotar camara a la derecha                               <Flecha Derecha>
    Subir posición de cámara en y                           <W>
    Bajar posición de cámara en y                           <S>
    Desplazar a la izquierda la cámara                      <A>
    Desplazar a la derecha la cámara                        <D>


Si esto NO funciona correctamente -> 40 directo (o menos)

Se deben incluir luces y sombras en la escena

Cómo entregar el proyecto ?

    En un sobre amarillo con hilo rojo:
        un CD / DVD / pendrive con el proyecto
            carpeta HTML con archivo index.html, three.min.js, todas las imagenes en un folder img
            carpeta Screeenshot con 2 imagenes jpg de impresiones de pantalla (diferentes) de la escena
            carpeta doc
                Documento PDF que contenga una explicación completa y todos los detalles de la implementación
                    incluyendo hoja de presentación y todo el código como Apendice del documento usando un font monospace
        una impresión a color de "la mejor vista de sus escena"

    un ZIP con todo el conteniodo del CD / DVD / pendrive

Límite de entrega: Antes de Examen FINAL

    Martes 29 de Noviembre, 12:30 hrs
        aula 2404 antes del examen final
    Tanto el sobre amarillo antes de iniciar el examen FINAL como el ZIP en BlackBoard


Pueden trabajar en Parejas
