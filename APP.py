import os
import subprocess     # ← 确保这一行在这里
import re
from flask import Flask, render_template, abort


app = Flask(__name__,
            static_folder="static",
            template_folder="templates")
ASSIGN_DIR = "Assignments"

def assignment_number(fn: str) -> int:
    """
    从 'Assignment_10.py' 里提取出 10 这个数字并返回，
    如果匹配不上，就放到最后（返回一个很大的数）。
    """
    m = re.match(r"Assignment_(\d+)\.py$", fn)
    return int(m.group(1)) if m else 10**9

@app.route("/")
def index():
    # 先找出所有 .py
    files = [f for f in os.listdir(ASSIGN_DIR)
             if f.startswith("Assignment_") and f.endswith(".py")]
    # 按数字大小排序
    files = sorted(files, key=assignment_number)
    return render_template("index.html", assignments=files)

# ... 其他路由不变 ...


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
