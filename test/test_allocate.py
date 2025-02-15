# test_allocate.py
from model import Batch, OrderLine
import pytest


def test_prefers_current_stock_batches_to_shipments():
	"""
	current stock batches are preferred to shipment batches
	:return:
	"""
	in_stock_batch = Batch("in-stock-batch", "RETRO-CLOCK", 100, eta=None)
	shipment_batch = Batch("shipment-batch", "RETRO-CLOCK", 100, eta=tomorrow)
	line = OrderLine("oref", "RETRO-CLOCK", 10)

	allocate(line, [in_stock_batch, shipment_batch])

	assert in_stock_batch.available_quantity == 90
	assert shipment_batch.available_quantity == 100


def test_prefers_earlier_batches():
	"""
	eearlier batches are preferred to later ones
	:return:
	"""
	earliest = Batch("speedy-batch", "MINIMALIST-SPOON", 100, eta=today)
	medium = Batch("normal-batch", "MINIMALIST-SPOON", 100, eta=tomorrow)
	latest = Batch("slow-batch", "MINIMALIST-SPOON", 100, eta=later)

	line = OrderLine("order1", "MINIMALIST-SPOON", 10)

	allocate(line, [latest, medium, earliest])

	assert earliest.available_quantity == 90
	assert medium.available_quantity == 100
	assert latest.available_quantity == 100


def test_returns_allocated_batch_ref():
	"""
	allocated batch ref is returned
	:return:
	"""
	in_stock_batch = Batch("in-stock-batch-ref", "HIGHBROW-POSTER", 100, eta=None)
	shipment_batch = Batch("shipment-batch-ref", "HIGHBROW-POSTER", 100, eta=tomorrow)
	line = OrderLine("oref", "HIGHBROW-POSTER", 10)


def test_raises_out_of_stock_exception_if_cannot_allocate():
	"""

	:return:
	"""
	batch = Batch('batch1', 'SMALL-FORK', 10, eta=today)
	allocate(OrderLine('order1', 'SMALL-FORK', 10), [batch])

	with pytest.raises(OutOfStock, match='SMALL-FORK'):
		allocate(OrderLine('order2', 'SMALL-FORK', 1) [batch])