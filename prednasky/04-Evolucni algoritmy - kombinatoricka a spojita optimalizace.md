Minule jsme si povídali o jednoduchém genetickém algoritmu a jeho variantách  vzhledem k různým genetickým operátorům a selekcím. Dneska se podíváme především na jiné způsoby, jak kódovat jedince. Ukážeme si i nějaké další aplikace evolučních algoritmů.

## Celočíselné kódování

Nejjednodušším rozšířením binárního kódování je celočíselné kódování, tedy zakódování jedince pomocí celých čísel. Takové kódování se hodí např. pokud cílem je řešit problém rozdělení množiny $N$ čísel na $k$ podmnožin se stejným součtem. Jedince potom reprezentujeme jako vektor $N$ čísel mezi 0 a $k-1$. Číslo na pozici $i$ potom říká, do které podmnožiny patří $i$-té číslo ze vstupní množiny. Využití ale je i více, podobně se dá kódovat i obarvení grafu a jiné problémy.

Pro celočíselné kódování můžeme používat jednoduchá zobecnění operátorů pro binární kódování. Implementace křížení dokonce ani nemusíme měnit - fungují pořád stejně, protože jedinec je stále vektor. Pro mutaci je možné vybrat několik variant. Například můžeme na dané pozici změnit číslo na libovolné jiné, nebo, pokud to pro daný problém dává smysl, číslo zvětšit (případně zmenšit) o 1, nebo jinou konstantu.

## Permutační kódování

Speciálním případem celočíselného kódování je permutační kódování. V tom je jedinec také kódován jako seznam čísel od 0 do $k$, zároveň ale chceme, aby se každé číslo v jedinci objevilo právě jednou. Takové kódování se hodí při řešení mnoha kombinatorických problémů. Typickým příkladem je známý problém obchodního cestujícího, tedy hledání nejkratší kružnice v úplném grafu, která prochází přes všechny vrcholy. Permutace potom udává pořadí, v jakém máme navštívit vrcholy. 

Permutační kódování se ale používá i v jiných problémech, často jako vstup pro heuristiku, která problém dále řeší. Například při řešení tzv. bin packing problému (naskládání objektů daných velikostí mezi 0 a 1 do přihrádek s jednotkovou velikostí tak, aby bylo přihrádek použito co nejméně), se dá použít tzv. first fit heuristika, kdy se objekt dá do první přihrádky, kam se vejde, a pokud taková není, tak se vytvoří nová. Tato heuristika na vstupu potřebuje pořadí, ve kterém má objekty zkoušet přidávat - to je dané právě jako permutace.

Největší komplikací pro permutační kódování je, jak vytvořit operátory. Jednoduché operátory pro celočíselné kódování velmi často vytvoří potomky, kteří nebudou permutace. Vymyslet mutaci, která vždy vrátí validní jedince je snadné a máme několik variant. Jedním příkladem může být mutace, která v jedinci prohodí hodnoty na dvou různých pozicích. Můžeme ale mít i mutaci, která podobným způsobem přesune nějakou část jedince na jiné místo, nebo nějakou část otočí pozpátku. To jaká mutace se hodí pro jaký problém závisí na tom, co kódování přesně vyjadřuje.

Větším problémem je, jak vytvořit křížení. Typickým přístupem zde je udělat něco jako 2-bodové křížení a potom opravit vzniklé řešení. Například _Order Crossover (OX)_ funguje tak, že prohodí prostřední část obou rodičů a zbylé pozice v potomcích doplní podle jejich pořadí ve druhém rodiči (začíná se vpravo od druhého křížícího bodu). 

    12|345|678      ..|186|...      45|186|723 (přeskakujeme čísla 186)
                ->              ->  
    34|186|527      ..|345|...      86|345|271 (přeskakujeme čísla 345)

Dalším populárním příkladem křížení je _Partially Mapped Crossover (PMX)_. V tom se opět napřed prohodí "prostřední" části jedince. Následně se ještě doplní hodnoty, které zatím v jedinci nejsou na jejich pozice z druhého rodiče. Zbytek se potom doplní tak, že prohozené dvojice v prostřední části udávají mapování, jakou hodnotou se má co nahradit. Například níže, chceme najít hodnotu na první místo prvního jedince. Původně tam byla hodnota 1, ale ta už je v prohozené části. Tam se ale nahrazovala za hodnotu 3, která ještě v jedinci není - místo 1 tedy dáme na tuto pozici hodnotu 3. Pro ostatní pozice podobně. Občas se může stát, že řetězen nahrazení je delší, protože i prohozená hodnota v daném jedinci je. V takovém případě postupujeme úplně stejně s novou hodnotou.

    12|345|678      .2|186|.7.      32|186|574 (1->3, 6->5, 8->4)
                ->              ->  
    34|186|527      ..|345|.27      18|345|627 (3->1, 4->8, 5->6) 

Speciálně pro problém obchodního cestujícího se potom ještě často používá tzv. _Edge Recombination (ER)_. V tomto křížení je cílem kombinovat hrany z obou řešení do jednoho. Ke každému vrcholu (hodnotě v jedinci) se teda vyhledají všechny vrcholy, které s ním v jednom nebo ve druhém jedinci sousedí (nezapomeňte, že první sousedí s posledním - hledáme kružnice). Potom se začne vrcholem, který má nejkratší seznam sousedů. Z těch se zase vybere ten, který má nejkratší seznam sousedů a ten se dá na druhé místo. Oba vrcholy se vyškrtnou ze seznamů sousedů všech ostatních vrcholů. Stejně se potom postupuje s dalšími sousedy, přičemž pokud má více vrcholů stejný (nejmenší) počet sousedů, vybere se jeden z nich náhodně.

## Spojitá optimalizace - kódování pomocí reálných čísel

Velmi častou oblastí, kde se používají evoluční algoritmy je optimalizace funkcí $\mathbb{R^n} \to \mathbb{R}$. Pomocí takových funkcí je možné zakódovat mnoho praktických problémů od ladění parametrů různých procesů, přes problémy strojového učení, až po hledání vah neuronových sítí - například ve zpětnovazebním učení.

Pro spojitou optimalizaci jsou jedinci kódovaní jako vektory čísel (typicky typu float, nebo double). V takovém případě je relativně snadné vymyslet nějaké genetické operátory. Mutace pro spojité kódování se dělí na dva typy - zatížené (biased) a nezatížené (unbiased). Nezatížené mutace prostě vygenerují nové číslo z rozsahu pro danou proměnnou, naopak zatížené mutace vychází z hodnoty, která se na dané pozici už vyskytuje a pouze ji upraví. Typickým příkladem je Gaussovská mutace, která k danému číslu přičte hodnotu z normálního rozdělení se střední hodnotou 0 a nějakým vhodným rozptylem. 

Pro křížení existuje také několik variant - můžeme opět používat $n$-bodové křížení, která už známe, nebo můžeme používat tzv. aritmetická křížení, kde se potomek získá jako vážený průměr rodičů. 

Problém výše zmíněných operátorů je, že mutují/kříží každou souřadnici vektoru nezávisle. Tohle dobře funguje pro separabilní funkce, tj. takové, které lze optimalizovat po složkách (zafixujeme všechny proměnné kromě jedné, přes tu najdeme optimum a máme jednu souřadnici optima). Navíc tyto operátory dělají ve všech směrech stejně velké změny a tedy nefungují dobře pro funkce, které mají vysokou podmíněnost. Představte si například funkci, jejíž vrstevnice jsou elipsy - funkce s malou podmíněností má obě osy elipsy skoro stejně dlouhé, vysoce podmíněné funkce mají naopak velký poměr délek os. Pokud jsou osy rovnoběžné s osami soustavy souřadnic, máme separabilní funkci. Pokud nejsou, je funkce neseparabilní.

Existuje relativně velké množství evolučních algoritmů, které řeší problémy s neseparabilitou a podmíněností funkcí. My si ukážeme jen tzv. _diferenciální evoluci (DE}_. V diferenciální evoluci se provádí mutace, která k danému jedinci přičte rozdíl dvou náhodně zvolených jedinců z populace. Díky tomu je tato mutace invariantní vůči libovolným rotacím a škálováním prohledávaného prostoru. Nevadí jí tedy ani neseparabilní nebo vysoce podmíněné funkce. Kromě této mutace se ještě provádí v zásadě uniformní křížení s dalším náhodným jedincem. V rámci selekce se potom potomek porovná s rodičem a v populaci se nechá jen lepší z nich.