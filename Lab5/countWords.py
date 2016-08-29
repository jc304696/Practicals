sentence = input("Type a sentence here: ")
words_in_sentence = sentence.split()
my_dict = {}

for word in words_in_sentence:
    if word in my_dict:
        my_dict[word] += 1
    else:
        my_dict[word] = 1

largest_word = max(len(word) for word in words_in_sentence)
for word in sorted(my_dict):
    print("{:{}} : {}".format(word,largest_word,my_dict[word]))



