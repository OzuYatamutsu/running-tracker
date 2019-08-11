from runningtracker.db_interface import _init_db, _get_db, DATABASE_NAME
from unittest import TestCase
from sqlite3 import connect
from pathlib import Path
from os import unlink


class TestSchema(TestCase):
    def setUp(self) -> None:
        self.db_schemas = [
            str(ddl_file.absolute())
            for ddl_file in Path('.').parent.joinpath('database').iterdir()
            if (
                str(ddl_file).startswith('schema') and
                str(ddl_file).endswith('.sql')
            )
        ]
        self.test_database_name = 'UNIT_TEST.db'

    def test_all_schemas_are_valid(self):
        ddl = ""
        for schema_file in self.db_schemas:
            with open(schema_file) as f:
                ddl = f.read()

            connect(self.test_database_name).cursor().executescript(ddl)
            unlink(self.test_database_name)
            assert True
        assert True

    def test_can_init_latest_schema_version(self):
        try:
            _init_db(connect(self.test_database_name))
        except Exception as e:
            unlink(self.test_database_name)
            raise

    def test_can_get_valid_db_object_against_latest_schema_version(self):
        try:
            db = _get_db()
            assert not not db
            assert not not db.cursor().execute("SELECT 'Hello, world'")
        except Exception as e:
            unlink(DATABASE_NAME)
            raise

    def tearDown(self) -> None:
        try:
            unlink(self.test_database_name)
            unlink(DATABASE_NAME)
        except:  # noqa
            pass
