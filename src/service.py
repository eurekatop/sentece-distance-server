from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer, util
import Levenshtein

app = Flask(__name__)

# Cargar el modelo de embeddings
model = SentenceTransformer('../hiiamsid/sentence_similarity_spanish_es')

@app.route('/similarity', methods=['POST'])
def calculate_similarity():
    try:
        # Obtener las oraciones desde la solicitud
        data = request.json
        sentence1 = data['sentence1']
        sentence2 = data['sentence2']

        # Obtener el algoritmo de similitud (por defecto, usa cosine)
        similarity_algorithm = data.get('similarity_algorithm', 'cosine')

        # Calcular la similitud usando el algoritmo especificado
        if similarity_algorithm == 'cosine':
            embeddings = model.encode([sentence1, sentence2])
            similarity_score = util.pytorch_cos_sim(embeddings[0], embeddings[1]).item()
        elif similarity_algorithm == 'levenshtein_distance':
            similarity_score = Levenshtein.distance(sentence1, sentence2)
        else:
            return jsonify({'error': 'Algoritmo de similitud no válido'}), 400

        return jsonify({'similarity_score': similarity_score})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
