#!/usr/bin/env python3
from model import ASTNodeVisitor


def pretty_print(program):
    printer = PrettyPrinter()
    program.accept(printer)
    print(printer.get_code())


class PrettyPrinter(ASTNodeVisitor):
    def __init__(self):
        self.code = ""
        self.indent = 0

    def get_code(self):
        if not self.code.endswith('}'):
            self.code += ';'
        return self.code

    def newline(self):
        self.code += "\n" + "\t" * self.indent

    def visit_block(self, block):
        if not block:
            self.newline()
            return
        self.indent += 1
        self.newline()
        for i, node in enumerate(block):
            if i != 0:
                self.newline()
            node.accept(self)
            if not self.code.endswith('}'):
                self.code += ";"
        self.indent -= 1
        self.newline()

    def visit_number(self, node):
        self.code += str(node.value)

    def visit_function(self, node):
        self.code += "{"
        self.visit_block(node.body)
        self.code += "}"

    def visit_function_definition(self, node):
        self.code += "def {}(".format(node.name)
        self.code += ", ".join(node.function.args)
        self.code += ") "
        node.function.accept(self)

    def visit_conditional(self, node):
        self.code += "if ("
        node.condition.accept(self)
        self.code += ") {"
        self.visit_block(node.if_true)
        self.code += "}"
        if node.if_false:
            self.code += " else {"
            self.visit_block(node.if_false)
            self.code += "}"

    def visit_print(self, node):
        self.code += "print "
        node.expr.accept(self)

    def visit_read(self, node):
        self.code += "read {}".format(node.name)

    def visit_function_call(self, node):
        node.fun_expr.accept(self)
        self.code += "("
        for i, argument in enumerate(node.args):
            if i != 0:
                self.code += ", "
            argument.accept(self)
        self.code += ")"

    def visit_reference(self, node):
        self.code += node.name

    def visit_binary_operation(self, node):
        self.code += "("
        node.lhs.accept(self)
        self.code += ")"
        self.code += " {} ".format(node.op)
        self.code += "("
        node.rhs.accept(self)
        self.code += ")"

    def visit_unary_operation(self, node):
        self.code += "{}".format(node.op)
        self.code += "("
        node.expr.accept(self)
        self.code += ")"
