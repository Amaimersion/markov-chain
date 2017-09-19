class Interaction(object):
    """The interaction module for inheritance.

    User interaction with a Markov chain.

    Functions:
        getter and setter for the self._data.

        getter and setter for the self._chain.
    """

    def __init__(self, name=None, **kwargs):
        """Creates a new instance of the MarkovChain.

        Args:
            name (str):
                Defaults to None.
                A name of an instance.

            **start (str):
                Defaults to "*START*".
                A start word of a sentence.

            **end (str):
                Defaults to "*END*".
                An end word of a sentence.

            **text_end (str):
                Defaults to "*TEXT_END*".
                An end word of a text.

            **window (int):
                Defaults to 1.
                Count of window for a chain.

            **data (any iterable type):
                Defaults to ().
                A data for creating the Markov Chain.

                Warning: be careful with change of this parameter.

                It should be an (any iterable type) which contain a values (list or tuple).
                The values contain a text (str) separated by a comma.

            **chain (dict):
                Defaults to {}.
                The Markov Chain.

                Warning: be careful with change of this parameter.

                It should be a (dict) with a keys (str) which contain a values (list or tuple).
                The values contain a text (str) separated by a comma.
        """
        super(Interaction, self).__init__()
        self.name = name
        self.start = kwargs.get("start", "*START*")
        self.end = kwargs.get("end", "*END*")
        self.text_end = kwargs.get("text_end", "*TEXT_END*")
        self.window = kwargs.get("window", 1)
        self._data = kwargs.get("data", ())
        self._chain = kwargs.get("chain", {})

    @property
    def data(self):
        """Return the data."""
        return self._data

    @data.setter
    def data(self, value):
        """Allows to set the data."""
        self._data = value

    @property
    def chain(self):
        """Return the chain."""
        return self._chain

    @chain.setter
    def chain(self, value):
        """Allows to set the chain."""
        self._chain = value
