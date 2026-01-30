"""
    Leap Year
     a. I/P -> Year, ensure it is a 4-digit number.
     b. Logic -> Determine if it is a Leap Year.
     c. O/P -> Print the year is a Leap Year or not.
"""

def check_leap_year(year):
    try:
        str_year = str(year)
        if  len(str_year)!=4:
            raise ValueError("Please Enter a four digit number only")
        elif year<0:
            raise ValueError("-ve number not allowed")

        if year%100==0:
            if year%400==0:
                print(f"{year} is a leap year")
            else:
                print(f"{year} is not leap year")
        elif year%4==0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")


    except  ValueError as e:
        print("Error ->", e)


def main():
    year = int(input("Enter year : "))
    check_leap_year(year)



if __name__ == "__main__":
    main()