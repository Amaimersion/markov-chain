class Initialization(object):
    """The initialization module for inheritance.

    Functions:
        init:
            assign a data.

        _initialization:
            creation a data.

        _create_elements:
            creation an elements.
    """

    def init(self, data):
        """Assign a data to the self._data.

        Note: this overwrites the self._data.

        Args:
            data (any iterable type).
        """
        if self._data:
            self._data = ()

        self._data = self._initialization(data)

    def _initialization(self, data):
        """Initialization of the data.

        The data is converted to the data for creating the Markov chain.

        Warning: a data should not be a pure str type.
        At least it should be (str,) or [str].

        If it will be pure str type, then each char from the
        data will be interpreted as an individual text.

        Note: the self._data will be a generator.

        So, if it used once, then it should be initializated again.

        Args:
            data (any iterable type):
                a data for creating the Markov Chain.

        Raises:
            TypeError:
                a data not iterable type.

        Returns:
            type - generator.
            The created data.
        """
        if not hasattr(data, "__iter__"):
            raise TypeError("data should be an iterable type")

        return (self._create_elements(text) for text in data)

    def _create_elements(self, text):
        """Creation an elements.

        Creates a elements for the data.

        Note: the text splitting into sentences by ". " chars.

        In this way, "4. Some text" will be converted to the
        "*START* 4. *END* *START* Some text *END* *TEXT_END*".

        Args:
            text (str):
                a text for creating the data.

        Returns:
            type - tuple.
            The created elements.

        Examples:
            Input: "One fish two fish red fish blue fish."
            Output: (
                '*START*', 'One', 'fish', 'two', 'fish',
                'red', 'fish', 'blue', 'fish.', '*END*', '*TEXT_END*'
            )
        """
        elements = (
            ". {end} {start} "
        ).format(
            end=self.end,
            start=self.start
        ).join(
            text.split(". ")
        ).split()

        elements.insert(0, self.start)
        elements.extend([self.end, self.text_end])

        return elements
