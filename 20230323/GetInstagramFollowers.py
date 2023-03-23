#Script para usar libreria de instagram
import instaloader

# Obtener instancia
instagram = instaloader.Instaloader()

# Login
instagram.interactive_login("sebasdeharbe")      # (ask password on terminal)

# Obtener un perfil
profile = instaloader.Profile.from_username(instagram.context, "sebasdeharbe")

# #Mostrar seguidores
seguidores = []
for follower in profile.get_followers(): 
    seguidores.append(follower.username)
    # print(follower.username)

# # Mostrar seguidos
# for followee in profile.get_followees():
#     print(followee.username)

    
print(profile.blocked_by_viewer)


