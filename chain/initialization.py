class Initialization(object):
    """The initialization module for inheritance.

    Functions:
        init:
            assign the data.

        init_append:
            append the data.

        _initialization:
            create the data.
    """
    
    def init(self, data):
        """Assign the data to the self._data."""
        if self._data:
            self._data = []
        self._initialization(data)

    def init_append(self, data):
        """Append the data to the self._data."""
        self._initialization(data)

    def _initialization(self, data):
        """Initialization of the data.
        
        The data is converted to the data for creating the Markov chain.

        Note: the data splitting into the sentences by ". " chars.

        In this way, "3. Some text" will be converted to the
        "*START* 3. *END* *START* Some text *END* *TEXT_END*".

        Args:
            data (list):
                The text for creating the Markov Chain.

        Raises:
            TypeError:
                The data not instance of a list.

        Examples:
            Input: [
                "One fish two fish red fish blue fish."
            ]
            self._data: [
                ['*START*', 'One', 'fish', 'two', 'fish', 
                'red', 'fish', 'blue', 'fish.', '*END*', '*TEXT_END*']
            ]
        """
        if not isinstance(data, list):
            raise TypeError("data should have a list type")

        for text in data:
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

            self._data.append(elements)
