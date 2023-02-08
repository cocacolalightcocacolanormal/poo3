import random


def lancer_de():
    throw1 = random.randit(1, 6)
    throw2 = random.randit(1, 6)
    throw3 = random.randit(1, 6)
    throw4 = random.randit(1, 6)

    if throw1 < throw2 and throw1 < throw3 and throw1 < throw4:
        return (throw2 + throw3 + throw4)

    elif throw2 < throw1 and throw2 < throw3 and throw2 < throw4:
        return (throw1 + throw3 + throw4)

    elif throw3 < throw2 and throw1 < throw3 and throw1 < throw4:
        return (throw2 + throw3 + throw4)

    elif throw4 < throw2 and throw4 < throw3 and throw4 < throw1:
        return (throw2 + throw3 + throw1)


def ptvie():
    throw5 = random.randit(1, 20)


class NPC:
    def __init__(self):
        self.force = lancer_de()
        self.agilite = lancer_de()
        self.constitution = lancer_de()
        self.intelligence = lancer_de()
        self.sagesse = lancer_de()
        self.charisme = lancer_de()
        self.race: str
        self.nom: str
        self.profession: str
        self.vie = ptvie()
        self.classearmure = lancer_de()

    def attributs(self):
        print('force:', self.force, "agilité:", self.agilite, "constitution:", self.constitution, "intelligence:",
              self.intelligence, "sagesse:", self.sagesse, "charisme:", self.charisme, "vie", self.vie)

#POO 3 
attaque = random.randit(1, 20)

#On crée la classe de monstre (kobold) 
class kobold(NPC):
#on transfert toutes les caractéristiques de la classe NPC à la classe de ce monstre
    def __init__(self):
        super().__init__()
#on crée la fonction d'attaquer
    def attaquer(self, cible):
        return
# on crée une fonction pour subir des dommages. On reçoit le nombre de dommages subis lors d'une attaque 
#critique, déterminée dans la fonction "attaquer" dans notre class héros. Si la variable attaquer est supérieur
#à la classe d'armure du monstre, le monstre reçoit un d6 de dommage. Si la variable est inférieur à la classe d'armure,
#l'attaque fait 0 dégats (ratée)
    def subir_dommage(self, nombredommagesubis):
        self.vie = self.vie - nombredommagesubis

        if attaque => self.classearmure:
            self.vie = self.vie - random.randit(1, 6)

        elif attaque < self.classearmure:
            self.vie = self.vie - 0
        

#pour notre class héros, on transfert les mêmes caractéristiques dans la classe NPC.
class hero(NPC):
    def __init__(self):
        super().__init__()
#on crée une fonction attaquer pour l'héros aussi. Ici, on écrit que si la variable "attaquer" est égal à 20, 
    # le monstre recevra des dommages d'un d8 (attaque critique). Si la variable est égal à 1, l'attaque est ratée
    def attaquer(self, cible):
        if attaque = 20:
            cible.subir_dommage(random.randit(1, 8))

        elif attaque = 1:
            print("attaque ratée")

    def subir_dommage(self, nombredommagesubis):
        return

