file = open('map.txt','r')
map = file.readlines()
file.close()
#1-top right
#2-horizontal
#3-top left
#4-vertical
#5-bottom left
#6-bottom right
generated="<!DOCTYPE html>\n<html lang='en'>\n<head>\n<meta charset='UTF-8'>\n<meta http-equiv='X-UA-Compatible' content='IE=edge'>\n<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n<link rel='stylesheet' href='style.css'>\n<title>Document</title>\n</head>\n<body>\n"
for i in map:
    generated+="\n<div class='row' style='display: flex;'>"
    for j in i:
        if j=='0':
            generated+="\n<div class='ground' style='display: inline-block;'></div>\n"
        if j=='1':
            generated+="\n<div class='road1' style='display: inline-block;'>\n<div id='ver'></div>\n<div id='lsv'></div>\n<div id='rsv'></div>\n<div id='hor'></div>\n<div id='lsh'></div>\n<div id='rsh'></div>\n<div id='turn'></div>\n<div id='ls'></div>\n<div id='rs'></div>\n</div>"
        if j=='2':
            generated+="\n<div class='road2' style='display: inline-block;'>\n<div id='main'></div>\n<div id='ls'></div>\n<div id='rs'></div>\n</div>"
        if j=='3':
            generated+="\n<div class='road3' style='display: inline-block;'>\n<div id='ver'></div>\n<div id='lsv'></div>\n<div id='rsv'></div>\n<div id='hor'></div>\n<div id='lsh'></div>\n<div id='rsh'></div>\n<div id='turn'></div>\n<div id='ls'></div>\n<div id='rs'></div>\n</div>"
        if j=='4':
            generated+="\n<div class='road4' style='display: inline-block;'>\n<div id='main'></div>\n<div id='ls'></div>\n<div id='rs'></div>\n</div>"
        if j=='5':
            generated+="\n<div class='road5' style='display: inline-block;'>\n<div id='ver'></div>\n<div id='lsv'></div>\n<div id='rsv'></div>\n<div id='hor'></div>\n<div id='lsh'></div>\n<div id='rsh'></div>\n<div id='turn'></div>\n<div id='ls'></div>\n<div id='rs'></div>\n</div>"
        if j=='6':
            generated+="\n<div class='road6' style='display: inline-block;'>\n<div id='ver'></div>\n<div id='lsv'></div>\n<div id='rsv'></div>\n<div id='hor'></div>\n<div id='lsh'></div>\n<div id='rsh'></div>\n<div id='turn'></div>\n<div id='ls'></div>\n<div id='rs'></div>\n</div>"
    generated+="\n</div>"
generated+="</body>\n</html>"
file2 = open('index.html','w')
file2.write(generated)