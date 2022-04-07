############
# bulldogpussyswag kotter
# 29.03.2022
# UL 10
############
import re as s


#IP-d
#avab faili
fail = open('tekstifail.txt')
for line in fail:
    #paneb arvud failist 6igesse j2rjekorda
    if s.search('^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$', line):
        print(line, end='')


#Parool
#avab faili
fail = open('tekstifail.txt')
#Teeb parooli mis sisaldab arve, suuritähi kui ka väikseid
for line in fail:
    if s.search('^.*(?=.{8,10})(?=.*[a-zA-Z])(?=.*?[A-Z])(?=.*\d)[a-zA-Z0-9[\]]+$', line):
        print(line, end='')
