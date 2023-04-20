# ! pip install konlp
# ! pip install gensim
# ! pip install re

from konlpy.tag import Kkma 
from konlpy.utils import pprint 
from konlp.kma.klt2000 import klt2000
import re

import gensim
from gensim.models import Word2Vec

k = klt2000()

with open(r"extracted_text_korean_only.txt", "r", encoding="utf-8") as file:
    listof_text = file.read()

morphs_data = [k.morphs(listof_text)] 
#print(morphs_data)

model = Word2Vec(sentences=morphs_data, vector_size=100, window=5, min_count=1, workers=4, sg=1)
model.save("word2vec_model")

w2v_dict = {word: model.wv.get_vector(word) for word in model.wv.key_to_index.keys()}
for key, value in w2v_dict.items():
    #print(key)
    with open ("w2v_dict.txt", 'a', encoding="utf-8") as file:
        file.write(key + "\n")

seed_set = ["재미", "슬픔", "충격", "우울", "좋다"]
new_seed_set = []
lengths_of_dictionaries = []

for keyword in seed_set:

    similar_words = model.wv.most_similar(keyword, topn = 100000)
    filtered_words = ((word, similarity) for word, similarity in similar_words if similarity >= 0.99)
    filtered_words_str = '\n'.join(str(word) for word in filtered_words)
    with open("first_dict.txt", "a+") as file:
        file.write(filtered_words_str)

    length_of_dict = 0
    for word, similarity in filtered_words:
        length_of_dict += 1
    with open("lengths_of_disctionaries.txt", "w") as file:
       file.write('\n'.join(lengths_of_dictionaries))

    #print(f"Expanded vocabulary for {keyword}:")
    #print(len(filtered_words))
    #for word, similarity in filtered_words:
    #    print(f"{word} ({similarity:.2f})")
    
with open("first_dict.txt", "r", encoding="utf-8") as file:
    contents = file.read()

new_seed_set = re.findall('[ㄱ-ㅎㅏ-ㅣ가-힣]+', contents)
my_set = set(new_seed_set)
unique_new_seed_set = list(new_seed_set)
# print(new_seed_set)

with open('output.txt', 'w', encoding='utf-8') as f:
    for keyword in unique_new_seed_set:
        if keyword in model.wv.key_to_index:
            similar_words = model.wv.most_similar(keyword, topn=100000)
            filtered_words = [(word, similarity) for word, similarity in similar_words if similarity >= 0.99]
            f.write(f'{keyword}: {filtered_words}\n')

with open("output.txt", "r", encoding="utf-8") as file:
    new = file.read()

final_dict = re.findall('[ㄱ-ㅎㅏ-ㅣ가-힣]+', new)
new_set = set(final_dict)
unique_final_dict = list(set(new_set))

with open("final_dict.txt", 'wb') as f:
        for word in unique_final_dict:
            f.write(bytes(word + '\n', encoding='utf-8'))
