from pynput import keyboard
import threading
# from pynput.keyboard import Key, Controller

# Crea una instancia del controlador de teclado
keyboard_controller = keyboard.Controller()

# Variables
key_buffer = ""

# Diccionario de teclas
keys = {
    "h1": "#",
    "h2": "##",
    "h3": "###",
    "h4": "####",
    "h5": "#####",
    "h6": "######",
    "zx": "<",
    "xz": ">",
    "azael": "Dungeonerig \u00A0 Master"
}

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
    print(key_buffer_final)
    initial_letter, suffix = extract_suffix(key_buffer_final)
    if initial_letter is not None and suffix is not None:
        combined_key = initial_letter + suffix
        if combined_key in keys:
            delete_characters(key_buffer_final)
            type_characters(key_buffer_final)
            reset_key_buffer()

def extract_suffix(key_buffer):
    # Encuentra la primera letra en el buffer
    first_letter_index = next((i for i, c in enumerate(key_buffer) if c.isalpha()), None)
    
    if first_letter_index is not None:
        # Extrae la letra inicial y el sufijo numérico
        initial_letter = key_buffer[first_letter_index]
        suffix = key_buffer[first_letter_index + 1:]

        return initial_letter, suffix

    return None, None

def type_characters(key_buffer_final):
    keyboard_controller.type(keys[key_buffer_final])
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
