Velmi častým typem vstupů, kterým se musí neuronové sítě zabývat jsou obrázky. V této oblasti dosáhly v poslední době neuronové sítě velkých pokroků. Dnes se podíváme, jakým způsobem s neuronovými sítěmi pro zpracování obrazu pracovat, jaké jsou dostupné architektury a podíváme se i na některé zajímavé výsledky a postupy, jakými jich bylo dosaženo.

## Konvoluční sítě

Hlavní problém se zpracováním obrázků pomocí neuronových sítí je jejich velikost -- typický obrázek má více než $100 \times 100$ pixelů, každý pixel má u barevných obrázků 3 barevné kanály. I takto malé obrázky tedy znamenají, že máme na vstupu 30 000 hodnot. To je pro plně propojené sítě hodně, a měly by velmi velké množství parametrů. 

Z tohoto důvodu se ve zpracování obrazu často používají tzv. konvoluční sítě. Ty jsou navržené tak, že čtou malé (např. $3 \times 3$) části obrázku a aplikují na ně pořád stejnou operaci (ta je stejně jako u perceptronových sítí jen skalární součin s vahami sítě). Důležité je, že tuto operaci aplikují na všechny možné pozice v obrázku (délka kroku při posunu "okénka" se označuje jako stride, typicky se okénka překrývají) a váhy jsou na všech pozicích sdílené. Pokud tedy máme jednu takovou konvoluční operaci popsanou výše, má neuronová síť jen 9 parametrů (27 pro barevné obrázky). Výstupem takové konvoluční vrstvy je potom "obrázek", který je stejně velký, jako vstupní obrázek (tady trochu záleží na tom, jak ošetříme okraje obrázku). Takovou konvoluční vrstvu typicky nemáme jen jednu, ale hned několik, které se aplikují na stejný obrázek - to nám umožňuje zpracovat obrázek pomocí mnoha konvolucí najednou. Dostáváme vlastně potom obrázek s podobnými rozměry jako měl vstupní obrázek, ale s větším počtem kanálů. Na ten se potom zase dají aplikovat konvoluční vrstvy stejným způsobem.

Pokud bych používali jen konvoluční vrstvy, měli bychom pořád stejně velké obrázky a nemohli bychom s nimi pořád nic moc dělat. Proto se v konvolučních sítích střídají konvoluční vrstvy a sub-sampling (pooling) vrstvy. Nejčastější takovou vrstvou je max-pooling, ta se aplikuje podobně jako konvoluční vrstva na všechny části obrázku (např. s rozměry $2 \times 2$) a vrací z nich maximum. U sub-sampling vrstev se naopak překrývání typicky nepoužívá. Tím sníží rozlišení na polovinu. Při takovém střídání konvolučních a sub-sampling vrstev nakonec dostaneme relativně malou reprezentaci vstupního obrázku, na kterou už můžeme aplikovat plně propojené vrstvy.

Co vlastně konvoluce dělají? Pokud si zobrazíme aktivace neuronů v jednotlivých vrstvách konvoluční sítě jako obrázky, uvidíme, že na prvních vrstvách po vstupu se chovají jako detektory hran, v hlubších vrstvách potom jednotlivé neurony mohou detekovat přítomnost složitějších objektů.

## Matoucí vzory

Ačkoliv konvoluční neuronové sítě dosahují velmi dobrých výsledků ve zpracování obrazu, objevuje se u nich jedna zajímavá vlastnost (zranitelnost) -- jsou náchylné na tzv. matoucí vzory, tj. obrázky, které jsou drobně upravené tak, že člověk typicky není schopný rozpoznat rozdíl, ale neuronová síť na ně vrací jiné odpovědi než na původní obrázky.

Původní zdůvodnění pro existenci takových vzorů bylo, že neuronové sítě jsou velmi nelineární a tedy drobné změny mohou vést k tomu, že se jejich výstupy výrazně změní. Ukazuje se ale, že na matoucí vzory jsou náchylné i jiné modely strojového učení, včetně lineárních modelů. Důvod pro matoucí vzory tedy může být přesně opačný, tj. že neuronové sítě jsou hodně lineární a malé změny, které se dostatečně nasčítají potom vedou ke špatné klasifikaci. 

Na aproximaci neuronových sítí pomocí lineárních modelů je založena velmi populární technika pro generování matoucích vzorů - FGSM (Fast Gradient Sign Method). Ta spočítá derivaci chybové funkce podle vstupu do neuronové sítě a přičte k tomuto vstupu $\varepsilon \cdot \mathrm{sign}(\nabla J)$, kde $\nabla J$ je právě tento gradient. Ukazuje se, že i malé změny pro $\varepsilon < 0.1$ mohou snadno zmást mnoho modelů neuronových sítí, které jinak dávají velmi dobré výsledky. 

Existence matoucích vzorů může být problém pro aplikaci neurnových sítí v oblastech, kde chyby mohou mít závažné důsledky, jako např. pro řízení autonomních vozidel. Ukazuje se dokonce, že matoucí vzory lze vytvořit i v reálném světě, kde např. speciální brýle jsou schopné zmást modely pro rozpoznávání obličejů, nebo speciální nálepky mohou způsobit, že vozidlo není schopné detekovat čáru oddělující jízdní pruhy, nebo naopak detekuje čáru tam, kde není.

## Přenos uměleckého stylu

Jednou z pěkných aplikací neuronových sítí je přenos uměleckého stylu mezi obrázky. Představte si např. že máte fotografii a chtěli byste z ní udělat obraz ve stylu Picassa. Pro přenos stylu se dají použít aktivace ve vnitřních vrstvách neuronové sítě. Ukazuje se potom, že samotné aktivace odpovídají obsahu obrázku a korelace mezi těmito aktivace odpovídají stylu. Přenos stylu se pak definuje jako optimalizační problém, kde cílem je dosáhnou (změnou vstupního obrázku) aktivací, které jsou podobné původní fotografii a zároveň mají korelace podobné obrázku v požadovaném stylu. Podle toho, jak hluboké vrstvy se zvolí dostáváme jiné části stylu - od tahů štětcem až po barvy a deformace obrazu.

## Generative Adversarial Networks

Dnes se pro přenos stylu mezi obrázky a pro generování obrázků často používají tzv. Generative Adversarial Networks. Ty se vlastně skládají ze dvou částí - generátoru a diskriminátoru. Generátor ma za úkol generovat obrázky, které jsou podobné obrázkům v nějaké trénovací množině a diskriminátor ma za úkol poznat, jestli předložené obrázky jsou generované generátorem, nebo jestli pochází z trénovací množiny. Generátor se potom snaží maximalizovat chybu diskriminátoru a diskriminátor se snaží svoji chybu minimalizovat. Tímto způsobem se obě sítě navzájem trénují. Po skončení trénování typicky diskriminátor nepoužíváme.

