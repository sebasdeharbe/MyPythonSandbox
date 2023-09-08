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
print('-------------------------------------------')
texto_cifrado = "pfnybfvrc dvderzn p.z. yn rerc,vqnql bfr arczver n y.d u.zocrd ryrtvc df ac.av. sfefc.l erczv,ncá ryvtvr,q. yn drtfcvqnq j yn zrqv.pcvqnql j r, rdn crnyvqnq ynd rdecryynd rdeá, sfrcn qry nypn,prm yn zrcn rivder,pvn qr yn rerc,vqnq ryvzv,n qr f, ayfznk. ry vzarcv. tnyápevp.m ancn crdenfcncy.l qror npnoncdr p., yn rerc,vqnqm"
clave = 13
mensaje_descifrado = descifrar_cesar(texto_cifrado, clave, ".abcdefghijklmnopqrstuvwxyz,")
print(mensaje_descifrado)