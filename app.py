from flask import Flask,request,jsonify
import streamlink

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_query_string():
    url = request.args.getlist('key')[0]
    print(url)
    try:
        streams = streamlink.streams(url)
        keys = [k for k in streams.keys()]
        data = dict()
        for k in keys:
            data[k] = streams[k].url 
        return jsonify(data)
        
    except streamlink.NoPluginError:
        return None

if __name__ == '__main__':
    app.run(debug=True)
