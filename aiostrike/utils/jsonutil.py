import json


class JsonUtils:
    def __init__(self, obj_to_jsonify):
        self.Object_To_jsonify = obj_to_jsonify

    def cvt_json(self):
        return_data = json.loads(self.Object_To_jsonify)
        return return_data

    def parse_entities(self):
        pass
