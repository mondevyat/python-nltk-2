import collections
import requests
import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

tags_dict = {
"NN": "Существительное",
"NNP": "Существительное NNp",
"NNS": "Существительное",
"NNPS": "Существительное",

"VB": "Глагол",
"VBG": "Глагол",
"VBD": "Глагол",
"VBN": "Глагол",
"VBP": "Глагол",
"VBZ": "Глагол",

"RB": "Наречие",
"RBR": "Наречие",
"RBS": "Наречие",

"JJ": "Прилагательное",
"JJR": "Прилагательное",
"JJS": "Прилагательное",

"IN": "Предлог",

"RP": "Частица",

"DT": "Определитель",

"UH": "Междометие",

"CC": "coordinating conjunction",
"CD": "cardinal digit",
"EX": "existential there",
"FW": "foreign word",
"LS": "list marker",
"MD": "modal",
"PDT": "predeterminer",
"POS": "possessive ending",
"PRP": "personal pronoun",
"PRP$": "possessive pronoun",
"TO": "infinite marker",
"WDT": "wh-determiner",
"WP": "wh-pronoun",
"WRB": "wh-adverb",
}

URL = 'https://gist.githubusercontent.com/nzhukov/b66c831ea88b4e5c4a044c952fb3e1ae/raw/7935e52297e2e85933e41d1fd16ed529f1e689f5/A%2520Brief%2520History%2520of%2520the%2520Web.txt'

response = requests.get(URL)
text = response.text

result = []

sentences = nltk.sent_tokenize(text)
for sent in sentences:
    result.extend(nltk.pos_tag(nltk.word_tokenize(sent)))

counter = collections.Counter()
for res in result:
    counter[res[1]] += 1

sort = []
for i in range(len(counter)):
    sort.append(counter[list(counter.keys())[i]])
sort.sort(reverse=True)

def get_key(counter, value):
    for k, v in counter.items():
        if v == value:
            return k

name_keys_eng=[]
for j in range(5):
    name_keys_eng.append(get_key(counter, sort[j]))

name_keys_ru=[]
for z in range(5):
    name_keys_ru.append(tags_dict.get(name_keys_eng[z]))

for answer in range(5):
    print(str(answer + 1) + '. ' + name_keys_ru[answer] + ' - ' + str(sort[answer]))