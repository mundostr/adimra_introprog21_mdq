# int, float, str, bool

# nro1 = 15
# nro2 = 16.5
# total = nro1 + nro2
# print(total)


titulo = "El resultado es "
total = 23.58
iva = total * 0.21
print(iva)

cadena_final = titulo + str(total) + " (iva " + str(iva) + ")."
print(cadena_final)

cadena_final_alternativa = f"El resultado es {total} (iva {iva:.3f})."
print(cadena_final_alternativa)
