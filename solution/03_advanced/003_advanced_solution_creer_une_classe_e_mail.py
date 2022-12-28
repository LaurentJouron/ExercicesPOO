class Email:
    number_of_mails_sent = 0

    def __init__(self, content):
        self.content = content
        self.is_sent = False

    def send_to(self, email):
        if not self.is_sent:
            self.is_sent = True
            Email.number_of_mails_sent += 1
            return "E-mail envoyé"
        return "L'e-mail a déjà été envoyé"


email = Email(content="La nouvelle formation est disponible !")
response_01 = email.send_to(email="JohnSmith@gmail.com")
response_02 = email.send_to(email="JohnSmith@gmail.com")


"""
Créer une classe e-mail - Solution

CODE:
    class Email:
        number_of_mails_sent = 0
     
        def __init__(self, content):
            self.content = content
            self.is_sent = False
     
        def send_to(self, email):
            if not self.is_sent:
                self.is_sent = True
                Email.number_of_mails_sent += 1
                return "E-mail envoyé"
            return "L'e-mail a déjà été envoyé"
     
    email = Email(content="La nouvelle formation est disponible !")
    response_01 = email.send_to(email="JohnSmith@gmail.com")
    response_02 = email.send_to(email="JohnSmith@gmail.com")

EXPLICATIONS:
    Le premier élément à créer était la méthode send_to dans la classe Email.
    Cette méthode devait posséder un paramètre email.
    def send_to(self, email):
    Il fallait ensuite créer un attribut de classe number_of_mails_sent dans la
    classe Email.
    On initialise la valeur de cet attribut à 0.
    class Email:
        number_of_mails_sent = 0
    Ensuite, il fallait vérifier dans la méthode send_to si l'e-mail n'a pas 
    déjà été envoyé.
    Nous faisons cette vérification avec une structure conditionnelle et nous
    vérifions que l'attribut is_sent n'est pas égal à True grâce à l'opérateur
    not :
    if not self.is_sent:
    Si l'e-mail n'a pas déjà été envoyé, nous incrémentons alors de 1
    l'attribut number_of_mails_sent de la classe Email :
    Email.number_of_mails_sent += 1
    Et nous modifions l'attribut is_sent pour le passer à True et ainsi 
    signifier que l'e-mail a bien été envoyé (et pour empêcher de l'envoyer 
    une seconde fois) :
    self.is_sent = True
    Il ne nous reste plus qu'à retourner les bonnes chaînes de caractères en 
    fonction de la situation.
    Si l'e-mail est envoyé, on retourne la chaîne de caractères à l'intérieur 
    de la structure conditionnelle.
    Sinon, on retourne l'autre chaîne de caractères à la fin de la méthode :
    def send_to(self, email):
        if not self.is_sent:
            self.is_sent = True
            Email.number_of_mails_sent += 1
            return "E-mail envoyé"
        return "L'e-mail a déjà été envoyé"
    Vous avez peut-être écrit votre code un peu différemment, en incluant une 
    condition else :
    def send_to(self, email):
        if not self.is_sent:
            self.is_sent = True
            Email.number_of_mails_sent += 1
            return "E-mail envoyé"
        else:
            return "L'e-mail a déjà été envoyé"
    Cela fonctionne également, mais le else est inutile.
    En effet, si la condition n'est pas vérifiée, le code à l'intérieur du 
    bloc d'instruction ne sera pas exécuté.
    On passera donc directement au deuxième return après le bloc if qui 
    ndiquera que le mail a déjà été envoyé.
    Le comportement est donc le même que si l'on mettait une condition else.
    
POINTS IMPORTANTS À RETENIR:
    Pour définir un attribut de classe, on crée cet attribut directement dans 
    la classe et non pas sur l'instance (donc pas sur self).
    Pour retourner une valeur dans une fonction, on utilise l'instruction 
    return.
"""