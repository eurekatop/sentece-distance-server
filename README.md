⚠️ This repo is for experimental purposes / PoC only.
# sentece-distance-server

#using 
https://huggingface.co/hiiamsid/sentence_similarity_spanish_es

Clone the repo inside ./hiiamsid

# Make sure you have git-lfs installed (https://git-lfs.com)
git lfs install
git clone https://huggingface.co/hiiamsid/sentence_similarity_spanish_es


#prod
gunicorn -w 4 --chdir ./src 'service:app'

#test
curl -X POST http://127.0.0.1:5000/similarity \
--header "Content-Type: application/json" \
--data '{"sentence1":"En el amor siempre hay algo de locura, y en la locura siempre hay algo de razón","sentence2":"No quiero que más nadie me hable de amor, ya me cansé, to esos trucos ya me los sé", "similarity_algorithm":"cosine"}'


curl -X POST http://127.0.0.1:5000/similarity \
--header "Content-Type: application/json" \
--data '{"sentence1":"Si lo intentas, a menudo estarás solo, y a veces asustado","sentence2":"Si lo intentas, a menudo estarás solo, y a veces atemorizado"}'


curl -X POST http://127.0.0.1:5000/similarity \
--header "Content-Type: application/json" \
--data '{"sentence1":"Si lo intentas, a menudo estarás solo, y a veces asustado","sentence2":"Si lo intentas, a menudo estarás solo, y a veces atemorizado", "similarity_algorithm":"levenshtein_distance"}'


curl -X POST http://127.0.0.1:5000/similarity \
--header "Content-Type: application/json" \
--data '{"sentence1":"Si lo intentas, a menudo estarás solo, y a veces asustado","sentence2":"Si lo intentas, a menudo estarás solo, y a veces atemorizado", "similarity_algorithm":"cosine", "measure":"dot_product"}'

curl -X POST http://127.0.0.1:5000/similarity \
--header "Content-Type: application/json" \
--data '{"sentence1":"Si lo intentas, a menudo estarás solo, y a veces asustado","sentence2":"Si lo intentas, a menudo estarás solo, y a veces atemorizado", "similarity_algorithm":"cosine", "measure":"pairwise_cos_sim"}'

curl -X POST http://127.0.0.1:5000/similarity \
--header "Content-Type: application/json" \
--data '{"sentence1":"Si lo intentas, a menudo estarás solo, y a veces asustado","sentence2":"Si lo intentas, a menudo estarás solo, y a veces atemorizado", "similarity_algorithm":"cosine", "measure":"cos_sim"}'




# USING
    
    ## BERT
    - https://huggingface.co/hiiamsid/sentence_similarity_spanish_es
    
    ## SBERT
    - https://www.sbert.net/docs/pretrained_models.html
        - Model: 
          - https://huggingface.co/sentence-transformers/all-MiniLM-L12-v2
          - https://huggingface.co/sentence-transformers/distiluse-base-multilingual-cased-v1   
          - https://huggingface.co/sentence-transformers/multi-qa-MiniLM-L6-cos-v1


