FROM python:3.9-slim 
WORKDIR /MAP
COPY MAP.py /MAP/rezprob.py
ENTRYPOINT [ "python","rezprob.py" ]