import json, os, time
DB_FILE = 'sample_data.json'

def _load():
    if not os.path.exists(DB_FILE):
        with open(DB_FILE,'w') as f:
            json.dump({'tasks':[], 'events':[]}, f)
    with open(DB_FILE) as f:
        return json.load(f)

def _save(data):
    with open(DB_FILE,'w') as f:
        json.dump(data, f, default=str, indent=2)

def create_task_db(user_id, title, due=None, remind_in_minutes=None):
    data = _load()
    task = {
        'id': int(time.time()*1000),
        'user_id': user_id,
        'title': title,
        'due_date': str(due) if due else None,
        'priority': 2,
        'status': 'todo',
        'created_at': str(time.time())
    }
    data['tasks'].append(task)
    _save(data)
    return task

def list_tasks(user_id):
    data = _load()
    return [t for t in data['tasks'] if t['user_id']==user_id]

def create_event_db(user_id, title, start, end):
    data = _load()
    ev = {
        'id': int(time.time()*1000),
        'user_id': user_id,
        'title': title,
        'start_time': str(start),
        'end_time': str(end)
    }
    data['events'].append(ev)
    _save(data)
    return ev
