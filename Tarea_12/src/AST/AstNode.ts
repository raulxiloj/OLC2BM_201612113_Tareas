export class AstNode {

    public static temps: number = 0;

    constructor(public left: AstNode, public right: AstNode, public operation: any) { }

    public generateC3D(): any {
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


    public new_temp() {
        AstNode.temps++;
        return "t" + AstNode.temps;
    }


}