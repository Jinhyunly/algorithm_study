import sys

words = sys.stdin.readline().rstrip().upper()

unique_words = list(set(words))
count_list = []

for word in unique_words:
  count_list.append(words.count(word))

if count_list.count(max(count_list)) > 1:
  print('?')
else:
 print(unique_words[count_list.index(max(count_list))])