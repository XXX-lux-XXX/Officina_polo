"Mediante la verifica precedente sviluppare un software python"

import random
import datetime
azione_utente = input("Benvenuto nella nostra officina\nHai portato la tua vettura incidentata [si \ no]:")

if azione_utente == "si" or azione_utente == "Si":
    print("\n\nUn nostro meccanico sta per eseguire un test alla vettura, ti conttatteremo per il risultato alla fine della diagnostica\n")
    #aggiunta timer
    risultato_test = random.randint(1,2)
    
    if risultato_test == 1:
        importo_prezzo = random.randint(50,1000)
        print("-------------------------------------------------------------------------------------------------------------------------------\n")
        print("Purtroppo un nostro tecnico ha riscontrato un danno alla tua vettura\nLa riparazione di quest'ultimo comporterebbe un ammontare di", importo_prezzo, "$\n")
        azione_utente = input("Desideri affrontare la riparazione e il costo della manodopera più il pezzo [si \ no]:")
        
        if azione_utente == "si" or azione_utente == "Si":
            print("\nPerfetto i nostri tecnici procederanno all'acquisto del pezzo e alla riparazione, nel frattempo eseguiremmo altri controlli\n\n")
            risultato_test = random.randint(1,2)
            
            if risultato_test == 1:
                importo_prezzo1 = random.randint(100,2000)
                print("Abbiamo riscontrato dei problemi anche nell'impianto elettrico e danni alla carrozzeria ad un ammontare di", importo_prezzo, "$")
                azione_utente = input("\nDesideri affrontare la riparazione e il costo della manodopera più il pezzo [si\no]: ")
                
                if azione_utente == "si" or azione_utente == "Si":
                    print("La ringraziamo molto\nI nostri tecnici hanno ordinato tutti i pezzi necessari\nnon appena arriveranno, precederemo con la riparazione\nVerrà avvertito quando la vettura sarà pronta e potrà venire a prenderla")
                    
                else:
                    print("Ci dispiace molto!\n Potrà venire a saldare la manodopera e ritirare la sua vettura quando vuole\nPoloOfficina Officina")
                
            else:
                print("Fortunatamente non abbimao riscontrato danno\nPotrà venire a ripredere la vettura quando vuole")

        else:
            print("Ci dispiace molto!\n Potrà venire a saldare la manodopera e ritirare la sua vettura quando vuole\nPoloOfficina Officina")
    else:
     print("Fortunatamente non abbimao riscontrato danno\nPotrà venire a ripredere la vettura quando vuole")
else:
    print("Fortunato!\nArrivederci\nPoloOfficina")
    
    
