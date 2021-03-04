import json
import helper
from models.results import Results


class ResultsController:

    def impostor(self, impostor, win_flg, posted_user_name, posted_user_id, group_id):
        last_insert_id = Results.create(impostor, win_flg, posted_user_name, posted_user_id, group_id)
        last_record = Results.last_insert_record(last_insert_id)

        return helper.format_records([Results.last_insert_record(last_insert_id)])

    def results(self, limit, order_by):
        records = Results.results(limit, order_by)

        return [helper.format_records(arr) for arr in list(helper.split_list(records))]

