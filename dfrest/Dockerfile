FROM python:3

COPY . /dfrest
WORKDIR /dfrest
RUN pip3 install Flask
RUN pip install -r requirements.txt
ENV FLASK_APP '/dfrest/dfserver.py'
CMD flask run --host=0.0.0.0 --port=5000