class user:
    def __init__(self, name, ataque, defesa):
        self.name = name
        self.ataque = ataque
        self.defesa = defesa
    def poder(self):
        poder = 1.2 * self.ataque + self.defesa
        return poder

p1 = user("prr", 100, 120)
print(f"seu poder é {p1.poder():.1f}")