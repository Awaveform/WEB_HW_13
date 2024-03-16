# WEB_HW_13
docker run --name contacts-postgres -p 5432:5432 -e POSTGRES_PASSWORD=567234 -d postgres

alembic init migrations

alembic revision --autogenerate -m "init"
alembic upgrade head

docker-compose up -d
poetry add python-dotenv
poetry add redis
poetry add

poetry add cloudinary

