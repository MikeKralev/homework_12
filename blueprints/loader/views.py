import logging

from flask import Blueprint, render_template, request
from functions import img_to_uploads, add_post

ALLOWED_EXTENSIONS = ['jpeg', 'png']


loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates/loader', static_folder='static')


@loader_blueprint.route('/post', methods=['GET'])
def add_post_page():
    return render_template("post_form.html")


@loader_blueprint.route('/post', methods=['POST'])
def add_show_new_post():
    picture = request.files.get('picture')
    text = request.form.get('content')

    if not picture and not text:
        logging.error('Нет изображения, либо текста')
        return 'ошибка загрузки'

    extension = picture.filename.split('.')[-1]
    if extension not in ALLOWED_EXTENSIONS:
        logging.info(f'некорректный формат изображения {picture.filename}')
        return 'некорректный формат изображения'

    img_to_uploads(picture)
    post = {'pic': f"./uploads/images/{picture.filename}", 'content': text}
    add_post(post)


    return render_template("post_uploaded.html", post=post)

