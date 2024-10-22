import pytest
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Определяем базу данных и модель
DATABASE_URL = "postgresql+psycopg2://postgres:654654@localhost/skypro"
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    user_email = Column(String, nullable=False)
    subject_id = Column(Integer, nullable=False)


# Фикстура для подключения к базе данных и создания тестовых данных
@pytest.fixture(scope="module")
def db_session():
    # Создаем движок и сессию
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()

    # Добавление тестовых данных
    test_data = [
        User(user_id=1, user_email='user1@example.com', subject_id=101),
        User(user_id=2, user_email='user2@example.com', subject_id=102),
        User(user_id=3, user_email='user3@example.com', subject_id=103)
    ]
    session.bulk_save_objects(test_data)
    session.commit()

    yield session  # Возврат сессии для тестов

    # Очистка тестовых данных после завершения всех тестов
    session.query(User).filter(User.user_id.in_([1, 2, 3])).delete(synchronize_session=False)
    session.commit()
    session.close()


# Тест на добавление пользователя
def test_add_user(db_session):
    new_user = User(user_id=4, user_email='user4@example.com', subject_id=104)
    db_session.add(new_user)
    db_session.commit()

    user = db_session.query(User).filter_by(user_id=4).first()

    # Проверка, что новый пользователь добавлен
    assert user is not None, "Пользователь не был добавлен"
    assert user.user_email == new_user.user_email, "Email пользователя не совпадает"

    # Очистка созданных данных
    db_session.delete(user)
    db_session.commit()


# Тест на изменение пользователя
def test_update_user(db_session):
    user = db_session.query(User).filter_by(user_id=1).first()
    new_email = 'updated_user@example.com'
    user.user_email = new_email
    db_session.commit()

    updated_user = db_session.query(User).filter_by(user_id=1).first()

    # Проверка, что email был обновлен
    assert updated_user.user_email == new_email, "Email пользователя не обновлен"

    # Возврат к исходному значению
    user.user_email = 'user1@example.com'
    db_session.commit()


# Тест на удаление пользователя
def test_delete_user(db_session):
    user_to_delete = db_session.query(User).filter_by(user_id=2).first()
    db_session.delete(user_to_delete)
    db_session.commit()

    deleted_user = db_session.query(User).filter_by(user_id=2).first()

    # Проверка, что пользователь был удален
    assert deleted_user is None, "Пользователь не был удален"
