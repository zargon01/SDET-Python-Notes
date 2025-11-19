# Pseudocode

### What is Pseudocode?

**Pseudocode** is a simple, informal way of describing a program or algorithm using plain English mixed with code-like keywords.  
It is **not real code** — a computer cannot execute it — but it looks similar to programming code and helps humans understand the logic clearly.

**Key Features**
- Written in simple words
- No strict syntax rules (no semicolons, no brackets, no data types)
- Much easier and faster than writing actual code
- Uses common keywords like INPUT, OUTPUT, IF, ELSE, THEN, etc.
- Main purpose: Plan and test the logic **before** writing the real program

### Common Pseudocode Keywords

| Keyword          | Meaning                              | Example                            |
|------------------|--------------------------------------|------------------------------------|
| START / BEGIN    | Beginning of pseudocode              | START                              |
| END              | End of pseudocode                    | END                                |
| INPUT / READ     | Take input from user                 | INPUT age                          |
| PRINT / OUTPUT / DISPLAY | Show output                | PRINT "Hello"                      |
| IF               | Start condition                      | IF marks ≥ 35 THEN                 |
| THEN             | Action when condition is true        | PRINT "Pass"                       |
| ELSE             | Action when condition is false       | PRINT "Fail"                       |
| ENDIF            | End of IF block                      | ENDIF                              |
| WHILE            | Repeat while condition is true       | WHILE count ≤ 10                   |
| ENDWHILE         | End of WHILE loop                    | ENDWHILE                           |
| REPEAT … UNTIL   | Repeat until condition becomes true  | REPEAT … UNTIL choice = "N"        |
| ← or =           | Assignment (store value)             | total ← total + 10                 |

### Advantages of Using Pseudocode

- Easy to read and write
- No syntax errors to worry about
- Helps catch logical mistakes early
- Can be easily converted into any programming language
- Understood by teachers, students, and non-programmers

### Rules for Writing Good Pseudocode

1. Use indentation for blocks (IF, loops)
2. Write one statement per line
3. Use CAPITAL letters for keywords (recommended)
4. Be clear and unambiguous
5. Keep it simple!

### Examples

**Example 1: Check if a number is positive**

START
INPUT number
IF number > 0 THEN
PRINT "Positive"
ELSE
PRINT "Not Positive"
ENDIF
END


**Example 2: Print numbers 1 to 5**

START
count ← 1
WHILE count <= 5
PRINT count
count ← count + 1
ENDWHILE
END


**Example 3: Simple calculator (addition)**

START
INPUT num1, num2
sum ← num1 + num2
PRINT "Sum =", sum
END