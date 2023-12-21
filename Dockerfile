FROM python:3.10
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "--chdir", "src", "app:server", "-b", ":8000"]
EXPOSE 8000
