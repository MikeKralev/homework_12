import logging

from flask import Blueprint, render_template, request
from functions import post_by_keyword


main_blueprint = Blueprint('main_blueprint', __name__, template_folder="templates/main", static_folder="static")


@main_blueprint.route("/")
def main_page():
    return render_template('index.html')


@main_blueprint.route("/search")
def search_page():
    logging.info('Выполнялся поиск')
    keyword = request.args.get('s', '')
    posts = post_by_keyword(keyword)
    return render_template('post_list.html', keyword=keyword, posts=posts)
