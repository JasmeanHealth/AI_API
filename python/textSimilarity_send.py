from multiprocessing.connection import Listener, Client
import pandas as pd
import sys

address = ('localhost', 6000)     # family is deduced to be 'AF_INET'
print('road excel')
df = pd.read_excel('../data/211225_data_summary_v1.xlsx')
doc_list = df['clincal_imp'].to_list()

from sentence_transformers import SentenceTransformer, util
print('road model')
model = SentenceTransformer('paraphrase-distilroberta-base-v1')

print('embeding data')
embeddings = model.encode(doc_list, convert_to_tensor=True)

def getTS(word = '갑자기 배가 아파요'):
    word2vec = model.encode(word, convert_to_tensor=True)
    scores = util.pytorch_cos_sim(word2vec, embeddings)
    df['score'] = scores[0]
    results = df.sort_values("score", ascending=False)

    js = results.head(10).to_json(orient='records')
    return js

while True:
    input_text = ''
    try:
        with Client(address, authkey=b'secret password') as conn:
            input_text = conn.recv()                  # => [2.25, None, 'junk', float]
            print(input_text)

        with Listener(address, authkey=b'secret password') as listener:
            with listener.accept() as conn:
                print('connection accepted from', listener.last_accepted)
                result = getTS(input_text) 
                conn.send(result)

    except ConnectionRefusedError:
        print('대기')