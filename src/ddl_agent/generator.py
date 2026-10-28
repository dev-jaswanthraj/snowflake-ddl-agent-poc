"""Deterministic DDL generator for a small approved type subset.

In production, validate LLM-produced mapping documents before using this renderer.
"""
import re

IDENTIFIER = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
ALLOWED_TYPES = {"VARCHAR", "NUMBER", "DATE", "TIMESTAMP_NTZ", "BOOLEAN", "FLOAT"}


def _identifier(value: str) -> str:
    if not isinstance(value, str) or not IDENTIFIER.fullmatch(value):
        raise ValueError(f"Invalid SQL identifier: {value!r}")
    return value.upper()


def generate_ddl(table: str, columns: list[dict[str, str]]) -> str:
    """Render CREATE TABLE from a vetted mapping, without executing it."""
    table_name = _identifier(table)
    if not columns:
        raise ValueError("At least one column is required")
    seen: set[str] = set()
    definitions = []
    for column in columns:
        name = _identifier(column["name"])
        data_type = column["type"].upper()
        if data_type not in ALLOWED_TYPES:
            raise ValueError(f"Unsupported SQL type: {data_type}")
        if name in seen:
            raise ValueError(f"Duplicate column: {name}")
        seen.add(name)
        definitions.append(f"    {name} {data_type}")
    return f"CREATE TABLE IF NOT EXISTS {table_name} (\n" + ",\n".join(definitions) + "\n);"

def _change_check():
    """
    Checking for the snowflake is connected with Github
    """
    pass
