# Practica-1-
# Impresora braille de bajo costo

## Descripción
Prototipo que convierte texto digital en braille usando un microcontrolador,
motores a pasos y un solenoide que marca los puntos en el papel.

## Hipótesis
Si se construye una impresora braille con un microcontrolador, motores a
pasos y un solenoide, entonces imprimirá texto legible con una precisión
mayor al 90 % y a un costo menor que una impresora comercial, porque cada
letra es una combinación fija de seis puntos controlable por programación.

## Materiales
Arduino/ESP32, 2 motores a pasos con drivers, solenoide, estructura con
guías, fuente de alimentación y papel grueso.

## Pruebas
Se imprimieron 5 frases (125 caracteres) y una persona leyó el resultado.

## Resultados
- Caracteres correctos: 117 de 125 (**93.6 %**).
- El texto fue legible en las 5 frases.
- Los errores se debieron a poca fuerza del solenoide en papel grueso.

## Conclusión
La hipótesis se cumplió: la precisión superó el 90 % y el costo fue menor
al de una impresora comercial.

## Autor
Fatima Anel Martinez Montero
