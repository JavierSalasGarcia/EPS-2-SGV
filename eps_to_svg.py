import sys
import cairosvg

def eps_to_svg(eps_file, svg_file):
    try:
        cairosvg.svg2svg(url=eps_file, write_to=svg_file)
        print(f"Conversión exitosa. El archivo SVG se ha guardado como {svg_file}")
    except Exception as e:
        print(f"Error durante la conversión: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python eps_to_svg.py archivo_entrada.eps archivo_salida.svg")
        sys.exit(1)

    eps_file = sys.argv[1]
    svg_file = sys.argv[2]

    eps_to_svg(eps_file, svg_file)