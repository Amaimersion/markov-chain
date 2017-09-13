class Creation(object):
    """The creation module for inheritance.

    Functions:
        create:
            assign the chain.

        create_append:
            append the chain.

        _creation:
            creating the chain.
    """

    def create(self):
        """Assign the chain to the self._chain."""
        if self._chain:
            self._chain = {}
        self._creation()

    def create_append(self):
        """Append the chain to the self._chain."""
        self._creation()

    def _creation(self):
        """Creating the chain.

        Creating the Markov chain based on self._data.
        The chain will assigned to the self._chain.

        Note: [
            "*START* text_1 *END* *TEXT_END*",
            "*START* text_2 *END* *TEXT_END*"
        ]
        text_2 - another text.

        In this way, a words from text_1
        WILL NOT BE UNITED with a words from text_2.

        Raises:
            ValueError:
                The data is empty.

        Examples:
            self._data: [
                "*START* One fish two fish red fish blue fish. *END* *TEXT_END*"
            ]
            self._chain: {
                'blue': ['fish.'], 
                'fish.': ['*END*'], 
                '*START*': ['One'], 
                '*END*': ['*TEXT_END*'], 
                'fish': ['two', 'red', 'blue'], 
                'two': ['fish'], 
                'One': ['fish'], 
                'red': ['fish']
            }
        """
        if not self._data:
            raise ValueError("data is empty")

        create_elements = lambda array, count, array_i=0, count_i=0: (
            array[i + array_i] for i in range(count + count_i)
        )

        self._chain[self.start] = []

        for text in self._data:
            for i in range(len(text) - self.window):
                elements = list(create_elements(text, self.window, i, 1))
                word = elements[-1]

                # adding a words for self.start key.
                if elements[0] == self.start:
                    key = " ".join(create_elements(elements, self.window, 1))
                    self._chain[self.start].append(key)

                key = " ".join(create_elements(elements, self.window))

                if (key in self._chain) and (key != self.start):
                    self._chain[key].append(word)
                elif key != self.start:
                    self._chain[key] = [word]
