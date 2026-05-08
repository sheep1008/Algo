dic = {'A' : 4, 'B' : 3, 'C' : 2, 'D' : 1}
answer= 0 
string = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
for s in string:
    answer += dic[s]
print(answer)