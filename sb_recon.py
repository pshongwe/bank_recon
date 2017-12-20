import re

regex = r"(BUA|EBL|MBA|HLU|HUB|LAA|LBO|LOH|MAH|MHL|MPK|NSK|ENJ|SOB|THE)|([0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9])|,([0-9]+),|(WD|DP|RVD|RVW)"

test_str = ("BUA\n"
	"20/07/2017,4212,WD\n"
	"24/07/2017,2512,WD\n"
	"25/07/2017,406,WD\n"
	"27/07/2017,462,WD\n"
	"EBL\n"
	"21/07/2017,4000,DP\n"
	"29/07/2017,1000,RVD\n"
	"31/07/2017,1000,RVD\n"
	"HLU\n"
	"01/07/2017,144,DP\n"
	"19/07/2017,1006,WD\n"
	"20/07/2017,5818,WD\n"
	"24/07/2017,5530,WD\n"
	"25/07/2017,562,WD\n"
	"28/07/2017,480,DP\n"
	"31/07/2017,4000,WD\n"
	"HUB\n"
	"25/07/2017,256,WD\n"
	"29/07/2017,1006,WD\n"
	"LAA\n"
	"20/07/2017,13898,WD\n"
	"LBO\n"
	"19/07/2017,1776,WD\n"
	"27/07/2017,1306,WD\n"
	"LOH\n"
	"07/07/2017,1188,WD\n"
	"19/07/2017,3233,WD\n"
	"24/07/2017,10382,WD\n"
	"25/07/2017,12667,WD\n"
	"26/07/2017,7858,WD\n"
	"27/07/2017,503,DP\n"
	"28/07/2017,1620,WD\n"
	"MAH\n"
	"17/07/2017,1006,WD\n"
	"27/07/2017,206,WD\n"
	"MHL\n"
	"20/07/2017,7312,WD\n"
	"25/07/2017,6018,WD\n"
	"27/07/2017,9806,WD\n"
	"MPK\n"
	"01/07/2017,506,WD\n"
	"24/07/2017,1902,WD\n"
	"25/07/2017,4424,WD\n"
	"27/07/2017,4012,WD\n"
	"NSK\n"
	"08/07/2017,282,WD\n"
	"10/07/2017,288,RVW\n"
	"19/07/2017,1506,WD\n"
	"24/07/2017,3760,WD\n"
	"25/07/2017,2798,WD\n"
	"ENJ\n"
	"17/07/2017,616,WD\n"
	"19/07/2017,3112,WD\n"
	"20/07/2017,4006,WD\n"
	"25/07/2017,106,WD\n"
	"27/07/2017,1006,WD\n"
	"SOB\n"
	"27/07/2017,3012,WD\n"
	"28/07/2017,1000,RVW\n"
	"THE\n"
	"01/07/2017,1000,RVW\n"
	"20/07/2017,8524,WD\n"
	"27/07/2017,10530,WD\n")

matches = re.finditer(regex, test_str)

for matchNum, match in enumerate(matches):
    matchNum = matchNum + 1
    
    #print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    output = ""
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        if match.start(groupNum) != -1:
        	output += match.group(groupNum).rstrip('\r\n')
        	

    
    print (output)