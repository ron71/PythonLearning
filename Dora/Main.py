import  shelve
from random import randint


while True:
    query = input().lower()
    testQuery = query 
    # We made copy of the query to work to change the test query in keys for better searching
    check = False
    with shelve.open('src/DoraShelve') as src:
        # Searching each directory key in query
        for keys in src['directory']:
            if keys in query:
                query = keys
                check = True
                break
        if check:
            print(src['replyDictionary'][query][0])
        else:
            # if nothing matches in shelve Randomly pick the reply from 'nothingToSay'
            print(src['nothingToSay'][randint(0,len(src['nothingToSay'])-1)])
