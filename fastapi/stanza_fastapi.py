from typing import Optional
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from typing import List
from fastapi.responses import HTMLResponse
import pandas as pd
import xlrd
import stanza
import  json



nlp_ner = stanza.Pipeline(lang='en', processors='tokenize,ner')
# doc = nlp("Chris Manning teaches at Stanford University. He lives in the Bay Area.")
# print(*[f'entity: {ent.text}\ttype: {ent.type}' for ent in doc.ents], sep='\n')


def get_language_model(language):
    nlp = stanza.Pipeline(language)
    return nlp
# nlp_es = stanza.Pipeline('es')
app = FastAPI(title="Stanza",
              description='''Stanza as a service''',
              version="1.0",
              )

class User(BaseModel):
    user_name: dict

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/get_ner/")
async def get_ner(input):
    nlp2 = stanza.Pipeline(lang='en', processors='tokenize,ner')
    doc = nlp2(input)
    return ([f'entity: {ent.text}\ttype: {ent.type}' for sent in doc.sentences for ent in sent.ents])

    # (*[f'entity: {ent.text}\ttype: {ent.type}' for ent in doc.ents], sep='\n')

    results = {}
    ind = input
    prsd_el = [el for el in nlp(ind).sentences]
    prsd = [f'entity: {ent.text}\ttype: {ent.type}' for ent in nlp_ner(ind).ents]
    results[ind] = prsd
    results = json.dumps(results)
    print(results)

    # r = HttpResponse(results, content_type='application/json')

    # return r#esults  #
    return results  #

@app.get("/es/get_sentence_parsing/")
async def get_parse_english(input):
    language = get_language_model("es")
    return parse_sentence(input, language)

@app.get("/en/get_sentence_parsing/")
async def get_parse_english(input):
    language = get_language_model("en")
    return parse_sentence(input, language)

@app.get("/ru/get_sentence_parsing/")
async def get_parse_english(input):
    language = get_language_model("ru")
    return parse_sentence(input, language)

@app.get("/de/get_sentence_parsing/")
async def get_parse_english(input):
    language = get_language_model("de")
    return parse_sentence(input, language)

@app.get("/fr/get_sentence_parsing/")
async def get_parse_english(input):
    language = get_language_model("fr")
    return parse_sentence(input, language)

@app.get("/ar/get_sentence_parsing/")
async def get_parse_english(input):
    language = get_language_model("ar")
    return parse_sentence(input, language)

def parse_sentence(input, language):
    results = {}
    ind = input
    prsd_el = [el for el in language(ind).sentences]
    prsd = [[{r"deprel":{det.deprel},
              r"deps":{det.deps},
              r"feats":det.feats,
              r"head":det.head,
              'id':det.id,
              "lemma":det.lemma,
              "misc":det.misc,
              "pos":det.pos,
              "text":det.text,
              "upos":det.upos,
              "xpos":det.xpos}
               for det in el.words] for el in language(ind).sentences]
    # prsd = [f'{el.words}' for el in nlp(ind).sentences]
    results[ind] = prsd
    # results = json.dumps(results)
    # print(f'{results}')

    # r = HttpResponse(results, content_type='application/json')

    # return r#esults  #
    return results  #
    # return f'{results}'  #

@app.get("/en/get_sentence_parsing/")
async def parse_english(input):
    results = {}
    ind = input
    prsd_el = [el for el in nlp(ind).sentences]
    prsd = [[{r"deprel":{det.deprel},
              r"deps":{det.deps},
              r"feats":det.feats,
              r"head":det.head,
              'id':det.id,
              "lemma":det.lemma,
              "misc":det.misc,
              "pos":det.pos,
              "text":det.text,
              "upos":det.upos,
              "xpos":det.xpos}
               for det in el.words] for el in nlp(ind).sentences]
    # prsd = [f'{el.words}' for el in nlp(ind).sentences]
    results[ind] = prsd
    # results = json.dumps(results)
    # print(f'{results}')

    # r = HttpResponse(results, content_type='application/json')

    # return r#esults  #
    return results  #
    # return f'{results}'  #

@app.get("/get_sentence_parsing_2/")
async def create_files_get(input):
    results = {}
    ind = input
    prsd_el = [el for el in nlp(ind).sentences]
    prsd = [[{r"deprel":{det.deprel},
              r"deps":{det.deps},
              r"feats":det.feats,
              r"head":det.head,
              'id':det.id,
              "lemma":det.lemma,
              "misc":det.misc,
              "pos":det.pos,
              "text":det.text,
              "upos":det.upos,
              "xpos":det.xpos}
               for det in el.words] for el in nlp(ind).sentences]
    # prsd = [f'{el.words}' for el in nlp(ind).sentences]
    results[ind] = prsd
    # results = json.dumps(results)
    # print(f'{results}')

    # r = HttpResponse(results, content_type='application/json')

    # return r#esults  #
    return results  #
    # return f'{results}'  #

@app.get("/get_sentence_parsing_without_quotes/")
async def create_files_get(input):
    results = {}
    ind = input
    prsd_el = [el for el in nlp(ind).sentences]
    prsd = [[{r"deprel":{det.deprel},
              r"deps":{det.deps},
              r"feats":det.feats,
              r"head":det.head,
              'id':det.id,
              "lemma":det.lemma,
              "misc":det.misc,
              "pos":det.pos,
              "text":det.text,
              "upos":det.upos,
              "xpos":det.xpos}
               for det in el.words] for el in nlp(ind).sentences]
    # prsd = [f'{el.words}' for el in nlp(ind).sentences]
    results[ind] = prsd
    # results = json.dumps(results)
    # print(f'{results}')

    # r = HttpResponse(results, content_type='application/json')

    # return r#esults  #
    return results  #
    # return f'{results}'  #

@app.get("/get_sentence_parsing_with_quotes/")
async def create_files_get(input):
    results = {}
    ind = input
    prsd_el = [el for el in nlp(ind).sentences]
    prsd = [[{r"deprel":{det.deprel},
              r"deps":{det.deps},
              r"feats":det.feats,
              r"head":det.head,
              'id':det.id,
              "lemma":det.lemma,
              "misc":det.misc,
              "pos":det.pos,
              "text":det.text,
              "upos":det.upos,
              "xpos":det.xpos}
               for det in el.words] for el in nlp(ind).sentences]
    # prsd = [f'{el.words}' for el in nlp(ind).sentences]
    results[ind] = prsd
    # results = json.dumps(results)
    # print(f'{results}')

    # r = HttpResponse(results, content_type='application/json')

    # return r#esults  #
    # return results  #
    return f'{results}'  #

@app.post("/post_sentence_parsing/")
async def create_files_post(input):
    results = {}
    ind = input
    prsd_el = [el for el in nlp(ind).sentences]
    prsd = [[{"deprel":det.deprel,
              "deps":det.deps,
              "feats":det.feats,
              "head":det.head,
              "id":det.id,
              "lemma":det.lemma,
              "misc":det.misc,
              "pos":det.pos,
              "text":det.text,
              "upos":det.upos,
              "xpos":det.xpos}
               for det in el.words] for el in nlp(ind).sentences]
    results[ind] = prsd
    results = json.dumps(results)
    print(results)
    # return results  #

@app.post("/files/")
async def create_files(files: List[bytes] = File(...)):
    df = pd.read_excel(files[0])
    fl = df.head(2)  # .to_dict()
    results = {}
    for index, row in fl.iterrows():
        ind = row[0]
        prsd_el = [el for el in nlp(ind).sentences]
        prsd = [[{"deprel":det.deprel,#"deprel":det.deprel,
                  "deps":det.deps,
                  "feats":det.feats,
                  "head":det.head,
                  "id":det.id,
                  "lemma":det.lemma,
                  "misc":det.misc,
                  "pos":det.pos,
                  "text":det.text,
                  "upos":det.upos,
                  "xpos":det.xpos}
                   for det in el.words] for el in nlp(ind).sentences]
        results[ind] = prsd
    results = json.dumps(results)
    return results  #

def create_files():
    df = pd.read_excel('C:\\Users\\user\\Downloads\\example.xlsx')
    fl = df.head(2)  # .to_dict()
    results = {}
    counter = 1

    for index, row in fl.iterrows():
        print("counter is:", counter)
        counter += 1
        ind = row[0]
        prsd_el = [el for el in nlp(ind).sentences]
        prsd = [[{"deprel":det.deprel,#"deprel":det.deprel,
                  "deps":det.deps,
                  "feats":det.feats,
                  "head":det.head,
                  "id":det.id,
                  "lemma":det.lemma,
                  "misc":det.misc,
                  "pos":det.pos,
                  "text":det.text,
                  "upos":det.upos,
                  "xpos":det.xpos}
                   for det in el.words] for el in nlp(ind).sentences]
        results[ind] = prsd
    results = json.dumps(results)

    return results  # b

@app.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile] = File(...)):
    return {"filenames": [file.filename for file in files]}


