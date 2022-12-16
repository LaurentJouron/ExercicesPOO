class Livre:
    pass


harry_potter = Livre()

"""
Créer une classe - Solution

CODE:

    class Livre:
        pass

    harry_potter = Livre()


EXPLICATIONS:
    Pour définir une classe, on utilise l'instruction class suivi du nom de la 
    classe :

    class Livre:
        pass
⚠️ Il ne faut pas oublier de terminer la ligne par le symbole deux-points.

👉 Pour que Python ne nous retourne pas d'erreur on est obligé de mettre au 
    moins une ligne de code à l'intérieur de la classe, dans ce cas-ci 
    l'instruction pass qui ne fait rien.

Il ne faut pas oublier également l'indentation avant l'instruction pass pour 
définir le bloc d'instruction comme appartenant à la classe Livre.

Pour créer une instance à partir d'une classe, on utilise la même syntaxe que 
pour appeler une fonction, avec les parenthèses :

    harry_potter = Livre()
Si on affiche le type de la variable harry_potter, on voit bien que l'objet 
est de type Livre :

>>> type(harry_potter)
< class '__main__.Livre' >
Et si on fait un print de la variable harry_potter, on voit bien qu'il s'agit 
d'une instance de la classe Livre :

>>> print(harry_potter)
<__main__.Livre object at 0x103fa4160>


POINTS IMPORTANTS À RETENIR:

    Pour créer une classe, on utilise l'instruction class suivie du nom de la 
    classe.
    
    Pour créer une instance à partir d'une classe, on fait une assignation 
    simple et on utilise les parenthèses.
"""