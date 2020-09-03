%{
   const { AstNode } = require('../../build/src/AST/AstNode.js');
%}

/*Tokens y expresiones regulares*/
%lex

integer           [0-9]+
double            {integer}"."{integer}
num               ({double} | {integer})
%%

\s+                           /*Omitir espacios en blanco*/

"+"             return '+'
"-"             return '-'
"*"             return '*'
"/"             return '/'
"("             return '('
")"             return ')'

{num}                        return 'number'
([a-zA-Z_])[a-zA-Z0-9_ñÑ]*	  return 'id';

<<EOF>>     return 'EOF'

/lex

%start Init

%%

Init: E EOF { return $1; };

E: E '+' T { $$ = new AstNode($1, $3, $2); }
   | E '-' T { $$ = new AstNode($1, $3, $2); }
   | T { $$ = $1; }
   ;

T: T '*' F { $$ = new AstNode($1, $3, $2); }
   | T '/' F { $$ = new AstNode($1, $3, $2); }
   | F {$$ = $1; }
   ;

F: '(' E ')' { $$ = $2; }
   | number { $$ = new AstNode(null, null, $1); }
   ;