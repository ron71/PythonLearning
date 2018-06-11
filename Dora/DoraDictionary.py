import shelve

directory = {'hi' : ['hi dora', 'hi', 'hello', 'hello dora', 'hey dora'],
             'what':['your name','your age', 'my age', 'sex', 'kiss'],
             'what\'s':['your name','your age', 'my age', 'sex', 'kiss'],
             'whats':['your name','your age', 'my age', 'sex', 'kiss']}

replyDictionary = {'hi' : ['Hello I am Dora :). How can I help you ?'],
                   'your name': 'I am glad you asked! My name is Dora.',
                   'your age': 'Ha ha, You are too funny. I was not born, I was Programmed :)',
                   'sex': 'What you wanna know about sex?',
                   'kiss': 'Come on, Try it'}

nothingToSay = ['Sorry, I didn\'t get that. Please be more specific', 'Sorry, don\'t understood. Try to ask again',
                'are you writing in an alien language coz I didn\'t get this.']
try:
    with shelve.open('src/DoraShelve') as src:
        src['directory'] = directory
        src['replyDictionary'] = replyDictionary
        src['nothingToSay'] = nothingToSay
except FileNotFoundError:
    print('Error : File Not found')
