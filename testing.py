#readfile = open('mystery1.txt')
#text = readfile.readlines()
#readfile.close()

def split_on_separators(original, separators):
    """ (str, str) -> list of str

    Return a list of non-empty, non-blank strings from original,
    determined by splitting original on any of the separators.
    separators is a string of single-character separators.

    >>> split_on_separators("Hooray! Finally, we're done.", "!,")
    ['Hooray', ' Finally', " we're done."]
    """
    
    result = [original]
    
    # Cycles through the set of separators individually    
    for string in result:    
        split_words = []
        for separator in separators:

    # Cycle through the strings in the list of strings from result

    # Extends the list split_words with the strings split at separator
            split_words.extend(string.split(separator))
    # result is now the list of strings split with separator
        result = split_words
    return result