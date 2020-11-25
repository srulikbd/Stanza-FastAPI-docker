FROM tiangolo/uvicorn-gunicorn:python3.8

RUN mkdir /fastapi

COPY requirements.txt /fastapi

WORKDIR /fastapi

RUN pip install -r requirements.txt 
RUN python -c 'import stanza; stanza.download("en")'
RUN python -c 'import stanza; stanza.download("es")'
RUN python -c 'import stanza; stanza.download("ru")'
RUN python -c 'import stanza; stanza.download("fr")'
RUN python -c 'import stanza; stanza.download("ar")'
RUN python -c 'import stanza; stanza.download("de")'
RUN rm -r /root/.cache
RUN apt-get -y clean 
RUN apt-get -y autoremove



COPY . /fastapi

EXPOSE 8000

CMD ["uvicorn", "stanza_fastapi:app", "--host", "0.0.0.0", "--port", "8000"]
