import awsgi
import sys
import flask

from flask_restful import Resource, Api


application = flask.Flask(__name__)
api = Api(application)
portNumber = 5000

if sys.argv.__len__() > 1:
  portNumber = sys.argv[1]

print("System running on port: {}".format(portNumber))


class Notification(Resource):
  def get(self):
    return flask.jsonify(status = 200, message = "OK")

# api.add_resource(Notification, "/version")
# @app.route("/version")
# def get_version():
#         return {"version": "1.0.0"}

# @app.route("/profile")
# def get_profile():
#         return jsonify(name="AWS Dev")
if __name__ == "__main__":
  application.run(host="0.0.0.0", port=portNumber)