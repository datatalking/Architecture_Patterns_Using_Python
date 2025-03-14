#
from datetime import date
from domain.model import OrderLine, Batch


def test_allocating_to_a_batch_reduces_the_available_quantity():
    """
	allocating to a batch reduces the available quantity
    :return:
    """
    batch = Batch("batch-001", "SMALL-TABLE", qty=20, eta=date.today)
    line = OrderLine("order-ref", "SMALL-TABLE", 2)

    batch.allocate(line)

    assert batch.available_quantity == 18


def test_deallocate():
    batch, line = make_batch_and_line("EXPENSIVE-FOOTSTOOL", 20, 2)
    batch.allocate(line)
    batch.deallocate(line)
    assert batch.available_quantity == 20


def make_batch_and_line(sku, batch_qty, line_qty):
    """
	create a batch and line
    :param sku:
    :param batch_qty:
    :param line_qty:
    :return:
    """
    return (
        Batch("batch-001", sku, batch_qty, eta=date.today()),
        OrderLine("order-123", sku, line_qty),
    )


def test_can_allocate_if_available_greater_than_required():
	"""
	can allocate if available > required
	:return:
	"""
	large_batch, small_line = make_batch_and_line("ELEGANT-LAMP", 20,2)
	assert large_batch.can_allocate(small_line)


def test_cannot_allocate_if_available_smaller_than_required():
	"""
	can't allocate if available < required'
	:return:
	"""
	small_batch, large_line = make_batch_and_line("ELEGANT-LAMP", 2, 20)
	assert small_batch.can_allocate(large_line) is False


def test_can_allocate_if_available_equal_to_required():
	"""
	can allocate if available = required
	:return:
	"""
	batch, line = make_batch_and_line("ELEGANT-LAMP", 2, 2)
	assert batch.can_allocate(line)

def test_cannot_allocate_if_skus_do_not_match():
	"""
	can't allocate if the sku's do not match
	:return:
	"""
	batch = Batch("batch-001", "UNCOMFORTABLE-CHAIR", 100, eta=None)
	different_sku_line = OrderLine("order-123", "EXPENSIVE-TOASTER", 10)
	assert batch.can_allocate(different_sku_line) is False


def test_can_only_deallocate_allocated_lines():
	"""
	deallocating an unallocated line has no effect
	:return:
	"""
	batch, unallocated_line = make_batch_and_line("DECORATIVE-TRINKET", 20, 2)
	batch.deallocate(unallocated_line)
	assert batch.available_quantity == 20


def test_allocation_is_idempotent():
	"""

	:return:
	"""
	batch, line = make_batch_and_line("ANGULAR-DESK", 20, 2)
	batch.allocate(line)
	batch.allocate(line)
	assert batch.available_quantity == 18
