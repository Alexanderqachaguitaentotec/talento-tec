def devolver_distintos(a, b, c):
  
 
  suma = a + b + c

  if suma > 15:
    return max(a, b, c)
  elif suma < 10:
    return min(a, b, c)
  else:
    return sorted([a, b, c])[1]


numero_mayor = devolver_distintos(10, 12, 5)
print(f"El número mayor es: {numero_mayor}")

numero_menor = devolver_distintos(2, 3, 4)
print(f"El número menor es: {numero_menor}")

numero_intermedio = devolver_distintos(7, 8, 9)
print(f"El número intermedio es: {numero_intermedio}")
