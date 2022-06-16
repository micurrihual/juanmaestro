import os

run = list(); nombre = list(); edad = list(); nota = list()

alumno = [run, nombre, edad, nota]

while True:

  os.system ("cls")
  print ("Menu Principal \n")

  print ("1. Agregar")
  print ("2. Consultar por Run")
  print ("3. Mostrar todos")
  print ("4. Salir \n")

  op = input ("Ingrese Opción: ")

  if op == "1":
    while True:
      try:
        xrun = input ("Ingrese run: ")
        xnombre = input ("Ingrese nombre: ")
        xedad = int (input("Ingrese edad: "))
        xnota = float (input ("Ingrese nota: "))
        
        if xrun.isnumeric() and len (xrun) == 2:
          if len(xnombre) >= 3 and len (xnombre) <= 100:
            if xedad >= 1 and xedad <= 130:
              if xnota >= 1.0 and xnota <= 7.0:
                break;
        input ("Algún dato no cumple con lo solicitado...")
      
      except Exception as e:

        print ("Algún dato es incorrecto...:", e)
        input ("Pulse una tecla")
  
    #Fuera del ciclo agrega datos a la lista

    run.append(xrun); nombre.append(xnombre); edad.append(xedad); nota.append(xnota)

    input ("Dato ingresa correctamente...pulse una tecla para continuar...")
  
  elif op=="2":
      try:

        xrun = input ("Ingre Run: ")
        i = run.index(xrun)

        print (f"{alumno[0][i]} {alumno[1][i]} {alumno[2][i]} {alumno[3][i]}")
        input ("Pulse una tecla para continuar...")
      
      except:

        input ("Run no existe en la lista")
  
  elif op == "3":

    n = len(nota)
    
    print ("LISTA DE ALUMNOS \n *****************************")

    for i in range(n):

      print (f"{alumno[0][i]} {alumno[1][i]} {alumno[2][i]} {alumno[3][i]}")

      input ("Pulse una tecla para continuar...")
    
  elif op == "4":

     break
  
  else:

    input ("Opcion no valida...pulse para continuar")