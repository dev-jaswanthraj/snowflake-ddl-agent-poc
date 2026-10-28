

import pytest

from ddl_agent.generator import generate_ddl


def test_valid_ddl():
    sql = generate_ddl(
        "customer_stage",
        [{"name": "customer_id", "type": "NUMBER"}, {"name": "name", "type": "VARCHAR"}],
    )
    assert "CREATE TABLE IF NOT EXISTS CUSTOMER_STAGE" in sql
    assert "CUSTOMER_ID NUMBER" in sql


@pytest.mark.parametrize("table", ["customer;DROP TABLE X", "bad name", "a.b"])
def test_rejects_unsafe_table_identifier(table):
    with pytest.raises(ValueError):
        generate_ddl(table, [{"name": "id", "type": "NUMBER"}])


def test_rejects_unsafe_type():
    with pytest.raises(ValueError):
        generate_ddl("customers", [{"name": "id", "type": "NUMBER); DROP TABLE X; --"}])


def test_rejects_duplicate_columns():
    with pytest.raises(ValueError):
        generate_ddl(
            "customers",
            [{"name": "id", "type": "NUMBER"}, {"name": "ID", "type": "NUMBER"}],
        )


def test_rejects_empty_columns():
    with pytest.raises(ValueError):
        generate_ddl("customers", [])
