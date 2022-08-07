from app import db

class MealPlan(db.Model):
    meal_plan_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(64), nullable=False, unique=True)
    type = db.Column(db.Integer, nullable=False)
    calories = db.Column(db.Integer)
    diet = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone=True))
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)
    user = db.relationship("User", back_populates="meal_plans")


    @staticmethod
    def stringify():
        return "Meal plan"
    
    
    def to_dict(self):
        return dict(
            id=self.meal_plan_id,
            title=self.title,
            type=self.type,
            calories=self.calories,
            diet=self.diet,
            date=self.date
        )


    @classmethod
    def from_dict(cls, data_dict, user):
        return cls(
            title=data_dict["title"],
            type=data_dict["type"],
            calories=data_dict.get("calories"),
            diet=data_dict.get("diet"),
            date=data_dict.get("date"),
            user=user
        )


    def update_meal_plan(self, data_dict):
        self.title=data_dict["title"],
        self.type=data_dict["type"],
        self.calories=data_dict.get("calories"),
        self.diet=data_dict.get("diet"),
        self.date=data_dict.get("date")