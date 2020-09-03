"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
class AstNode {
    constructor(left, right, operation) {
        this.left = left;
        this.right = right;
        this.operation = operation;
    }
    generateC3D() {
        if (this.left != null && this.right != null) {
            let aux = this.left.generateC3D();
            let aux2 = this.right.generateC3D();
            let op = this.operation;
            let temp = this.new_temp();
            this.operation = temp;
            return `${aux}\n${aux2}\n${temp} = ${this.left.operation} ${op} ${this.right.operation}`;
        }
        return "";
    }
    new_temp() {
        AstNode.temps++;
        return "t" + AstNode.temps;
    }
}
exports.AstNode = AstNode;
AstNode.temps = 0;
