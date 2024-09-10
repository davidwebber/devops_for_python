test:
	python3 -m unittest discover -s tests/unit

build:
	docker build -t dict_cache dict_cache
	docker build -t demo example_B

run:
	docker run -p 5000:5000 demo

