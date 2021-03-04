from amongus.database import db
from sqlalchemy import desc
from pytz import timezone
import datetime


class Results(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
    impostor = db.Column('impostor', db.String(50), nullable=False)
    win_flg = db.Column('win_flg', db.Boolean, nullable=False)
    posted_user_name = db.Column('posted_user_name', db.String(50), nullable=False)
    posted_user_id = db.Column('posted_user_id', db.String(50), nullable=False)
    group_id = db.Column('group_id', db.String(50))
    created_at = db.Column('created_at', db.DateTime, nullable=False, server_default=db.func.current_timestamp())
    updated_at = db.Column('updated_at', db.DateTime, nullable=False, server_default=db.func.current_timestamp())
    def find(result_id: int):
        return db.session.query(Results).get(result_id)

    def find_all(order_by: str='asc'):
        if type(order_by) is str and order_by.lower() == 'desc':
            return db.session.query(Results).order_by(desc(Results.id)).all()
        else:
            return db.session.query(Results).all()

    def find_latest(limit: int=10, order_by: str='asc'):
        results = db.session.query(Results)
        if type(order_by) is str and order_by.lower() == 'desc':
            return results.order_by(desc(Results.id)).limit(limit)
        else:
            return results.order_by(Results.id).limit(limit)

    def results(limit: int=None, order_by: str=None):
        records = Results.find_latest(limit, order_by) if limit else Results.find_all(order_by)

        return [{'id': record.id,
                 'impostor': record.impostor,
                 'win_flg': record.win_flg,
                 #'posted_user_name': record.posted_user_name,
                 #'posted_user_id': record.posted_user_id,
                 'created_at': Results._convert_datetime(record.created_at)} for record in records]

    def last_insert_record(result_id: int):
        record = Results.find(result_id)
        return {'id': record.id,
                'impostor': record.impostor,
                 'win_flg': record.win_flg,
                #'posted_user_name': record.posted_user_name,
                #'posted_user_id': record.posted_user_id,
                'created_at': Results._convert_datetime(record.created_at)}

    def _convert_datetime(datetime_utc: datetime):
        return Results._convert_datetime_to_s(Results._utc_to_jst(datetime_utc))

    def _utc_to_jst(datetime_utc: datetime):
        return timezone('Asia/Tokyo').localize(datetime_utc)

    def _convert_datetime_to_s(datetime_jst: datetime):
        return datetime_jst.strftime('%Y-%m-%d %H:%M:%S')

    def create(impostor: str, win_flg: int, posted_user_name: str, posted_user_id: str, group_id: str=None):
        results = Results()
        results.impostor = impostor
        results.win_flg = win_flg
        results.posted_user_name = posted_user_name
        results.posted_user_id = posted_user_id
        if group_id:
            results.group_id = group_id
        db.session.add(results)
        db.session.commit()

        return results.id

    def delete_all(self):
        Results.query.delete()
        db.session.commit()

    '''
    def delete(self):
        print('delete is called')
        db.session.query(Results).filter(Results.id != previous_results.id)
        db.session.delete(obj)
        db.session.commit()
    '''
