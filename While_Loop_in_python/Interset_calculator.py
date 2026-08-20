principle = 0
rate = 0
time = 0
while principle <= 0:
    principle = float(input(" Enter the Principle: "))
    if principle <= 0:
        print("Principle is invalid")
        print(principle)

        while rate <= 0:
            rate = float(input(" Enter the interset rate: "))
            if rate <= 0:
                print(" interset rate is invalid")
                print(rate)

                while time <= 0:
                    time = float(input(" Enter the time in years: "))
                    if time <= 0:
                        print(" time is invalid")
                        print(time)







