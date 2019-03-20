Zatím jsme se bavili o použití evolučních algoritmů v případě, kdy se řešení dalo zakódovat do jednoduché struktury -  vektoru nějakých hodnot - a všichni jedinci měli stejnou délku tohoto vektoru. Dnes se podíváme na několik příkladů, kde je struktura řešení složitější. 

## Genetické programování

Genetické programování je technika, která umožňuje pomocí evolučních algoritmů automatiky vytvářet programy. Často jen ve formě výrazů. Lze ji ale použít (jak uvidíme níže) k návrhu elektronických obvodů a podobných komplikovaných struktur. Existuje několik forem genetického programování podle toho, jakým způsobem je zakódovaný jedinec. My se podíváme na několik z nich. Velmi oblíbenou knihou o genetickém programování je [Field Guide to Genetic Programming](http://www.gp-field-guide.org.uk/) (je ke stažení zdarma).

### Lineární genetické programování

V lineárním genetickém programování je jedinec zapsaný jako posloupnost instrukcí, které se potom provádí na nějakém simulovaném počítači. Příkladem lineárního genetického programu může být například (z Wikipedie).

    input/   # gets an input from user and saves it to register F
    0/       # sets register I = 0
    save/    # saves content of F into data vector D[I] (i.e. D[0] := F)
    input/   # gets another input, saves to F
    add/     # adds to F current data pointed to by I (i.e. F := F + D[0])
    output/. # outputs result from F

Program je zapsaný v jazyce [Slash/A](https://github.com/arturadib/slash-a), který používá dva registry $F$ (pro floaty a vstup/výstup) a $I$ (pro indexování do $D$) a pole hodnot $D$. Na stránkách jazyka můžete vidět i složitější programy v něm napsané.

Operace s jedinci v lineárním genetickém programování jsou relativně jednoduché. Sice už nemají všichni jedinci stejnou délku jako dříve, ale pořád je možné dělat například mutace, které změní instrukci za nějakou jinou, nebo můžeme křížit jedince tak, že zkombinujeme části z jednoho programu s částmi z jiného programu.

### Kartézské genetické programování

V kartézském genetickém programování (Cartesian GP), jedinec kóduje program zadaný na mřížce $r \times l$, která má $r$ řádek a $l$ vrstev (sloupců). Jedinec je potom vektor $r \times l$ genů, a každý gen se skládá ze dvou částí - kódu (jména) funkce, kterou počítá, a indexů do předchozích vrstev, ze kterých bere vstupy. V první vrstvě indexy ukazují do pole vstupů. Navíc pro každý požadovaný výstup jedinec obsahuje index, kde se tento výstup v něm počítá. 

V kartézském genetickém programování se typicky používá jen mutace, která změní funkci, její vstupy, nebo výstup programu. Pěkný úvod do kartézského genetického programování (s obrázky) je i na webu [www.cartesiangp.com/](https://www.cartesiangp.com/).

### Gramatická evoluce

V gramatické evoluci se využívá formálního zápisu syntaxe programovacího jazyka pomocí bezkontextové gramatiky. Jedinec je potom kódován jako posloupnost čísel, která určuje, jaké pravidlo z gramatiky se má použít pro přepis aktuálně prvního neterminálu. Protože pravidel pro každý neterminál může být více, nezáleží přímo na konkrétní hodnotě, ale bere se pravidlo, které se spočítá z hodnoty modulo počet možností. 

Problémem v gramatické evoluci je, když je jedinec moc krátký a po jeho zpracování zbydou ve výrazu ještě nějaké neterminály. Takový jedinec potom nemůže být vyhodnocen. Tomu se zabraňuje tím, že se snažíme generovat delší jedince - pokud jedinec nepoužije některé své geny, tak to až tak nevadí.

Jako operátory můžeme zase používat varianty známých $n$-bodových operátorů a mutací, které náhodně mění některé geny v jedinci. Kromě toho ale můžeme použít i křížení, které vybere z každého jedince gen, kde se začíná zpracovávat nějaký neterminál a prohodí ho s pozicí ve druhém jedinci, kde se objeví ten samý neterminál. Kromě této pozice se prohazují i další geny, které se týkají zpracování tohoto neterminálu (tj. dokud se nepřejde na další neterminál v jedinci před zpracováním tohoto). Toto křížení vlastně prohazuje celé podstromy mezi danými jedinci. Velkou výhodou tohoto křížení je, že dává sémanticky smysl a navíc pokud máme dva validní rodiče, tak vždy vytvoří validního potomka.

### Stromové genetické programování

Stromové genetické programování (běžněji označované jen jako genetické programování) reprezentuje jedince pomocí stromu, který v uzlech obsahuje funkce (neterminály) a v listech vstupy nebo konstanty. Strom se potom vyhodnocuje od listů ke kořeni. Hodnota kořene je potom výstup programu.

Taková reprezentace umožňuje implementovat celou škálu různých rozumných genetických operátorů a pro genetické programování je typické, že se operátorů používá zároveň relativně velké množství. Typickými příklady operátorů jsou křížení, která prohazují podstromy, nebo mutace, které změní terminál/neterminál na nějaký jiný. Další mutace potom třeba nahradí podstrom novým, náhodně vygenerovaným, případě rovnou terminálem. 

V genetickém programování je i problém, jak inicializovat počáteční populaci - jednou z možností je generovat náhodné stromy s nějakou pevně danou hloubkou (v této hloubce už se vždy použije terminál), nebo s daným počtem neterminálů (zbytek stromu se opět doplní terminály). Nejčastěji se asi používá varianta těchto dvou přístupů, kdy každý generuje polovinu populace (tomuto přístupu se říká ramped half-and-half). 

Otázkou také je, jak v genetickém programování pracovat s číselnými konstantami. Není úplně možné dát všechna čísla mezi terminály - bylo by jich pak moc. Často se zadávají mezi terminály jen základní konstanty (0, 1, 2, apod.) a předpokládá se, že si program další hodnoty spočítá sám z nich. Další možností je mít speciální operátory, které mění hodnoty konstant podobně jako se to dělá ve spojité optimalizaci.

Základní genetické programování popsané výše má řadu rozšíření. V programech se např. často pracuje s hodnotami různých typů jako jsou čísla nebo boolean. To je možné i v genetickém programování, stačí k jednotlivým neterminálům připsat, jaké mají typy vstupů a výstupů. Operátory s tím potom musí umět pracovat. Přidáním typů dostáváme typované genetické programování.

Dalším rozšířením jsou tzv. automaticky definované funkce, kdy dáme algoritmu možnost vytvořit si vlastní definice některých neterminálů. Ty potom může volat na různých místech programu. Někdy se v automaticky definovaných funkcích omezuje množina vstupů, nebo možných neterminálů tak, aby se programu pomohlo s prohledáváním.

## Evoluce pravidel

Další oblastí, kde se používají jedinci se složitějším kódováním je strojové učení a evoluce klasifikačních pravidel. V té jedinci reprezentují množinu pravidel, která se snaží klasifikovat zadané vstupy. Např. pokud je vstupem vektor $n$ čísel, tak jedinec může být množina pravidel typu $c_1, c_2, c_n -> k$, která znamená, že pokud pro každé $i$ pro $i$-tý vstup platí podmínka $c_i$ potom objekt patří do třídy $k$. Je potřeba nějak vyřešit situaci, kdy daný objekt splňuje všechny podmínky pro více pravidel. Potom můžeme nechat pravidla hlasovat (tj. přiřadíme jako třídu tu nejčastější), nebo se můžeme rozhodnout podle prvního splněného pravidla (potom ale záleží na pořadí v jedinci).

Máme celou řadu genetických operátorů, které můžeme pro zadanou reprezentaci jedince využít - křížení může opět probíhat relativně jednoduše tak, že se zkombinují pravidla z obou rodičů. Pro mutace můžeme například měnit předpovězenou třídu pro dané pravidly, měnit podmínky na levé straně pravidla (buď za jiné podmínky, nebo v nich upravovat třeba konstanty pokud tam nějaké jsou). V případě, že mají pravidla různé váhy, můžeme měnit i ty. 

