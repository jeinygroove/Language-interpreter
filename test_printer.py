#!/usr/bin/env python3
import pytest
from model import *
from printer import *


def test_program1(capsys):
    program = FunctionDefinition('main', Function(['arg1'], [
        Read('x'),
        Print(Reference('x')),
        Conditional(
            BinaryOperation(Number(2), '==', Number(3)),
            [
                Conditional(Number(1), [], [])
            ],
            [
                FunctionCall(Reference('exit'), [
                    UnaryOperation('-', Reference('arg1'))
                ])
            ],
        ),
    ]))

    pretty_print(program)
    captured = capsys.readouterr()
    assert captured.out == """\
def main(arg1) {
\tread x;
\tprint x;
\tif ((2) == (3)) {
\t\tif (1) {
\t\t}
\t} else {
\t\texit(-(arg1));
\t}
}
"""


def test_program2(capsys):
    program = FunctionDefinition(
        'factorial', Function(['n'], [
            Conditional(
                BinaryOperation(Reference('n'),
                                '==',
                                Number(0)),
                [Number(1)],
                [
                    BinaryOperation(
                        Reference('n'),
                        '*',
                        FunctionCall(
                            Reference('factorial'), [
                                BinaryOperation(
                                    Reference('n'),
                                    '-',
                                    Number(1))
                            ])
                    )
                ])
        ]))

    pretty_print(program)
    captured = capsys.readouterr()
    assert captured.out == """\
def factorial(n) {
\tif ((n) == (0)) {
\t\t1;
\t} else {
\t\t(n) * (factorial((n) - (1)));
\t}
}
"""


def test_number(capsys):
    number = Number(10)
    pretty_print(number)
    captured = capsys.readouterr()
    assert captured.out == "10;\n"


def test_functiondefinition(capsys):
    func = FunctionDefinition("foo", Function([], []))
    pretty_print(func)
    captured = capsys.readouterr()
    assert captured.out == """\
def foo() {
}
"""


def test_conditional(capsys):
    condition = Conditional(Number(42), [], [])
    pretty_print(condition)
    captured = capsys.readouterr()
    assert captured.out == """\
if (42) {
}
"""


def test_print(capsys):
    func_print = Print(Number(42))
    pretty_print(func_print)
    captured = capsys.readouterr()
    assert captured.out == "print 42;\n"


def test_read(capsys):
    func_read = Read('x')
    pretty_print(func_read)
    captured = capsys.readouterr()
    assert captured.out == "read x;\n"


def test_functioncall(capsys):
    scope = Scope()
    FunctionDefinition(
        'func', Function(['n'], [Reference('n')])).evaluate(scope)
    call = FunctionCall(Reference('func'), [
        Number(10)
    ])
    pretty_print(call)
    captured = capsys.readouterr()
    assert captured.out == "func(10);\n"


def test_reference(capsys):
    refer = Reference('x')
    pretty_print(refer)
    captured = capsys.readouterr()
    assert captured.out == "x;\n"


def test_binary_operation(capsys):
    operation = BinaryOperation(Number(1), "*",
                                BinaryOperation(Number(2), "+", Number(3)))
    pretty_print(operation)
    captured = capsys.readouterr()
    assert captured.out == "(1) * ((2) + (3));\n"


def test_unary_operation(capsys):
    operation = UnaryOperation('-', Number(42))
    pretty_print(operation)
    captured = capsys.readouterr()
    assert captured.out == "-(42);\n"
