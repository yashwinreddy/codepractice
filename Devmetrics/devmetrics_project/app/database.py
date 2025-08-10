from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, String, Integer, Float, DateTime
from datetime import datetime

DATABASE_URL = "sqlite+aiosqlite:///./devmetrics.db"

engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    username = Column(String, primary_key=True, index=True)
    name = Column(String)
    bio = Column(String)
    followers = Column(Integer)
    public_repos = Column(Integer)
    last_updated = Column(DateTime, default=datetime.utcnow)

class Analytics(Base):
    __tablename__ = "analytics"
    username = Column(String, primary_key=True, index=True)
    total_commits_30d = Column(Integer)
    pr_opened = Column(Integer)
    pr_merged = Column(Integer)
    avg_merge_time_hours = Column(Float)
    issues_opened = Column(Integer)
    issues_closed = Column(Integer)
    avg_issue_close_time_hours = Column(Float)
    developer_score = Column(Float)
    last_calculated = Column(DateTime, default=datetime.utcnow)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
