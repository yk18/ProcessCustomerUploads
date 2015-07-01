__author__ = 'ykogan'

import ReadMongoDB
import ReadCustomerUploads
import re

existing_models = ReadMongoDB.read_mongodb_server_models()

#for existing_model in existing_models:
#    print(existing_model)

uploaded_models = ReadCustomerUploads.read_server_models()

matching_models = dict()
for uploaded_model in uploaded_models:
    umodel_name = str(uploaded_model).upper()
    umodel_words = [x for x in re.split('\W+', umodel_name) if x != '']
    for existing_model in existing_models:
        emodel_name = str(existing_model).upper()
        emodel_words = [x for x in re.split('\W+', emodel_name) if x != '']
        model_match = list(set(umodel_words) & set(emodel_words))
        if len(model_match) == len(umodel_words):
            matching_models["_".join(sorted(umodel_words))] = 'Exists'
            break
        elif len(model_match) > 0:
            if ("_".join(sorted(umodel_words)) in matching_models):
                temp_set = re.split("\W+", str(matching_models["_".join(sorted(umodel_words))]))
                if (len(temp_set) >= len(matching_models)):
                    continue

            matching_models["_".join(sorted(umodel_words))] = "Partial match (" + "_".join(sorted(model_match)) + ")"
            #print ("_".join(sorted(umodel_words)), "Partial match (" + "_".join(sorted(model_match)) + ")")
            #print(" with ",  "_".join(sorted(emodel_words)))

    if (not "_".join(sorted(umodel_words)) in matching_models):
            matching_models["_".join(sorted(umodel_words))] = 'No match at all'

print ("========= EXISTING MODELS\n")
for model in dict(filter(lambda x: x[1] == "Exists" ,matching_models.items())):
    print(model)

print ("\n========= PARTIALLY MATCHED MODELS\n")
for model in dict(filter(lambda x: str(x[1]).find("Partial match") == 0 ,matching_models.items())):
    print(model, str(matching_models[model]).replace("Partial match ",""))


print ("\n========= MISSING MODELS\n")
for model in dict(filter(lambda x: x[1] == "No match at all" ,matching_models.items())):
    print(model)

