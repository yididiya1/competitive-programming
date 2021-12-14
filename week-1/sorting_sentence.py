def sortSentence(s):
        words = s.split(" ")
        ordered_words = [""]*len(words)
        for i in words:
            word = str(i)
            final_word = word[:-1]
            index = word[-1]
            ordered_words[int(index)-1] = final_word
            
       
        joined_string = ' '.join([str(w) for w in ordered_words])
        return joined_string

example = sortSentence("is2 sentence4 This1 a3")
print(example)