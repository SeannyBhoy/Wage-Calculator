sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
try:
    fr = float(sr)
    fh = float(sh)
except:
        print("Error, please enter numeric input")
        quit()

#Overtime Calc
#print(fh, fr)
if fh > 44:
    reg = fr * fh
    otp = (fh - 44) * (fr * 0.5)
    print(reg + otp)
    xp = reg + otp
else:
    xp = fh * fr
#Tax Calc
atp = (xp * 0.85)

print("Gross Regular Pay:",reg)
print("Gross Overtime Pay:",otp)

print("Total Gross:",xp)
print("Total Net:",atp)
