class PasswordPolicy():
    def __init__(self, min, max, char):
        self.min = int(min)
        self.max = int(max)
        self.char = char

    def check_password_old(self, pwd):
        count = pwd.count(self.char)
        print(f"Checking if {count} is in between {self.min} and {self.max} for {self.char} in {pwd}...", end="")
        if self.min <= count <= self.max:
            print("Yes")
            return True

        print("No")
        return False

    def check_password(self, pwd):
        print(f"checking if {self.char} is in position {self.min - 1} or {self.max - 1} for {pwd}...", end="")

        if (pwd[self.min - 1] == self.char) ^ (pwd[self.max - 1] == self.char):
            print("Yes")
            return True
        print("No")
        return False


with open('input') as reader:
    valid_passwords = 0
    for line in reader:
        policy, pwd = line.split(":")
        pwd = pwd.strip()
        bounds, char = policy.split(" ")
        char_min, char_max = bounds.split("-")
        policy = PasswordPolicy(char_min, char_max, char)
        if policy.check_password(pwd):
            valid_passwords += 1


print(valid_passwords)