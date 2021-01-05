from randomuser import RandomUser

# Generate a single user
user = RandomUser()

# Generate a list of 10 random users
user_list = RandomUser.generate_users(10)

# вывести пол человека, имя, фамилию, номер телефона, email, место проживания
for user in user_list:
    print(
        user.get_gender(),
        user.get_first_name(),
        user.get_last_name(),
        user.get_phone(),
        user.get_email(),
        user.get_state(),
    )
