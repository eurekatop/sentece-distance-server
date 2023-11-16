from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer, util
import Levenshtein
import os
from config import config
import numpy as np

app = Flask(__name__)

env = os.environ.get('FLASK_ENV', 'development')
if env == 'production':
    config = config.ProductionConfig()
else:
    config = config.DevelopmentConfig()



# Cargar el modelo de embeddings
model = SentenceTransformer('../hiiamsid/sentence_similarity_spanish_es')
#model2 = SentenceTransformer('../models/all-MiniLM-L12-v2')
#model2 = SentenceTransformer('../models/distiluse-base-multilingual-cased-v1')
#model2 = SentenceTransformer('../models/multi-qa-MiniLM-L6-cos-v1')


@app.route('/similarity', methods=['POST'])
def calculate_similarity():
    try:
        # Obtener las oraciones desde la solicitud
        data = request.json
        #sentence1 = "Is The product :" + data['sentence2'] + " only is made of without another ingredients?"
        sentence1 = "És el producto :" + data['sentence2'] + " solamente compuesto de sin otros ingredientes ni añadidos, siendo el siguiente el único ingrediente principal?"
        #sentence1 = "És el producto :" + data['sentence2'] + " solamente compuesto de " + data['sentence1'] + "sin otros ingredientes ni añadidos, siendo el siguiente el único ingrediente principal, es el base de ?"
        sentence2 = "Sólo es " + data['sentence1']

        # Obtener el algoritmo de similitud (por defecto, usa cosine)
        similarity_algorithm = data.get('similarity_algorithm', 'cosine')
        
        sentence11 = "Está el producto " + data['sentence2'] + " únicamente compuesto de, sin añadidos : "
        sentence22 = data['sentence1']



        # Calcular la similitud usando el algoritmo especificado
        if similarity_algorithm == 'cosine':
            embeddings = model.encode([sentence1, sentence2, sentence11, sentence22])
            #embeddings2 = model2.encode([sentence11, sentence22])


            measure = data.get('measure', 'cos_sim')



            if measure == 'cos_sim':
                similarity_score = util.pytorch_cos_sim(embeddings[0], embeddings[1]).item()
            elif measure == 'pairwise_cos_sim':
                similarity_score = util.pairwise_cos_sim(embeddings[0],
                                         embeddings[1]).item()
            elif measure == 'dot_score':
                similarity_score = util.dot_score(embeddings[0], embeddings[1]).item()
            elif measure == 'heuristic':
                similarity_score_1 = util.pytorch_cos_sim(embeddings[0], embeddings[1]).item()
                similarity_score_2 = util.pytorch_cos_sim(embeddings[2], embeddings[3]).item()
                similarity_score_3 = util.pytorch_cos_sim(embeddings[0], embeddings[3]).item()

                similarity_score = (similarity_score_1 + similarity_score_2 + similarity_score_3) / 3


                #similarity_score_1 = util.pytorch_cos_sim(embeddings2[0], embeddings2[1]).item()
                #similarity_score = (similarity_score * 2 + similarity_score_1) / 2

                if data['sentence2'].startswith(data['sentence1']):
                    similarity_score = similarity_score*10;



            else:
                measure = 'unknown'
                similarity_score = util.dot_score(embeddings[0], embeddings[1]).item()
        elif similarity_algorithm == 'levenshtein_distance':
            similarity_score = Levenshtein.distance(sentence1, sentence2)
        else:
            return jsonify({'error': 'Algoritmo de similitud no válido'}), 400

        return jsonify({'similarity_score': similarity_score, 'xsentence2':data['sentence2'], 'xmeasure':measure})
        

    except Exception as e:
        return jsonify({'error': str(e)}), 500


print ( config )

if __name__ == '__main__':
    app.run(debug=config.DEBUG)
