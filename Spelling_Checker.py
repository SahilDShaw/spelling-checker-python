import os

def Find_Difference(string1, string2, dp):
    n = len(string1)
    m = len(string2)

    for i in range(n-1, -1, -1):
        dp[i][m][0] = n-i
        dp[i][m][1] = dp[i][m][2] = -1
        dp[i][m][3] = i

    for j in range(m-1, -1, -1):
        dp[n][j][0] = m-j
        dp[n][j][2] = dp[n][j][3] = -1
        dp[n][j][1] = j

    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if string1[i]==string2[j]:
                dp[i][j][0] = dp[i+1][j+1][0]
                dp[i][j][1] = dp[i][j][2] = dp[i][j][3] = -1

            else:
                val = min(dp[i+1][j+1][0],min(dp[i+1][j][0],dp[i][j+1][0])) + 1
                dp[i][j][0] = val
                if val == dp[i+1][j+1][0]+1:
                    dp[i][j][1] = i
                    dp[i][j][2] = dp[i][j][3] = -1
                elif val == dp[i][j+1][0]+1:
                    dp[i][j][2] = j
                    dp[i][j][1] = dp[i][j][3] = -1

                else:
                    dp[i][j][3] = i
                    dp[i][j][2] = dp[i][j][1] = -1
                    
    return dp[0][0][0]

def Calculate_Edit_Distance(string1, string2):
    m = len(string1)
    n = len(string2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if string1[i - 1] == string2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
     
    return dp[-1][-1]

def Find_Edit_Distance(inp):
    # trying read from testout.txt if not found nothing happens
    try:
        tp = open("testout.txt", mode = 'r')
        tmp = ""
        found = False
        sz=len(inp)
        for tmp in tp:
            word=tmp[:sz]
            if word==inp:
                found = True
                print("\nFound in testout.txt\n", end = '')
                print(tmp + "\n", end = '')
                break
        tp.close()
    except:
        pass
    
    
    if not found:
        print("\nWord not found in testout.txt\n", end = '')
        try:
            fp = open("book.txt", mode = 'r')
        except:
            print("book.txt could not open\n", end = '')
            exit(1)
        
        try:
            t = open("testout.txt", mode = 'a+')
        except:
            print("testout.txt could not open!\n", end = '')
            exit(1)
        
        distance = None
        minimum_distance = 4
        temp = ""
        minStr = ""

        t.write(inp + "\t")
        print(inp + "\t", end = '')

        for temp in fp:
            temp = temp[:-2]
            distance = Calculate_Edit_Distance(inp,temp)
            
            if distance < minimum_distance:
                minimum_distance = distance
                minStr = temp
            
            if distance == 0:
                t.write("\tOK.")
                print("OK.", end = '')
                break
        
        if minimum_distance > 3:
            t.write("\tNONE.")
            print("NONE.", end = '')
            
        elif minimum_distance!=0 and minimum_distance < 4:
            t.write(minStr + "\t")
            print(minStr + "\t", end = '')

            n = len(inp)
            m = len(minStr)
            
            dp = [[[0 for x in range(4)] for x in range (m+1)] for y in range(n+1)]
            
            Find_Difference(inp, minStr, dp)
            
            s = ""
            i = 0
            j = 0
            while i<n and j<m:
                if dp[i][j][1]!=-1:
                    s += "Update: " + inp[i] + " to " + minStr[j] + "\t"
                    i += 1
                    j += 1
                elif dp[i][j][2]!=-1:
                    s += "Insert: " + minStr[j] + "\t"
                    j += 1
                elif dp[i][j][3]!=-1:
                    s += "Delete: " + inp[i] + "\t"
                    i += 1
                else:
                    i += 1
                    j += 1

            while j<m:
                s += "Insert: " + minStr[j] + "\t"
                j += 1
            while i<n:
                s += "Delete: " + inp[i] + "\t"
                i += 1

            print(s, end = '')
            t.write(s)

        t.write("\n")
        print("\n", end = '')
        t.close()

def main():
    while True:
        os.system("cls")
        print("Menu:\n", end = '')
        print("1)Enter a word\n", end = '')
        print("2)Exit\n", end = '')
        
        ch = ""
        inp = ""
        ch = input("Enter Your Choice: ")
        os.system("cls")
        
        if ch == "1":
            inp = input("Enter a word: ")
            Find_Edit_Distance(inp)
        elif ch == "2":
            exit()
        else:
            print("Invalid Input. ", end = '')

        print("\nEnter a key to continue....\n", end = '')
        input()

if __name__ == "__main__":
    main()