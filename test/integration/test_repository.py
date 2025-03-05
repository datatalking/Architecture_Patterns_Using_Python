# pylint: disable=protected-access
from domain import model
from adapters import repository


def test_repository_can_save_a_batch(session):
	batch = model.Batch("batch1", "RUSTY-SOAPDISH", 100, eta=None)

	repo = repository.SqlAlchemyRepository(session)
	repo.add(batch)
	session.commit