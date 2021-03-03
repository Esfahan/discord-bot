from amongus.database import db
from sqlalchemy import desc
from pytz import timezone


class Results(db.Model):
    #__tablename__ = 'results'
    #__table_args__ = {'extend_existing': True}

    id = db.Column('id', db.Integer, primary_key = True)
    winner = db.Column('winner', db.String(50), nullable=False)
    user_name = db.Column('user_name', db.String(50), nullable=False)
    user_id = db.Column('user_id', db.String(50), nullable=False)
    group_id = db.Column('group_id', db.String(50))
    created_at = db.Column('created_at', db.DateTime, nullable=False, server_default=db.func.current_timestamp())
    updated_at = db.Column('updated_at', db.DateTime, nullable=False, server_default=db.func.current_timestamp())

    def find(result_id):
        return db.session.query(Results).get(result_id)

    def find_all():
        return db.session.query(Results).all()

    def results():
        records = Results.find_all()
        return [{'id': record.id,
                 'winner': record.winner,
                 #'user_name': record.user_name,
                 #'user_id': record.user_id,
                 'created_at': Results._convert_datetime(record.created_at)} for record in records]

    def last_insert_record(result_id):
        record = Results.find(result_id)
        return {'id': record.id,
                'winner': record.winner,
                #'user_name': record.user_name,
                #'user_id': record.user_id,
                'created_at': Results._convert_datetime(record.created_at)}

    def _convert_datetime(datetime_utc):
        return Results._convert_datetime_to_s(Results._utc_to_jst(datetime_utc))

    def _utc_to_jst(datetime_utc):
        return timezone('Asia/Tokyo').localize(datetime_utc)

    def _convert_datetime_to_s(datetime_jst):
        return datetime_jst.strftime('%Y-%m-%d %H:%M:%S')

    def create(winner, user_name, user_id, group_id):
        print(f'winner: {winner}')
        print(f'user_name: {user_name}')
        print(f'user_id: {user_id}')
        print(f'group_id: {group_id}')

        results = Results()
        results.winner = winner
        results.user_name = user_name
        results.user_id = user_id
        #if group_id:
        #    results.group_id = group_id
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
