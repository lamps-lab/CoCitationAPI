# CoCitationAPI
Calculate co-citation index of a given paper

Currently the API uses the Semantic Scholar API to obtain citing and cited papers (defined below).

If Paper A ---- cites ----> Paper B, then Paper A is the citing paper, Paper B is the cited paper. 

Put SCORE.csv and cocitation_v2.py in the same directory and then run cocitation_v2.py. It will output cocitation.csv in the same directory. The first row and column in cocitation.csv represents the DOI of papers, which is the same as the fifth column in SCORE.csv. Each value in cocitation.csv is the co-citation value between two papers from SCORE.csv.
