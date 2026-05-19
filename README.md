## Getting Started / Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/salvatigua/qatar-2022-analytics.git
   cd qatar-2022-analytics
    ```

2. **Source Data Setup (Mandatory)**
The raw StatsBomb dataset (https://www.kaggle.com/datasets/saurabhshahane/statsbomb-football-data) is too large to be hosted on GitHub and is excluded via .gitignore. To replicate this project, you must manually create a folder named archive/ in the root directory and place the original StatsBomb data/ folder inside it:

```plaintext
qatar-2022-analytics/
└── archive/
    └── data/
        ├── matches/
        ├── events/
        └── lineups/
```

3. **Data Isolation**
If you wish to re-run the isolation process, execute the Python pipeline to extract the 64 World Cup matches into the clean workspace:

```bash
python isolate_world_cup.py
```
