import os
import subprocess
from flask import Flask, render_template, abort
from jinja2 import TemplateNotFound

app = Flask(
    __name__,
    static_folder="static",
    template_folder="templates"
)

ASSIGN_DIR = "Assignments"

@app.route("/")
def index():
    try:
        files = sorted(f for f in os.listdir(ASSIGN_DIR)
                       if f.startswith("Assignment_") and f.endswith(".py"))
    except FileNotFoundError:
        files = []
    return render_template("index.html", assignments=files)

@app.route("/view/<filename>")
def view(filename):
    # 原来动态渲染 .py 的逻辑保持不变
    path = os.path.join(ASSIGN_DIR, filename)
    if not os.path.isfile(path):
        abort(404)

    with open(path, encoding="utf-8") as f:
        code = f.read()

    proc = subprocess.Popen(
        ["python", path],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )
    lines = []
    for _ in range(20):
        line = proc.stdout.readline()
        if not line:
            break
        lines.append(line)
    proc.kill()
    output = "".join(lines)

    return render_template("detail.html",
                           title=filename,
                           code=code,
                           output=output)

# <<< 新增这一段，让 Flask 也去渲染那些搬到 templates/ 的 Assignment_*.html >>>
@app.route("/<template_name>.html")
def render_static_html(template_name):
    try:
        # 试着当成 Jinja 模板渲染
        return render_template(f"{template_name}.html")
    except TemplateNotFound:
        abort(404)

if __name__ == "__main__":
    app.run(debug=True)
