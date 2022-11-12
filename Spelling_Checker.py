# before executing the code please upload the 'book.txt' file to file section in Google Colab
# this program takes an word as an input then calculates its edit distance from each of the word present in 'book.txt'
# if the word's distance from all the words is MORE THAN 3 then our program does not give any suggestion and prints NONE.
# else we find out the word with smallest distance from the given word
# then calculate the steps to reach the correct word using Calculate_Steps function
# after that we print the output on the console and save it inside 'testout.txt'.

# In this way, we employ DYNAMIC PROGRAMMING in 
# 1) calculating edit distance, 
# 2) calculating steps to reach correct word, and 
# 3) reading already calculated words from 'testout.txt'

import os

# calculates the steps to convert string1 to string2
def Calculate_Steps(string1, string2, dp):
    n = len(string1)
    m = len(string2)

    for i in range(n-1, -1, -1):
        # storing the minimum distance in the index 0
        dp[i][m][0] = n-i 
        # storing -1 for update and insert operation   
        dp[i][m][1] = dp[i][m][2] = -1  
        # storing index of character to be deleted for delete operation
        dp[i][m][3] = i    

    for j in range(m-1, -1, -1):
        # storing the minimum distance in the index 0
        dp[n][j][0] = m-j
        # storing -1 for delete and insert operation  
        dp[n][j][2] = dp[n][j][3] = -1
        # storing index of character to be updated for update operation
        dp[n][j][1] = j

    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            # if characters are equal no need to perform any operation
            if string1[i]==string2[j]: 
                # the edit disance will be same as for the state i+1,j+1
                dp[i][j][0] = dp[i+1][j+1][0]
                # No need to perform any operation therefore storing -1 for every operation
                dp[i][j][1] = dp[i][j][2] = dp[i][j][3] = -1

            else:
                # Minimum distance for the state will be minimum value among three operations + 1
                val = min(dp[i+1][j+1][0],min(dp[i+1][j][0],dp[i][j+1][0])) + 1
                dp[i][j][0] = val
                # if minimum value is for update operaion
                if val == dp[i+1][j+1][0]+1:
                    dp[i][j][1] = i
                    dp[i][j][2] = dp[i][j][3] = -1
                # if minimum value is for insert operation
                elif val == dp[i][j+1][0]+1:
                    dp[i][j][2] = j
                    dp[i][j][1] = dp[i][j][3] = -1
                # if minimum value is for delete operation
                else:
                    dp[i][j][3] = i
                    dp[i][j][2] = dp[i][j][1] = -1                
    return dp[0][0][0]

# calculates the edit distance between string1 and string2
def Calculate_Edit_Distance(string1, string2):
    m = len(string1)
    n = len(string2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        # minimum distance for i,0 state is i
        dp[i][0] = i
    for j in range(n + 1):
        # minimum distance for 0,j state is j
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # if both the characters are equal no need to perform any operation
            if string1[i - 1] == string2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            # selecting the optimal operation for the state
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
     
    return dp[-1][-1]

def Find_Edit_Distance(inp):
    # trying read from testout.txt if not found nothing happens
    found = False
    try:
        tp = open("testout.txt", mode = 'r')
        tmp = ""
        sz=len(inp)
        # checking if the input word have already been calculated
        for tmp in tp:
            word=tmp[:sz]

            if word==inp:
                found = True
                print("\nWord already computed\n", end = '')
                print(tmp + "\n", end = '')
                break
        tp.close()
    except:
        pass
    
    # if the input word is not found in the testout.txt file
    if not found:
        print("\nWord not already computed\n", end = '')
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
        # restrinting the maximum distance for the input word to 4
        minimum_distance = 4
        temp = ""
        minStr = ""
        # writing the input word in testout.txt file
        t.write(inp + "\t")
        print(inp + "\t", end = '')

        # traversing in the book.txt file to calculate the edit distance for each word present in the file and the input word.
        for temp in fp:
            temp = temp[:-2]
            distance = Calculate_Edit_Distance(inp,temp)
            # if the distance is smaller than the minimum_distance updating the value of minimum_distance and minstr
            if distance < minimum_distance:
                minimum_distance = distance
                minStr = temp
            # if distance is zero, it means word is present in the dictionary, therfore print ok.
            if distance == 0:
                t.write("\tOK.")
                print("OK.", end = '')
                break
            
        # if minimum distance is greater than 4 it means no word in the book.txt is appropriate enough for the input word
        if minimum_distance > 3:
            t.write("\tNONE.")
            print("NONE.", end = '')
         
        # if minimum_distance is greater than 0 and smaller than 4, computing the optimal steps for minstr   
        elif minimum_distance!=0 and minimum_distance < 4:
            t.write(minStr + "\t")
            print(minStr + "\t", end = '')

            n = len(inp)
            m = len(minStr)
            
            dp = [[[0 for x in range(4)] for x in range (m+1)] for y in range(n+1)]
            
            # calling the function to store information of all states in the 3-D matrix dp
            Calculate_Steps(inp, minStr, dp)
            
            # printing the optimal operations for each state with the help of dp matrix
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
            # writing the operations in the testout.txt file
            t.write(s)

        t.write("\n")
        print("\n", end = '')
        t.close()

def main():
    while True:
        os.system("cls")
        # Given two options for the user to choose from
        print("Menu:\n", end = '')
        print("1)Enter a word\n", end = '')
        print("2)Exit\n", end = '')
        
        ch = ""
        inp = ""
        ch = input("Enter Your Choice: ")
        os.system("cls")
        
        # selecting the first option
        if ch == "1":
            inp = input("Enter a word: ")
            # calling the function to print appropriate steps for the input word
            Find_Edit_Distance(inp)
            
        # selecting the exit option
        elif ch == "2":
            exit()
            
        # in case of invalid input user is send back to the menu 
        else:
            print("Invalid Input. ", end = '')

        print("\nPress Enter to Continue....\n", end = '')
        input()

if __name__ == "__main__":
    main()