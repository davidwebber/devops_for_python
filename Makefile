test:
	python3 -m unittest discover -s tests/unit

flask-run:
	flask --app flask_app run

gunicorn-run:
	gunicorn -w 1 flask_app:app

docker-build:
	docker build -t dict_cache dict_cache
	docker build -t demo flask_app

docker-run:
	docker run -p 5000:5000 demo

curl-get:
	curl -s localhost:5000/v1/key/a | python3 -m json.tool

curl-set:
	curl -X POST -d '{"value":"hello world"}' -H "Content-Type: application/json" -s localhost:5000/v1/key/a | python3 -m json.tool
	
