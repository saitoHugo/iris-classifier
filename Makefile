dev:
	(cd iris_api/ && python app.py)

dev-old:
	(cd iris-api/ && uvicorn main:app --reload --workers 1 --host 0.0.0.0 --port 8080)

docker-build:
	docker build -t iris-api .

docker-run:
	docker run -d -p 8080:8080 --name iris-api-local-container iris-api:latest

docker-clean:
	(docker stop iris-api-container && docker rm iris-api-container )

test:
	pytest -ra


