import keyboard

def on_key_event(e):
    if e.event_type == keyboard.KEY_DOWN:
        # Concatenar la tecla presionada al buffer
        global key_buffer
        key_buffer += e.name

        # Verificar si la combinación "h6" está presente en el buffer
        if "h6" in key_buffer:
            keyboard.write('######')
            key_buffer = ""  # Limpiar el buffer después de imprimir
            # exit()

# Configurar la función de manejo de eventos para cualquier tecla
keyboard.hook(on_key_event)

# Mantener el programa en ejecución
try:
    print("El programa está escuchando. Presiona 'esc' para salir.")
    keyboard.wait('shift + esc')
except KeyboardInterrupt:
    pass
finally:
    # Limpiar y detener la escucha del teclado
    keyboard.unhook_all()
    print("Programa detenido.")
