#
import model


def test_orderline_mapper_can_load(session):
    """
    test if orderlines can be loaded
    :param session:
    :return:
    """
    session.execute(
        "INSERT INTO order_lines (orderid, sku, qty) VALUES "
        '("order1", "RED-CHAIR", 12),'
        '("order1", "RED-TABLE", 13),'
        '("order2", "BLUE-LIPSTICK", 14)'
    )
    expected = [
        model.OrderLine("order1", "RED-CHAIR", 12),
        model.OrderLine("order1", "RED-TABLE", 13),
        model.OrderLine("order2", "BLUE-LIPSTICK", 14),
    ]
    assert session.query(model.OrderLine).all() == expected


def test_orderline_mapper_can_save_lines(session):
    """
    can orderlines be saved
    :param session:
    :return:
    """
    new_line = model.OrderLine("order1", "DECORATIVE-WIDGET", 12)
    session.add(line)
    session.commit()

    rows = list(session.execute('SELECT orderid, sku, qty FROM order_lines"'))
    assert rows == [("order1", "DECORATIVE-WIDGET", 12)]
