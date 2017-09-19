class Creation(object):
    """The creation module for inheritance.

    Functions:
        create:
            assign a chain.

        _creation:
            creation a chain.

        _create_text:
            creation a text.
    """

    def create(self):
        """Assign a chain to the self._chain.

        Note: this overwrites the self._chain.
        """
        if self._chain:
            self._chain = {}

        self._creation()

        # self._data now is an empty generator.
        self._data = ()

    def _creation(self):
        """Creation of the chain.

        Creating the Markov chain based on self._data.

        Note: (
            "*START* text_1 *END* *TEXT_END*",
            "*START* text_2 *END* *TEXT_END*"
        )
        text_2 is another text.

        In this way, a words from text_1
        WILL NOT BE UNITED with a words from text_2.

        Raises:
            ValueError:
                the self._data is empty.
        """
        if not self._data:
            raise ValueError("data is empty")

        self._chain[self.start] = []

        [self._create_text(text) for text in self._data]

    def _create_text(self, text):
        """Creation a text.

        Fills up the self._chain.

        Warning: a text should not be a pure str type.
        At least it should be (str,) or [str].

        Args:
            text (any iterable type):
                a data for the self._chain.

        Examples:
            self._data: (
                "*START* One fish two fish red fish blue fish. *END* *TEXT_END*",
            )
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
        create_elements = lambda text, count, text_i=0, count_i=0: [
            text[i + text_i] for i in range(count + count_i)
        ]

        for i in range(len(text) - self.window):
            elements = create_elements(text, self.window, i, 1)
            word = elements[-1]

            # adding a words for the self.start key.
            if elements[0] == self.start:
                key = " ".join(create_elements(elements, self.window, 1))
                self._chain[self.start].append(key)

            key = " ".join(create_elements(elements, self.window))

            if (key != self.start) and (key in self._chain):
                self._chain[key].append(word)

            elif key != self.start:
                self._chain[key] = [word]
