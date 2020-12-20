"""Idea taken from https://www.notion.so/Analogies-Generator-9b046963f52f446b9bef84aa4e416a4c"""

import os
import sys
#sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(r'C:\\Users\\Mohamed Sabri\\Desktop\Bullying-Project\gpt3-sandbox-master'))))

pip install -r Desktop/Bullying-Project/gpt3-sandbox-master/api/requirements.txt --user

sys.path.insert(1, r'C:\Users\Mohamed Sabri\Desktop\Bullying-Project\gpt3-sandbox-master')

os.environ["OPENAI_CONFIG"] = 'C:/Users/Mohamed Sabri/Desktop/Bullying-Project/gpt3-sandbox-master/openai.cfg'

from api import GPT, Example, UIConfig
from api import demo_web_app

import pandas as pd

bully_main = pd.read_csv(r'Desktop\Bullying-Project\bully_main.csv')

# Construct GPT object and show some examples
gpt = GPT(engine="davinci",
          temperature=0.5,
          max_tokens=100)

gpt.add_example(Example('Neural networks are like',
                        'genetic algorithms in that both are systems that learn from experience.'))
gpt.add_example(Example('Social media is like',
                        'a market in that both are systems that coordinate the actions of many individuals.'))
gpt.add_example(Example(
    'A2E is like', 'lipofuscin in that both are byproducts of the normal operation of a system.'))
gpt.add_example(Example('Haskell is like',
                        'LISP in that both are functional languages.'))
gpt.add_example(Example('Quaternions are like',
                        'matrices in that both are used to represent rotations in three dimensions.'))
gpt.add_example(Example('Quaternions are like',
                        'octonions in that both are examples of non-commutative algebra.'))

# Define UI configuration
config = UIConfig(description="Analogies generator",
                  button_text="Generate",
                  placeholder="Memes are like")

demo_web_app(gpt, config)

print(gpt.get_top_reply(prompt))

#! set OPENAI_CONFIG=/Desktop/Bullying-Project/gpt3-sandbox-master/openai.cfg


import os
import sys

sys.path.insert(1, r'C:\Users\Mohamed Sabri\Desktop\Bullying-Project\gpt3-sandbox-master')

os.environ["OPENAI_CONFIG"] = 'C:/Users/Mohamed Sabri/Desktop/Bullying-Project/gpt3-sandbox-master/openai.cfg'

from api import GPT, Example, UIConfig
from api import demo_web_app

# Construct GPT object and show some examples
gpt = GPT(engine="davinci",
          temperature=0.5,
          max_tokens=100)

# Define UI configuration
config = UIConfig(description="Analogies generator",
                  button_text="Generate",
                  placeholder="Memes are like")

demo_web_app(gpt, config)
