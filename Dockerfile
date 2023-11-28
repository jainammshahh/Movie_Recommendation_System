from python:3.8-slim-buster

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app
RUN pip install Flask==2.3.2
RUN pip install gunicorn==19.9.0
RUN pip install Jinja2==2.11.3
RUN pip install MarkupSafe==1.1.1
RUN pip install Werkzeug==0.15.5
RUN pip install numpy>=1.9.2
RUN pip install scipy>=0.15.1
RUN pip install nltk==3.5
RUN pip install scikit-learn>=0.18
RUN pip install pandas>=0.19
RUN pip install beautifulsoup4==4.9.1
RUN pip install jsonschema==3.2.0
RUN pip install tmdbv3api==1.6.1
RUN pip install lxml==4.6.3
RUN pip install urllib3==1.26.5
RUN pip install requests==2.23.0
RUN pip install pickleshare==0.7.5

CMD ["python3","main.py"]
