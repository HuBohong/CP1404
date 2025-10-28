class User:
    def __init__(self, name = ""):
        self.name = name
        self.number_of_tacos = 5
        self.score = 0

    def __str__(self):
        return f"{self.name} {self.number_of_tacos} tacos left {self.score} points"

    def receive_taco(self, taco):
        self.number_of_tacos += 1

    def give_taco(self, receiver):
        if self.number_of_tacos > 0:
            self.number_of_tacos -= 1
            receiver.score += 1
        else:
            print("No tacos to give!")

if __name__ == '__main__':


    user_one = User("Alice")
    user_two = User("Bob")
    user_one.give_taco (user_two)
    print(user_one)
    print(user_two)