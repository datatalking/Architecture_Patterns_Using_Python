from datetime import datetime
from flask import Flask, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import config
from domain import model
from adapters import orm, repository
from service_layer import services

orm.start_mappers()
get_session = sessionmaker(bind=create_engine(config.get_postgres_uri()))
app = Flask(__name__)


@app.route("/add_batch")
def add_batch():
	session = get_session
	repo = repository.SqlAlchemyRepository(session)
	eta = request.json["eta"]
	if eta is not None:
		eta = datetime.fromisoformat(eta).date()
	services.add_batch(
		request.json["ref"],
		request.json["sku"],
		request.json["qty"],
		eta,
		repo,
		session,
	)
	return "OK", 201
