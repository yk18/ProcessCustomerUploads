__author__ = 'ykogan'

import ReadMongoDB
import re
import numpy as np
import pandas as pd
import numexpr
import ReadCustomerUploads
import ListServerModels

#existing_models = MongoDB.read_mongodb_server_models()
existing_models = ReadCustomerUploads.read_server_models()

known_series = ListServerModels.getKnownSeries()
known_models = ListServerModels.getKnownModels()
known_generations = ListServerModels.getKnownGenerations()
words_to_skip = ListServerModels.getWordsToSkip()

all_words = dict()
rev_all_words = dict()

w2w = np.zeros([2000,2000])
df = pd.DataFrame(columns=("Series", "Model", "Generation", "SKU", "Description"))


for existing_model in existing_models:

    emodel_name = str(existing_model).upper()
    emodel_words = [x for x in re.split('\W+', emodel_name) if x != '']

    for word in emodel_words:
        if (not word in all_words):
            all_words[word] = len(all_words)
            rev_all_words[all_words[word]] = word

    series = ""
    model = ""
    generation = ""
    sku = ""

    for word in emodel_words:
        if(word in words_to_skip):
            continue
        elif (word in known_series):
            series = word
        elif (word in known_models):
            model = word
        elif (word in known_generations):
            generation = word
        elif (len(word) > 6 and word[0] >= '0' and word[0] <= '9'): # here should come a regex
            sku = word

    if (len(series) + len(model) + len(generation) + len(sku) > 0):
        df.loc[len(df)] = [series, model, generation, sku, existing_model]
#    else:
#        print (existing_model)

pd.set_option('expand_frame_repr', False)
print(len(df))
#print(df.query('Model == ""'))
#print(df[["Series", "Model", "Generation", "SKU"]].query('SKU != ""'))
print(df)
#print (df.query('SKU == "" and Series == "" and Model == ""'))
exit()

#    for word_1 in emodel_words:
#        for word_2 in emodel_words:
#            if (word_1 != word_2):
#                w2w[all_words[word_1]][all_words[word_2]] += 1


#df = pd.DataFrame(columns=("First Word", "Second Word","Frequency"))

#for i in range(1000):
#    for j in range(1000):
#        if (w2w[i][j] > 0):
            #print (rev_all_words[i], rev_all_words[j], w2w[i][j])
#           df.loc[len(df)] = [rev_all_words[i], rev_all_words[j], w2w[i][j]]

#print(df.sort("Frequency", ascending = False))
sum_all = np.sum(w2w, axis=0)
occurs = dict()

for i in range (len(all_words)):
    word = rev_all_words[i]
    occurs[word] = sum_all[i]

#for item in sorted(occurs.items(), key=lambda x:x[1], reverse = True):
#    print(item)

for i in range(len(all_words)):
    for j in range(len(all_words)):
         #if (sum_all[i] == w2w[i][j] and sum_all[j] > w2w[i][j]):
            if (w2w[i][j] > 0 and sum_all[i] < sum_all[j] and len(rev_all_words[i]) > 6 ):
             print(rev_all_words[i], " is a ", rev_all_words[j],  w2w[i][j], sum_all[i], sum_all[j])