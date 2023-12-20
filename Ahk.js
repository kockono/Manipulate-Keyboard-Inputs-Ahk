// const readline = require('readline');

// const rl = readline.createInterface({
//   input: process.stdin,
//   output: process.stdout
// });

// let keyBuffer = '';

// // Registrando el evento 'keypress' directamente en stdin
// process.stdin.on('keypress', (str, key) => {
//   console.log( `Buffer: ${key}` )
  
//   if (key) {
//     // Concatenar tanto el carácter como el nombre de la tecla al buffer
//     keyBuffer += key.name || str;
//     console.log( `${keyBuffer}` )

//     // Verificar si la combinación "h6" está presente en el buffer
//     if (keyBuffer.includes('h6')) {
//       console.log('######');
//       keyBuffer = ''; // Limpiar el buffer después de imprimir
//     }
//   }
// });

// // Habilitar eventos 'keypress' en stdin
// rl.input.on('keypress', (_, key) => {
//   if (key && key.name === 'escape') {
//     // Limpiar y salir con 'esc'
//     rl.close();
//     console.log('Programa detenido.');
//   }
// });

// // Iniciar la escucha de eventos 'keypress'
// rl.input.setRawMode(true);
// rl.input.resume();

// console.log('El programa está escuchando. Presiona \'esc\' para salir.');
// h6 

// Type "Hello World" then press enter.
var robot = require("robotjs");

// Speed up the mouse.
setTimeout(() => {
  // Type "Hello World".
  robot.typeString("Hello World");
  console.log('Hello World')
  // Press enter.
  robot.keyTap("enter");
}, 5000);

