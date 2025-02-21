from flask import Flask, render_template, request
import os
from image_caption import generate_caption

app = Flask(__name__)

UPLOAD_FOLDER = "static/"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        file = request.files["file"]
        if file:
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(file_path)
            caption = generate_caption(file_path)
            return render_template("index.html", uploaded_image=file_path, caption=caption)
    return render_template("index.html", uploaded_image=None, caption=None)

if __name__ == "__main__":
    app.run(debug=True)
