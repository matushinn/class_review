from customer import Customer
#B-8

if __name__ == "__main__":
    ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
    ken.info_split_pipe()

    tom = Customer(first_name="Tom", family_name="Ford", age=57)
    ken.info_split_pipe()  # "Tom Ford,57,1500" という値を返す

    ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
    ieyasu.info_split_pipe()  # "Ieyasu Tokugawa,73,1200" という値を返す