def count_words(sentence: str):
    caracteres = "!&@$%^,._?#$*():;<>/"
    new_sentence = sentence
    for caractere in caracteres:
        if caractere in new_sentence:
            new_sentence = new_sentence.replace(caractere, " ")
            
    sentence_list = sorted(new_sentence.split())
    words_count = {}
    
    for word in sentence_list:
        while word.startswith("'"):
            word = word[1:]
        while word.endswith("'"):
            word = word[:-1]
        if word.startswith('"') or word.endswith('"'):
            word = word.replace('"', "")
            

        if word:
            if word.lower() in words_count.keys():
                words_count[word.lower()] += 1
            else:
                words_count[word.lower()] = 1
    return words_count

