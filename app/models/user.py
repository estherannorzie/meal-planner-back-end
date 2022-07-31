from app import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    meal_plans = db.relationship("MealPlan", back_populates="user")


    def to_dict(self):
        return dict(
            id=self.user_id,
            username=self.username,
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email
        )

    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            username=data_dict["username"],
            first_name=data_dict["first_name"],
            last_name=data_dict["last_name"],
            email=data_dict["email"]
        )
    
    def update_email(self, data_dict):
        self.email = data_dict["email"]