# Генератор текста.
Генератор текста, который основан на алгоритме цепи Маркова. Python 3 скрипт генерирует псевдослучайный текст, который основан на порядке слов в другом тексте.

#### Узнайте больше о цепи Маркова (этот проект основан на этих ресурсах):
  - [EN](https://hackernoon.com/from-what-is-a-markov-model-to-here-is-how-markov-models-work-1ac5f4629b71)
  - [RU](https://tproger.ru/translations/markov-chains/)

#### Обратите внимание: эта реализация цепи Маркова чувствительна к регистру и чувствительна к пунктуации.

Вы можете прочитать это на других языках: [English](README.md).

[Журнал изменений](CHANGELOG.ru.md).


## Возможности
  - генерация псевдослучайного текста.
  - работа с файлами.


## Установка
Легчайший способ начать - это скачать этот репозиторий.

```python
from markov_chain import MarkovChain

chain = MarkovChain()
chain.init(["One fish two fish red fish blue fish."])
chain.create()
print(chain.generate())
```

Для удовлетворительного результата нужна большая текстовая база. Вы можете использовать [эту](https://yadi.sk/d/dM1Ogbav3MrXZv) текстовую базу или создать свою собственную.


## Руководство
Для полного понимания я рекомендую прочитать ресурсы, которые были приведены выше. Сейчас я кратко объясню логику программы.

#### Логика генерации
Во время генерации случайное слово выбирается на основе предыдущего слова. В предложении "One fish two fish red fish blue fish." после слова "fish" идут следующие слова: "two", "red", "blue". В этом случае, после слова "fish" будет выбрано одно из этих слов с вероятностью 1/3. Предположим, что было выбрано слово "blue". Какое слово идет после "blue"? Именно, слово "fish"! (Обратите внимание: "fish" != "fish."). Следующее слово - "fish". Что идет после "fish"? После "fish" текст заканчивается и ничего больше. Поэтому шанс закончить текст 1/1 или 100%.

Вы можете проследить эту последовательность самостоятельно:
```python
"*START* One fish two fish red fish blue fish. *END* *TEXT_END*"

{'One': ['fish'], '*END*': ['*TEXT_END*'], 'two': ['fish'], '*START*': ['One'], 'fish': ['two', 'red', 'blue'], 'red': ['fish'], 'blue': ['fish.'], 'fish.': ['*END*']}
```

#### Окно
На самом деле "окно" - это количество предыдущих слов. Последний пример содержал одно окно. В предложении "One fish two fish red fish blue fish." после слов "fish red" идет следующее слово: "fish.". После "red fish": "blue" -> "fish blue": "fish.", "blue fish." -> текст заканчивается.

Чем больше размер окна, тем больше корректность генерации. Корректность - смысл предложения.

Вы можете проследить эту последовательность самостоятельно:
```python
"*START* One fish two fish red fish blue fish. *END* *TEXT_END*"

{'*START* One': ['fish'], 'fish two': ['fish'], 'fish red': ['fish'], 'blue fish.': ['*END*'], 'fish. *END*': ['*TEXT_END*'], 'fish blue': ['fish.'], 'red fish': ['blue'], 'two fish': ['red'], 'One fish': ['two'], '*START*': ['One fish']}
```


## API Reference
  - #### MarkovChain instance:
  
    ##### Аргументы:
    
      - ``name (str)``:
    
        По умолчанию ``None``.
      
        Имя экземпляра.

      - ``**start (str)``:
    
        По умолчанию ``"*START*"``.
      
        Начальное слово предложения.

      - ``**end (str)``:
     
        По умолчанию ``"*END*"``.
       
        Конечное слово предложения.

      - ``**text_end (str)``:
      
        По умолчанию ``"*TEXT_END*"``.
        
        Конечное слово текста.

      - ``**window (int)``:
      
        По умолчанию ``1``.
        
        Число окон для цепи.

      - ``**data (любой итерируемый тип)``:
      
        По умолчанию ``()``.
        
        Данные для создания цепи.

        Предупреждение: будьте осторожны с изменением этого параметра.

        Это должен быть (любой итерируемый тип), который содержит значения (list or tuple). Значения содержат текст (str), который разделен запятой.

      - ``**chain (dict)``:
      
        По умолчанию ``{}``.
        
        Цепь Маркова.

        Предупреждение: будьте осторожны с изменением этого параметра.

        Это должен быть (dict) с ключами (str), который содержит значения (list or tuple). Значения содержат текст (str), который разделен запятой.
  
  - #### init():
  
    ##### Аргументы:
  
      - ``data (любой итерируемый тип)``:
    
        Данные для создания цепи Маркова.
      
  - #### create()
      
  - #### generate():
  
    ##### Аргументы:
  
      - ``**start (str)``:
    
        По умолчанию ``self.start``.
      
        Начало предложения.

        Предупреждение: цепь чувствительна к регистру и чувствительна к пунктуации.

      - ``**max_words (int)``:
    
        По умолчанию ``20``.
      
        Максимальное количество слов в предложении.

      - ``**max_length (int)``:
    
        По умолчанию ``max_words * 10``.
      
        Максимальное количество символов в предложении.

      - ``**punctuation (bool)``:
    
        По умолчанию ``True``.
      
        Проверка пунктуации. True - включить. False - выключить.

        Note: если False, то следующие параметры не будут работать.

      - ``**end_chars (str)``:
     
        По умолчанию ``".!?"``.
       
        Символы, которые должны стоять в конце предложения.

      - ``**not_end_chars (str)``:
     
        По умолчанию ``','``.
       
        Символы, которые не должны стоять в конце предложения. Они будут заменены **end_char символом.

      - ``**end_char (str)``:
      
        По умолчанию ``'.'``.
        
        Если последний символ предложения не в **end_chars, то **end_char будет присоединен к концу предложения.
        
    ##### Возвращает:
     
      тип - ``str``.
      
      Если **start найден, то текст будет сгенерирован. 
      
      Иначе текст будет равен **start.
  

## Расширения
Расширения расширяют базовые возможности цепи Маркова.

#### Список расширений:
| Имя           | Путь             | Описание           |
| ------------- |:---------------: | :-----------------:|
| File          | .extensions/file | Работа с файлами.  |

#### File API Reference:
  - #### SQLiteFile instance:

    ##### Аргументы:
      - ``name (str)``:
    
        По умолчанию ``None``.
      
        Имя экземпляра.

      - ``**path (str)``:
    
        Путь к базе данных SQLite.

    ##### Методы:
      - ``generate()``

  - #### file.json:
    - #### save():
    
      ##### Аргументы:
      
        - ``data (dict)``:
        
          данные для записи.

        - ``path (str)``:
      
          путь к файлу.
    
    - #### read():
     
      ##### Аргументы: 
       
        - ``path (str)``:
      
          путь к файлу.
           
      ##### Возвращает:
       
        тип - ``dict``.
          
        Данные файла.

  - #### file.pickle:
    - #### save():
    
      ##### Аргументы:
      
        - ``data (dict)``:
        
          данные для записи.

        - ``path (str)``:
      
          путь к файлу.
    
    - #### read():
     
      ##### Аргументы: 
       
        - ``path (str)``:
      
          путь к файлу.
           
      ##### Возвращает:
       
        тип - ``dict``.
          
        Данные файла.

  - #### file.sqlite:
    - #### save():
    
      ##### Аргументы:
      
        - ``data (dict)``:
        
          данные для записи.

        - ``path (str)``:
      
          путь к файлу.
     

## Примеры корректного использования

#### Обычное использование

```python
from markov_chain import MarkovChain

chain = MarkovChain("Simple test MarkovChain instance")
chain.init(["One fish two fish red fish blue fish."])
chain.create()
print(chain.generate())
```

#### Аргументы экземпляра

```python
from markov_chain import MarkovChain

chain = MarkovChain("Hard test MarkovChain instance", window=2)
chain.init(("Today you are you. That is truer than true. There is no one alive who is you-er than you.",))
chain.create()
print(chain.generate())
```

#### Аргументы генерации

```python
from markov_chain import MarkovChain

text = (i for i in ("You have brains in your head. You have feet in your shoes. You can steer yourself any direction you choose. You're on your own.", "The more that you read, the more things you will know. The more that you learn, the more places youll go."))

chain = MarkovChain("Insane test MarkovChain instance")
chain.init(text)
chain.create()
print(chain.generate(start="You", max_words=10))
```

#### Файлы JSON/PICKLE/SQLITE

```python
from markov_chain import MarkovChain, extensions

chain = MarkovChain()
test_json = extensions.file.json.read("markov_chain/examples/common/text.json")
chain.init(test_json["text"]["simple"])
chain.create()
print(chain.generate())
extensions.file.json.save(chain.chain, "test_json.json")
```

#### Экземпляр SQLiteFile

```python
from markov_chain import extensions

chain = extensions.file.SQLiteFile(path="test_sqlite.sqlite")
print(chain.generate())
```

#### JSON из [текстовой базы](https://yadi.sk/d/dM1Ogbav3MrXZv)

```python
from markov_chain import MarkovChain, extensions

chain = MarkovChain()
text = extensions.file.json.read("pr.json")
chain.init(text["messages"])
chain.create()
print(chain.generate())
```


## Примеры некорректного использования

#### Чувствительность к регистру

```python
from markov_chain import MarkovChain

chain = MarkovChain("Hard test MarkovChain instance")
chain.init(["Today you are you. That is truer than true. There is no one alive who is you-er than you."])
chain.create()
print(chain.generate(start="You"))
```
      
#### Количество стартовых слов != количество окон

```python
from markov_chain import MarkovChain

chain = MarkovChain("Hard test MarkovChain instance", window=2)
chain.init(["Today you are you. That is truer than true. There is no one alive who is you-er than you."])
chain.create()
print(chain.generate(start="You"))
```  


## Сотрудничество
Pull requests всегда приветствуются.


## Лицензия
Лицензия MIT

Copyright (c) 2017 Сергей Кузнецов

Данная лицензия разрешает лицам, получившим копию данного программного обеспечения и сопутствующей документации (в дальнейшем именуемыми «Программное Обеспечение»), безвозмездно использовать Программное Обеспечение без ограничений, включая неограниченное право на использование, копирование, изменение, слияние, публикацию, распространение, сублицензирование и/или продажу копий Программного Обеспечения, а также лицам, которым предоставляется данное Программное Обеспечение, при соблюдении следующих условий:

Указанное выше уведомление об авторском праве и данные условия должны быть включены во все копии или значимые части данного Программного Обеспечения.

ДАННОЕ ПРОГРАММНОЕ ОБЕСПЕЧЕНИЕ ПРЕДОСТАВЛЯЕТСЯ «КАК ЕСТЬ», БЕЗ КАКИХ-ЛИБО ГАРАНТИЙ, ЯВНО ВЫРАЖЕННЫХ ИЛИ ПОДРАЗУМЕВАЕМЫХ, ВКЛЮЧАЯ ГАРАНТИИ ТОВАРНОЙ ПРИГОДНОСТИ, СООТВЕТСТВИЯ ПО ЕГО КОНКРЕТНОМУ НАЗНАЧЕНИЮ И ОТСУТСТВИЯ НАРУШЕНИЙ, НО НЕ ОГРАНИЧИВАЯСЬ ИМИ. НИ В КАКОМ СЛУЧАЕ АВТОРЫ ИЛИ ПРАВООБЛАДАТЕЛИ НЕ НЕСУТ ОТВЕТСТВЕННОСТИ ПО КАКИМ-ЛИБО ИСКАМ, ЗА УЩЕРБ ИЛИ ПО ИНЫМ ТРЕБОВАНИЯМ, В ТОМ ЧИСЛЕ, ПРИ ДЕЙСТВИИ КОНТРАКТА, ДЕЛИКТЕ ИЛИ ИНОЙ СИТУАЦИИ, ВОЗНИКШИМ ИЗ-ЗА ИСПОЛЬЗОВАНИЯ ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ ИЛИ ИНЫХ ДЕЙСТВИЙ С ПРОГРАММНЫМ ОБЕСПЕЧЕНИЕМ.
