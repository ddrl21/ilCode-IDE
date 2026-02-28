<!DOCTYPE html>
<html>
<head>
    <title>ilCode IDE</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.2/codemirror.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.2/codemirror.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.2/mode/javascript/javascript.min.js"></script>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background: #f5f5f5;
        }
        h1 {
            margin-top: 0;
            color: #333;
        }
        #editor-container {
            border: 1px solid #ccc;
            border-radius: 4px;
            margin-bottom: 10px;
        }
        .CodeMirror {
            height: 300px;
            font-size: 14px;
        }
        .toolbar {
            display: flex;
            gap: 10px;
            margin: 10px 0;
            flex-wrap: wrap;
        }
        button {
            padding: 8px 16px;
            background: #4CAF50;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 14px;
        }
        button:hover {
            background: #45a049;
        }
        button.docs-btn {
            background: #2196F3;
        }
        button.docs-btn:hover {
            background: #0b7dda;
        }
        #output {
            background: #1e1e1e;
            color: #d4d4d4;
            padding: 10px;
            border-radius: 4px;
            font-family: 'Courier New', monospace;
            white-space: pre-wrap;
            min-height: 100px;
            max-height: 200px;
            overflow: auto;
            border: 1px solid #333;
        }
        #docs-panel {
            background: #fff3cd;
            border: 1px solid #ffeeba;
            border-radius: 4px;
            padding: 15px;
            margin: 10px 0;
            max-height: 300px;
            overflow-y: auto;
            font-size: 14px;
            display: none;  /* hidden by default */
        }
        #docs-panel h3 {
            margin-top: 0;
            color: #856404;
        }
        #docs-panel pre {
            background: #f8f9fa;
            padding: 8px;
            border-radius: 4px;
            overflow-x: auto;
        }
        #docs-panel code {
            background: #f1f1f1;
            padding: 2px 4px;
            border-radius: 3px;
        }
        .example-link {
            color: #007bff;
            cursor: pointer;
            text-decoration: underline;
        }
        .example-link:hover {
            color: #0056b3;
        }
    </style>
</head>
<body>
    <h1>🚀 ilCode Playground</h1>
    
    <div class="toolbar">
        <button onclick="runCode()">▶ Run</button>
        <button class="docs-btn" onclick="toggleDocs()">📘 Toggle Docs</button>
    </div>

    <div id="editor-container">
        <textarea id="code">// Write your ilCode here
let $name = "ilCode"
function hello($x) {
    echo "Hello, " + $x
}
hello($name)</textarea>
    </div>

    <!-- Documentation Panel (hidden initially) -->
    <div id="docs-panel">
        <h3>📚 ilCode Language Reference</h3>
        <p><strong>ilCode</strong> blends Python, JavaScript, PHP & Kotlin.</p>
        
        <h4>🔹 Variables</h4>
        <ul>
            <li><code>let $var = value</code> – mutable</li>
            <li><code>val $var = value</code> – immutable (cannot be reassigned)</li>
            <li>Prefix <code>$</code> is optional but recommended.</li>
        </ul>

        <h4>🔹 Functions</h4>
        <pre>function name($param1, $param2) {
    // body
}</pre>

        <h4>🔹 Output</h4>
        <ul>
            <li><code>echo expression</code> – prints value</li>
            <li><code>print(expression)</code> – same as echo</li>
        </ul>

        <h4>🔹 Comments</h4>
        <pre>// single line comment</pre>

        <h4>🔹 Data Types & Operators</h4>
        <ul>
            <li>Numbers (integers) and strings</li>
            <li><code>+</code> (addition or concatenation)</li>
            <li><code>-</code> (subtraction)</li>
        </ul>

        <h4>📋 Examples (click to load)</h4>
        <p>
            <span class="example-link" onclick="loadExample(1)">Hello World</span> |
            <span class="example-link" onclick="loadExample(2)">Function with params</span> |
            <span class="example-link" onclick="loadExample(3)">Immutable val</span>
        </p>
    </div>

    <div id="output"></div>

    <script>
        var editor = CodeMirror.fromTextArea(document.getElementById('code'), {
            lineNumbers: true,
            mode: 'javascript',
            theme: 'default'
        });

        function runCode() {
            var code = editor.getValue();
            fetch('/run', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({code: code})
            })
            .then(resp => resp.json())
            .then(data => {
                document.getElementById('output').innerText = data.output;
            });
        }

        function toggleDocs() {
            var panel = document.getElementById('docs-panel');
            panel.style.display = panel.style.display === 'none' ? 'block' : 'none';
        }

        function loadExample(id) {
            var examples = {
                1: `// Hello World example
let $greeting = "Hello, ilCode!"
echo $greeting`,
                2: `// Function with parameters
function add($a, $b) {
    echo $a + $b
}
add(5, 3)`,
                3: `// val cannot be changed
val $pi = 3.14
echo $pi
// $pi = 3.1415  // would cause an error`
            };
            editor.setValue(examples[id]);
            // Optionally auto-run or just let user run manually
        }
    </script>
</body>
</html>
