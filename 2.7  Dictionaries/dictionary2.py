monthConversions ={
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print("Example: Jan,Feb,Mar.....")
print("Short form of month to get their full form")
a = input()
print(monthConversions.get(a))