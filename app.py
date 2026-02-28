from flask import Flask, request, jsonify, render_template
import sys
from io import StringIO
import re
import os

# Your existing Interpreter class remains the same
class Interpreter:
    def __init__(self):
        self.vars = {}
        self.functions = {}

    def run(self, code):
        lines = code.strip().split('\n')
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if not line or line.startswith('//'):
                i += 1
                continue

            if line.startswith('function '):
                match = re.match(r'function\s+(\w+)\(([^)]*)\)\s*{?', line)
                if not match:
                    raise SyntaxError(f"Invalid function definition: {line}")
                name = match.group(1)
                params = [p.strip() for p in match.group(2).split(',') if p.strip()]
                body = []
                i += 1
                brace_count = 1
                while i < len(lines):
                    l = lines[i].strip()
                    if '}' in l:
                        brace_count -= 1
                        if brace_count == 0:
                            break
                    body.append(l)
                    if '{' in l:
                        brace_count += 1
                    i += 1
                self.functions[name] = (params, body)
                i += 1
                continue

            elif line.startswith('let ') or line.startswith('val '):
                parts = line.split(' ', 2)
                kind = parts[0]
                rest = parts[2] if len(parts) > 2 else ''
                match = re.match(r'\$?(\w+)\s*=\s*(.*)', rest)
                if not match:
                    raise SyntaxError(f"Invalid assignment: {line}")
                var_name = '$' + match.group(1) if not match.group(1).startswith('$') else match.group(1)
                expr = match.group(2)
                value = self.eval_expr(expr)
                if kind == 'val' and var_name in self.vars:
                    raise Exception(f"Cannot reassign val: {var_name}")
                self.vars[var_name] = value
                i += 1

            else:
                self.exec_statement(line)
                i += 1

    def eval_expr(self, expr):
        expr = expr.strip()
        if '+' in expr:
            parts = expr.split('+')
            return self.eval_expr(parts[0]) + self.eval_expr(parts[1])
        elif '-' in expr:
            parts = expr.split('-')
            return self.eval_expr(parts[0]) - self.eval_expr(parts[1])
        if expr.startswith('$'):
            if expr not in self.vars:
                raise NameError(f"Undefined variable: {expr}")
            return self.vars[expr]
        try:
            return int(expr)
        except ValueError:
            return expr.strip('"').strip("'")

    def exec_statement(self, line):
        if line.startswith('echo '):
            content = line[5:].strip()
            value = self.eval_expr(content)
            print(value)
        elif line.startswith('print(') and line.endswith(')'):
            content = line[6:-1].strip()
            value = self.eval_expr(content)
            print(value)
        else:
            match = re.match(r'(\w+)\((.*)\)', line)
            if match:
                name = match.group(1)
                args_str = match.group(2)
                args = [self.eval_expr(a.strip()) for a in args_str.split(',') if a.strip()]
                if name not in self.functions:
                    raise NameError(f"Undefined function: {name}")
                params, body = self.functions[name]
                if len(args) != len(params):
                    raise TypeError(f"{name} expects {len(params)} arguments, got {len(args)}")
                old_vars = self.vars.copy()
                for p, a in zip(params, args):
                    self.vars[p if p.startswith('$') else '$'+p] = a
                for b in body:
                    self.exec_statement(b)
                self.vars = old_vars
            else:
                raise SyntaxError(f"Unknown statement: {line}")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run_code():
    code = request.json.get('code', '')
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    try:
        interp = Interpreter()
        interp.run(code)
        output = redirected_output.getvalue()
    except Exception as e:
        output = str(e)
    finally:
        sys.stdout = old_stdout
    return jsonify({'output': output})

if __name__ != '__main__':
    # When running on Gunicorn, don't use the built-in server
    pass

if __name__ == '__main__':
    # For local development only
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
