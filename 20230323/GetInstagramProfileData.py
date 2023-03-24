#Script para usar libreria de instagram
import instaloader
import sys
import os
import requests
from io import BytesIO
from PIL import Image
print(sys.version)

# Obtener instancia instaloader
instagram = instaloader.Instaloader()

# Login
user = input("Usuario de instagram para loguearse: ")
instagram.interactive_login(user)      # (ask password on terminal)

# Obtener un perfil
perfil = input("Usuario a investigar: ")
profile = instaloader.Profile.from_username(instagram.context, perfil)

controlPosts = input("Escriba 'S' para descargar posts: ")
if controlPosts == 'S':
    posts = profile.get_posts()
    for i in posts:
        response = requests.get(i.url)
        imagen = Image.open(BytesIO(response.content))
        if not os.path.exists('./data'):
            os.makedirs('./data')
        filepath = './data/'+str(i.mediaid)+'.jpg'
        imagen.save(filepath)

## -> Seguidores
seguidores = []
for follower in profile.get_followers(): 
    seguidores.append(follower.username)
control = input("Escriba 'S' para imprimir seguidores: ")
if control == 'S': 
    print(follower.username)

## -> Seguidos
controlSeguidos = input("Escriba 'S' para imprimir Seguidos que no siguen: ")
if controlSeguidos == 'S': 
    seguidos = []
    print('Seguidos que no siguen')
    for followee in profile.get_followees():
        seguidos.append(followee.username)
        if not followee.username in seguidores:
            print(followee.username)
    print('.......................................................................................................................')

controlSeguidores = input("Escriba 'S' para imprimir Seguidores que no sigue: ")
if controlSeguidores == 'S':
    print('Seguidores que no sigue')
    for follower in seguidores:
        if not follower in seguidos: 
            print(follower)