class Interaction(object):
    """The interaction module for inheritance.

    User interaction with the Markov chain.

    Functions:
        getter and setter for self._data.

        getter and setter for self._chain.
    """

    def __init__(self, name=None, **kwargs):
        """Creating a new instance of the MarkovChain.

        Args:
            name (str):
                Defaults to None.
                The name of the instance.

            **start (str):
                Defaults to "*START*".
                The start word of a sentence.

            **end (str):
                Defaults to "*END*".
                The end word of a sentence.

            **text_end (str):
                Defaults to "*TEXT_END*".
                The end word of the text.

            **window (int):
                Defaults to 1.
                Count of window for the chain.

            **data (list):
                Defaults to [].
                The data for creating the Markov Chain.

                Warning: be careful with change of this parameter.

                It should be a (list) which contain the values (list).
                The values contain text (str) separated by comma.

            **chain (dict):
                Defaults to {}.
                The Markov Chain.

                Warning: be careful with change of this parameter.

                It should be a (dict) with the keys (str) which contain 
                the values (list). 
                The value contain the text (str) separated by comma.
        """
        super(Interaction, self).__init__()
        self.name = name
        self.start = kwargs.get("start", "*START*")
        self.end = kwargs.get("end", "*END*")
        self.text_end = kwargs.get("text_end", "*TEXT_END*")
        self.window = kwargs.get("window", 1)
        self._data = kwargs.get("data", [])
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
