from flask import Flask, request, jsonify
from flask_cors import CORS
from judgeLib.judge import test, judge
import subprocess
import os

app = Flask(__name__)
CORS(app)  # 啟用CORS，允許跨域請求

@app.route('/compile', methods=['POST'])
def compile():
    data = request.json
    code_string = data['code']  # 獲取從前端傳來的代碼字符串

    # 將字符串寫入臨時文件
    temp_filename = 'temp_code.py'
    with open(temp_filename, 'w') as f:
        f.write(code_string)
    
    try:
        # 執行Python文件
        result = subprocess.run(['python', temp_filename], capture_output=True, text=True)
        output = result.stdout if result.returncode == 0 else result.stderr
    except Exception as e:
        output = str(e)
        
    os.remove(temp_filename)   # 刪除臨時文件
    
    return jsonify({'result': output})

if __name__ == '__main__':
    app.run(debug=True)
