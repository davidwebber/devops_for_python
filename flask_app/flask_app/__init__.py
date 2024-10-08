from flask import Flask, request, render_template
import dict_cache

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/v1/key/')
@app.route('/v1/key/<key>', methods=['GET', 'POST'])
def key(key = None):
    
    if key is None:
        value = None
        msg = "Please specify a key"
        success = False
    
    elif request.method == 'GET':
        value, success = dict_cache.get_value(key)
        if success:
            msg = "it worked!"
        else:
            msg = f"key '{key}' not found"
    
    elif request.method == 'POST':
        data = request.get_json()

        if 'value' not in data.keys():
            msg = "POST did not contain JSON key/value pair of type {'value': 'my_value'}."
            success = False
            value = data
        else:
            value, success = dict_cache.set_value(key, data['value'])
            msg = None
    rsp = {'value': value, 'success': success, 'msg': msg}
    # Flask automatically calls Flask.json.jsonify on dictionary return values
    return rsp


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))