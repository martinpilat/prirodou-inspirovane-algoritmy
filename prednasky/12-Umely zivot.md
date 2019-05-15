Poslední téma, o kterém se budeme bavit je umělý život. Ten se zabývá systémy připomínajícími skutečný život. Cílem je pochopit, jak život (organismy) fungují a komunikují, případně život vytvořit. V umělém životě se studuje i chování skupin různých organismů.

Oblast umělého života se dá rozdělit do třech částí, podle nástrojů, které používá. V softwarovém (soft) umělém životě se používají počítačové simulace k popisu a modelování života, interakcí mezi jedinci a druhy apod. V hardwarovém umělém životě je cílem vytvořit umělé organismy, typicky jako roboty. Mokrý (anglicky wet) umělý život zase studuje biochemické procesy s cílem vytvořit např. umělou DNA. 

Oblast umělého života naráží i na filosofické otázky, jako co vůbec je život, a jestli ho lze vytvořit mimo oblast chemie a biologie. Zastánci tzv. silného umělého života (strong ALife) tvrdí, že to možné je, a že život je obecný proces, který nezávisí na konkrétním médiu. Naopak pozice slabého umělého života je, že to nejde a cílem slabého umělého života je život studovat pomocí simulací.

## Celulární automaty

Jednou z prvních technik, které byly v umělém životě studovány jsou celulární automaty. To jsou (typicky) 1D nebo 2D mřížky, kde každé políčko může mít jednu z $k$ barev. V nejjednodušším případě jsou barvy jen dvě. Potom se často říká, že na některých políčkách je organismus a na jiných není. Na základě barvy políčka a jeho sousedů do dané vzdálenosti se potom definují pravidla pro změny barev políček.

Cíle výzkumu celulárních automatů mohou být různé - od studia celulárních automatů jako takových, až po hledání pravidel, která umožňují modelování reálných systémů (např. šíření požáru, nebo pohyb aut na silnici).

### Game of Life

Jedním z nejznámějších 2D celulárních automatů je Conwayova Game of Life. Ve 2D automatech závisí nová hodnota každého políčka na všech okolních políčkách. V případě Game of Life jsou pravidla jednoduchá:

1. živá buňka s méně než dvěma nebo více než třemi živými sousedy umírá
2. živá buňka s dvěma nebo třemi živými sousedy přežívá
3. mrtvá buňka s právě třemi živými sousedy ožívá

Na základě těchto velmi jednoduchých pravidel se dají implementovat docela zajímavé organismy, které se množí, pohybují apod. Doporučuji si najít nějaký online simulátor a pohrát si s ním (případně se podívat na materiály ze cvičení). 

Z hlediska teoretické informatiky je zajímavé, že takto definovaný celulární automat je ve skutečnosti Turingovsky úplný. Na game of life implementující univerzální Turingův stroj se můžete podívat na [web Paula Rendella](http://rendell-attic.org/gol/utm/index.htm).

## Langtonův mravenec

Dalším příkladem jednoduchého chování, které může mít relativně komplikované projevy je tzv. Langtonův mravenec. Jde o mravence, který se pohybuje na mřížce se dvěma barvami. Při každém pohybu přebarví svoje políčko na opačnou barvu. V závislosti na počáteční barvě políčka se potom rozhoduje, jestli má jít doleva, nebo doprava.

Tato jednoduchá pravidla vedou k velmi složitému emergentnímu chování. Na počátku je chování mravence celkem jednoduché s vytvářením jednoduchých tvarů, potom se mravenec začne chovat chaoticky a pseudonáhodně. Nakonec ale začne opakovat posloupnost 104 kroků, které tvoří tzv. dálnici - mravenec tím utíká stále jedním směrem. 

Zdá se (ale zatím to není dokázáno), že nezávisle na počáteční konfiguraci (pokud je tato konečná) mravenec vždy nakonec začne generovat tuto dálnici. 

Naopak se podařilo dokázat, že i mravence lze považovat za úplný výpočetní model.

## Simulace života (Tierra)

Zajímavou oblastí umělého života jsou simulace a prostředí, kde se simuluje život počítačových programů. Typickým příkladem takového systému je Tierra. Ta je implementována jako emulátor jednoduchého počítačového kódu s 32 různými instrukcemi (32 je možných kombinací instrukcí a parametrů). Tyto instrukce obsahují jednoduché aritmetické instrukce, podmínky, skoky a dva typy no-op - NOP0 a NOP1. Tyto dva typy se používají pro definování cílů skoků. Pokud máme někde instrukci pro skok, následuje po ní několik NOPx instrukcí. Při skoku se potom hledá nejbližší místo v paměti, kde je komplementární posloupnost instrukcí (NOP0 je komplementární k NOP1 a naopak). Tímto způsobem Tierra řeší problém s adresováním místo používání absolutních nebo relativních adres. Má to také připomínat komplementární páry bází v DNA. 

Všichni jedinci v systému Tierra běží "paralelně" - každý má přiřazen virtuální procesor, který vždy provede několik instrukcí jedince a následně se provede několik instrukcí dalšího jedince atd. Jedinci nemohou přepisovat instrukce jiného jedince, ale mohou je číst a vykonávat (cíle skoku mohou být i v jiných jedincích).

Na začátku simulace začíná s jedním jedincem, který umí sám sebe zkopírovat. Při kopírování je malá šance, že dojde k mutaci bitu v jedinci. Ukazuje se, že tímto způsobem se po nějaké době vyvinou zajímaví jedinci - někteří se chovají jako paraziti, neobsahují vlastní kopírovací proceduru, ale pokud žijí v populace s jedinci, kteří ji mají, tak ji mohou použít. Díky tomu jsou menší a mohou se rychleji kopírovat. Objevily se ale i další zajímavé typy jedinců. Někteří se umí těmto parazitům bránit. Jiní jsou hyper-paraziti - "přesvědčí" parazita, aby kopíroval je, místo sebe.

Moc pěkné povídání o systému Tierra je přímo v [originálním článku](https://www.cc.gatech.edu/~turk/bio_sim/articles/tierra_thomas_ray.pdf).

Systém Tierra inspiroval další podobné systémy, jako např. Avida.

## Creatures

Počítačová hra Creatures je dalším příkladem umělého života. Hráč v ní ma za úkol starat se o tzv. Norny, což jsou hravé příšerky. Musí je učit (Norni mají neuronovou síť jako mozek), pomáhat jim prozkoumávat prostředí a bránit se před jinými druhy.

## Simulace složitých systémů

Jednou z aplikací umělého života jsou i simulace složitých (nejen) biologických systémů. Takové simulace mohou být dvou základních typů. Black-box simulace se soustředí na imitaci nějakého chování bez ohledu na to, jestli jejich vnitřní struktura nějakým způsobem souvisí s reálnou vnitřní strukturou. Na druhou stranu white-box modely se soustředí na simulaci založenou na principech, které byly pozorovány i v reálném světě. Typicky jsou založené na přesném pochopení studovaného systému.