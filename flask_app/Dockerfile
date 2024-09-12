from dict_cache

WORKDIR /working/flask_app

# copy the current directory, ignoring files in .dockerignore
COPY . ./

RUN pip install .

EXPOSE 5000

CMD ["flask", "--app", "flask_app", "run", "--host=0.0.0.0"]
