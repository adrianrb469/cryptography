import os
import numpy as numpy
from PIL import Image, ImageDraw
import piexif
import pyzipper

# Definir las imágenes "poneglyphs"
poneglyphs = {
    "luffy": "resources/poneglyphs/luffy.jpeg",
    "zoro": "resources/poneglyphs/zoro.jpeg",
    "usopp": "resources/poneglyphs/usopp.jpeg",
    "sanji": "resources/poneglyphs/sanji.jpeg",
    "nami": "resources/poneglyphs/nami.jpeg",
    "robin": "resources/poneglyphs/robin.jpeg",
}

# Función para crear un ZIP con contraseña en Windows
def zip_with_password(zip_path, file_path, password):
    with pyzipper.AESZipFile(zip_path, 'w', compression=pyzipper.ZIP_LZMA, encryption=pyzipper.WZ_AES) as zf:
        zf.setpassword(password.encode())
        zf.write(file_path, os.path.basename(file_path))


# Función para crear imágenes "poneglyph"
def create_poneglyph_image(text, challenge, password, location):
    # Abrir la imagen de la lista de "poneglyphs"
    img = Image.open(poneglyphs[challenge])
    d = ImageDraw.Draw(img)

    # Agregar texto visible en la imagen
    d.text((10, 10), text, fill=(255, 255, 0))

    # Verificar si la imagen tiene EXIF
    exif_data = img.info.get("exif")

    if exif_data:
        exif_dict = piexif.load(exif_data)
    else:
        # Si no hay EXIF, inicializamos un diccionario vacío
        exif_dict = piexif.load(piexif.dump({}))

    # Agregar el texto como metadato EXIF (campo Artist o UserComment)
    exif_dict["0th"][piexif.ImageIFD.Artist] = text.encode(
        "utf-8"
    )  # Usando 'Artist' para almacenar el texto

    # Convertir los metadatos a formato EXIF
    exif_bytes = piexif.dump(exif_dict)

    # Guardar la imagen con el texto visible y los metadatos# Guardar la imagen con el texto visible y los metadatos
    image_path = f"challenges/{challenge}/poneglyph.jpeg"
    img.save(image_path, exif=exif_bytes)
    # Guardar un zip de la imagen con password
     
    # validar si el Os es Windows
    if os.name == 'nt':
        print('Windows', os.name)
        zip_with_password(f"{location}/poneglyph.zip", image_path, password)
        os.remove(image_path)
    else:
        print('Linux', os.name)
        # Crear un archivo ZIP con contraseña
        os.system(f"zip -P {password} -r {location}/poneglyph.zip {image_path}")
        # Eliminar la imagen original
        os.system(f"rm {image_path}")
