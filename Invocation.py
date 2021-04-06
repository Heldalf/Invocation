# Créé par DKa, le 18/03/2021 en Python 3.4
########################
#####  Invocation  #####
########################
#provisoire qui ne fonctinne pas
from random import*
from tkinter import*
from PIL import Image, ImageTk

'''La liste des différentes classes'''
Saber=["Flamme Serpens", "Ray Starling", "Lloyd Serpens", "Laevatein Serpens"]
Lancer=["Camus Egreffin", "Gray Egreffin", "Scathach", "Ephraim Marvell"]
Archer=["Nathaniel DRAYER", "Rinslet Laurenfrost", "Gilgamesh", "Hubert Tsuchimikado"]
Rider=["Arès Nox Fleuret", "Michalis Messida", "Sophie Milkanvich", "Malik Caesar"]
Assassin=["Ryougi Mana", "Mochizuki Chiyome", "Naigo", "Glass"]
Caster=["Gelda Nebilim", "Edna", "Kasque", "Archimède"]
Berserker=["Flamme Serpens 'Wrath'", "Arcueid Brunestrud", "Laevatein 'Reine Sanguinaire'", "Eizen"]
Avenger=["Angra Mainyu", "Rose Serpens 'Oblivion'", "Mule La Mor"]
World_Cancer=["Ardyn Izunia", "Vicious Varienti"]
Ruler=["Yggdrasill", "Gabranth Amicitiia", "Nils Didek Foreigner"]
Foreigner=["Zwei", "Abigail Egreffin", "Kurumi Ultina"]

def affiche(path):
    fichier = Image.open(path)
    photo = ImageTk.PhotoImage(fichier)
    Canevas.photo=photo
    Canevas.configure(width = fichier.size[0], height = fichier.size[1],background='red')
    Canevas.create_image(0,0,anchor=NW,image=photo)



def summon(classe):
    global Saber, Lancer, Archer, Rider, Assassin, Caster, Berserker, Avenger, World_Cancer, Ruler, Foreigner
    '''commentaire: invocation. retourne un nom'''
    if classe=="Saber":
        Servant=choice(Saber)
    if classe=="Lancer":
        Servant=choice(Lancer)
    if classe=="Archer":
        Servant=choice(Archer)
    if classe=="Rider":
        Servant=choice(Rider)
    if classe=="Assassin":
        Servant=choice(Assassin)
    if classe=="Caster":
        Servant=choice(Caster)
    if classe=="Berserker":
        Servant=choice(Berserker)
    if classe=="Je suis celui qui dirigera ta vengeance.":
        print("Félicitations, vous avez invoqué la classe Avenger. Vous voilà maître de la vengeance.")
        Servant=choice(Avenger)
    if classe=="Je suis celui qui contrôlera tout les pouvoirs du monde.":
        print("Félicitations, vous avez invoqué la classe Foreigner. Vous dirigez des pouvoirs qui ne sont pas issus de ce monde.")
        Servant=choice(Foreigner)
    if classe=="Je suis celui qui dirigera et supportera le monde sur ses épaules.":
        print("Félicitations, vous avez invoqué la classe Ruler. Vous êtes un protecteur de la balance et de l'équilibre.")
        Servant=choice(Ruler)
    if classe=="Ma volonté est synonime de corruption, disgrâce et dépravation. Je suis celui qui mènera le monde à sa perte.":
        print("Félicitation, vous avez invoqué la classe World Cancer. Vous êtes un ennemi du Monde, précipitant sa destruction. ")
        Servant=choice(World_Cancer)
    return Servant





'''appelle la fonction summon et stocke le nom obtenu dans Servant'''
Servant=summon(input("Choisissez un nom entre Saber, Lancer, Archer, Rider, Assassin, Caster ou Berserker"))
print("le nom de mon Servant est : ",Servant)


'''créé la fenêtre où est censé apparaître l'image'''
window2 = Tk()
window2.title("Mon Servant")

Canevas = Canvas(window2)
Canevas.pack()

'''fait apparaître une image différente en fonction du nom dans Servant'''
if Servant=="Flamme Serpens":
    affiche("Flamme.png")

elif Servant=="Lloyd Serpens":
    affiche("Lloyd.png")

elif Servant=="Ray Starling":
    affiche("Ray.png")

elif Servant=="Laevatein Serpens":
    affiche("Laevatein.png")

elif Servant=="Camus Egreffin":
    affiche("Camus.png")

elif Servant=="Gray Egreffin":
    affiche("Gray.png")

elif Servant=="Scathach":
    affiche("Scathach.png")

elif Servant=="Ephraim Marvell":
    affiche("Ephraim.png")

elif Servant=="Nathaniel DRAYER":
    affiche("DRAYER.png")

elif Servant=="Rinslet Laurenfrost":
    affiche("Rinslet.png")

elif Servant=="Gilgamesh":
    affiche("Gilgamesh.png")

elif Servant=="Hubert Tsuchimikado":
    affiche("Hubert.png")

elif Servant=="Arès Nox Fleuret":
    affiche("Ares.png")

elif Servant=="Michalis Messida":
    affiche("Michalis.png")

elif Servant=="Sophie Milkanvich":
    affiche("Sophie.png")

elif Servant=="Malik Caesar":
    affiche("Malik.png")

elif Servant=="Ryougi Mana":
    affiche("Mana.png")

elif Servant=="Mochizuki Chiyome":
    affiche("Chiyome.png")

elif Servant=="Naigo":
    affiche("Naigo.png")

elif Servant=="Glass":
    affiche("Glass.png")

elif Servant=="Gelda Nebilim":
    affiche("Nebilim.png")

elif Servant=="Edna":
    affiche("Edna.png")

elif Servant=="Kasque":
    affiche("Kasque.png")

elif Servant=="Archimède":
    affiche("Archimedes.png")

elif Servant=="Flamme Serpens 'Wrath'":
     affiche("Flamme Berserk.png")

elif Servant=="Arcueid Brunestrud":
     affiche("Arcueid.png")

elif Servant=="Laevatein 'Reine Sanguinaire'":
     affiche("Bloody Queen.png")

elif Servant=="Eizen":
     affiche("Eizen.png")

elif Servant=="Angra Mainyu":
    affiche("Angra Mainyu.png")

elif Servant=="Rose Serpens 'Oblivion'":
    affiche("Rose Oblivion.png")

elif Servant=="Mule La Mor":
    affiche("Mule.png")

elif Servant=="Ardyn Izunia":
    affiche("Ardyn.png")

elif Servant=="Vicious Varienti":
    affiche("Vicious.png")

elif Servant=="Yggdrasill":
    affiche("Yggdrasill.png")

elif Servant=="Gabranth Amicitiia":
    affiche("Gabranth.png")

elif Servant=="Nils Didek Foreigner":
    affiche("Nils.png")

elif Servant=="Zwei":
    affiche("Zwei.png")

elif Servant=="Abigail Egreffin":
    affiche("Abigail.png")

elif Servant=="Kurumi Ultina":
    affiche("Kurumi.png")

window2.mainloop()



























