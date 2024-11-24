FROM python:3.9-slim 
WORKDIR /MAP
#COPY /Users/anast/Desktop/MAP.py /MAP/rezprob.py
COPY MAP.py /MAP/rezprob.py
ENTRYPOINT [ "python","rezprob.py" ]