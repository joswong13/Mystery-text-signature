##########  Provided helper function. ############

def clean_up(s):
    """ (str) -> str

    Return a new string based on s in which all letters have been
    converted to lowercase and punctuation characters have been stripped 
    from both ends. Inner punctuation is left untouched. 

    >>> clean_up('Happy Birthday!!!')
    'happy birthday'
    >>> clean_up("-> It's on your left-hand side.")
    " it's on your left-hand side"
    """
    
    punctuation = """!"',;:.-?)([]<>*#\n\t\r"""
    result = s.lower().strip(punctuation)
    return result

def clean_lists(text):
    ''' (list of string) -> list of string
    
    Precondition: text is list of string.
    
    Return a new list of string based on text which converts the list of string
    to list of words that has been stripped of punctuation and converted to 
    lowercase.
    
    >>> clean_lists(['James Fennimore Cooper\n', 'Peter, Paul and Mary\n'])
    ['james', 'fennimore', 'cooper', 'peter', 'paul', 'and', 'mary']
    
    >>> clean_lists(['And why the sea is boiling hot;\n',
         'and whether pigs have wings.\n'])
    ['and', 'why', 'the', 'sea', 'is', 'boiling', 'hot', 'and', 'whether', 
    'pigs', 'have', 'wings']    
    
    '''
    
    clean_words = []
    
    # #########################################################################
    # For each string in list, split the string into list of words and call
    # function clean_up to remove punctuation and lowercase the letters.
    # Then append words to list and return list of words.
    # #########################################################################
    
    for strings in text:
        words = strings.split()
        for i in range(len(words)):
            results = clean_up(words[i])
            if not results == '':
                clean_words.append(results)
    return clean_words


##########  Complete the following functions. ############

def avg_word_length(text):
    """ (list of str) -> float

    Precondition: text is non-empty. Each str in text ends with \n and
    text contains at least one word.

    Return the average length of all words in text. 
    
    >>> text = ['James Fennimore Cooper\n', 'Peter, Paul and Mary\n']
    >>> avg_word_length(text)
    5.142857142857143 
    
    >>> text = ['The average word length of this sentence\n', 'should be\n']
    >>> avg_word_length(text)
    4.666666666666667
    """
    
    average_words = 0
    
    # Separating the list of strings into list of words
    clean_words = clean_lists(text)
    
    # #########################################################################    
    # For each word in clean_words, take the length of each word and divide by
    # the total number of words.
    # #########################################################################
    
    for x in range(len(clean_words)):
            average_words = average_words + len(clean_words[x])
    return (average_words / len(clean_words))
   
    

def type_token_ratio(text):
    """ (list of str) -> float

    Precondition: text is non-empty. Each str in text ends with \n and
    text contains at least one word.

    Return the Type Token Ratio (TTR) for this text. TTR is the number of
    different words divided by the total number of words.

    >>> text = ['James Fennimore Cooper\n', 'Peter, Paul, and Mary\n',
        'James Gosling\n']
    >>> type_token_ratio(text)
    0.8888888888888888
    
    >>> text = ['Row, Row, Row your boat, gentley down the stream\n']
    >>> type_token_ratio(text)
    0.7777777777777778
    """

    append_tokens = []
    
    # Separating the list of strings into list of words
    clean_words = clean_lists(text)
    
    # For each token in the list of clean_words, append token once to 
    # accumulator and then dividie by the total number of words.
    
    for tokens in clean_words:
        if tokens not in append_tokens:
            append_tokens.append(tokens)
    return len(append_tokens) /  len(clean_words)
            

    
                
def hapax_legomena_ratio(text):
    """ (list of str) -> float

    Precondition: text is non-empty. Each str in text ends with \n and
    text contains at least one word.

    Return the hapax legomena ratio for text. This ratio is the number of 
    words that occur exactly once divided by the total number of words.

    >>> text = ['James Fennimore Cooper\n', 'Peter, Paul, and Mary\n',
    'James Gosling\n']
    >>> hapax_legomena_ratio(text)
    0.7777777777777778
    
    >>> text = ['Row, Row, Row your boat, gentley down the stream\n']
    >>> hapax_legomena_ratio(text)
    0.6666666666666666
    """

    first_tokens = []
    more_than_once_tokens = []
    
    # Separating the list of strings into list of words
    clean_words = clean_lists(text)
    
    # #########################################################################
    # The following code appends the words from clean_words into a first_tokens
    # for the first time they appear. If the words appear more times after the
    # first, they are appended into the more_than_once_tokens list only once.
    # The difference is taken between the tokens that appear once (first_tokens)
    # and tokens that appear more than once (more_than_once_tokens).
    # #########################################################################
    
    for tokens in clean_words:
        if tokens not in first_tokens:
            first_tokens.append(tokens)
        elif tokens not in more_than_once_tokens:
            more_than_once_tokens.append(tokens)
    return (len(first_tokens) - len(more_than_once_tokens)) /  len(clean_words)    



def split_on_separators(original, separators):
    """ (str, str) -> list of str

    Return a list of non-empty, non-blank strings from original,
    determined by splitting original on any of the separators.
    separators is a string of single-character separators.

    >>> split_on_separators("Hooray! Finally, we're done.", "!,")
    ['Hooray', ' Finally', " we're done."]
    
    >>> split_on_separators("Row, Row, Row your boat", ".!,")
    ['Row', ' Row', ' Row your boat']
    """
    
    result = [original]
    
    # Cycles through the set of separators individually    
    for separator in separators:
        split_words = []
        
    # #########################################################################
    # Cycle through the strings in the list of strings from result. Extends the 
    # list split_words with the strings split at separator. result is now 
    # the list of strings split with separator.
    # #########################################################################    
        
        for string in result:
            split_words.extend(string.split(separator))    
        result = split_words
    return result
                
    
def avg_sentence_length(text):
    """ (list of str) -> float

    Precondition: text contains at least one sentence.
    
    A sentence is defined as a non-empty string of non-terminating 
    punctuation surrounded by terminating punctuation or beginning or 
    end of file. Terminating punctuation is defined as !?.

    Return the average number of words per sentence in text.   

    >>> text = ['The time has come, the Walrus said\n',
         'To talk of many things: of shoes - and ships - and sealing wax,\n',
         'Of cabbages; and kings.\n',
         'And why the sea is boiling hot;\n',
         'and whether pigs have wings.\n']
    >>> avg_sentence_length(text)
    17.5
    
    >>> text = ['Row! Row, Row your boat. Gentley down the stream?\n']
    >>> avg_sentence_length(text)
    3.0
    """

    number_of_sentences = 0
    
    # Joins the list of strings into a single string and remove the right space.
    strings = ' '.join(text).rstrip()
    
    # Seperates the single string into a list of strings based on separators
    # and puts the result in a list of sentences.
    list_of_sentences = split_on_separators(strings, "!?.")
    
    clean_words = clean_lists(list_of_sentences)
    
    # Number of sentences accumulator
    for sentences in list_of_sentences:
        if not sentences == '':
            number_of_sentences += 1
    return len(clean_words) /  number_of_sentences

    

def avg_sentence_complexity(text):
    """ (list of str) -> float

    Precondition: text contains at least one sentence.    

    A sentence is defined as a non-empty string of non-terminating
    punctuation surrounded by terminating punctuation or beginning or
    end of file. Terminating punctuation is defined as !?.
    Phrases are substrings of sentences, separated by one or more of ,;:

    Return the average number of phrases per sentence in text.

    >>> text = ['The time has come, the Walrus said\n',
         'To talk of many things: of shoes - and ships - and sealing wax,\n',
         'Of cabbages; and kings.\n',
         'And why the sea is boiling hot;\n',
         'and whether pigs have wings.\n']
    >>> avg_sentence_complexity(text)
    3.5
    
    >>> text = ['The place was full, and they wandered about looking \n'
    'for a table, catching odds and ends of conversation as they did so.\n']
    >>> avg_sentence_complexity(text)
    3.0
    """
    
    number_of_sentences = 0
    phrases = []
    
    # Joins the list of strings into a single string and remove the right space.
    strings = ' '.join(text).rstrip()
    
    # Seperates the single string into a list of strings based on separators
    # and puts the result in a list of sentences.    
    list_of_sentences = split_on_separators(strings, "!?.") 
    
    # #########################################################################
    # For each sentence in the list_of_sentences, accumulates the number of 
    # sentences and extends the list phrases with strings separated by 
    # separator.
    # #########################################################################
    
    for sentence in list_of_sentences:
        if not sentence == '':
            number_of_sentences += 1
            phrases.extend(split_on_separators(sentence, ",;:"))
    return len(phrases) / number_of_sentences
    
    
def compare_signatures(sig1, sig2, weight):
    """ (list, list, list of float) -> float

    Return a non-negative float indicating the similarity of the two 
    linguistic signatures, sig1 and sig2. The smaller the number the more
    similar the signatures. Zero indicates identical signatures.
    
    sig1 and sig2 are 6-item lists with the following items:
    0  : Author Name (a string)
    1  : Average Word Length (float)
    2  : Type Token Ratio (float)
    3  : Hapax Legomena Ratio (float)
    4  : Average Sentence Length (float)
    5  : Average Sentence Complexity (float)

    weight is a list of multiplicative weights to apply to each
    linguistic feature. weight[0] is ignored.

    >>> sig1 = ["a_string" , 4.4, 0.1, 0.05, 10.0, 2.0]
    >>> sig2 = ["a_string2", 4.3, 0.1, 0.04, 16.0, 4.0]
    >>> weight = [0, 11.0, 33.0, 50.0, 0.4, 4.0]
    >>> compare_signatures(sig1, sig2, weight)
    12.000000000000007
    
    >>> sig1 = ["a_string" , 4.8, 0.1, 0.03, 20.0, 3.0]
    >>> sig2 = ["a_string2", 4.9, 0.2, 0.07, 19.0, 4.0]
    >>> weight = [0, 11.0, 33.0, 50.0, 0.4, 4.0]
    >>> compare_signatures(sig1, sig2, weight)
    10.800000000000006
    """
    # Cycles through each item in list to calculate value for linguistic 
    # signatures and adds the value to accumulator
    
    comparison = 0
    for i in range(1, len(sig1)):
        comparison = comparison + (abs(sig1[i] - sig2[i]) * weight[i])
    return comparison

