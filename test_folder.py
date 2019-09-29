from folder import *
from model import *


def test_end_to_end():
    program = BinaryOperation(
        Number(10),
        '-',
        UnaryOperation(
            '-',
            BinaryOperation(
                Number(3),
                '+',
                BinaryOperation(
                    Reference('x'),
                    '-',
                    Reference('x')
                )
            )
        )
     )
    assert fold_constants(program) == Number(13)


def test_num_op_num():
    program = BinaryOperation(
        Number(10),
        '+',
        Number(32)
    )
    assert fold_constants(program) == Number(42)


def test_num0_multiply_ref():
    program = BinaryOperation(
        Number(0),
        '*',
        Reference('x')
    )
    assert fold_constants(program) == Number(0)


def test_ref_multiply_num0():
    program = BinaryOperation(
        Reference('x'),
        '*',
        Number(0)
    )
    assert fold_constants(program) == Number(0)


def test_subtract_equal_refs():
    program = BinaryOperation(
       Reference('x'),
       '-',
       Reference('x')
    )
    assert fold_constants(program) == Number(0)


def test_negative_num():
    program = UnaryOperation(
        '-',
        Number(73)
    )
    assert fold_constants(program) == Number(-73)
