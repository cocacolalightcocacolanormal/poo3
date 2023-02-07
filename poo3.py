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

    def attributs(self):
        print('force:', self.force, "agilité:", self.agilite, "constitution:", self.constitution, "intelligence:",
              self.intelligence, "sagesse:", self.sagesse, "charisme:", self.charisme, "vie", self.vie)


attaque = random.randit(1, 20)


class kobold(NPC):

    def __init__(self):
        super().__init__()


    def attaquer(self, cible):
        return


    def subir_dommage(self, nombredommagesubis):
        return


class hero(NPC):
    def __init__(self):
        super().__init__()


    def attaquer(self, cible):




    def subir_dommage(self, nombredommagesubis):
        return



#Voici comment on fait une attaque:
#le héros lance un dé à 20 faces (d20):
#S’il obtient un 20, c’est une attaque critique
#On réussit à toucher l’adversaire peu importe sa classe d’armure. Le monstre subit alors un d8 de dommage.
#S’il obtient un 1, c’est une attaque ratée
#S’il obtient un nombre entre 2 et 19, il doit vérifier s’il le nombre obtenu est plus grand ou égal à la classe d’armure du monstre
#Si oui, il réussit à toucher l'adversaire et ce dernier subit un d6 de dommage
#Si non, le coup n’a pas fonctionné
