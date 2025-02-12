from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
   return "<p>Hello, World!</p>"

# inspect posted data
@app.route('/viewer', methods=['GET','POST'])
def viewer():
   inspect = {}
   inspect['args'] = request.args
   inspect['form'] = request.form
   inspect['values'] = request.values
   inspect['first'] = request.form.get('first')
   inspect['last'] = request.form.get('last')
   inspect['path'] = request.path
   inspect['url'] = request.url
   inspect['base_url'] = request.base_url
   inspect['content_encoding'] = request.content_encoding
   inspect['content_length'] = request.content_length
   inspect['content_type'] = request.content_type
   inspect['host'] = request.host
   inspect['mimetype'] = request.mimetype
   if (request.method == 'POST' and
       'application/json' in request.headers.get('Content-Type')):
       inspect['receivedJson'] = request.get_json()
   return jsonify(inspect)


# start server
if __name__ == '__main__':
   app.run(debug=True, port=3000)
