from flask import Flask
import pandas as pd
from flask_cors import CORS
import pandas as pd
from datetime import date, datetime
import gensim.downloader as api
import copy

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

ydf_template = {
    "Core": {
        "Health": {
            "Total": 0,
            "Skill Tree": {
                "Brazilian Jiu Jistu": {
                    "Total": 0,
                    "White Belt": [0, 2000],
                    "Blue Belt": [0, 2000],
                    "Purple Belt": [0, 2000],
                    "Brown Belt": [0, 2000],
                    "Black Belt": [0, 2000]
                },
                "Alpha Male": {
                    "Total": 0,
                    "Level 1": [0, 2000],
                    "Level 2": [0, 2000],
                    "Level 3": [0, 2000],
                    "Level 4": [0, 2000],
                    "Level 5": [0, 2000]
                }
            }
        },

        "Intelligence": {
            "Total": 0,
            "Skill Tree": {
                "AI Research": {
                    "Total": 0,
                    "Level 1": [0, 2000],
                    "Level 2": [0, 2000],
                    "Level 3": [0, 2000],
                    "Level 4": [0, 2000],
                    "Level 5": [0, 2000]
                },
                "Crypto Development": {
                    "Total": 0,
                    "Level 1": [0, 2000],
                    "Level 2": [0, 2000],
                    "Level 3": [0, 2000],
                    "Level 4": [0, 2000],
                    "Level 5": [0, 2000]
                },
                "Quantitative Finance": {
                    "Total": 0,
                    "Level 1": [0, 2000],
                    "Level 2": [0, 2000],
                    "Level 3": [0, 2000],
                    "Level 4": [0, 2000],
                    "Level 5": [0, 2000]
                },
                "Russian": {
                    "Total": 0,
                    "Level 1": [0, 2000],
                    "Level 2": [0, 2000],
                    "Level 3": [0, 2000],
                    "Level 4": [0, 2000],
                    "Level 5": [0, 2000]
                },
                "Business Acumen": {
                    "Total": 0,
                    "Level 1": [0, 2000],
                    "Level 2": [0, 2000],
                    "Level 3": [0, 2000],
                    "Level 4": [0, 2000],
                    "Level 5": [0, 2000]
                },
            }
        },

        "Soul": {
            "Total": 0,
            "Skill Tree": {
                "YouTube Content Creator": {
                    "Total": 0,
                    "Level 1": [0, 2000],
                    "Level 2": [0, 2000],
                    "Level 3": [0, 2000],
                    "Level 4": [0, 2000],
                    "Level 5": [0, 2000]
                },
                "Sigma Male": {
                    "Total": 0,
                    "Level 1": [0, 2000],
                    "Level 2": [0, 2000],
                    "Level 3": [0, 2000],
                    "Level 4": [0, 2000],
                    "Level 5": [0, 2000]
                }
            }
        }
    },
    "Info": {
        "Height": "5'7\"",
        "Weight": 165,
        "BMI": 24,
        "Body Fat": 14,
        "USD": 25000,
        "ADA": 10000
    }
}

skill_to_valid_list = {
    "Brazilian Jiu Jistu": ["BJJ"],
    "Alpha Male": ["Workout", "Half-Murph", "Gym", "Haircut"],
    "AI Research": ["Research", "YARVIS", "UROP", "Polygence", "BD", "Kathryn", "LIS Lunch", "IJCAI", "Ani", "Research Meetings", "TLPK Meeting"],
    "Crypto Development": ["Aneta", "Anet", "Crypto", "Crypto Investment", "Austin", "Coin Bureau", "DeGPT", "DeGPT Doc", "Nitram", "Derek"],
    "Quantitative Finance": ["Quant", "Coq", "Class"],
    "Russian": ["Russian", "Madina"],
    "Business Acumen": [],
    "YouTube Content Creator": ["YT - GPT", "YT"],
    "Sigma Male": ["Movie", "Friends", "Groceries", "Cleaned", "Sev", "Call Parents", "Read", "Going Out", "Clean"],
}

skip_list = ['Vacation', 'Game', 'Shower', 'Dinner', 'Eat', 'Slept', 'Sleep', 'Life Logs', 'Morning Routine', 'Email', 'Relaxed', 'Relax', 'Nap', 'Life', 'Logs', 'Pack', 'Car Inspection', 'Notion', 'Travel', 'Plov']

def get_ydf():
    # TODO Maybe get date range and/or GOOGLE_SHEET_ID 
    def create_ydf_from_google_sheet():
        GOOGLE_SHEET_ID = '1lsdfjD7Nn_t09MceOEkpplY7X2tWs1ea_Kkp7qa9FuY'
        text = pd.read_csv('https://docs.google.com/spreadsheets/d/' + 
                    GOOGLE_SHEET_ID +
                    '/export?gid=0&format=csv',
                    # Set first column as rownames in data frame
                    index_col=0,
                    )
        # for i, (index, row) in enumerate(df.iterrows()):
        #   print(row)
        # TODO parse google sheet text to ydf
        return text

    # Count Tasks from Google Sheet
    text = create_ydf_from_google_sheet()
    after_start = False
    task_count = {}
    time_list = None
    for i, (index, row) in enumerate(text.iterrows()):
        if index == "START":
            after_start = True
        elif type(index) == str and "Date" in index:
            time_list = row.values
        elif after_start:
            if datetime.strptime(index,"%m/%d/%Y") < datetime.now():
                for task in row.values:
                    if type(task) == str and "/" in task:
                        tasks = [task.split("/")[0], task.split("/")[1]]
                    else:
                        tasks = [task]

                    for task in tasks:
                        if task in task_count:
                            task_count[task] += 1 if len(tasks) == 1 else 0.5
                        else:
                            task_count[task] = 1 if len(tasks) == 1 else 0.5

    # Add task count to ydf
    ydf = copy.deepcopy(ydf_template)
    for task, hrs in task_count.items():
        # Don't count towards anything
        if type(task) != str:
            continue
        if task in skip_list:
            continue
        if 'Plan' in task:
            continue
        if ' till ' in task:
            task = task.split(' till ')[0]
        # Try to match remaining
        found_match = False
        for core_skill, val in ydf_template['Core'].items():
            for skill, skill_tree in val['Skill Tree'].items():
                if found_match:
                    continue
                if task in skill_to_valid_list[skill]:
                    ydf['Core'][core_skill]['Total'] += hrs
                    ydf['Core'][core_skill]['Skill Tree'][skill]['Total'] += hrs
                    found_match = True

        if not found_match:
            raise NotImplementedError

    return ydf

@app.route('/')
def hello_world():
    return 'Flask: Hello World from Docker'

@app.route('/api')
def rest_hello_world():
    return get_ydf()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')