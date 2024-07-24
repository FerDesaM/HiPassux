from app.domain.repositories.user_repository import User,UserRepository

class UserService:

    def __init__(self, user_repository):
        self.user_repository = user_repository

    @staticmethod
    def get_all_users(self):
        return self.UserRepository.get_all_users()

    @staticmethod
    def create_user(self ,username, first_name, last_name, birth_date, phone_number, gender, email, password):
        new_user = User(
            username=username,
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date,
            phone_number=phone_number,
            gender=gender,
            email=email,
            password=password
        )
        self.UserRepository.add_user(new_user)