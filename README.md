# Text generator
The text generator based on the Markov Chain algorithm. The Python 3 script generates a pseudo random text based on arrangement of words in an another text.

#### Learn more about the Markov Chain (this project based on this resources):
  - [EN](https://hackernoon.com/from-what-is-a-markov-model-to-here-is-how-markov-models-work-1ac5f4629b71)
  - [RU](https://tproger.ru/translations/markov-chains/)

#### Note: this implementation of the Markov Chain is case-sensitive and punctuation-sensitive.

You can read this in other languages: [Русский](README.ru.md).

[Changelog](CHANGELOG.md).


## Features
  - generation of a pseudo random text.
  - work with a files.


## Installation
The easiest way to get started is download the this repository.

```python
from markov_chain import MarkovChain

chain = MarkovChain()
chain.init(["One fish two fish red fish blue fish."])
chain.create()
print(chain.generate())
```

For a satisfactory result, a large text base is needed. You can use [this](https://yadi.sk/d/dM1Ogbav3MrXZv) text base or create your own.


## Guide
For full understanding, I recommend reading the resources that were given above. Now I will briefly describe the logic of the program.

#### Generation logic
During generation, a next word is selected based on a previous word. In the sentence "One fish two fish red fish blue fish." after a "fish" word goes the next words: "two", "red", "blue". So, after a "fish" will be selected one of this words with a chance 1/3. Suppose that the "blue" word was selected. What word goes after the "blue"? Yes, the "fish." word! (Note: "fish" != "fish."). So, the next word is the "fish.". That goes after the "fish."? After the "fish." the text is ends and nothing more. So, the chance of finish the text is 1/1 or 100%.

You can trace this sequence yourself:
```python
"*START* One fish two fish red fish blue fish. *END* *TEXT_END*"

{'One': ['fish'], '*END*': ['*TEXT_END*'], 'two': ['fish'], '*START*': ['One'], 'fish': ['two', 'red', 'blue'], 'red': ['fish'], 'blue': ['fish.'], 'fish.': ['*END*']}
```

#### Window
A "window" is actually count of previous words. The last example was a one-window chain. In the sentence "One fish two fish red fish blue fish." after the "fish red" word goes the next word: "fish". After the "red fish": "blue" -> "fish blue": "fish.", "blue fish." -> text is ends.

The higher a number of windows, the higher a correctness of generation. Correctness is a meaning of a sentence.

You can trace this sequence yourself:
```python
"*START* One fish two fish red fish blue fish. *END* *TEXT_END*"

{'*START* One': ['fish'], 'fish two': ['fish'], 'fish red': ['fish'], 'blue fish.': ['*END*'], 'fish. *END*': ['*TEXT_END*'], 'fish blue': ['fish.'], 'red fish': ['blue'], 'two fish': ['red'], 'One fish': ['two'], '*START*': ['One fish']}
```


## API Reference
  - #### MarkovChain instance:
  
    ##### Args:
    
      - ``name (str)``:
    
        Defaults to ``None``.
      
        A name of an instance.

      - ``**start (str)``:
    
        Defaults to ``"*START*"``.
      
        A start word of a sentence.

      - ``**end (str)``:
     
        Defaults to ``"*END*"``.
       
        An end word of a sentence.

      - ``**text_end (str)``:
      
        Defaults to ``"*TEXT_END*"``.
        
        An end word of a text.

      - ``**window (int)``:
      
        Defaults to ``1``.
        
        Count of window for a chain.

      - ``**data (any iterable type)``:
      
        Defaults to ``()``.
        
        A data for creating the Markov Chain.

        Warning: be careful with change of this parameter.

        It should be an (any iterable type) which contain a values (list or tuple). The values contain a text (str) separated by a comma.

      - ``**chain (dict)``:
      
        Defaults to ``{}``.
        
        The Markov Chain.

        Warning: be careful with change of this parameter.

        It should be a (dict) with a keys (str) which contain a values (list or tuple). The values contain a text (str) separated by a comma.
  
  - #### init():
  
    ##### Args:
  
      - ``data (any iterable type)``:
    
        A data for creating the Markov Chain.
      
  - #### create()
      
  - #### generate():
  
    ##### Args:
  
      - ``**start (str)``:
    
        Defaults to ``self.start``.
      
        Start of a sentence.

        Warning: the chain is case-sensitive and punctuation-sensitive.

      - ``**max_words (int)``:
    
        Defaults to ``20``.
      
        The maximum number of words in a sentence.

      - ``**max_length (int)``:
    
        Defaults to ``max_words * 10``.
      
        The maximum number of chars in a sentence.

      - ``**punctuation (bool)``:
    
        Defaults to ``True``.
      
        Punctuation check. True - turn on. False - turn off.

        Note: if False, then the next parameters will not work.

      - ``**end_chars (str)``:
     
        Defaults to ``".!?"``.
       
        A chars which should stand at the end of a sentence.

      - ``**not_end_chars (str)``:
     
        Defaults to ``','``.
       
        A chars which should not stand at the end of a sentence. They will be replaced by **end_char.

      - ``**end_char (str)``:
      
        Defaults to ``'.'``.
        
        If a last char of a sentence is not in **end_chars, then the **end_char will be appended to the end of a sentence.
        
    ##### Returns:
     
      type - ``str``.
      
      If **start will found, then a text will be generated.

      Else a text will be equal to **start.
  

## Extensions
An extensions expand a basic capabilities of the Markov Chain.

#### List of an extensions:
| Name          | Path             | Description        |
| ------------- |:---------------: | :-----------------:|
| File          | .extensions/file | Work with a files. |

#### File API Reference:
  - #### SQLiteFile instance:

    ##### Args:
      - ``name (str)``:
    
        Defaults to ``None``.
      
        The name of the instance.

      - ``**path (str)``:
    
        Path to the SQLite database.

    ##### Methods:
      - ``generate()``

  - #### file.json:
    - #### save():
    
      ##### Args:
      
        - ``data (dict)``:
        
          the data for write.

        - ``path (str)``:
      
          a path to the file.
    
    - #### read():
     
      ##### Args: 
       
        - ``path (str)``:
      
          a path to the file.
           
      ##### Returns:
       
        type - ``dict``.
          
        The file data.

  - #### file.pickle:
    - #### save():
    
      ##### Args:
      
        - ``data (dict)``:
        
          the data for write.

        - ``path (str)``:
      
          a path to the file.
    
    - #### read():
     
      ##### Args: 
       
        - ``path (str)``:
      
          a path to the file.
           
      ##### Returns:
       
        type - ``dict``.
          
        The file data.

  - #### file.sqlite:
    - #### save():
    
      ##### Args:
      
        - ``data (dict)``:
        
          the data for write.

        - ``path (str)``:
      
          a path to the file.
     

## Examples of correct usage

#### Basic usage

```python
from markov_chain import MarkovChain

chain = MarkovChain("Simple test MarkovChain instance")
chain.init(["One fish two fish red fish blue fish."])
chain.create()
print(chain.generate())
```

#### Instance arguments

```python
from markov_chain import MarkovChain

chain = MarkovChain("Hard test MarkovChain instance", window=2)
chain.init(("Today you are you. That is truer than true. There is no one alive who is you-er than you.",))
chain.create()
print(chain.generate())
```

#### Generation arguments

```python
from markov_chain import MarkovChain

text = (i for i in ("You have brains in your head. You have feet in your shoes. You can steer yourself any direction you choose. You're on your own.", "The more that you read, the more things you will know. The more that you learn, the more places youll go."))

chain = MarkovChain("Insane test MarkovChain instance")
chain.init(text)
chain.create()
print(chain.generate(start="You", max_words=10))
```

#### JSON/PICKLE/SQLITE File

```python
from markov_chain import MarkovChain, extensions

chain = MarkovChain()
test_json = extensions.file.json.read("markov_chain/examples/common/text.json")
chain.init(test_json["text"]["simple"])
chain.create()
print(chain.generate())
extensions.file.json.save(chain.chain, "test_json.json")
```

#### SQLiteFile Instance

```python
from markov_chain import extensions

chain = extensions.file.SQLiteFile(path="test_sqlite.sqlite")
print(chain.generate())
```

#### JSON from the [text base](https://yadi.sk/d/dM1Ogbav3MrXZv)

```python
from markov_chain import MarkovChain, extensions

chain = MarkovChain()
text = extensions.file.json.read("pr.json")
chain.init(text["messages"])
chain.create()
print(chain.generate())
```


## Examples of incorrect usage

#### Case-sensitive

```python
from markov_chain import MarkovChain

chain = MarkovChain("Hard test MarkovChain instance")
chain.init(["Today you are you. That is truer than true. There is no one alive who is you-er than you."])
chain.create()
print(chain.generate(start="You"))
```
      
#### Number of the start words != number of the windows

```python
from markov_chain import MarkovChain

chain = MarkovChain("Hard test MarkovChain instance", window=2)
chain.init(["Today you are you. That is truer than true. There is no one alive who is you-er than you."])
chain.create()
print(chain.generate(start="You"))
```  


## Contributing
Pull requests are always welcome.


## License
The MIT License (MIT)

Copyright (c) 2017 Sergey Kuznetsov

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
