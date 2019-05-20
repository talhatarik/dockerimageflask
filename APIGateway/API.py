
from flask import render_template, jsonify, Blueprint, request


service = Blueprint('Api', __name__,)


@service.route('/5bayt', methods=['POST'])
def index():
        #GET.
        accessTokenGET = request.args.get('AccessToken')   
        accessTokenSecretGET = request.args.get('AccessTokenSecret')

        #POST
        textPOST = request.values.get('Text')


        if accessTokenGET == "Admin" and accessTokenSecretGET == "Admin":
                return jsonify(textPOST)
        else:
                return jsonify('KEY  hatası')

               

