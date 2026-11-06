# Ground-truth per frame vs track IDs; ID switch when same GT object changes track ID.
gt_to_track=[{'personA':7},{'personA':7},{'personA':9},{'personA':9}, {}, {'personA':9}]
last={};switches=0
for frame in gt_to_track:
    for obj,track in frame.items():
        if obj in last and last[obj]!=track:switches+=1
        last[obj]=track
assert switches==1
# Real MOT metrics (IDF1, HOTA) require standardized annotation and matching.
