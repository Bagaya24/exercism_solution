def count_words(sentence: str):
    caracteres = "!&@$%^,._?#$*():;<>/"
    new_sentence = sentence
    for caractere in caracteres:
        if caractere in new_sentence:
            new_sentence = new_sentence.replace(caractere, " ")
            
    sentence_list = sorted(new_sentence.split())
    words_count = {}
    
    for word in sentence_list:
        the_word = word
        while the_word.startswith("'"):
            the_word = the_word[1:]
        while the_word.endswith("'"):
            the_word = the_word[:-1]
        if the_word.startswith('"') or the_word.endswith('"'):
            the_word = word.replace('"', "")
            

        if the_word:
            if the_word.lower() in words_count.keys():
                words_count[the_word.lower()] += 1
            else:
                words_count[the_word.lower()] = 1
    return words_count

