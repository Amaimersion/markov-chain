import pickle


class Pickle(object):
    """Work with a pickle file.

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
        with open(path, "wb") as file:
            pickle.dump(data, file)

    @staticmethod
    def read(path):
        """Reads the data from the pickle file.

        Args:
            path (str):
                the path to the file.

        Return:
            type - dict. File data.
        """
        with open(path, "rb") as file:
            return pickle.load(file)
            