from marshmallow import Schema, fields

class OutageSchema(Schema):
    id = fields.Int()
    numconfirmed = fields.Int()
    deadcomponents = fields.Str()
    restoredcount = fields.Int()
    psr = fields.Int()
    psrc = fields.Int()
    gsp = fields.Str()
    opzone_id = fields.Str()
    numconfirmed = fields.Str()
    unpredicted = fields.Str()

class LocationSchema(Schema):
    id = fields.Int()
    premise_id = fields.Int()
    post_code = fields.Str()
    uploaddate = fields.DateTime()
    isactive = fields.Int()
    fault_id = fields.Str()

class OpzoneSchema(Schema):
    id = fields.Int()
    opzone_id = fields.Str()
    opzone_name = fields.Str()
    oz_parent_id = fields.Str()
    oz_type = fields.Str()

outage_schema = OutageSchema()
location_schema = LocationSchema()
opzone_schema = OpzoneSchema()

def serialize_outage_data(record):
    return {
        'id': record.id,
        'numconfirmed': record.numconfirmed,
        'deadcomponents': record.deadcomponents,
        'restoredcount': record.restoredcount,
        'psr': record.psr,
        'psrc': record.psrc,
        'gsp': record.gsp,
        'opzone_id': record.opzone_id,
        'unpredicted': record.unpredicted
    }
