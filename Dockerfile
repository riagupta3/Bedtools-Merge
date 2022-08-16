FROM python:3.7-slim
RUN apt update
RUN apt-get install bedtools
RUN pip install biopython
