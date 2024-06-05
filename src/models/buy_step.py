from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from src.db.database import Base


class BuyStep(Base):
    __tablename__ = "buy_step"

    id = Column(Integer, primary_key=True, index=True)
    buy_id = Column(Integer, ForeignKey("buy.id"), nullable=False)
    step_id = Column(Integer, ForeignKey("step.id"), nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=True)

    buy = relationship("Buy")
    step = relationship("Step")

    def __repr__(self):
        return f"<BuyStep {self.buy_id} {self.step_id} {self.start_date} {self.end_date}>"