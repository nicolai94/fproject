# import pytest
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from src.database import meta
# from src.main import app
#
# SQLALCHEMY_DATABASE_URL = "sqlite://:memory:"
#
#
# engine_test = create_engine(SQLALCHEMY_DATABASE_URL)
#
# SessionLocal = sessionmaker(bind=engine_test, autocommit=False, autoflush=False)
#
# meta.bind = engine_test
#
#
# def get_test_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
#
#
#
# @pytest.fixture(autouse=True, scope="session")
# def prepare_database():
#     with engine_test.begin() as conn:
#         conn.run_sync(meta.create_all)
#     yield
#     with engine_test.begin() as conn:
#         conn.run_sync(meta.drop_all)
#
#
#
