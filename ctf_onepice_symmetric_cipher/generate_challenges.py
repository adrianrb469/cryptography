import os
import random
import numpy as numpy
import hashlib
import shutil
from resources.poneglyph_content import get_texts
from resources.create_poneglyph_image import create_poneglyph_image
from resources.random_folders import main as random_folders
from resources.create_docker_file import create_docker_file
from utils.luffy_xor import xor_cipher
from utils.zoro_rc4 import generate_rc4
from utils.usopp_cipher import usopp_cipher
from utils.nami_chacha import nami_cipher


active_challenges = {
    "luffy": True,  # 1
    "zoro": True,  # 2
    "usopp": True,  # 3
    "nami": True,  # 4
    "sanji": False,  # 5
    "robin": False,  # 6
}
# Solicitar el carné del estudiante
student_id = input("Ingrese su carné: ")
random_number = random.randint(0, 5)


def create_directory(challenge, cipher_text, flag_password):
    # Directorio para el reto
    challenge_dir = f"challenges/{challenge}"

    # Crear directorio si no existe
    os.makedirs(challenge_dir, exist_ok=True)

    # Copiar el script de carpetas aleatorias
    ruta1, ruta2 = random_folders(challenge)
    print("Ruta1: ", ruta1)
    print("Ruta2: ", ruta2)
    return ruta1, ruta2


def create_flag_challange(challenge, flag_password):

    if challenge == "luffy":
        flag_xored = xor_cipher(flag_password, student_id)
        return flag_xored.hex()
    if challenge == "zoro":
        flag_cr4 = generate_rc4(flag_password, student_id)
        return flag_cr4.hex()
    if challenge == "usopp":
        flag_usopp = usopp_cipher(flag_password, 1234)
        return flag_usopp.hex()
    if challenge == "nami":
        flag_nami = nami_cipher(flag_password, student_id)
        return flag_nami.hex()
    else:
        return flag_password


def create_flag(challenge, flag_password, location):
    # Copiar el Dockerfile template
    create_docker_file(challenge, flag_password)

    # Guardar la flag
    flag_student_challenge = f"{student_id}_{challenge}_{random_number}"
    flag_hash = hashlib.md5(flag_student_challenge.encode()).hexdigest()
    flag = f"FLAG_{flag_hash}"
    print("flag location: ", location)
    # Cifrar flag con student_id
    with open(f"{location}/flag.txt", "w") as flag_file:
        challenge_flag = create_flag_challange(challenge, flag)
        flag_file.write(challenge_flag)

    return flag


# Función para generar los retos
def build_challenges():
    # remove old challenges directory
    # remove old challenges directory
    if os.path.exists("challenges"):
        print("Removing challenges directory")
        shutil.rmtree("challenges")
        os.system("rm -rf challenges")
    flag_password = "onepiece"

    texts = get_texts(random_number)
    # Generar las flags y cifrados
    for challenge, text in texts.items():
        # Verificar si el reto está activo
        if active_challenges[challenge] == False:
            continue

        # Cifrar el texto con el id del estudiante
        cipher_text = xor_cipher(text, student_id)
        location_flag, location_img = create_directory(
            challenge, cipher_text, flag_password
        )
        # Generar imagen "poneglyph"
        create_poneglyph_image(
            cipher_text.decode("utf-8"), challenge, flag_password, location_img
        )
        # Crear la flag
        flag_password = create_flag(challenge, flag_password, location_flag)

build_challenges()
print("Retos generados con éxito!")
