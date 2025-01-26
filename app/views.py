from flask import Blueprint, jsonify, request
from .models import NeopOutageData, LocationDetail, Opzones
from .serializers import serialize_outage_data
from . import db

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/outage-data', methods=['GET'])
def get_outage_data():
    # Fetch data from the database
    try:
        limit = request.args.get('limit', type=int, default=750)
        incident_id = request.args.get('id', type=str)
        
        query = NeopOutageData.query
        if incident_id:
            query = query.filter_by(incidentid=incident_id)
        
        outage_data = query.limit(limit).all()
        
        # Serialize and return response
        data = [serialize_outage_data(record) for record in outage_data]
        return jsonify({'data': data, 'count': len(data)})

    except Exception as e:
        return jsonify({'error': str(e)}), 500
