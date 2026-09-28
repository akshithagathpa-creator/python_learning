import random
#choices = {'clover', 'liles', 'tulips', 'rose'}

fortunes = [
    'you are goin to find something so random and precious today',
    'you are goin to have a very good day today',
    'manifesting for you!',
    'you will get over the manchild!!'
    
]

#choices[fortunes]

print("your fortune is: ")
print(random.choices(fortunes))

import time

sentences = [
    "Do you even see me or do you know who I am?",
    "or how do i look now?, you don't like me like that",
    "Come and tell me so much, you beautiful heart, oh I'm gonna listen to you.... please",
    "All the numbers too big can't get out of the game oh i want paint it like you pleaseee",
    "I want to be your decalcomania, I want youuuuu"
]

for sentence in sentences:
    for word in sentence.split():
        print(word, end=" ", flush=True)
        time.sleep(0.4)
    print()   