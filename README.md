# CoCitationAPI
Calculate co-citation index of a given paper

Currently the API uses the Semantic Scholar API to obtain citing and cited papers (defined below).

If Paper A ---- cites ----> Paper B, then Paper A is the citing paper, Paper B is the cited paper. 

==========================================================================================================================================

How to use the files:
1.
Put SCORE.csv and cocitation_v8.py in the same directory and then run cocitation_v8.py. It will output cocitation.json and yearss.json in the same directory. 

You can change line 33 to calculate co-citation for more papers. For example, the current line says "for k in range(1, 51):", it means calculate co-citation for paper 1 to paper 50.

Note: "The API is freely available, but enforces a rate limit and will respond with HTTP status 429 'Too Many Requests' if the limit is exceeded (100 requests per 5 minute window per IP address)." That's why I have to slow down the speed of this code. It takes about 2 hours for 50 papers.

2.
Put SCORE.csv and cocitation_v7.py in the same directory and then run cocitation_v7.py. This generates similar outputs to the previous one.

The difference is that:
cocitation_v7.py can select papers that cited the source paper in a certain time range with the variable "YearGap". It's set to 3 by default and this can be modeified by the user.

3
bibliographic_coupling.py selects the papers that cites the same paper with the source paper and then calculates bibliographic coupling values. Output is BibliographicCoupling.json.
