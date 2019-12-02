def scan(sentence):
    #Accept a string as an argument
    #Create an array to return all of the necessary information
    results = []
    
    #split that string into an array
    split_string = sentence.lower().split(" ")
    
    #look for any direction words in the array
    for word in split_string:
        if word in ('north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back'):
            results.append(('direction', word))
        elif word in ('go', 'kill', 'eat', 'stop'):
            results.append(('verb', word))
        elif word in ('the', 'in', 'of', 'from', 'at', 'it'):
            results.append(('stop', word))
    #return all the direction words as an array of tuples with 'direction' and the direction
    return results