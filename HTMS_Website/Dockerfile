FROM python:3.12.0a4-slim



WORKDIR /htms_website

COPY ./requirements.txt ./

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2 


RUN pip install --no-cache-dir -r requirements.txt

COPY ./ ./htms_website

EXPOSE 8000

CMD [ "python", "manage.py", "runserver","0.0.0.0:8000"] 




# RUN apt-get update && apt-get install -y curl
# RUN curl -sL https://deb.nodesource.com/setup_19.x | bash -
# RUN apt-get install -y nodejs