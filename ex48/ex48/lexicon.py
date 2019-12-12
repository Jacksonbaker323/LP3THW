def scan(sentence):
    #Accept a string as an argument
    #Create an array to return all of the necessary information
    results = []
    
    #split that string into an array
    split_string = sentence.split(" ")
    
    #look for any direction words in the array
    for word in split_string:
        if word.lower() in ('north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back'):
            results.append(('direction', word))
        elif word.lower() in ('go', 'kill', 'eat', 'stop'):
            results.append(('verb', word))
        elif word.lower() in ('the', 'in', 'of', 'from', 'at', 'it'):
            results.append(('stop', word))
        elif word.lower() in ('bear', 'princess'):
            results.append(('noun', word))
        elif word.isdigit():
            results.append(('number', word))
        else:
            results.append(('error', word))
    #return all the direction words as an array of tuples with 'direction' and the direction
    return results