words_num = int(input())
words_list = []

for _ in range(words_num):
    word = str(input())
    word_count = len(word)
    words_list.append((word_count, word))
print(words_list)
#중복 삭제
words_list = list(set(words_list))
print(words_list)
#단어 숫자 정렬 > 단어 알파벳 정렬
words_list.sort()
print(words_list)
for word in words_list:
    print(word[1])