from app import db
from sqlalchemy.schema import CheckConstraint
from sqlalchemy.orm import validates

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(16), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String(16), nullable=False)
    last_name = db.Column(db.String(16), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    meal_plans = db.relationship("MealPlan", back_populates="user")

    # https://stackoverflow.com/questions/50174325/define-minimum-length-for-postgresql-string-column-with-sqlalchemy
    __table_args__ = (
        CheckConstraint("char_length(password) > 11",
                        name="password_min_length"),
    )

    @validates(password)
    def validate_password(self, key, password) -> str:
        if len(password) < 12:
            raise ValueError("Password is too short.")
        return password


    @staticmethod
    def stringify():
        return "User"

    def to_dict(self):
        return dict(
            id=self.user_id,
            username=self.username,
            password=self.password,
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email
        )

    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            username=data_dict["username"],
            password=data_dict["password"],
            first_name=data_dict["first_name"],
            last_name=data_dict["last_name"],
            email=data_dict["email"]
        )
    
    def update_user(self, data_dict, user_current_email, user_current_password):
        self.email=data_dict["email"] if data_dict.get("email") else user_current_email,
        self.password=data_dict["password"] if data_dict.get("password") else user_current_password