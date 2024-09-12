from app import db
from datetime import datetime, timezone
from sqlalchemy.orm import Mapped

class UserTable(db.Model):
    __tablename__: str = "users"
    id: Mapped[int] = db.Column(db.Integer, primary_key=True)
    name: Mapped[str] = db.Column(db.String(255), nullable=False)
    email: Mapped[str] = db.Column(db.String(255), unique=True, nullable=False)
    password: Mapped[str] = db.Column(db.Text, nullable=False)
    created_at: Mapped[datetime] = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))