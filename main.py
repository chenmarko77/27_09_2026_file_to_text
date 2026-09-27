from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
	content = None
	error = None

	if request.method == "POST":
		uploaded_file = request.files.get("file")
		if uploaded_file is None or not uploaded_file.filename:
			error = "Оберіть текстовий файл."
		else:
			try:
				content = uploaded_file.read().decode("utf-8-sig")
			except UnicodeDecodeError:
				error = "Файл має бути текстовим у кодуванні UTF-8."

	return render_template("main.html", content=content, error=error)


if __name__ == "__main__":
	app.run(debug=True)
