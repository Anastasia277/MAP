FROM python:3.9-slim 
WORKDIR /MAP
COPY MAP.py /MAP/MapImage.py
ENTRYPOINT [ "python","MapImage.py" ]