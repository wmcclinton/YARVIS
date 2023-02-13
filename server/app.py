from flask import Flask
import pandas as pd
app = Flask(__name__)

ydf = {
    "Core": {
        "Health": {
            "Total": 1010,
            "Skill Tree": {
                "Brazilian Jiu Jistu": {
                    "Total": 1010,
                    "White Belt": [1000, 2000],
                    "Blue Belt": [10, 2000],
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

@app.route('/')
def hello_world():
    return 'Flask: Hello World from Docker'

@app.route('/api')
def rest_hello_world():
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
    print(create_ydf_from_google_sheet())
    return ydf

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')