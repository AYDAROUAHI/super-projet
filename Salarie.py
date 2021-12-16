"""
Created on Wed Dec  8 17:42:25 2021

@author: abidslim
"""

from Personnel import Personnel

class Salarie(Personnel):
    
    def __init__(self):
        super().__init__()
    
    def affichier_coordonnees(self):
        self.get_coordonnees()
        
    def update_fonction(self):
        nouv_fun=str(input('Donner la nouvelle fonction : '))
        self.fonction_=nouv_fun
        
    def affichage_salaire (self):
        # Pas de tableau 7 !! affichage du style
        # le salarié prenom+nom a .. comme salaire
        rez='N° : '+str(self.num_)+"\n"
        rez+='Nom du salarié : '+self.prenom_+' '+self.nom_+"\n"
        rez+='Adresse : '+self.adresse_+"\n"
        rez+='Ville : '+self.ville_+"\n"
        rez+='Fonction : '+self.fonction_+"\n"
        rez+='salaire à payer : '+str(self.salaire_)
        return rez
    
