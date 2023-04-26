run:
	docker-compose up --build --remove-orphans
rund:
	docker-compose up --build --remove-orphans -d
stop:
	docker-compose down