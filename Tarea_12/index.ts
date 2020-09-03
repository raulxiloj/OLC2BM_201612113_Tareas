import { AstNode } from "./src/AST/AstNode";

const Parser = require('../src/grammar/grammar');

console.log("Entrada: 15+5*2+5/2");
let ast = Parser.parse('15+5*2+5/2');

console.log(ast.generateC3D());