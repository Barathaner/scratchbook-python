from PIL import Image

def reduce_image_size(input_image_path, output_image_path, max_size=(800, 800), quality=85):
    """
    Verkleinert das Bild auf die angegebene maximale Größe, während die Qualität beibehalten wird.

    :param input_image_path: Pfad zum Eingabebild
    :param output_image_path: Pfad zum Ausgabebild
    :param max_size: Maximale Größe (Breite, Höhe) in Pixeln
    :param quality: Qualitätsstufe (1-100) für die Komprimierung des Bildes
    """
    with Image.open(input_image_path) as img:
        # Verkleinere das Bild, ohne das Seitenverhältnis zu ändern
        img.thumbnail(max_size)
        
        # Speichere das Bild mit der angegebenen Qualität
        img.save(output_image_path, quality=quality)
        print(f"Bildgröße erfolgreich reduziert und gespeichert unter {output_image_path}")

# Beispielaufruf
input_image_path = './IMG_20241002_225348 (3).jpg'
output_image_path = './reduced_image.jpg'

reduce_image_size(input_image_path, output_image_path, max_size=(800, 800), quality=85)
