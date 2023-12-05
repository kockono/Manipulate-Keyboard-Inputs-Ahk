// Type "Hello World" then press enter.
var robot = require("robotjs");

// Type "Hello World".
robot.typeString("Hello World");

// Press enter.
robot.keyTap("enter");
console.log( "Hello World" );



// const robot = require('robotjs');

// // Inicializar robotjs
// robot.setKeyboardDelay(10);

// // Escuchar eventos de teclado
// const listener = require('keypress');
// listener(process.stdin);

// let keyBuffer = '';

// process.stdin.on('keypress', (ch, key) => {
//   if (key) {
//     // Concatenar la tecla presionada al buffer
//     keyBuffer += key.name;

//     if(keyBuffer.includes('h1')) {
//       console.log("¡Se presionó 'h1'! Escribiendo 'Hola Mundo'");
//       robot.typeString('Hola Mundo');
//       keyBuffer = '';  // Limpiar el buffer después de escribir
//     }

//     // Verificar si la combinación "Shift + Esc" está presente en el buffer
//     if (keyBuffer.includes('shift') && key.name === 'escape') {
//       // Acciones cuando se presiona 'Shift + Esc'
//       console.log("¡Se presionó 'Shift + Esc'! Escribiendo 'Hola Mundo'");
//       robot.typeString('Hola Mundo');
//       keyBuffer = '';  // Limpiar el buffer después de escribir
//     }
//   }
// });

// // Iniciar la escucha de teclado
// process.stdin.setRawMode(true);
// process.stdin.resume();

// // Mantener el programa en ejecución
// console.log("El programa está escuchando. Escribe 'Shift + Esc' para escribir 'Hola Mundo'.");
// process.stdin.on('end', () => {
//   console.log("Programa detenido.");
//   process.exit();
// });
