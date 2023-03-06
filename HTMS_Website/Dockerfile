FROM python:3.11.2-slim



WORKDIR /htms_website

COPY ./requirements.txt ./



RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2 

# RUN apt-get update \
#     && apt-get install -y libpq-dev \
#     && pip install psycopg2

RUN pip install --no-cache-dir -r requirements.txt

COPY ./ ./

EXPOSE 8003

CMD ["gunicorn", "--workers", "3", "--timeout", "86400", "--bind", "0.0.0.0:8003", "HTMS_Website.wsgi:application"]
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000" ]






# RUN apt-get update && apt-get install -y curl
# RUN curl -sL https://deb.nodesource.com/setup_19.x | bash -
# RUN apt-get install -y nodejs