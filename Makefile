run:
	python -m src.app

docker_start:
	docker build -t state_of_the_rnart_website .
	docker run -it -p 8050:8050 state_of_the_rnart_website