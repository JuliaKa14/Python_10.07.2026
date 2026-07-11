from database.db import Session
from sqlalchemy import text

# Позитивный тест: проверяем добавление новой записи в таблицу species


def test_create_species():
    session = Session()

    try:
        # Добавляем тестовую запись с уникальным species_id
        session.execute(
            text(
                """
                INSERT INTO species
                (species_id, type_id, species_name,
                 species_amount, date_start, species_status)
                VALUES
                (9999, 1, 'тестовый вид',
                 5, '2020-01-01', 'active')
                """
            )
        )

        # Сохраняем изменения в базе
        session.commit()

        # Проверяем, что запись появилась
        result = session.execute(
            text(
                """
                SELECT *
                FROM species
                WHERE species_id = 9999
                """
            )
        )

        assert result.fetchone() is not None

    finally:
        # Удаляем тестовую запись после проверки
        session.execute(
            text(
                """
                DELETE FROM species
                WHERE species_id = 9999
                """
            )
        )

        session.commit()
        session.close()

# Позитивный тест: проверяем изменение записи в таблице species


def test_update_species():
    session = Session()

    try:
        # Создаем запись для изменения
        session.execute(
            text(
                """
                INSERT INTO species
                (species_id, type_id, species_name,
                 species_amount, date_start, species_status)
                VALUES
                (9998, 1, 'старое имя',
                 5, '2020-01-01', 'active')
                """
            )
        )

        session.commit()

        # Изменяем название записи
        session.execute(
            text(
                """
                UPDATE species
                SET species_name = 'новое имя'
                WHERE species_id = 9998
                """
            )
        )

        session.commit()

        # Проверяем, что данные изменились
        result = session.execute(
            text(
                """
                SELECT *
                FROM species
                WHERE species_id = 9998
                AND species_name = 'новое имя'
                """
            )
        )

        assert result.fetchone() is not None

    finally:
        # Удаляем созданную запись после теста
        session.execute(
            text(
                """
                DELETE FROM species
                WHERE species_id = 9998
                """
            )
        )

        session.commit()
        session.close()

# Позитивный тест: проверяем удаление записи из таблицы species


def test_delete_species():
    session = Session()

    try:
        # Создаем запись, которую будем удалять
        session.execute(
            text(
                """
                INSERT INTO species
                (species_id, type_id, species_name,
                 species_amount, date_start, species_status)
                VALUES
                (9997, 1, 'удаляемый вид',
                 5, '2020-01-01', 'active')
                """
            )
        )

        session.commit()

        # Удаляем созданную запись
        session.execute(
            text(
                """
                DELETE FROM species
                WHERE species_id = 9997
                """
            )
        )

        session.commit()

        # Проверяем, что записи больше нет
        result = session.execute(
            text(
                """
                SELECT *
                FROM species
                WHERE species_id = 9997
                """
            )
        )

        assert result.fetchone() is None

    finally:
        session.close()
