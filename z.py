from pynput import keyboard
# from pynput.keyboard import Key, Controller

# Crea una instancia del controlador de teclado
keyboard_controller = keyboard.Controller()

# Variables
key_buffer = ""

# Diccionario de teclas
keys = {
    "h1": "##",
    "h2": "###",
    "h3": "####",
    "h4": "#####",
    "h5": "######",
    "h6": "#######"
}

def on_press(key):
    global key_buffer
    try:
        key_buffer += key.char
        # Checa que exista la propiedad en el diccionario
        
        print(keys[key_buffer])
        # check_keys(keys[key_buffer])
        keyboard_controller.type('##')
    except AttributeError:
        key_buffer = ""
        print('special key {0} pressed'.format(key))


def check_keys(key):
    global key_buffer
    if key == "h1":
      for i in key_buffer:
        keyboard_controller.press(keyboard.Key.backspace)
    key_buffer = ""



# def reset_key_buffer_after_delay():
#     global key_buffer
#     threading.Timer(1.0, reset_key_buffer).start() 

def reset_key_buffer():
    key_buffer = ""
    print(key_buffer)

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
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
