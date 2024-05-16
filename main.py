def main():
    characters = set()
    wordcount=0
    sortenddict={}
    enddict={}
    with open("books/frankenstein.txt") as f:
        text = f.read()
        words = text.lower()
        wordsplit = words.split()
        wordcount = len(wordsplit)
        print (wordcount)
        words = [*words]
        characters.update(words)
        for char in characters:
            if char.isalpha():
                count = 0
                for i in range(0,len(words)):
                    if words[i] == char: count+=1
                enddict[char] = count
    
    
    def short(item):
        return item[1]

    sortenddict=sorted(enddict.items(), key=short, reverse=True)

    print("--- Begin report of books/frankenstein.txt ---")
    print(wordcount, " words found in the document")
    for letter in sortenddict:
        print(f"The '{letter[0]}' character was found {letter[1]} times")
    print("--- End report ---")

    


main()