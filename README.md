# Stanza

This repository wrap stanford stanza wonderful parser, using docker as a container and fastapi for http requests.
you can change the code inside for determine your desired supported languages.
installing guide:
install docker.

for deployment: (terminal commands)

cd /package/directory/

docker-compose build

docker-compose-up


*And then use following http request:*

Get parsing of an English text:
localhost:8000/en/get_sentence_parsing/?input="YOUR-SENTENCE-HERE"

Get parsing of a Spanish text:
localhost:8000/es/get_sentence_parsing/?input="YOUR-SENTENCE-HERE"

Get parsing of an French text:
localhost:8000/fr/get_sentence_parsing/?input="YOUR-SENTENCE-HERE"

Get parsing of a German text:
localhost:8000/de/get_sentence_parsing/?input="YOUR-SENTENCE-HERE"

Get parsing of an Arabic text:
localhost:8000/ar/get_sentence_parsing/?input="YOUR-SENTENCE-HERE"

Get parsing of a Russian text:
localhost:8000/ru/get_sentence_parsing/?input="YOUR-SENTENCE-HERE"

Get NER of a text:
localhost:8000/get_ner/?input="YOUR-SENTENCE-HERE"
