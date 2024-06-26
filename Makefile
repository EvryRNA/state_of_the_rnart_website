docker_start:
	docker build -t state_of_the_rnart_website .
	docker run -it -p 8000:8000 -v ${PWD}/src/data:/app/src/data state_of_the_rnart_website

run_gunicorn:
	gunicorn --chdir src dash_helper:server -b :8000
