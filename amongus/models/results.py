from amongus.database import db
from sqlalchemy import desc
from pytz import timezone
import datetime


class Results(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
    impostor = db.Column('impostor', db.String(50), nullable=False)
    impostor02 = db.Column('impostor02', db.String(50), default=None)
    impostor03 = db.Column('impostor03', db.String(50), default=None)
    win_flg = db.Column('win_flg', db.Boolean, nullable=False)
    win_flg02 = db.Column('win_flg02', db.Boolean, default=None)
    win_flg03 = db.Column('win_flg03', db.Boolean, default=None)
    posted_user_name = db.Column('posted_user_name', db.String(50), nullable=False)
    posted_user_id = db.Column('posted_user_id', db.String(50), nullable=False)
    posted_server_id = db.Column('posted_server_id', db.String(50))
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
                 'impostor02': record.impostor02,
                 'win_flg02': record.win_flg02,
                 'impostor03': record.impostor03,
                 'win_flg03': record.win_flg03,
                 #'posted_user_name': record.posted_user_name,
                 #'posted_user_id': record.posted_user_id,
                 'created_at': Results._convert_datetime(record.created_at)} for record in records]

    def last_insert_record(result_id: int):
        record = Results.find(result_id)
        return {'id': record.id,
                'impostor': record.impostor,
                 'win_flg': record.win_flg,
                 'impostor02': record.impostor02,
                 'win_flg02': record.win_flg02,
                 'impostor03': record.impostor03,
                 'win_flg03': record.win_flg03,
                #'posted_user_name': record.posted_user_name,
                #'posted_user_id': record.posted_user_id,
                'created_at': Results._convert_datetime(record.created_at)}

    def _convert_datetime(datetime_utc: datetime):
        return Results._convert_datetime_to_s(Results._utc_to_jst(datetime_utc))

    def _utc_to_jst(datetime_utc: datetime):
        return timezone('Asia/Tokyo').localize(datetime_utc)

    def _convert_datetime_to_s(datetime_jst: datetime):
        return datetime_jst.strftime('%Y-%m-%d %H:%M:%S')

    def create(impostor: str, win_flg: int,
               impostor02: str, win_flg02: int,
               impostor03: str, win_flg03: int,
               posted_user_name: str, posted_user_id: str, posted_server_id: str=None):
        print('create is called')
        print(impostor02)
        print(win_flg02)
        print(impostor03)
        print(win_flg03)

        results = Results()
        results.impostor = impostor
        results.win_flg = win_flg
        results.posted_user_name = posted_user_name
        results.posted_user_id = posted_user_id
        if posted_server_id:
            results.posted_server_id = posted_server_id

        if impostor02 and isinstance(win_flg02, bool):
            results.impostor02 = impostor02
            results.win_flg02 = win_flg02
        if impostor03 and isinstance(win_flg03, bool):
            results.impostor03 = impostor03
            results.win_flg03 = win_flg03

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
