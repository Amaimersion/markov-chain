from .interaction import Interaction
from .initialization import Initialization
from .creation import Creation
from .generation import Generation


class MarkovChain(Interaction, Initialization, Creation, Generation):
    """MarkovChain.

    Note: the Markov chain will be
    case-sensitive and punctuation-sensitive.

    Warning: MarkovChain requires the next modules
    for correct work: Interaction, Initialization,
    Creation, Generation.

    Examples:
        chain = MarkovChain()
        chain.init(("One fish two fish red fish blue fish.",))
        chain.create()
        text = chain.generate()
    """

    pass
