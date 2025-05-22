


# import pytest
# from fastapi.testclient import TestClient
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from app.main import app  
# from app.core.dependencies import get_db
# from app.database.database import Base


# # This is a temporary database that will be created and destroyed for each test run
# # (SQLite in-memory)
# SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
# TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# @pytest.fixture(scope="function")
# def db_session():
#     """
#     Create a new database session for a test.
#     """
#     Base.metadata.create_all(bind=engine)
#     db = TestingSessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
#         Base.metadata.drop_all(bind=engine)

# @pytest.fixture(scope="function")
# def client(db_session):
#     """
#     Create a test client for the FastAPI app.
#     """
#     def override_get_db():
#         """
#         Override the get_db dependency to use the test database session.
#         """
#         try:
#             yield db_session
#         finally:
#             pass
#     app.dependency_overrides[get_db] = override_get_db
#     with TestClient(app) as c:
#         yield c
#     app.dependency_overrides.clear()
