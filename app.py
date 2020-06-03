from flask import Flask, request
import streamlink

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_query_string():
    url = request.args.getlist('key')[0]
    print(url)
    try:
        streams = streamlink.streams(url)
        # return streams['best'].url
        return streams
    except streamlink.NoPluginError:
        return None


if __name__ == '__main__':
    app.run(debug=True)
