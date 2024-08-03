input = ("S3(TR)3SL")
inputs = list(input)
num = 0
bead = -1
beadInbrac = ""
answer = ""
totalnumbsofbeads = [0,0,0,0]
def isint(isint):
    try:
        int(isint)
        return True
    except:
        return False

while bead < (len(inputs)-1):
    bead += 1

    if isint(inputs[bead]) == False:
        answer += inputs[bead]

    elif isint(inputs[bead]) and inputs[bead+1] != "(":
        num = int(inputs[bead])
        for i in range(num):
            answer += inputs[bead+1]
        bead += 1

    elif isint(inputs[bead]) and inputs[bead+1] == "(":
        num = int(inputs[bead])
        bead += 2
        while inputs[bead] != ")":
            beadInbrac += inputs[bead]
            bead += 1
        for i in range(num):
            answer += beadInbrac
print(answer)
answer = list(answer)
for i in range (len(answer)):
    if(answer[i] == "S"):
        totalnumbsofbeads[0] +=1
    elif(answer[i] == "T"):
        totalnumbsofbeads[1] +=1
    elif(answer[i] == "R"):
        totalnumbsofbeads[2] +=1
    elif(answer[i] == "L"):
        totalnumbsofbeads[3] +=1
print("S: ",totalnumbsofbeads[0],"T: ",totalnumbsofbeads[1],"R: ",totalnumbsofbeads[2],"L: ",totalnumbsofbeads[3])