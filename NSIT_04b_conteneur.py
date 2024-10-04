class Conteneur():
    """ les éléments à stocker dans le conteneur font exactement la hauteur et la largeur du conteneur.
        Il faut donc les rentrer les uns après les autres.
        Lorsque nous devons les sortir, le dernier entré sera le premier sorti.
        Les éléments à stocker sont désignés par une référence (une chaîne de caractère)
        Par exemple "A1" ou "BZ3".
    """
    def __init__(self,maxi = 20):
        # Constructeur de la classe Conteneur
        self.nb_colis_max = maxi
        self.colis = colis
    
    def est_vide(self)->bool:
        """ Renvoie True si le conteneur est vide
            Sinon renvoie False
        """
        if len(self.colis)>0:
            return False
        else:
            return True
    
    def est_plein(self)->bool:
        """ Renvoie True si le conteneur est plein.
            Sinon renvoie False
        """
        if len(self.colis)>=self.nb_colis_max :
            return True
        else:
            return False
    
    def empile(self, nom_colis)->bool:
        """ Ajoute l'élément nom_colis dans la liste des colis si le conteneur n'est pas plein.
            Renvoie True si c'est possible, sinon, affiche un message d'alerte et renvoie False
        """
        print("Il y a", len(self.colis)," dans le conteneur, sur un max de ", self.nb_colis_max)
        if self.est_plein():
            print("Le conteneur est plein")
            return False
        else:
            return self.colis.append(mon_colis)
    
    def depile(self)->bool:
        """ Si le conteneur n'est pas vide, enlève le dernier élément de la liste des colis.
            Affiche le nom de l'élément enlevé et renvoie cet élément.
            Sinon affiche un message d'alerte et renvoie None.
        """
        if self.est_vide():
            #print("La pile est vide")
            return ...
        ...
        print("J'ai sorti:", colis_sorti)
        return ...


if __name__ == "__main__":
	c = Conteneur()
	c.empile('f5')
	c.empile('f4')
	c.empile('f1')
	c.empile('f2')
	c.empile('f3')
	c.depile()
	c.depile()
