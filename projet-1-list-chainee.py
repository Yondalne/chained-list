
class Etudiant:
    def __init__(self, firstName, secondName, card, moy = 0):
        self.ref = ""
        self.nomprenom = secondName+" "+firstName
        self.noCarte = card
        self.moy = moy
        self.suiv = None
        
    def setMoyenne(self, moy):
        self.moy = moy
    
    def setRef(self, ref):
        self.ref = ref
        
    def setSuiv(self, ref):
        self.suiv = ref
    
        
class ListEtudiant:
    def __init__(self):
        self.content = []
    
    def ajout(self, item):
        self.content.append(item)
        ref = len(self.content)-1
        if ref >= 1 :
            self.content[ref-1].setSuiv(ref)
        self.content[ref].setRef(ref)
        
        self.tri()
        print("Etudiant ajoute avec succes")
        
    def show(self):
        for etudiant in self.content:
            print(etudiant.nomprenom)
    
    def inverseListe(self):
        self.content.reverse()
        self.show()
    
    def supprimer(self, nocard):
        ref = list(filter(lambda x: x.noCarte == nocard, self.content))
        if len(ref) == 0:
            print("Ce numero de classe n'existe pas dans cette classe")
        else:
            ref = ref[0].ref
            self.content.pop(ref)
            print("Etudiant supprime avec succes")
    
    def tri (self):
        self.content.sort(key=lambda x: x.nomprenom)
        self.show()
    
    def promoFinal(self):
        self.content = list(filter(lambda x: x.moy >= 12, self.content))
        self.show()
      
    def fusion(self, secondList):
        newPromo = ListEtudiant()
        for etudiant in self.content:
            newPromo.ajout(etudiant)
        
        for etudiant in secondList.content:
            newPromo.ajout(etudiant)
        
        newPromo.tri()
        
        return newPromo
          

################### Debut Test ####################

    ########### Creation d'une liste ###########
student1 = Etudiant("Ben Ali", "Cherif", "19-ESATIC0006AB", 14)
student2 = Etudiant("Bomo Noemi", "Bouaki", "19-ESATIC0007AB", 16)
student3 = Etudiant("Amangoua", "Amangoua", "19-ESATIC0008AB", 15)
student4 = Etudiant("Arouna", "Sidibe", "19-ESATIC0009AB", 11)
student5 = Etudiant("Abraham", "David", "19-ESATIC0010AB", 11)

m1Info = ListEtudiant()

        ####### Test Ajout
m1Info.ajout(student1)
m1Info.ajout(student2)
m1Info.ajout(student3)
m1Info.ajout(student4)
m1Info.ajout(student5)

        ####### Test Tri
m1Info.tri() 

    ########### Creation d'une 2e liste ###########
studentA = Etudiant("Tizier", "Tah", "19-ESATIC0011AB", 10)
studentB = Etudiant("Christophe", "Boua", "19-ESATIC0012AB", 12)
studentC = Etudiant("Assane", "Dao", "19-ESATIC0013AB", 11)
studentD = Etudiant("Jules", "Side", "19-ESATIC0014AB", 7)
studentE = Etudiant("Charles", "Tounkara", "19-ESATIC0015AB", 9)

m1Rtel = ListEtudiant()

m1Rtel.ajout(studentA)
m1Rtel.ajout(studentB)
m1Rtel.ajout(studentC)
m1Rtel.ajout(studentD)
m1Rtel.ajout(studentE)

m1Rtel.tri()


print("Liste M1 Info")
m1Info.show()


        ####### Test Supprimer
print("\n Suppression de 19-ESATIC0010AB")
m1Info.supprimer("19-ESATIC0011AB")
m1Info.show()


        ####### Test PromoFinal
m1Info.promoFinal()
print("Promo finale m1 info: ")
m1Info.show()
print("\n")

print("Promo finale m1 rtel: ")
m1Rtel.promoFinal()
m1Rtel.show()
print("\n")


        ####### Test Fusion
print("Nouvelle Promo")    
newPromo = m1Info.fusion(m1Rtel)
newPromo.show()


print("\n ###################### Renitialisation des listes ######################")
m1Info.__init__()
m1Rtel.__init__()
print("\n ######################  Renitialisation Terminee  ######################")
