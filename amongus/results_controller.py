import json
import helper
from models.results import Results


class ResultsController:

    def winner(self, winner, user_name, user_id, group_id):
        last_insert_id = Results.create(winner, user_name, user_id, group_id)
        last_record = Results.last_insert_record(last_insert_id)

        return helper.format_records([Results.last_insert_record(last_insert_id)])

    def results(self):
        records = Results.results()
        return [helper.format_records(arr) for arr in list(helper.split_list(records))]
