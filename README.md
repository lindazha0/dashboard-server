# dashboard-server
Central server for embedded systems sensor node project.  Captures MQTT messages, archives them, and displays a dashboard.

## Quick Start
1. Clone the repository
2. Install dependencies for Python and Flask
   ```bash
   pip install -r requirements.txt
   ```
3. Run the scripts, or the flask server wither in the debug mode or for deployment. What each script does is explained below.

## Structure
The projects contains the following useful files:
```bash
.
|   # documentation & data
├── README.md
├── requirements.txt
├── data.db     # SQLite database
|
|   # scripts for db interaction (also try `sqlite3`) and logger (load DB from MQTT broker)
├── initdb.sh   # Initializes the database
├── printdb.py  # Prints the database
├── logger.py   # MQTT logger script
├── util
|   └── fakenode.py # Fake sensor node sending MQTT messages
|
|   # dashboard
├── main.py     # Flask server for the dashboard, could run manually with `flask --app=main run`
├── debug       # Debugging script, run with `./debug` for the dashboard overview
├── deploy      # Deployment script for the dashboard
├── static
│   └── style.css
├── templates
    └── index.html
```