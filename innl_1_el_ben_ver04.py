"""

Av Kjetil Lindmark (kjetil.lindmark@outlook.com)

Oppdatert 2024 10 30

Programmet beregner kostnaden for en el-bil og en bensinbil 
ved en kjørelengde på 10 000 kilometer pr. år

"""

#%% Data for begge biltyper

K = 10000  # Kjørte kilometer (km)
T = 8.38  # Trafikkforsikringsavgift (trf kr per dag)
D = 365  # Dager i et år (dager aar)

#%% Data for en el-bil

F = 5000  # Forsikring (fors kr per år el)
DR = 0.2*2  # Drivstoff kostnad pr kilometer (dr kr per km el)
B = 0.1  # Bompenger pr. kilometer (b pr km el)

#%% Data for en bensinbil

F1 = 7500  # Forsikring (fors kr per km ben)
DR1 = 1  # Drivstoff kostnad pr. kilometer (dr kr per km ben)
B1 = 0.3  # Bompenger pr. kilometer (b per km ben)

#%% Beregninger

EB = (T*D) + F + (DR*K) + (K*B)  # Kostnad for en el-bil ved 10 000 km kjøring pr. år

BB = (T*D) + F1 + (DR1*K) + (K*B1)  # Kostnad for en bensinbil ved 10 000 kjøring pr. år

#%% Print resultatet

print(f"Kostnaden for en el-bil som kjører {K} kilometer i året er kr. {EB:.2f}")
print(f"Kostnaden for en bensinbil som kjører {K} kilometer i året er kr. {BB:.2f}")
