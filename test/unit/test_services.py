# test_services.py

def test_add_batch():
	repo, session = FakeRepository([]), FakeSession()
	services.add_batch("b1", "CRUNCHY-ARMCHAIR", 100, None, repo, session)
	assert repo.get("b1") is not None
	assert session.committed