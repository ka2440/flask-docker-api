from flask import Flask, request, jsonify
from flask.views import MethodView
import copy

# ディクショナリ
users = [
    {"user_id": "1", "name": "tujimura", "age": 11},
    {"user_id": "2", "name": "mori", "age": 20},
    {"user_id": "3", "name": "shimada", "age": 50},
    {"user_id": "4", "name": "kyogoku", "age": 70}
    ]

# 関数ベースのルーティング関数
def routers(api):
    # 取得
    # HTTPリクエストにクエリパラメータあり
    # 全件取得 or ageフィルタリング
    @api.route('/functionalBase', methods=['GET'])
    def get_users():
        # GETリクエストを処理
        age = request.args.get('age')
        if age:
            return jsonify(list(filter(lambda user: user['age'] == int(age), users)))
        return jsonify(users)

    # 登録
    # HTTPリクエストからJSONを受け取る
    # JSONデータを新規登録
    @api.route('/functionalBase', methods=['POST'])
    def post_user():
        # POSTリクエストを処理
        data = request.get_json()
        res_users = copy.deepcopy(users)
        res_users.append(data)
        return jsonify(res_users), 201

# flaskインスタンス作成
def create_app():
    # 作成
    api = Flask(__name__)

    # 関数ベースのルーティング設定
    routers(api)

    # クラスベースのビューを関数ベースのビューに変換
    user_view = UserAPI.as_view('user_api')

    # エンドポイントを設定
    api.add_url_rule('/classBase', view_func=user_view, methods=['GET',])
    api.add_url_rule('/classBase', view_func=user_view, methods=['POST',])
    api.add_url_rule('/classBase/<string:user_id>', view_func=user_view, methods=['PUT', 'DELETE'])

    return api
