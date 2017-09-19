import random


class Generation(object):
    """The generation module for inheritance.

    Functions:
        generate

        _generation:
            generation of a text.

        _check_errors:
            check for errors.

        _generate_word:
            generation of a word.

        _check_punctuation:
            punctuation check.
    """

    def generate(self, **kwargs):
        return self._generation(**kwargs)

    def _generation(self, **kwargs):
        """Generation of a text.

        Generates a text based on the self._chain.

        Grammar:
            - the first char of a sentence will be capitalized.
            - at the end of a text will be stand **end_char.

        Args:
            **start (str):
                Defaults to self.start.
                Start of a sentence.

                Warning: the chain is case-sensitive
                and punctuation-sensitive.

            **max_words (int):
                Defaults to 20.
                The maximum number of words in a sentence.

            **max_length (int):
                Defaults to max_words * 10.
                The maximum number of chars in a sentence.

            **punctuation (bool):
                Defaults to True.
                Punctuation check.
                True - turn on.
                False - turn off.

                Note: if False, then the next
                parameters will not work.

            **end_chars (str):
                Defaults to ".!?".
                A chars which should stand
                at the end of a sentence.

            **not_end_chars (str):
                Defaults to ','.
                A chars which should not stand
                at the end of a sentence.
                They will be replaced by **end_char.

            **end_char (str):
                Defaults to '.'.
                If a last char of a sentence is not in
                **end_chars, then the **end_char
                will be appended to the end of a sentence.

        Returns:
            type - str.
            If **start will found, then a text will be generated.
            Else a text will be equal to **start.

        Raises:
            see _check_errors doc.

        Examples:
            self._chain = {
                'two': ['fish'],
                'red': ['fish'],
                'One': ['fish'],
                'fish': ['two', 'red', 'blue'],
                '*END*': ['*TEXT_END*'],
                '*START*': ['One'],
                'fish.': ['*END*'],
                'blue': ['fish.']
            }

            generate()
            Output: "One fish blue fish.".

            generate(start="blue")
            Output: "Blue fish".

            case-sensitive:
            generate(start="Fish")
            Output: "Fish".

            punctuation-sensitive:
            generate(start="red", punctuation="!", end_char="!")
            Output: "Red fish two fish two fish blue fish.!"
        """
        self._check_errors()

        key = kwargs.get("start", self.start)
        max_words = kwargs.get("max_words", 20)
        max_length = kwargs.get("max_length", max_words * 10)
        punctuation = kwargs.get("punctuation", True)

        if punctuation:
            end_chars = kwargs.get("end_chars", ".!?")
            not_end_chars = kwargs.get("not_end_chars", ',')
            end_char = kwargs.get("end_char", '.')

        # add a word to the end of a key.
        change_key = lambda key, word: "{} {}".format(key, word)
        # create a key without a first word.
        create_key = lambda key: ' '.join(key.split()[1::])

        # a future sentence.
        words = []

        # if user **start.
        if key != self.start:
            words.append(key.capitalize())
        else:
            # values in self._chain[self.start]
            # can contain the self.start,
            # the self.end or the self.text_end.
            word = self._generate_word(key)
            new_word = (
                ' '.join(
                    word
                    .replace(self.start, '')
                    .replace(self.end, '')
                    .replace(self.text_end, '')
                    .split()
                ).capitalize()
            )
            words.append(new_word)

            max_words -= len(word.split())
            max_length -= len(new_word)
            key = create_key(change_key(key, word))

        word = self._generate_word(key)

        if word is not None:
            capitalize = False

            while (max_words) and (max_length > 0):
                if word == self.text_end:
                    break

                elif word == self.start:
                    key = create_key(change_key(key, word))
                    capitalize = True

                elif word == self.end:
                    key = create_key(change_key(key, word))

                    if punctuation:
                        self._check_punctuation(
                            words, end_chars, not_end_chars, end_char
                        )

                else:
                    if capitalize:
                        words.append(word.capitalize())
                        capitalize = False
                    else:
                        words.append(word)

                    max_words -= 1
                    max_length -= len(word)
                    key = create_key(change_key(key, word))

                word = self._generate_word(key)

        if punctuation:
            self._check_punctuation(
                words, end_chars, not_end_chars, end_char
            )

        return ' '.join(words)

    def _check_errors(self):
        """Check for errors.

        Raises:
            ValueError:
                the self._chain is empty.
        """
        if not self._chain:
            raise ValueError("chain is empty")

    def _generate_word(self, key):
        """Generation of a word.

        Args:
            key (str):
                a key for access to the values
                in the self._chain.

        Returns:
            if key in self._chain:
                type - str.
                The random value.
            else:
                type - None.
        """
        return random.choice(self._chain[key]) if key in self._chain else None

    def _check_punctuation(self, words, end_chars, not_end_chars, end_char):
        """Punctuation check.

        This function changes a list (words).

        Args:
            words (list):
                a list of the words.

            end_chars (str):
                end chars.

            not_end_punct (str):
                not end chars.

            end_char (str):
                a char for the end of the word.
        """
        last_char = ''.join(words[-1][-1])

        if last_char not in end_chars:
            if last_char not in not_end_chars:
                words[-1] = "{}{}".format(words[-1], end_char)
            else:
                words[-1] = "{}{}".format(
                    words[-1][0:len(words[-1]) - 1:],
                    end_char
                )
