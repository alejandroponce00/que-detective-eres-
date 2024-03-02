print("bienvenido al cuestionario:Cual superdetective eres?")
print("contesta las siguientes preguntas")
# Pregunta al candidato una pregunta
actividad = input("¿Cómo te gustaría pasar tu noche?\n(A) Leyendo un libro\n(B) Asistiendo a una fiesta\n")
if actividad == "A":
    print("¡Leer un libro, excelente elección!")
elif actividad == "B":
    print("¿Asistir a una fiesta? ¡Suena divertido!")
else:
    print("Debes escribir A o B, digamos simplemente que te gusta leer.")
    actividad = "A"

# Pregunta al candidato una segunda pregunta
trabajo = input("¿Cuál es tu trabajo soñado?\n(A) Curador en el Smithsonian\n(B) Dirigir un negocio\n")
if trabajo == "A":
    print("¡Curador, excelente elección!")
elif trabajo =="B":
    print("¿Dirigir un negocio? ¡Suena divertido!")
else:
    print("Debes escribir A o B, digamos simplemente que quieres ser curador en el Smithsonian.")
    trabajo = "A"

# Pregunta al candidato una tercera pregunta
valor = input("¿Qué es más importante?\n(A) Dinero\n(B) Amor\n")
if valor == "A":
    print("¡Dinero, excelente elección!")
elif valor =="B":
    print("¿Amor? ¡Suena divertido!")
else:
    print("Debes escribir A o B, digamos simplemente que el dinero es más importante para ti.")
    valor = "A"

# Pregunta al candidato una cuarta pregunta
década = input("¿Cuál es tu década favorita?\n(A) 1910\n(B) 2010\n")
if década == "A":
    print("¡1910, excelente elección!")
elif década =="B":
    print("¿2010? ¡Suena divertido!")
else:
    print("Debes escribir A o B, digamos simplemente que la década de 1910 es tu favorita.")
    década = "A"

# Pregunta al candidato una quinta pregunta
viaje = input("¿Cuál es tu forma favorita de viajar?\n(A) Manejando\n(B) Volando\n")
if viaje == "A":
    print("¡Manejar, excelente elección!")
elif viaje =="B":
    print("¿Volando? ¡Suena divertido!")
else:
    print("Debes escribir A o B, digamos simplemente que tu forma favorita de viajar es manejando.")
    viaje = "A"

# Imprime sus elecciones
print(f"Elegiste {actividad}, luego {trabajo}, luego {valor}, luego {década}, luego {viaje}.")

# Crea algunas variables para puntuación
sam_like = 0
cam_like = 0
kai_like = 0
indy_like = 0

# Actualiza las variables de puntuación según la elección de actividad
if actividad == "A":
    sam_like += 2
    indy_like += 2
    kai_like += 2
else:
    cam_like += 1
    indy_like += 1

# Actualiza las variables de puntuación según la elección de trabajo
if trabajo == "A":
    sam_like += 2
    indy_like += 2
    cam_like -= 1
else:
    sam_like -= 1
    kai_like += 2
    indy_like += 1

# Actualiza las variables de puntuación según la elección de valor
if valor == "A":
    sam_like -= 1
    kai_like += 1
else:
    sam_like += 2
    cam_like += 2
    indy_like += 1

# Actualiza las variables de puntuación según la elección de década
if década == "A":
    cam_like += 2
    sam_like += 2
else:
    kai_like += 1
    indy_like += 2

# Actualiza las variables de puntuación según la elección de viaje
if viaje == "A":
    sam_like -= 2
    kai_like += 1
    indy_like -= 1
else:
    sam_like += 1
    cam_like += 1
    kai_like -= 1

# Imprime los resultados dependiendo de la puntuación
if sam_like >= 3:
    print("¡Eres más como Sam de Ojo Agudo!")
elif cam_like >= 3:
    print("¡Eres más como Cam el Curioso!")
elif kai_like >= 3:
    print("¡Eres más como Kai el Perspicaz!")
else:
    print("¡Eres más como Indy el Inquisitivo!")
