import os 
from flask import Flask, request, render_template, flash, redirect, url_for
from werkzeug.utils import secure_filename
#app cre
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secret key

UPLOAD_FOLDER = 'uploads'  # Default folder where uploaded files will be saved
ALLOWED_EXTENSIONS = {'pdf', 'docx'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def select_files():
    return render_template("upload_folder.html")

@app.route('/upload', methods=['POST'])
def upload_files():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    files = request.files.getlist('file')

    # Use the default folder without asking for a folder name
    new_folder_path = os.path.join(app.config['UPLOAD_FOLDER'])

    # Clear the folder by removing all existing files
    for filename in os.listdir(new_folder_path):
        file_path = os.path.join(new_folder_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

    os.makedirs(new_folder_path, exist_ok=True)

    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(new_folder_path, filename))

    flash('Files uploaded and saved to the default folder')
    from practice import readfile
    result=readfile(request.form.get("keywords"))
    # print(result)
    return render_template("file_contents.html",data=result)
    # return redirect(url_for('select_files'))

if __name__ == '__main__':
    app.run(debug=True)
