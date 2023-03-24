from flask import request, jsonify
from tf_idf.train import top5
from tf_idf import app


# 编写api接口形式
@app.route('/', methods=['POST'])
def index():
    if request.form.get("case", type=str, default=None):
        case = request.form.get("case", type=str, default=None)  # 获取表单数据
        similar_cases = top5(case)
        print(case)
        return jsonify({
            "code": 200,
            "message": f"cases recommend successful",
            "data": similar_cases
        })
    else:
        return jsonify({
            "code": 400,
            "message": f"cases recommend fail",
            "data": None
        })


# if __name__ == "__main__":
#     print(top5("一段话"))
