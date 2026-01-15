# Nested Exception Handling
# We have to open a file which is present inside the excecption handling folder name -> demo_file.txt
# So if the file does not exsist it will raise some error
# and if we can't read that file then also error must come


file_path = r"D:\BridgeLabz-Apexon-Training\BridgeLabz-Apexon-Training\Python Training\Python\Exception Handling\demo_file.txt"

try:
    print("Opening a file")
    f = open(file_path)
    try:
        text = f.read() # raise exception if can't read the file from whatever reason like network issue
        print(text)
    except Exception as e:
        print(f"{file_path} could not able to read! {e}")
    finally:
        f.close()
        print("file is closed")
except FileNotFoundError as e:
    print("File does not exist",e)


print("Program is finished")


### Nested exception handling is not recommended as it makes exception handling more complex ###

#### Raising Exceptions in Python ####
# We have the option to throw an exception if certain conditions are met. It allows us to interrupt
# the program based on our requirement.
value = int(input("Enter value less than 10: "))
if value >= 10:
    raise ValueError("Please add number lower than 10..") #These kind exception raised by the developer only.
else:
    print("You Won the Bet!!!")
