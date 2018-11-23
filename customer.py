class Customer:
    def __init__(self,first_name,family_name,age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age


    def full_name(self):
        print(f"{self.first_name} {self.family_name}")

    def entry_fee(self):
        if self.age > 65:
            amount = 1200
            print(amount)

        if self.age >= 20 and self.age < 65:
            amount = 1500
            print(amount)

        if self.age < 20:
            amount = 1000
            print(amount)


#ken = Customer(first_name="Ken", family_name="Tanaka")
#ken.full_name()  # "Ken Tanaka" という値を返す

#tom = Customer(first_name="Tom", family_name="Ford")
#tom.full_name()  # "Tom Ford" という値を返す

