from app import db

class MealPlan(db.Model):
    meal_plan_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)
    calories = db.Column(db.Integer)
    diet = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    user = db.relationship("User", back_populates='meal plans')