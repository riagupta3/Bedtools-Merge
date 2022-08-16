FROM python:3.7-slim
RUN apt update
RUN apt-get install bedtools
RUN pip install biopython
COPY merge.py merge.py
RUN chmod +x merge.py
ENTRYPOINT python merge.py
LABEL io.batchx.manifest=10
COPY manifest /batchx/manifest/
