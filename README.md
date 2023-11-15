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



