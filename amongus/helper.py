

def format_records(records):
    return '---------------------------------------\n' + '\n---------------------------------------\n'.join(['\n'.join([f'{k}: {v}' for k, v in record.items()]) for record in records])

# Discord content must be 2000 or fewer in length
def split_list(records, num=10):
    for idx in range(0, len(records), num):
        yield records[idx:idx + num]
