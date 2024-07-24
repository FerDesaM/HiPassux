from app.domain.entities.user import db, User
from app.domain.repositories.base_repository import BaseRepository

class UserRepository(BaseRepository):

    @staticmethod
    def get_all_users():
        return User.query.all()
        # Obtiene todos los usuarios de la base de datos.

    def add(self, user):
        db.session.add(user)
        db.session.commit()
        # Añade un usuario a la base de datos y confirma la transacción.

    def remove(self, user):
        db.session.delete(user)
        db.session.commit()
        # Elimina un usuario de la base de datos y confirma la transacción.