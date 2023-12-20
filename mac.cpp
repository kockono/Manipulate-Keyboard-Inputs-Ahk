#include <cstdlib>
#include <termios.h>
#include <unistd.h>

char getch() {
    char buf = 0;
    struct termios old = {0};
    if (tcgetattr(0, &old) < 0)
        perror("tcsetattr()");
    old.c_lflag &= ~ICANON;
    old.c_lflag &= ~ECHO;
    old.c_cc[VMIN] = 1;
    old.c_cc[VTIME] = 0;
    if (tcsetattr(0, TCSANOW, &old) < 0)
        perror("tcsetattr ICANON");
    if (read(0, &buf, 1) < 0)
        perror("read()");
    old.c_lflag |= ICANON;
    old.c_lflag |= ECHO;
    if (tcsetattr(0, TCSADRAIN, &old) < 0)
        perror("tcsetattr ~ICANON");
    return (buf);
}

int main() {
    std::string keyBuffer;

    std::cout << "El programa está escuchando. Presiona 'esc' para salir." << std::endl;

    while (true) {
        char key = getch();

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

    return 0;
}