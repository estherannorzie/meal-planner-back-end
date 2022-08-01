from app import db

class MealPlan(db.Model):
    meal_plan_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    type = db.Column(db.Integer, nullable=False)
    calories = db.Column(db.Integer)
    diet = db.Column(db.Integer)
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
            diet=self.diet
        )


    @classmethod
    def from_dict(cls, data_dict, user):
        return cls(
            title=data_dict.get("title"),
            type=data_dict.get("type"),
            calories=data_dict.get("calories"),
            diet=data_dict.get("diet"),
            user=user
        )