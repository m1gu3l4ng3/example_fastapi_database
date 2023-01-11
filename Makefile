up:
	poetry export -f requirements.txt --output requirements.txt --without-hashes
	docker-compose up -d
down:
	docker-compose down
