#include <iostream>
#include <conio.h>

int main() {
    std::string keyBuffer;

    std::cout << "El programa está escuchando. Presiona 'esc' para salir." << std::endl;

    while (true) {
        if (_kbhit()) {
            char key = _getch();

            // Concatenar la tecla presionada al buffer
            keyBuffer += key;

            // Verificar si la combinación "h6" está presente en el buffer
            if (keyBuffer.find("h6") != std::string::npos) {
                std::cout << "######";
                keyBuffer.clear(); // Limpiar el buffer después de imprimir
            }

            // Salir si se presiona 'esc'
            if (key == 27) {
                std::cout << "Programa detenido." << std::endl;
                break;
            }
        }
    }

    return 0;
}
