# Problem Solving

## Questions to all the problems I have face 

- [x] **`Printer Errors`**

   In a factory a printer prints labels for boxes. For one kind of boxes the printer has to use colors which, for the sake of simplicity, are named with letters from a to m.

   The colors used by the printer are recorded in a control string. For example a "good" control string would be aaabbbbhaijjjm meaning that the printer used three times color a, four times color b, one time color h then one time color a...

   Sometimes there are problems: lack of colors, technical malfunction and a "bad" control string is produced e.g. aaaxbbbbyyhwawiwjjjwwm.

   You have to write a function printer_error which given a string will output the error rate of the printer as a string representing a rational whose numerator is the number of errors and the denominator the length of the control string. Don't reduce this fraction to a simpler expression.

   The string has a length greater or equal to one and contains only letters from ato z.
   
   *Examples:*
   ```Javascript
   s="aaabbbbhaijjjm"
   error_printer(s) => "0/14"

   s="aaaxbbbbyyhwawiwjjjwwm"
   error_printer(s) => "8/22"
   ``` 

- [x] **`Ones and Zeros`**

   Given an array of one's and zero's convert the equivalent binary value to an integer.
   Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

   *Examples:*
   ```Javascript
   Testing: [0, 0, 0, 1] ==> 1
   Testing: [0, 0, 1, 0] ==> 2
   Testing: [0, 1, 0, 1] ==> 5
   Testing: [1, 0, 0, 1] ==> 9
   Testing: [0, 0, 1, 0] ==> 2
   Testing: [0, 1, 1, 0] ==> 6
   Testing: [1, 1, 1, 1] ==> 15
   Testing: [1, 0, 1, 1] ==> 11
   ```
   However, the arrays can have varying lengths, not just limited to 4.

- [x] **`Complementary DNA`**

   Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

   If you want to know more http://en.wikipedia.org/wiki/DNA

   In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". You have function with one side of the DNA (string, except for Haskell); you need to get the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

   More similar exercise are found here http://rosalind.info/problems/list-view/ (source)

   ```Javascript
   DNAStrand ("ATTGC") # return "TAACG"

   DNAStrand ("GTAT") # return "CATA"
   ```

- [x] **`Equal Sides of An Array`**
   
   You are going to be given an array of integers. Your job is to take that array and find an index N where the sum of the integers to the left of N is equal to the sum of the integers to the right of N. If there is no index that would make this happen, return -1.

   - For example:
   Let's say you are given the array {1,2,3,4,3,2,1}:
   Your function will return the index 3, because at the 3rd position of the array, the sum of left side of the index ({1,2,3}) and the sum of the right side of the index ({3,2,1}) both equal 6.

   Let's look at another one. 
   You are given the array {1,100,50,-51,1,1}: 
   Your function will return the index 1, because at the 1st position of the array, the sum of left side of the index ({1}) and the sum of the right side of the index ({50,-51,1,1}) both equal 1.

   - Last one:
   You are given the array {20,10,-80,10,10,15,35}
   At index 0 the left side is {}
   The right side is {10,-80,10,10,15,35}
   They both are equal to 0 when added. (Empty arrays are equal to 0 in this problem)
   Index 0 is the place where the left side and right side are equal.

   Note: Please remember that in most programming/scripting languages the index of an array starts at 0.

   - Input:
   An integer array of length 0 < arr < 1000. The numbers in the array can be any integer positive or negative.

   - Output:
   The lowest index N where the side to the left of N is equal to the side to the right of N. If you do not find an index that fits these rules, then you will return -1.

   - Note:
   If you are given an array with multiple answers, return the lowest correct index.
   An empty array should be treated like a 0 in this problem.

- [x] **`Don't Give me Five`**

   In this kata you get the start number and the end number of a region and should return the count of all numbers except numbers with a 5 in it. The start and the end number are both inclusive!

   Examples:
   ```Javascript
   1,9 -> 1,2,3,4,6,7,8,9 -> Result 8
   4,17 -> 4,6,7,8,9,10,11,12,13,14,16,17 -> Result 12
   ```

   The result may contain fives. ;-)
   The start number will always be smaller than the end number. Both numbers can be also negative!

- [ ] **`Highest and Lowest`**

   In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

   Example:
   ```Javascript
   highAndLow("1 2 3 4 5"); // return "5 1"
   highAndLow("1 2 -3 4 5"); // return "5 -3"
   highAndLow("1 9 3 4 -5"); // return "9 -5"
   ```

   - Notes:

   All numbers are valid Int32, no need to validate them.
   There will always be at least one number in the input string.
   Output string must be two numbers separated by a single space, and highest number is first.

- [ ] **`Your order, please`**

   Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

   Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

   If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

   Examples:
   ```Javascript
   "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
   "4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
   ""  -->  ""
   ```

- [x] **`Amount of Sets from 0 to N`**

   Giving a number return the amount of sets of numbers that add up to that number and that they are consecutive and less than that number

   Example:
   ```Javascript
   input = 21
   answer = 3
   because [1, 2, 3, 4, 5, 6], [6, 7, 8], [10, 11]
   ```

- [x] **`Mumbling`**

   This time no story, no theory. The examples below show you how to write function accum:

   Example:
   ```Javascript
   accum("abcd");    // "A-Bb-Ccc-Dddd"
   accum("RqaEzty"); // "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
   accum("cwAt");    // "C-Ww-Aaa-Tttt"
   ```

   `The parameter of accum is a string which includes only letters from a..z and A..Z.`

- [x] **`Palindrone`**

   Determine whether an integer is a palindrone. An integer is a palindrone when it reads the same backwards as forward.

   Example:
   ```Javascript
   input = 1234321
   output = true

   input = -121
   output = false
   ```

- [x] **`What's the real floor?`**

   Americans are odd people: in their buildings, the first floor is actually the ground floor and there is no 13th floor ('cause of superstition).

   Write a function that given an American floor (passed as an integer) returns the real floor.
   Moreover, your function should work for basement floors too: just return the same value as the passed one.
   
   Usage Examples:
   ```Javascript
   getRealFloor(1) == 0 
   getRealFloor(0) == 0 // Special case to please Europeans
   getRealFloor(5) == 4
   getRealFloor(15) == 13
   getRealFloor(-3) == -3
   ```
- [x] **`Palindrome - JP Morgarn Hireview Question`**

   Giving a number, check if that number is a palindrone, 
   if is not, reverse that number and add it to the original number given, 
   and keep doing the same recursively until the result of the addition is a palindrone,
   And, if the number given is a palindrome, one addition has to be made.

   Return should be an array or list with two values, number of additions and palindrone found.

   Contrains: number >= 0 

   Examples:
   ```Javascript
   input  -->  0    output  -->  [ 0, 0 ]
   input  -->  121  output  -->  [ 1, 242 ]
   input  -->  97   output  -->  [ 6, 44044 ]
   input  -->  481  output  -->  [ 3, 2552 ]
   input  -->  793  output  -->  [ 3, 3113 ]
   ```

- [x] **`How Many Coins to get to Total - JP Morgan Hireview Question`**

   You are giving coins of values 1, 2, 4. You are also given a total which you have to arrive at.
   Find the minimum number of coins to arrive at the total. 

   `Input:`
   Your program should read lines from standard input. Each line contains a positive integer number
   which represents the total you have to arrive at.

   `Output:`
   Print out the minimum number of coins required to arrive at the total.

   Example:
   ```Javascript
   input --> 20 output --> 5
   input --> 11 output --> 4	
   ```

- [x] **`No Duplicates Digits - JP Morgan (CHASE) Question`**

   Giving a number, check if that number has duplicates digits,
   If it does, reverse that number and add it to the original number given, and keep doing the same
   recursively until the result of the addition has no duplicates.
   And, if the number given has no duplicates, at least one addition has to be made.
 
   Return should be an array or list with two values, number of additions and the result found.
   Return [amount of addition, result]
   Constrains: - Only positive numbers

   Examples:
   ```Javascript
   Input  --> 1234 
   Output --> result --> 1234
              result --> 5555
              answer --> [ 2, 9876 ]
   ---------------------------------
   Input  --> result --> 112
   Output --> result --> 323
              answer --> [ 2, 534 ]
   --------------------------------
   Input  --> 555 
   Output --> result --> 555
              result --> 1110
              result --> 1665
              result --> 2220
              result --> 2775
              result --> 3330
              result --> 3885
              result --> 4440
              result --> 4995
              result --> 5550
              answer --> [ 10, 6105 ]
   ```

- [ ] **`Find the missing term in an Arithmetic Progression`**

   An Arithmetic Progression is defined as one in which there is a constant difference between the consecutive terms of a given series of numbers. You are provided with consecutive elements of an Arithmetic Progression. There is however one hitch: exactly one term from the original series is missing from the set of numbers which have been given to you. The rest of the given series is the same as the original AP. Find the missing term.

   You have to write the function findMissing(list), list will always be at least 3 numbers. The missing term will never be the first or last one.

   Examples:
   ```Javascript
   findMissing([1, 3, 5, 9, 11]) == 7
   ```

   ...
   PS: This is a sample question of the facebook engineer challenge on interviewstreet. I found it quite fun to solve on paper using math, derive the algo that way. Have fun!

- [ ] **`Multiplication of Numbers in an Array`**

   Giving an array return the multiplication of all numbers of the array except  for the item at index i.
   
   Examples:
   ```Javascript
   Input:  [1, 2, 3, 4]
   Output: [29, 13, 8, 9]
   ------------------------
   Input: [1, 3, 5, 7]
   Outpu: [105, 35, 21, 15]
   ```

- [x] **`Reverse an Integer`**

   --- Directions
   Given an integer, return an integer that is the reverse ordering of numbers.

   --- Examples:   
   ```Javascript 
   reverseInt(15) === 51
   reverseInt(981) === 189
   reverseInt(500) === 5
   reverseInt(-15) === -51
   reverseInt(-90) === -9
   ```

- [x] **`Reverse a String`**

   --- Directions
   Given a string, return a new string with the reversed order of characters
   
   --- Examples:
   ```Javascript
   reverse('apple') === 'leppa'
   reverse('hello') === 'olleh'
   reverse('Greetings!') === '!sgniteerG'
   ```

- [x] **`Check if a string is a Palindrone`**

   --- Directions
   Given a string, return true if the string is a palindrome
   or false if it is not.  Palindromes are strings that
   form the same word if it is reversed. *Do* include spaces
   and punctuation in determining if the string is a palindrome.

   --- Examples:
   ```Javascript
   palindrome("abba") === true
   palindrome("abcdefg") === false
   ```
- [x] **`Fizzbuzz`**

   --- Directions
   Given a string, return the character that is most
   commonly used in the string.
   
   --- Examples:
   ```Javascript
   maxChar("abcccccccd") === "c"
   maxChar("apple 1231111") === "1"
   ```

- [x] **`Implement a Stack - Amazon`**

   Implement a stack that has the following methods:
   
   --- Directions
   push(val), which pushes an element onto the stack
   pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
   max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.

- [x] **`Count Security Alerts - HRT Practice`**

  Problem
  You are given a list of strings representing alert types generated by a security system.

  Task 1
  Return a dictionary showing how many times each alert appears.
  Write a function that returns a dictionary with alert counts.

  --- Examples:
  ```Python
  SecurityAlerts.count_security_alert_types(alerts) == {'WAF_BLOCK': 3, 'BOT_DETECTED': 2, 'LOGIN_FAIL': 3}
  ```

  Task 2
  Now we add structure, just like real security logs.
  Return a dictionary counting alerts by type, ignoring severity.

  --- Examples:
  ```Python
  SecurityAlerts.count_structure_security_alert_types(structure_alert) == {'WAF_BLOCK': 2, 'BOT_DETECTED': 2, 'LOGIN_FAIL': 2}
  ```

  Task 3
  Count only alerts with severity "high", grouped by type.

  --- Examples:
  ```Python
  SecurityAlerts.count_alert_with_high_severity(high_sev_alerts) == {'WAF_BLOCK': 2, 'LOGIN_FAIL': 1}
  ```

  Task 4 - Top-K High Severity Alerts
  1. Only consider alerts with severity "high" (case-insensitive).
  2. Count how many times each alert type appears.
  3. Return the top 2 alert types by count.
    - If there is a tie, include both.
    - Output can be a list of alert types or a dictionary of type → count.

  --- Examples:
  ```Python
  SecurityAlerts.count_top_k_high_sev_alerts(top_k_high_sev_alerts) == {'WAF_BLOCK': 2, 'LOGIN_FAIL': 2}
  ```

- [x] **`- HRT Practice`**

  You are given a list of HTTP log entries like this:

  Task:
  Return a dictionary showing how many times each status code appears on a list of dictionaries.

  --- Examples:
  ```Python
  HTTPStatus.count_http_status(logs) == {403: 6}
  ```

- [x] **`Sliding Window | Failed Login Logs Rate Detection - HRT Practice`**

  Task 1
  Detect IPs that have 3 or more requests within any 10-second window.

  --- Examples:
  ```Python
  SlidingWindow.failed_login_rate_detection(ip_logs) == ['1.1.1.1', '2.2.2.2']
  ```

- [x] **`LOG Parsing Aggregation`**

  Problem
  You are given application logs.
  Each log contains an IP, endpoint, and HTTP status.

  Task 1:
  Return the top 2 endpoints that produced the most 4xx or 5xx errors.

- [x] **`Unique Suspicious IPs`**
  
  Problem
  You’re given a list of security events.
  Each event contains an IP and an action.
  
  Return a set of IPs that performed any suspicious action.
  
  Suspicious actions are:
  "LOGIN_FAIL"
  "WAF_BLOCK"
  "BOT_DETECTED"

- [x] **``Log Analysis - Practice Problems``**

  Task 1: simulate_grep
  
  Problem Statement:
  Given a list of log strings, return a list of logs that contain a given keyword. This is similar to the UNIX grep command.

  --- Examples:
  ```Python
  logs_line = [
   "ERROR failed login from 1.1.1.1",
   "INFO user logged in",
   "WARN suspicious activity detected",
   "ERROR database connection failed"
  ]
  keyword = "ERROR"
   
  simulate_grep(logs_line, keyword) == [
   "ERROR failed login from 1.1.1.1",
   "ERROR database connection failed"
  ]
  ```

  Task 2: detect_burst_errors
  
  Problem Statement:
  Given a list of log strings, detect if there are 3 or more consecutive logs containing a specific keyword. Return True if such a burst exists, else return False.

  --- Examples:
  ```Python
  logs_line = [ 
   "ERROR failed login from 1.1.1.1",
   "ERROR database connection failed",
   "ERROR something else",
   "INFO user logged in"
  ]
   
   keyword = "ERROR"
   detect_burst_errors(logs_line, keyword) == True
  ```
  
  Task 3: ten_sec_error_logs
  
  Problem Statement:
  Given a list of logs with timestamps and messages, detect if 3 or more logs containing a keyword occur within any 10-second window. Return True if such a burst occurs, otherwise False.

  --- Examples:
  ```Python
  logs = [
   {"timestamp": 1, "message": "ERROR failed login"},
   {"timestamp": 3, "message": "INFO user logged in"},
   {"timestamp": 5, "message": "ERROR db connection failed"},
   {"timestamp": 8, "message": "ERROR something else"},
   {"timestamp": 15, "message": "ERROR again"}
  ]
  
  ten_sec_error_logs(logs) == True
  ```

- **``Queue Base Sliding Window``**

  Problem: Suspicious IP Rate Detection
  
  You are given a list of application logs.
  Each log entry contains:
  ip (string)
  timestamp (integer, seconds, sorted in ascending order)
  status (integer HTTP status code)

  Goal:
  Detect all IP addresses that have:
     3 or more failed requests (status >= 400)
     Within any 10-second window
     Across any endpoint (endpoint does not matter)
  Return the unique suspicious IPs.

