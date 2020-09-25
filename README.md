# CoCitationAPI
Calculate co-citation index of a given paper

Currently the API uses the Semantic Scholar API to obtain citing and cited papers (defined below).

If Paper A ---- cites ----> Paper B, then Paper A is the citing paper, Paper B is the cited paper. 

Put SCORE.csv and cocitation_v8.py in the same directory and then run cocitation_v8.py. It will output cocitation.json and yearss.json in the same directory. 

You can change line 33 to calculate co-citation for more papers. For example, the current line says "for k in range(1, 51):", it means calculate co-citation for paper 1 to paper 50.
