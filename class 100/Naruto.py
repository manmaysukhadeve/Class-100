class Naruto (object):
    def __init__(self,name,age,skills):
        self.name = name
        self.age = age
        self.skills = skills
    def fight(self):
        print("start fight")

kakashi = Naruto ("kakashi",26,"Copyninja")
Sauske = Naruto ("Sauske",16,"sharingan")
print(kakashi.age)
print(Sauske.skills)
print(kakashi.fight())