import json


class Json(object):
    """Work with a json file.

    Functions:
        save:
            save the data in a file.

        read:
            read the data from a file.
    """

    @staticmethod
    def save(data, path):
        """Save the data in a file.

        Args:
            data (dict):
                the data for write.

            path (str):
                a path to the file.
        """
        with open(path, 'w', encoding="utf-8") as file:
            data = json.dumps(data, ensure_ascii=False)
            file.write(data)

    @staticmethod
    def read(path):
        """Read the data from a file.

        Args:
            path (str):
                a path to the file.

        Returns:
            type - dict.
            The file data.
        """
        with open(path, 'r', encoding="utf-8") as file:
            return json.load(file)
