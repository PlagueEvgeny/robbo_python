import os
import time

start_time = time.time()

def get_words(filename):
    with open(filename, encoding="utf8") as file:
        text = file.read()
    text = text.replace("\n", " ")
    text = text.replace(',', '').replace('.',  '').replace('?', '').replace('!','')
    text = text.lower()
    words = text.split()
    words.sort()
    return words

def get_words_dict(words):
    words_dict = dict()

    for word in words:
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
            print("--- %s seconds ---" % (time.time() - start_time))
        else:
            words_dict[word] = 1
    return words_dict

def main():
    filename = input()
    if not os.path.exists(filename):
        print("File error")
    else:
        words = get_words(filename)
        words_dict = get_words_dict(words)
        print(f"Кол-во слов: {len(words)}")
        print(f"Кол-во уникальных слов: {len(words_dict)}")
        print("Все слова:")
        for word in words_dict:
            print(word.ljust(20), words_dict[word])

        print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()

        
        
    
