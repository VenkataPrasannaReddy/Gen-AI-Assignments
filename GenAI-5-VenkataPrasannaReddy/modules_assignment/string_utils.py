def capitalize_words(text):
    list_of_words=text.split(" ")
    for i in range(len(list_of_words)):
        list_of_words[i]=list_of_words[i].capitalize()
    return " ".join(list_of_words)
def reverse_string(text):
    return text[::-1]
def word_count(text):
    list_of_words=text.split(" ")
    return len(list_of_words)