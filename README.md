# Language-interpreter
It is the school project done in the second semester. It's a language interpreter, written on Python with the help of Visitor pattern. This language can execute programm which is represented as an abstract syntax tree.

The abstract tree can contain these commands:
* Arythmetic expression
* Conditional expression (represented as a `Conditional` object)
* Function definition (represented as a `FunctionDefinition` object)
* Print construction (represented as a `Print` object)
* Read construction (represented as a `Read` object)

An arithmetic expression is one of the following list:
* Number (represented as a `Number` object)
* Name (represented as a `Reference` object)
* Binary operation (represented as `BinaryOperation`), the arguments of which are arithmetic expressions
* Unary operation (represented as `UnaryOperation`), the argument of which is an arithmetic expression
* Function call (represented as `FunctionCall`)

Also this tree can be reduced(class `ConstantFolder`) to not include operations of the form:
* `BinaryOperation (Number, AnyBinOp, Number)`, where `Number` is any object of the` Number` class, and `AnyBinOp` is any binary operation from the list of valid binary operations
* `UnaryOperation (AnyUnOp, Number)`, where `AnyUnOp` is any operation from the list of valid unary operations
* `BinaryOperation (Number (0), '*', Reference)`, where `Number (0)` is an object of the `Number` class, which contains the value` 0`, and `Reference` is any object of the` Reference` class
* `BinaryOperation (Reference, '*', Number (0))`
* `BinaryOperation (Reference (name),‘ - ’, Reference (name))`, where `Reference (name)` is an object of the Reference class containing the name `name`

