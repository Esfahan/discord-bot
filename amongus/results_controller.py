import json
import helper
from models.results import Results


class ResultsController:

    def impostor(self, **kwargs):
        last_insert_id = Results.create(kwargs['impostor'],
                                        kwargs['win_flg'],
                                        kwargs['impostor02'],
                                        kwargs['win_flg02'],
                                        kwargs['impostor03'],
                                        kwargs['win_flg03'],
                                        kwargs['posted_user_name'],
                                        kwargs['posted_user_id'],
                                        kwargs['posted_server_id'])
        last_record = Results.last_insert_record(last_insert_id)

        return helper.format_records([Results.last_insert_record(last_insert_id)])

    def results(self, limit, order_by):
        records = Results.results(limit, order_by)

        return [helper.format_records(arr) for arr in list(helper.split_list(records))]

