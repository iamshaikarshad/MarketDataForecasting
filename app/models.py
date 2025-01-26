from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class NeopOutageData(db.Model):
    __tablename__ = 'neop_outage_data'

    id = db.Column(db.Integer, primary_key=True)
    numconfirmed = db.Column(db.Integer)
    deadcomponents = db.Column(db.String)
    restoredcount = db.Column(db.Integer)
    psr = db.Column(db.Integer)
    psrc = db.Column(db.Integer)
    gsp = db.Column(db.String)
    opzone_id = db.Column(db.String)
    numconfirmed = db.Column(db.String)
    unpredicted = db.Column(db.String)

    location = db.relationship('Location', backref='neop_outage_data', lazy='dynamic')
    location_details = db.relationship('LocationDetail', backref='neop_outage_data', lazy='dynamic')
    opzones = db.relationship('Opzones', backref='neop_outage_data', lazy='dynamic')

class Location(db.Model):
    __tablename__ = 'premise_locations'

    id = db.Column(db.Integer, primary_key=True)
    premise_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    post_code = db.Column(db.String)
    uploaddate = db.Column(db.DateTime)
    isactive = db.Column(db.Integer)
    fault_id = db.Column(db.String, db.ForeignKey('neop_outage_data.incidentid'), index=True)
    parent = db.relationship('NeopOutageData', backref='locations')

class LocationDetail(db.Model):
    __tablename__ = 'asset_locations'

    id = db.Column(db.Integer, primary_key=True)
    fault_id = db.Column(db.String, db.ForeignKey('neop_outage_data.incidentid'), primary_key=True)
    asset_id = db.Column(db.String, primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    northing = db.Column(db.Float)
    easting = db.Column(db.Float)
    uploaddate = db.Column(db.DateTime)
    isactive = db.Column(db.Integer)
    gsp = db.Column(db.String, nullable=False)

    parent = db.relationship('NeopOutageData', backref='location_details')

class Opzones(db.Model):
    __tablename__ = 'opzones'

    id = db.Column(db.Integer, primary_key=True)
    opzone_id = db.Column(db.String, db.ForeignKey('neop_outage_data.opzone_id'), primary_key=True)
    opzone_name = db.Column(db.String)
    oz_parent_id = db.Column(db.String, db.ForeignKey('neop_outage_data.opzone_id'))
    oz_type = db.Column(db.String)

    parent = db.relationship('NeopOutageData', backref='opzones')