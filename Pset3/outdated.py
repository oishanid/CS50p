months = [
    "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
]  # YYYY-MM-DD

while True:
    try:
        date = input("Date: ")  # MM-DD-YYYY inputted like 9/8/26 or September 8, 2026
        clean_date = date.replace("/", " ").replace(",", " ").split()
        month, day, year = clean_date
        # could've done: if len(month) != 4: pass
        if month in months:  # Check if 2nd format is inputted correctly
            if "/" in date or not "," in date:
                pass
            else:  # If inputted correctly, go forward
                if month in months:
                    month = months.index(month) + 1
                    day = int(day)
                    year = int(year)
                    if day > 31 or month > 12:
                        pass
                    else:
                        break
        else:  # If 1st (number) format
            month = int(month)
            day = int(day)
            year = int(year)
            if day > 31 or month > 12:
                pass
            else:
                break
    except:
        pass

print(f"{year:04}-{month:02}-{day:02}")
