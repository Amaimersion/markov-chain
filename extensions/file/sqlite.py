import os.path
import random
import sqlite3

try:
    from ...chain.interaction import Interaction
    from ...chain.generation import Generation
except ValueError:
    from chain.interaction import Interaction
    from chain.generation import Generation


class SQLiteFile(Interaction, Generation):
    """Work with a SQLite database.

    Note: this class allows only generation
    based on the data from a SQLite database.

    It's can not be used for initialization
    and creation. Use MarkovChain instead.

    Functions:
        _check_error:
            check errors.

        _create_cursor:
            create connect and create cursor.

        _generate_word:
            get a random word from the SQLite database.
    """

    def __init__(self, name=None, **kwargs):
        super(SQLiteFile, self).__init__()
        self.name = name
        self.path = kwargs.get("path")

    def _check_error(self):
        """Check errors.
        
        Raises:
            ValueError:
                path is empty.

            FileNotFoundError:
                file not found.
        """
        if not self.path:
            raise ValueError("path is empty")

        if not os.path.exists(self.path):
            raise FileNotFoundError("no such file")

        self._create_cursor()

    def _create_cursor(self):
        """Create connect and create cursor."""
        self.connect = sqlite3.connect(self.path)
        self.cursor = self.connect.cursor()

    def _generate_word(self, key):
        """Get a random word from the SQLite database.

        Args:
            key (str):
                the key for the word.

            cursor (sqlite3.Cursor):
                interaction with the database.

        Returns:
            If key was not found - None.
            Otherwise random word - str.
        """
        self.cursor.execute("""
            SELECT id
            FROM keys
            WHERE key = ?
        """, (key,))
        key_id = self.cursor.fetchone()

        if key_id is not None:
            key_id = key_id[0]
        else:
            return None

        self.cursor.execute("""
            SELECT element
            FROM elements
            WHERE key_id = ?
        """, (key_id,))
        elements = self.cursor.fetchall()

        return "".join(random.choice(elements))


class SQLite(object):
    """Work with a SQLite database.

    Functions:
        save:
            save the data to a database.
    """

    @staticmethod
    def save(data, path):
        """Save the data to a database.

        Warning: If something goes wrong,
        then the database will be empty.

        The database doesn't make sense if 
        it will not contain the keys, the elements
        or the indexes. For this reason commit 
        comes after all necessary query.

        Args:
            data (dict):
                the data for write.

            path (str):
                a path to the database.

        Raises:
            FileExistsError:
                file already exists.
        """
        if os.path.exists(path):
            raise FileExistsError("file already exists")

        connect = sqlite3.connect(path)
        cursor = connect.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS keys
            (id INTEGER PRIMARY KEY AUTOINCREMENT, key TEXT)
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS elements
            (key_id INTEGER, element TEXT)
        """)

        # speed up the insert query.
        cursor.execute("PRAGMA synchronous = OFF")
        cursor.execute("PRAGMA journal_mode = OFF")

        values = [((key),) for key in data.keys()]
        cursor.executemany("""
            INSERT INTO keys (key)
            VALUES (?)
        """, values)
        del values

        cursor.execute("""
            SELECT id
            FROM keys
        """)
        id_values = cursor.fetchall()

        values = list(data.values())
        values = [
            (key_id[0], element) 
            for key_id in id_values 
            for element in values[key_id[0] - 1]
        ]
        del id_values
        cursor.executemany("""
            INSERT INTO elements
            VALUES (?, ?)
        """, values)
        del values

        cursor.execute("""
            CREATE INDEX IF NOT EXISTS key_index 
            ON keys (key)
        """)
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS element_index 
            ON elements (key_id)
        """)

        connect.commit()
        connect.close()
