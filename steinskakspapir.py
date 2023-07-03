import random
spiller_valg = input("hva velger du (stein,skaks papir): \n")
mulige_valg = ["stein,saks,papir"] 
pc_valg=random.choice(mulige_valg)

print(f"\n du valgte {spiller_valg},CUP valgte {pc_valg}\n")

if spiller_valg == pc_valg:
 print(f"begge valgte{spiller_valg}.ingen vinner")
elif spiller_valg == "stein":
    if pc_valg == "saks":
       print("stein knuser saks! du vinner!")
    else: 
        print("papir dekker stein! du taper!")

elif spiller_valg == "papir":
    if pc_valg == "stein":
       print("papir knuser stein ! du vinner!")
    else: 
        print("saks knuser papir! du vinner!")
elif spiller_valg == "saks":
    if pc_valg == "papir":
       print("saks knuser papir ! du vinner!")
    else: 
        print("stein knuser saks ! du taper!")


