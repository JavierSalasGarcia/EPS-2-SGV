# Conversor EPS a SVG

Este script de Python convierte archivos en formato EPS (Encapsulated PostScript) a formato SVG (Scalable Vector Graphics) utilizando la biblioteca `cairosvg`.

## Requisitos previos

- Python 3.6 o superior
- pip (gestor de paquetes de Python)

## Instalación

1. Clona este repositorio o descarga el script `eps_to_svg.py`.

2. Instala las dependencias necesarias usando pip:

   ```
   pip install cairosvg
   ```

## Uso

Para convertir un archivo EPS a SVG, ejecuta el script desde la línea de comandos de la siguiente manera:

```
python eps_to_svg.py archivo_entrada.eps archivo_salida.svg
```

Reemplaza `archivo_entrada.eps` con la ruta a tu archivo EPS y `archivo_salida.svg` con la ruta deseada para el archivo SVG resultante.

## Ejemplo

```
python eps_to_svg.py mi_imagen.eps mi_imagen_convertida.svg
```

## Notas

- Asegúrate de que tienes permisos de escritura en el directorio donde deseas guardar el archivo SVG de salida.
- Si encuentras algún error, verifica que el archivo EPS de entrada sea válido y que la biblioteca `cairosvg` esté correctamente instalada.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir cambios mayores antes de enviar un pull request.
