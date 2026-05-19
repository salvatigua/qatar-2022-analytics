import os
import json
import shutil

# 1. Define source and destination paths
SOURCE_MATCHES = "archive/data/matches/43/106.json"
SOURCE_EVENTS_DIR = "archive/data/events/"
SOURCE_LINEUPS_DIR = "archive/data/lineups/"

DEST_BASE = "world_cup_2022_clean"
DEST_MATCHES_DIR = os.path.join(DEST_BASE, "matches")
DEST_EVENTS_DIR = os.path.join(DEST_BASE, "events")
DEST_LINEUPS_DIR = os.path.join(DEST_BASE, "lineups")

# Create destination directories if they do not exist
os.makedirs(DEST_MATCHES_DIR, exist_ok=True)
os.makedirs(DEST_EVENTS_DIR, exist_ok=True)
os.makedirs(DEST_LINEUPS_DIR, exist_ok=True)

print("Starting data isolation for World Cup 2022...")

# 2. Read the matches file to extract World Cup match IDs
with open(SOURCE_MATCHES, "r", encoding="utf-8") as f:
    matches = json.load(f)

# Save a copy of the matches file into the clean destination directory
shutil.copy(SOURCE_MATCHES, os.path.join(DEST_MATCHES_DIR, "world_cup_matches.json"))

match_ids = []
for match in matches:
    match_ids.append(match["match_id"])

print(f"Found {len(match_ids)} registered matches for World Cup 2022.")

# 3. Iterate and copy only the corresponding event and lineup files
copied_events = 0
copied_lineups = 0

for m_id in match_ids:
    filename = f"{m_id}.json"
    
    # Full source paths
    ev_source_path = os.path.join(SOURCE_EVENTS_DIR, filename)
    li_source_path = os.path.join(SOURCE_LINEUPS_DIR, filename)
    
    # Copy Event file if it exists
    if os.path.exists(ev_source_path):
        shutil.copy(ev_source_path, os.path.join(DEST_EVENTS_DIR, filename))
        copied_events += 1
        
    # Copy Lineup file if it exists
    if os.path.exists(li_source_path):
        shutil.copy(li_source_path, os.path.join(DEST_LINEUPS_DIR, filename))
        copied_lineups += 1

print("\n--- Process Completed Successfully ---")
print(f"Matches copied: 1 (containing the {len(match_ids)} structured fixtures)")
print(f"Isolated event files: {copied_events} out of {len(match_ids)}")
print(f"Isolated lineup files: {copied_lineups} out of {len(match_ids)}")
print(f"All data saved in local directory: '{DEST_BASE}/'")