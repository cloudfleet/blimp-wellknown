from flask import Flask, jsonify, request
import settings, getopt, sys, os
app = Flask(__name__)


@app.route('/host-meta.json', methods=['GET'])
def send_host_meta_json():
    return jsonify({
        "links": settings.LINKS
    })

@app.route('/host-meta', methods=['GET'])
def send_host_meta_xrd():
    return settings.JINJA_ENV.get_template("host-meta.xrd.tpl").render(links=settings.LINKS)

opts, args = getopt.getopt(sys.argv[1:], "h:p:", ["host=", "port="])

options = dict(opts)

hostname = "0.0.0.0"
port = 80

if "-h" in options:
    hostname = options["-h"]

if "--host" in options:
    hostname = options["--host"]

if "-p" in options:
    port = int(options["-p"])

if "--port" in options:
    port = int(options["--port"])


if __name__ == '__main__':
    app.run(host=hostname, port=port)

