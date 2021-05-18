file = open('map.txt','r')
map = file.readlines()
file.close()
#1-top right
#2-horizontal
#3-top left
#4-vertical
#5-bottom left
#6-bottom right
#c-crossroads
#7-approach1 crossing left right and bottom road
#8-approach2 crossing left top and bottom road
#9-approach3 crossing left right and top road
#A-approach4 crossing right top and bottom road
generated="<!DOCTYPE html>\n<html lang='en'>\n<head>\n<meta charset='UTF-8'>\n<meta http-equiv='X-UA-Compatible' content='IE=edge'>\n<link rel='stylesheet' href='style.css'>\n<title>Document</title>\n</head>\n<body>\n"
for i in map:
    generated+="\n<div class='row' style='display: flex;'>"
    for j in i:
        if j=='0':
            generated+="\n<div class='ground' style='display: inline-block;'></div>\n"
        if j=='1':
            generated+="\n<div class='road1' style='display: inline-block;'>\n<div id='ver'></div>\n<div id='lsv'></div>\n<div id='rsv'></div>\n<div id='hor'></div>\n<div id='lsh'></div>\n<div id='rsh'></div>\n<div id='turn'></div>\n<div id='ls'></div>\n<div id='rs'></div>\n</div>"
        if j=='2':
            generated+="\n<div class='road2' style='display: inline-block;'>\n<div id='main'></div>\n<div id='lss'></div>\n<div id='rss'></div>\n</div>"
        if j=='3':
            generated+="\n<div class='road3' style='display: inline-block;'>\n<div id='ver'></div>\n<div id='lsv'></div>\n<div id='rsv'></div>\n<div id='hor'></div>\n<div id='lsh'></div>\n<div id='rsh'></div>\n<div id='turn'></div>\n<div id='ls'></div>\n<div id='rs'></div>\n</div>"
        if j=='4':
            generated+="\n<div class='road4' style='display: inline-block;'>\n<div id='main'></div>\n<div id='lss'></div>\n<div id='rss'></div>\n</div>"
        if j=='5':
            generated+="\n<div class='road5' style='display: inline-block;'>\n<div id='ver'></div>\n<div id='lsv'></div>\n<div id='rsv'></div>\n<div id='hor'></div>\n<div id='lsh'></div>\n<div id='rsh'></div>\n<div id='turn'></div>\n<div id='ls'></div>\n<div id='rs'></div>\n</div>"
        if j=='6':
            generated+="\n<div class='road6' style='display: inline-block;'>\n<div id='ver'></div>\n<div id='lsv'></div>\n<div id='rsv'></div>\n<div id='hor'></div>\n<div id='lsh'></div>\n<div id='rsh'></div>\n<div id='turn'></div>\n<div id='ls'></div>\n<div id='rs'></div>\n</div>"
        if j=='c':
            generated+="\n<div class='crossroads' style='display: inline-block;'>\n<div id='centre'></div>\n<div id='tc'></div>\n<div id='trs'></div>\n<div id='tls'></div>\n<div id='lc'></div>\n<div id='lrs'></div>\n<div id='lls'></div>\n<div id='bc'></div>\n<div id='brs'></div>\n<div id='bls'></div>\n<div id='rc'></div>\n<div id='rrs'></div>\n<div id='rls'></div>\n</div>"
        if j=='7':
            generated+="\n<div class='approach1' style='display: inline-block;'>\n<div id='s'></div>\n<div id='sts'></div>\n<div id='bsc'></div>\n<div id='bsls'></div>\n<div id='bsrs'></div>\n<div id='bls'></div>\n<div id='brs'></div>\n</div>"
        if j=='8':
            generated+="\n<div class='approach2' style='display: inline-block;'>\n<div id='s'></div>\n<div id='sts'></div>\n<div id='bsc'></div>\n<div id='bsls'></div>\n<div id='bsrs'></div>\n<div id='bls'></div>\n<div id='brs'></div>\n</div>"
        if j=='9':
            generated+="\n<div class='approach3' style='display: inline-block;'>\n<div id='s'></div>\n<div id='sts'></div>\n<div id='bsc'></div>\n<div id='bsls'></div>\n<div id='bsrs'></div>\n<div id='bls'></div>\n<div id='brs'></div>\n</div>"
        if j=='A':
            generated+="\n<div class='approach4' style='display: inline-block;'>\n<div id='s'></div>\n<div id='sts'></div>\n<div id='bsc'></div>\n<div id='bsls'></div>\n<div id='bsrs'></div>\n<div id='bls'></div>\n<div id='brs'></div>\n</div>"
    generated+="\n</div>"
generated+="<div class='car'>\n<div id='ltw'></div>\n<div id='rtw'></div>\n<div id='lbw'></div>\n<div id='rbw'></div>\n<div id='b'></div>\n<div id='fg'></div>\n<div id='bg'></div>\n<div id='rg'></div>\n<div id='lg'></div>\n<div id='ct'></div>\n<div id='ltl'></div>\n<div id='rtl'></div>\n<div id='lbl'></div>\n<div id='rbl'></div>\n</div>"
generated+="\n<script src='script.js'> </script>\n</body>\n</html>"
file2 = open('index.html','w')
file2.write(generated)