 # Función para contar las apariciones de una letra en un texto
def contar_letras(texto, letras):
  conteo = {}
  for letra in letras:
    conteo[letra] = 0
  for letra in texto.lower():
    if letra in conteo:
      conteo[letra] += 1
  return conteo

# Función para obtener la cantidad de palabras en un texto
def contar_palabras(texto):
  palabras = texto.split()
  return len(palabras)

# Función para obtener la primera y última letra de un texto
def obtener_primera_ultima_letra(texto):
  primera_letra = texto[0]
  ultima_letra = texto[-1]
  return primera_letra, ultima_letra

# Función para invertir el orden de las palabras en un texto
def invertir_orden_palabras(texto):
  palabras = texto.split()
  palabras.reverse()
  texto_invertido = " ".join(palabras)
  return texto_invertido

# Pedir al usuario que ingrese un texto
texto = input("Ingrese un texto: ")

# Pedir al usuario que ingrese tres letras
letras = input("Ingrese tres letras: ")

# Contar las apariciones de cada letra
conteo_letras = contar_letras(texto, letras)

# Contar la cantidad de palabras
cantidad_palabras = contar_palabras(texto)

# Obtener la primera y última letra
primera_letra, ultima_letra = obtener_primera_ultima_letra(texto)

# Invertir el orden de las palabras
texto_invertido = invertir_orden_palabras(texto)

# Mostrar los resultados al usuario
print("**Resultados:**")
print(f"Conteo de letras: {conteo_letras}")
print(f"Cantidad de palabras: {cantidad_palabras}")
print(f"Primera letra: {primera_letra}")
print(f"Última letra: {ultima_letra}")
print(f"Texto invertido: {texto_invertido}")
