import torch
import numpy as np
import openai

from transformers import AutoModelForSequenceClassification

new_model = AutoModelForSequenceClassification.from_pretrained('./model/')
# new_model = new_model.to('cuda')

from transformers import AutoTokenizer

new_tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')

def get_prediction(text):
    encoding = new_tokenizer(text, return_tensors="pt", padding="max_length", truncation=True, max_length=128)
    print(encoding)
    # encoding = encoding["input_ids"]
    # print(encoding)
    # for k, v in encoding.items():
    #     print(k, v)
    # print(encoding.items())
    # print(encoding.items())
    # encoding = new_tokenizer.tokenize(text)
    # encoding = new_tokenizer.convert_tokens_to_ids(encoding)
    # encoding = {k: v.to('cuda') for k ,v in encoding.items()}


    outputs = new_model(**encoding)
    print(outputs)
    # logits = outputs[0]
    # predictions = torch.argmax(logits, dim=1)
    # print(predictions)
    # print(outputs)
    logits = outputs.logits
    print(logits)

    sigmoid = torch.nn.Sigmoid()
    probs = sigmoid(logits.squeeze().cpu())
    probs = probs.detach().numpy()
    print(probs)
    label = np.argmax(probs, axis=-1)

    print(probs)
    print(label)

    if label == 1:
        return {
            'advertisement': 1,
            'probability': probs[1]
        }
    else:
        return {
            'advertisement': 0,
            'probability': probs[0]
        }


get_prediction('Such a fun night celebrating Margarita Day with @cointreau - the highlight was definitely catching up with the gorgeous @aesha_jean 💗💗💗 #ad')




def AnalyseDescription(description_text):
    openai.api_key = "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"

    brand = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content":f"analyse this instagram description and identify any potential brands and products that might be advertised on the post, '${description_text}'. write your response just and only as a python list containing only potential brands and product name, do not include in your response any other data"}]
    )
    return(brand)

print(AnalyseDescription("Such a fun night celebrating Margarita Day with @cointreau - the highlight was definitely catching up with the gorgeous @aesha_jean 💗💗💗"))