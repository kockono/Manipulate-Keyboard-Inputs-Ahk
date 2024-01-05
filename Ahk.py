from pynput import keyboard # Para escuchar las teclas presionadas
import threading # Para crear un hilo que ejecute una función cada cierto tiempo
import re # Para usar expresiones regulares
from keys_dict import keys # Importa el diccionario de teclas

# Crea una instancia del controlador de teclado
keyboard_controller = keyboard.Controller()

# Variables
key_buffer = ""

def on_press(key):
    global key_buffer
    try:
      if key.char is not None: # Si es un caracter agregalo al buffer
        key_buffer += key.char
        check_keys(key_buffer)
    except AttributeError:
        print('special key {0} pressed'.format(key))
        reset_key_buffer()
    else:
        print('alphanumeric key {0} pressed'.format(key))
        #code to run if no error is raised

def check_keys(key_buffer_final):
    for key, value in keys.items():
        if key_buffer_final.endswith(key):
            extracted_key = re.search(rf'{key}$', key_buffer_final).group()
            delete_characters(extracted_key)
            type_characters(extracted_key)
            reset_key_buffer()

def type_characters(key_buffer_final):
    text_to_type = keys[key_buffer_final]
    for char in text_to_type:
        keyboard_controller.press(char)
        keyboard_controller.release(char)
        if char.isspace():
           keyboard_controller.press(keyboard.Key.space)
    reset_key_buffer_with_delay()

def delete_characters(key_buffer_final):
      for i in key_buffer_final:
        keyboard_controller.press(keyboard.Key.backspace)

def reset_key_buffer():
    global key_buffer
    key_buffer = ""

def reset_key_buffer_with_delay():
    # Reiniciar el key_buffer después de 0.5 segundos
    threading.Timer(0.5, reset_key_buffer).start()

# Metodo para salir del programa
def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.f10:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

# def on_activate_z():
#     keyboard.Controller.type('>')

# def on_activate_i():
#     keyboard.Controller.type('<')

# with keyboard.GlobalHotKeys({
#         '<shift>+z': on_activate_z,
#         '<alt>+z': on_activate_i}) as h:
#     h.join()