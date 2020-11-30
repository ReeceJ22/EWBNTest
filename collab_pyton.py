def main():
    usertime = float(input("Enter the number of seconds: "))
    #< 60
    if usertime < 60:
        print('The number of seconds is less than one minute')
    #> 60
    if usertime >=60:
        print(int(usertime), 'seconds are equal to:')
    #sec in day
    day = usertime // 86400
    timeDay = usertime % 86400
    if day >= 1:
        print(int(day), ' full day(s) and ',int(timeDay), 'seconds.')
    #Sec in hour
    hour = usertime // 3600
    #R
    timeHour = usertime % 3600
    if hour >= 1:
        print(int(hour), ' full hours(s) and ',int(timeHour), 'seconds.')
    #Secin minute
    minutes = usertime // 60
    #R
    timeMin = usertime % 60
    if minutes >= 1:
        print(int(minutes), ' full minutes(s) and ',int(timeMin), 'seconds.')
    #loop
    restart=input("Do you want to try a different number? [y/n]")
    if restart == "y":
        main()
    else:
        exit()

main()
