


import tkinter as Tk
window = Tk.Tk()
window.title("Pay Calculator")
window.resizable(width=False, height=False)
def calculate_wage():
    sh = ent_hours.get(
    )
    sr = ent_rate.get()
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

    label_gr["text"] = "Regular Gross", reg
    label_og["text"] = "Overtime Gross", otp
    label_tg["text"] = "Total Gross", xp

    label_total_net["text"] = "Total Net", atp



frm_hours = Tk.Frame(master=window)
ent_hours = Tk.Entry(master=frm_hours, width=10)
lbl_hours = Tk.Label(master=frm_hours, text="Hours Worked")



frm_rate = Tk.Frame(master=window)
ent_rate = Tk.Entry(master=frm_rate, width=10)
lbl_rate = Tk.Label(master=frm_rate, text="Wage")

frm_net = Tk.Frame(master=window)
label_total_net=Tk.Label(master=frm_net)

frm_gr = Tk.Frame(master=window)
label_gr=Tk.Label(master=frm_gr)

frm_og = Tk.Frame(master=window)
label_og=Tk.Label(master=frm_og)

frm_tg = Tk.Frame(master=window)
label_tg=Tk.Label(master=frm_tg)


btn_calc = Tk.Button(
    master=window,
    text="Calculate",
    command=calculate_wage
)
frm_hours.grid(row=2,column=0)
lbl_hours.grid(row=2,column=0,)
ent_hours.grid(row=2,column=1,)
frm_rate.grid(row=3,column=0)
lbl_rate.grid(row=3,column=0,)
ent_rate.grid(row=3,column=1,)
btn_calc.grid(row=4,column=0)
frm_gr.grid(row=5,column=1)
label_gr.grid(row=5,column=1)
frm_og.grid(row=6,column=1)
label_og.grid(row=6,column=1)
frm_tg.grid(row=7,column=1)
label_tg.grid(row=7,column=1)
frm_net.grid(row=8,column=1)
label_total_net.grid(row=8,column=1)

window.mainloop()


#sh = input("Enter Hours: ")
#sr = input("Enter Rate: ")
