from operator import attrgetter

from class_coding_folder.practiceWeekTwo import scary_monsters


class Monster:
    def __init__(self, name="Mike", number_of_teeth=0, color="blue"):
        """Initialize a Monster object with a name, number of teeth, and color."""
        self.name = name
        self.number_of_teeth = number_of_teeth
        self.color = color

    def __str__(self):
        """Return a string representation of the Monster."""
        return f"Monster Name: {self.name}, Teeth: {self.number_of_teeth}, Color: {self.color}"

    def __repr__(self):
        """Return a string representation of the Monster."""
        return str(self)

    def is_scary(self):
        """Determine if the monster is scary based on the number of teeth."""
        return self.number_of_teeth > 16 or self.color == "red"


if __name__ == '__main__':
    monster_one = Monster("DDD", 10, "red")
    monster_two = Monster()
    monster_three = Monster("ZZZ", 20, "green")
    monster_four = Monster("AAA", 5, "blue")
    # print(monster_one)
    # print(monster_two)
    # print(monster_one.is_scary())
    # print(monster_two.is_scary())
    monsters = [monster_one, monster_two, monster_three, monster_four]
    # monsters.sort(key=attrgetter("number_of_teeth"))
    # print(monsters)

    scary_monsters = [monster for monster in monsters if monster.is_scary()]
    print(scary_monsters)
