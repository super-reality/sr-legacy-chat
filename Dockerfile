FROM python:3.7.5

# USER app
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt --no-cache-dir
RUN pip install git+https://github.com/huggingface/transformers.git
RUN pip install rasa[spacy]
# RUN pip install rasa[transformers]
RUN pip install rasa[convert]
RUN python -m spacy download en_core_web_md
RUN python -m spacy link en_core_web_md en
