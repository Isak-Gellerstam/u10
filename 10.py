# Python har inbyggda funktioner för att hantera datum och tid. Modulen time innehåller funktioner för att hämta nuvarande tid och konvertera till olika format. Modulen datetime ger tillgång till objekt för datum och tid, samt metoder för att manipulera och formatera dem. Använd dessa moduler för att skapa program som kan hantera datum och tid.

# https://www.w3schools.com/python/gloss_python_date.asp
# https://www.w3schools.com/python/python_datetime.asp
# https://www.w3schools.com/python/gloss_python_date_strftime.asp

# Om du tycker det är svårt - kolla min exempelkod nedan.

# UPPGIFTER
# 1. Gör ett program som skriver ut dagens datum och tid
# 2. Prova olika sätt att skriva ut tid/datum
# 3. Gör så klockan uppdateras automatiskt
# 4. Gör ett tidtagarur
# 5. Lägg till klockan i ett annat program/spel du har skapat
# 6. ÖVERKURS: Skriv ett program som frågar användaren efter ett specifikt datum (månad, dag och år) och sedan beräknar antalet dagar mellan det datumet och dagens datum.
# 7. ÖVERKURS: Gör en larmklocka eller timer där man kan ställa in tid för nedräkning. Något ska hända när tiden är ute


from datetime import datetime
import os
import time

# 1.
# x = datetime.now()
# print(x)

# 2.
# print(x.year)
# print(x.strftime("%A"))
# time.sleep(2)

# 3.
# while True:
    
#     os.system('cls')
#     x = datetime.now()
#     print(x.strftime("%c"))
#     time.sleep(1)
    
# 4.

# start_time = time.time()    

# while True:

#     os.system('cls')

#     current_time = time.time()

#     elapsed_time = current_time - start_time

#     if elapsed_time < 0:
#         elapsed_time = 0

#     elapsed_time_tuple = time.localtime(elapsed_time)

#     elapsed_time_formatted = time.strftime("%M:%S", elapsed_time_tuple)


#     print("Elapsed time:", elapsed_time_formatted)



#     time.sleep(1)


# 5.



# import random

# running = True

# start_time = time.time()   

# while running:          
#     os.system('cls')        
#     number = random.randint(1,100)         
#     tries = 7

#     print(
#         f""
#         "---Gissa ett talet mällan 1 och 100---\n" 
#         " ---Skriv talet 0 för att avsluta---\n" 
#         "     ---Du har sju gissningar---\n"
#     )

#     print(number)

#     while tries > 0:
#         try:    
#             guess = int(input(f"Skriv din gisning :"))
#         except:        
#             print(f"\nSkriv en sifra IDIOT\n")
#             continue          

#         if guess == 0:      
#             print(f"\nSpelet avslutat\n")
#             running = False
#             break

#         tries -= 1  

#         if guess == number:
#             print(f"\n--- Du gissade rätt! ---")
#             print(f"\nMed {tries} gissningar kvar")

#             current_time = time.time()

#             elapsed_time = current_time - start_time

#             if elapsed_time < 0:
#                 elapsed_time = 0

#             elapsed_time_tuple = time.localtime(elapsed_time)

#             elapsed_time_formatted = time.strftime("%M:%S", elapsed_time_tuple)


#             print("Elapsed time:", elapsed_time_formatted)
#             break

#         if tries == 0:
#             print(f"\n--- Du förlorade! --- ")
#             print(f"\nTalet var: {number}")
#             break

#         elif guess < number:
#             print(f"\nTalet är högre")
#         else:
#             print(f"\nTalet är lägre") 

#         print(f"{tries} Gånger kvar\n")


#     if not running:
#         break

#     again = input(f"\nVill du spela i gen | JA = Enter | / | NEJ = N | :")
#     if again.upper() == "N":         #Slutar spel lopen om man vill det 
#         running = False

