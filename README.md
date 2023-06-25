# canbus_sniffer

Vítejte v README k projektu vlastního autorádia s podporou multifunkčního volantu!

Tento projekt slouží jako součást mé závěrečné zkoušky u ITnetwork (programátor www aplikací v jazyce Python)

## Popis projektu
Cílem tohoto projektu je vytvořit software, který slouží k odposlechu a analýze komunikace na sběrnici CANBUS v automobilech. Specificky se zaměřuji na "sniffer" sběrnice CANBUS připojený k autorádiu. Software je napsán v jazyce Python.

## Co je sběrnice CAN?
Sběrnice CAN je standardní komunikační protokol používaný v automobilech pro přenos dat mezi různými komponenty. CAN umožňuje spolehlivou a robustní sériovou komunikaci mezi různými zařízeními v automobilu, jako jsou řídící jednotky, senzory, aktuátory a další periferie. Používá se k přenosu informací o stavu motoru, brzdového systému, klimatizace, rádia a dalších systémů.

## Implementace sběrnice CAN v projektu
V mém projektu využívám Arduino a jiný projekt jako rozhraní mezi sběrnicí CAN a mým programem. Arduino je programovatelný mikrokontrolér, který mi umožňuje snadno číst a zapisovat data na sběrnici CAN.

Pomocí projektu se připojím arduinem k sběrnici CAN a zachytávám komunikační zprávy, které jsou odesílány mezi různými komponentami automobilu. Tyto zprávy jsou pak ukládány do textového souboru pro další zpracování.

## Python program pro zpracování zpráv
Napsal jsem program v jazyce Python, který otevírá tento textový soubor a analyzuje zachycené zprávy. Program spočítá výskyt každé zprávy a vytvoří slovník, který slouží jako počítadlo (counter). Tento slovník mi poskytuje informace o tom, jak často se jednotlivé zprávy vyskytují.

Program také nabízí několik funkcí pro zobrazení zpráv na základě výběru ID nebo počtu výskytů. To mi umožní rychle najít zprávu, která odpovídá tlačítku na volantu, které jsem zmáčkl nejčastěji.

## Využití zpráv pro ovládání autorádia
Po nalezení odpovídající zprávy pro dané tlačítko na volantu ji mohu aplikovat dál na autorádio. Zpráva obsahuje informace o požadované akci, například změně rádiové stanice, zvýšení/znížení hlasitosti nebo přepnutí na předchozí/ další skladbu.

## Rozšíření projektu
Plánuji dál rozšiřovat tento projekt. Některé z navrhovaných rozšíření jsou:
* Vylepšená vizualizace: Přidám grafické rozhraní (GUI), které umožní uživatelům jednodušší sledování a analýzu zachycených zpráv.
* Live monitorování: Software bude běžet v reálném čase přímo na sériové lince připojené k autu přes USB. To umožní okamžitý přístup k novým zprávám a jejich analýzu v reálném čase.
* Dekódování zpráv: Zprávy, které jsou zachyceny ve formátu HEX (šestnáctková soustava), budou v softwaru dekódovány a převedeny na formát BIN (dvojková soustava). Tím získám srozumitelná data pro další analýzu a zpracování.

## Spuštění aplikace
* Všechny soubory nahrajte do jedné složky, jako projekt.
* Pomocí terminálu najděte cestu složky projektu
* zadejte příkaz do terminálu bez uvozovek pro spuštění aplikace " python.exe .\main.py -f CAN.txt "
