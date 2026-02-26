priser = {
    "hamburgare" : 50,
    "pommes frites" : 25,
    "läsk" : 20,
    "milkshake" : 30,
    "sallad" : 45,
    "mcnuggets" : 35
}

Försäljning_per_dag = [
    {"hamburgare" : 180, "pommes frites" : 210, "läsk" : 270, "milkshake" : 120, "sallad" : 2, "mcnuggets" : 120},
    {"hamburgare" : 210, "pommes frites" : 220, "läsk" : 280, "milkshake" : 120, "sallad" : 1, "mcnuggets" : 130},
    {"hamburgare" : 200, "pommes frites" : 230, "läsk" : 250, "milkshake" : 120, "sallad" : 2, "mcnuggets" : 110},
    {"hamburgare" : 190, "pommes frites" : 240, "läsk" : 310, "milkshake" : 120, "sallad" : 3, "mcnuggets" : 140},
    {"hamburgare" : 220, "pommes frites" : 200, "läsk" : 320, "milkshake" : 120, "sallad" : 2, "mcnuggets" : 120},
    {"hamburgare" : 210, "pommes frites" : 230, "läsk" : 290, "milkshake" : 120, "sallad" : 4, "mcnuggets" : 110},
    {"hamburgare" : 180, "pommes frites" : 180, "läsk" : 300, "milkshake" : 120, "sallad" : 2, "mcnuggets" : 130},
    {"hamburgare" : 170, "pommes frites" : 210, "läsk" : 320, "milkshake" : 120, "sallad" : 5, "mcnuggets" : 100},
    {"hamburgare" : 180, "pommes frites" : 220, "läsk" : 260, "milkshake" : 120, "sallad" : 2, "mcnuggets" : 110},
    {"hamburgare" : 200, "pommes frites" : 240, "läsk" : 290, "milkshake" : 120, "sallad" : 4, "mcnuggets" : 120}
]

inkomster_per_dag = []

#kolla när jag magiskt gör 2 raders värt av kod till 37 :cold:
total_hamburgare = 0
for hamburgare in Försäljning_per_dag:
    total_hamburgare += hamburgare["hamburgare"]
total_hamburgare_money = total_hamburgare * priser["hamburgare"]
inkomster_per_dag.append(total_hamburgare_money)

total_pommes_frites = 0
for pommes_frites in Försäljning_per_dag:
    total_pommes_frites += pommes_frites["pommes frites"]
total_pommes_frites_money = total_pommes_frites * priser["pommes frites"]
inkomster_per_dag.append(total_pommes_frites_money)

total_läsk = 0
for läsk in Försäljning_per_dag:
    total_läsk += läsk["läsk"]
total_läsk_money = total_läsk * priser["läsk"]
inkomster_per_dag.append(total_läsk_money)

total_milkshake = 0
for milkshake in Försäljning_per_dag:
    total_milkshake += milkshake["milkshake"]
total_milkshake_money = total_milkshake * priser["milkshake"]
inkomster_per_dag.append(total_milkshake_money)

total_sallad = 0
for sallad in Försäljning_per_dag:
    total_sallad += sallad["sallad"]
total_sallad_money = total_sallad * priser["sallad"]
inkomster_per_dag.append(total_sallad_money)

total_mcnuggets = 0
for mcnuggets in Försäljning_per_dag:
    total_mcnuggets += mcnuggets["mcnuggets"]
total_mcnuggets_money = total_mcnuggets * priser["mcnuggets"]
inkomster_per_dag.append(total_mcnuggets_money)

sum_inkomster_per_dag = sum(inkomster_per_dag)
#koden är ful som fan, men den funkar :shrug:
print("McDonalds inkomster över 10 dagar:", sum_inkomster_per_dag, "kr.")