import os
from app.helpers import clean_data
import joblib
from flask import request
from flask_restful import Resource, abort
import pandas as pd

from app import  api

model = joblib.load(os.getenv('MODEL_WEIGHTS_PATH', './RandomForestPipeline.joblib'))

class HealthCheck(Resource):

    def get(self) -> dict : 
        """Check if API is reachable

        Returns:
            [dict]: [Simple message to show API is reachable.]
        """
        return {'hello': 'world'}


api.add_resource(HealthCheck, '/')


class Prediction(Resource):

    def post(self) -> dict : 
        """Get predicitons from api. Features should be passed in request body 
        in the format {features:[{feature_set_1}, {feature_Set_2}, etc.]}. See
        Documentation for full body format

            Returns:
                [dict]: [json object containing predictions of the requested feature sets.]
        """

        data_columns = [
            'Wave_700', 'Wave_701', 'Wave_702', 'Wave_703', 'Wave_704', 'Wave_705', 'Wave_706', 
            'Wave_707', 'Wave_708', 'Wave_709', 'Wave_710', 'Wave_711','Wave_712', 'Wave_713', 
            'Wave_714', 'Wave_715', 'Wave_716', 'Wave_717','Wave_718', 'Wave_719', 'Wave_720', 
            'Wave_721', 'Wave_722', 'Wave_723', 'Wave_724', 'Wave_725', 'Site', 'Growing Season', 
            'Genotype', 'Treatment'
        ]

        payload = request.get_json()
        data = payload.get('features')
        if not data:
            message = f"""Bad request: Please format request like {{"features": [{{feat1: .124, ... featN:.5678}}, {{feat1: .124, ... featN:.5678}}]}}"""
            abort(400, message=message)
        
        try:
            payload_df = pd.DataFrame(data)
        except Exception as e:
            message = f"""Bad request: Please format request like {{"features": [{{feat1: .124, ... featN:.5678}}, {{feat1: .124, ... featN:.5678}}]}}"""
            abort(400, message=message)

        missing_cols = set(data_columns) - set(payload_df.columns)
        if missing_cols:
            message = f"""Bad request: missing the following features: {",".join([col for col in missing_cols])}. """
            abort(400, message=message)
        
        payload_df = clean_data(payload_df)

        genotype_idx = data_columns.index('Genotype')
        data_columns[genotype_idx] = 'Genotype_Cleaned'
        payload_df = payload_df[data_columns]
        
        response_data = model.predict(payload_df).tolist()

        return {'predictions': response_data}

api.add_resource(Prediction, '/predict/')