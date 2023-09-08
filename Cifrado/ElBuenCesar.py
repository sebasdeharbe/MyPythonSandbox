def descifrar_cesar(texto, clave, alfabeto):
  """
  Descifra un mensaje cifrado con el cifrado César.

  Args:
    texto: El mensaje cifrado.
    clave: La clave del cifrado.

  Returns:
    El mensaje descifrado.
  """

  mensaje_descifrado = ""
  for letra in texto:
    if letra in alfabeto:
      pos_letra = alfabeto.index(letra)
      pos_letra_desplazada = (pos_letra - clave) % len(alfabeto)
      letra_desplazada = alfabeto[pos_letra_desplazada]
      mensaje_descifrado += letra_desplazada
    else:
      mensaje_descifrado += letra

  return mensaje_descifrado


texto_cifrado = "pfx htrywfxjsfx xtr htqt pf wtuf nryjwntw rt uzjijx ijñfw vzj rfinj pf ajf ijgjx hfqgnfwpf wjlzpfwqjryj d rt ijgjx htqufwynwpf htr jcywfstx"
clave = 5
mensaje_descifrado = descifrar_cesar(texto_cifrado, clave, "abcdefghijklmnñopqrstuvwxyz")
print(mensaje_descifrado)