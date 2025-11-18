import re
from datetime import datetime

INTENTS = ['create_task','schedule_meeting','set_reminder','get_summary','plan_day','check_tasks']

def parse_message(text):
    t = text.lower().strip()
    # simple rules
    if any(w in t for w in ['remind me','reminder']):
        intent = 'set_reminder'
    elif any(w in t for w in ['meeting','schedule','meet']):
        intent = 'schedule_meeting'
    elif any(w in t for w in ['add task','todo','to-do','task','add a task']):
        intent = 'create_task'
    elif 'plan my day' in t or 'plan the day' in t:
        intent = 'plan_day'
    elif 'summary' in t or ('today' in t and 'summary' in t):
        intent = 'get_summary'
    else:
        intent = 'create_task'  # default

    # extract a date/time naive
    date_match = re.search(r'(tomorrow|today|on \w+ \d{1,2}|at \d{1,2}(am|pm)?)', t)
    entities = {}
    if date_match:
        entities['time'] = date_match.group(0)

    # extract title heuristically (take after keywords if possible)
    title = t
    # try to clean common prefixes
    for prefix in ['remind me to ', 'remind me to', 'remind me ', 'add task ', 'add a task ', 'create task to ', 'create task ']:
        if title.startswith(prefix):
           title = title[len(prefix):]
            break

    entities['title'] = title[:200]
    return {'intent': intent, 'entities': entities}
