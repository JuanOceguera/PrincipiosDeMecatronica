void setup()
{
  DDRB = DDRB | B10000000;// Data Direction Register B: Inputs 0-6, Output 7
}

void loop()
{
  asm(
    "inicio: \n\t"
    "LDI r16, 45\n\t"
    "LDI r17, 255\n\t"
    "IN r25, 0x03\n\t"
    "sbrs r25, 0x06 \n\t" //checa si el boton es presionado para cambiar a la otra rutina
    "call botonPres \n\t" //si el boton es presionado llama a esta subrutina, si no se salta esta linea
    "sbi 0x05,0x07 \n\t" //Pone en 1 el bit 0x07 del registro I/O 0x05 (es el PortB)
    "call tiempo \n\t" // Llama a la rutina tiempo y vuelve cuando hay un ret
    "cbi 0x05,0x07 \n\t" //Pone en 0 el bit 0x07 del registro I/O 0x05 (es el PortB)
    "call tiempo \n\t" //Llama a la rutina tiempo y vuelve cuando hay un ret
    "jmp main \n\t" // Salta a la etiqueta main (el principio)
    "tiempo: \n\t" //Rutina tiempo
    "LDS r22, 16 \n\t" //Carga en el registro 22 el valor de la memoria 16
    "LOOP_3: \n\t" //Empiezael tercer loop
    "LDS r21, 17 \n\t" //Carga en el registro 21 el valor de la memoria 17
    "LOOP_2: \n\t" //Empieza el loop 2
    "LDS r20, 17 \n\t" //Carga en el registro 20 el valor de la memoria 17
    "LOOP_1: \n\t" //Empieza el loop 1
    "DEC r20 \n\t" //Las siguientes 2 lineas decrementan el registro 20 hasta que llega a 0
    "BRNE LOOP_1 \n\t" //Cuando llega a 0 el registro 20 pasa a la siguiente instrucción
    "DEC r21 \n\t" //Las siguientes 2 lineas decrementan el registro 21 hasta que llega a 0
    "BRNE LOOP_2 \n\t" //Cuando llega a 0 el registro 21 pasa a la siguiente instrucción
    "DEC r22 \n\t" //Las siguientes 2 lineas decrementan el registro 22 hasta que llega a 0
    "BRNE LOOP_3 \n\t" //Cuando llega a 0 el registro 22 pasa a la siguiente instrucción
    "ret \n\t" //Regresa al último call llamado
    "botonPres: \n\t"
    "LDI r16, 113\n\t"
    "LDI r17, 114\n\t"
    "ret \n\t"
  );
}
