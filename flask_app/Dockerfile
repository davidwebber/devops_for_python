#from python:3
from dict_cache

WORKDIR /app
COPY requirements.txt /app
COPY api.py /app

# COPY dict_cache /app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["flask", "--app", "api", "run", "--host=0.0.0.0"]

#CMD /bin/bash