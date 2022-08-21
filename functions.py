import json


def read_from_file(path='./posts.json'):
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
        return data


def post_by_keyword(keyword):
    result = []
    keyword_low = keyword.lower()
    posts = read_from_file()
    for post in posts:
        if keyword_low in post['content'].lower():
            result.append(post)
    return result


def img_to_uploads(file):
    file.save(f"./uploads/images/{file.filename}")


def add_post(post):
    posts = read_from_file()
    posts.append(post)
    with open('./posts.json', 'w', encoding='utf-8') as f:
        json.dump(posts, f, ensure_ascii=False)
