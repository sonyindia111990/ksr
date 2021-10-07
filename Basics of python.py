# 1. PRINT STATEMENT: [syntax: print()]

print("hello world")

# 2. PRINT BLANK LINES:

print(4 * "\n")  # it's print 4 blank lines

""" NOTE:
        1. print("\n\n\n\n")  this is another print statement to print 4 blank lines """

# 3. PRINT END COMMAND: [syntax : print("", end ="")]
""" NOTE:
        1. In  python(above 3+ version) every print() statement have end command, the default value of end command 
           is '\n'. because of that after every print statement next statement comes/print in newline in output.
        2. You can end a print statement with any character or string using this 'end' parameter.
        3. For example if you replace end statement with space then the next print statement not printed in newline
           because we replaced end statement value i.e \n with space so next statement print along with current print 
           statement with space. check below print statements"""

print("---print end command start---\n")

print("default print statement,")  # here we didn't mention any end command, so the default value is '\n'
print("without end command\n")

print("1st print statement with space end command,", end=' ')  # here we replaced '\n' with space by using end command
print("2nd print statement w/o end command\n")

print("1st print statement with space end command,", end=' ')  # replaced '\n' with space
print("2nd print statement with character(!) end command", end='!')  # replaced '\n' with '!' character, so next print
# statement print beside this.

print("\n---print end command end---\n")

# 4. MAIN FUNCTION: [syntax : def function_name()]

print("--- main() start---\n")


def main():  # here we declare main()
    print("main function start")
    var1 = 1
    print(var1)
    var2 = "inside main()"
    print(var2)
    print("main function end\n")


main()  # here we call the main(), if you want to run main() we must call it.
print("outside the main()\n")

print("---main() end---\n")

# 5. DECLARE AND RE-DECLARE VARIABLE:

print("---declare and re-declare start---\n")

var3 = 1  # here we declare the variable with integer
print("var3 value before re-declare:", var3)
var3 = "var3 successfully re-declared"  # here we re-declare the variable with string
print("var3 value after re-declare:", var3)

print("\n---declare and re-declare end---\n")

# 6. ATTACH/CONCATENATE VARIABLES:

print("---Concatenate Variables start---\n")

var4 = " string var4 "
var5 = 5
var6 = " string var6 "
var7 = 7

print("concatenate string var4 with integer var5 is: ", var4 + str(var5))
print("concatenate string var4 with string var6 is: ", var4 + var6)
print("concatenate integer with integer is:", str(var5) + str(var7))

print("\n---Concatenate Variables end---\n")

"""NOTE:
        1. we can not concatenate string with integer directly, so we use str() method to declare integer value as
           string.  
        2. similarly we can't concatenate integer with integer directly its do addition. so we have to use str() method
           to concatenate integer with integer.    
"""

# 6. LOCAL AND GLOBAL VARIABLES:

"""NOTE:
        1. any variable declared in inside function (var10) is called  LOCAL VARIABLE
        2. any variable declared in outside function (var8,var9) is called GLOBAL VARIABLE
        3. all variables we used in function is must declare before function calling other wise its leeds to error
        4. if you declaring a variable as GLOBAL VARIABLE (var11) then you shouldn't declare that variable
           before global syntax in inside the function, if you did that leeds to error
        5. if you use any local variable (var10) outside function its leeds to error.
        6. we can use global variable (var8,var9) inside function but we can't use local variable (var10) outside 
           function without declaring as global variable (var11).
"""
print("---local and global variable start---\n")

var8 = "var8 is global variable"  # here var8 is global variable
var9 = "var9 is global variable"
print(var8)


def main2():
    print("\nmain2() start\n")

    var8 = "var8 is local variable"  # here var8 is local variable. the value of var8 valid inside this function only.
    print(var8)
    var10 = "var10 is local variable"  # var10 is local variable because its define in inside function. if you used
    # var10 variable outside the function without define its leeds to error because its local variable.
    print(var10)
    print(var9)  # we printing/calling global variable inside function.
    global var11  # make sure that var11 is not declare before this syntax, if you declared its leeds to error.
    var11 = "var11 declared as global variable inside function"
    print("inside function var11 value:", var11)
    print("\nmain2() end\n")


main2()
print(var8)
print("outside function var11 value:", var11)

print("\n---local and global variable end---\n")

# 7. DELETE VARIABLE: [syntax: del variable_name ]

var12 = 12
del var12  # var12 variable is deleted.

# 8. SPECIAL AND ESCAPE CHARACTER:

""" NOTE:
        1. In python "\t" and "\n" is called as "SPECIAL CHARACTER" and "\" called as "ESCAPE CHARACTER"
           '\t' is a tab
           '\n' is a new line
           '\' is escape character, it means '\' becomes hide/escape and print content before and next to it. 
"""

print("---special and escape character start---\n")
print("1. '\\t'character")  # ESCAPE character
print("apple", "\torange")  # special character '\t' it's gives space b/w two words.
print("2. '\\n'character")  # ESCAPE character
print("apple\n", "orange", "\n")  # special character '\n' it's produce new line b/w two words
print("3. '\\'escape character")  # ESCAPE character
print("it\'s raining here")  # ESCAPE character '\' it's produce single/double quotations.
print("\"hello\"")  # ESCAPE character '\' it's produce single/double quotations.
print("'\'hello")
print("\n---special and escape character end---\n")

# 9. RAW STRING: [syntax: print(r"") or print(R"")]

""" NOTE:
        1. raw strings means it's print text/value inside the quotation r"" or R"" as it is.
        2. its define with R"" or r"".
"""
print("---raw string start---\n")
print(r"hello '\n' and '\t' this is raw string example")  # RAW STRING: it's print text after 'r' or 'R' as it is
print(R"hello '\n' and '\t' this is raw string example")
print("\n---raw string end---\n")

# the content b/w """ """ is taken as paragraph or multiple line string, it is used when need to print paragraphs
# syntax: print(""" """). if you not mention print statement with """ """ quotation  it is not print in o/p.
