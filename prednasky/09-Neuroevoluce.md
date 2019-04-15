Bavili jsme se už evolučních algoritmech i neuronových sítích. Dnešní téma je neuroevoluce, tj. evoluce neuronových sítí. Toto téma se aktuálně opět stává velmi aktuálním kvůli rozvoji metod založených na hlubokém učení. Algoritmy pro neuroevoluci se v poslední době rozšiřují do algoritmů pro hledání architektur neuronových sítí.

Oblast neuroevoluce můžeme rozdělit do třech podoblastí podle toho, co algoritmy přesně hledají - na evoluci vah sítí, evoluci topologie a na evoluci obojího najednou.

## Evoluce vah sítě

Evoluce vah neuronové sítě je z hlediska kódování jedince nejjednodušší. Předpokládáme zde, že architektura neuronové sítě je fixní, tj. je fixní i počet jejích vah, celá evoluce se redukuje na problém spojité optimalizace. Nejčastěji se v této oblasti používají jednoduché evoluční strategie - ke každému genu jedince se přičte náhodné číslo z normálního rozdělení s nulovou střední hodnotou a malých rozptylem (který je stejný pro všechny váhy). Složitější evoluční strategie se typicky moc nepoužívají, protože jejich režie na adaptaci vah může být dost velká.

Proč používat evoluci místo gradientních metod? Gradientní metody jsou často rychlejší v případě učení s učitelem, např. pro trénování sítí pro klasifikaci. Pro zpětnovazební učení ale má evoluce několik podstatných výhod. Jednou z nich jsou výrazně lepší možnosti paralelizace a více CPU jader - ve zpětnovazebním učení je totiž hlavní problém vyhodnocení prostředí, které může trvat relativně dlouho ve srovnání s dobou potřebnou na vypočítání gradientu a propagaci vah. Navíc toto vyhodnocení často nelze dělat na GPU. Evoluční strategie lze velmi dobře paralelizovat a nejsou výjimkou ani algoritmy, kde evoluční strategie běží na stovkách CPU.

Druhou oblastí, kde evoluční strategie mají navrch jsou prostředí s řídkými odměnami - představte si hru, kde dostanete skóre až na konci a ne v každém kroku v průběhu. V takové hře běžné algoritmy pro hluboké zpětnovazební učení naráží na to, že se jejich odhady odměn propagují velmi pomalu (pro všechny stavy kromě toho posledního je po prvním dohrání hry odhad 0). Evolučním strategiím tohle nevadí - tak jako tak používají fitness až na konci. Občas se dokonce evoluční strategie kombinují s algoritmy pro hluboké zpětnovazební učení tak, že hry odehrané v evoluci se používají pro trénování sítí právě v algoritmech hlubokého zpětnovazebního učení.

## Evoluce vah i topologie

Typickým algoritmem, který vyvíjí váhy sítě i její topologii zároveň je NEAT (Neuro-evolution of Augmenting Topologies). Algoritmus NEAT je trochu podobný algoritmům kartézského genetického programování. Jeho jedinci jsou tvořeni seznamem, který obsahuje v každá položce informaci o jedné váze v neuronové síti - odkud vede, kam, a jaká je její hodnota. Kromě toho každá váha ještě má příznak, jestli je tento spoj v síti aktivní a také své "inovační číslo" - identifikátor, který má za cíl poznat, jaké váhy ve dvou různých jedincích mají stejnou historii a tedy by měly mít i podobnou funkci. To se používá v rámci genetických operátorů.

NEAT používá dva typy mutací - přidání neuronu a přidání hrany. V obou případech se při přidání hrany generuje pro každou novou hranu nové inovační číslo. Při přidání hrany se přidá nová hrana na konec jedince, při přidání neuronu se vybere hrana v jedinci, ta se rozdělí na dvě přidáním neuronu, nové hrany se přidají na konec jedince a původní hrana se nastaví jako neaktivní.

Křížení se v NEAT dělá pomocí inovačních čísel. Dva jedinci, kteří se mají křížit se "zarovnají" podle inovačních čísel. Hrany se stejným inovačním číslem, které jsou v obou jedincích se dědí náhodně z jednoho nebo z druhého. Hrany, které jsou jen v jednom jedinci se dědí z toho lepšího z těchto dvou. Pokud je nějaká hrana v jednom jedinci neaktivní a v druhém aktivní, ve výsledku je aktivní/neaktivní s danou pravděpodobností.

Kromě těchto operátorů NEAT používá ještě zajímavou techniku rozdělení populace na více druhů. Jedinci každého druhu potom explicitně sdílí fitness, tj. fitness každého jedince je vydělena počtem jedinců stejného druhu, a tím se dává nově objeveným myšlenkám (strukturám) čas pro to, aby se vylepšily pomocí genetických operátorů. Druhy jsou definovány pomocí vzdálenosti mezi jedinci. Ta se počítá na základě počtu stejných a různých genů (podle inovačních čísel) a podle podobnosti genů, které jsou v obou jedincích.

Při inicializaci NEAT začíná z minimálních struktur, tj. neuronových sítí, které neobsahují žádné skryté neurony - všechny spoje vedou jen mezi vstupy a výstupy.

### HyperNEAT

Algoritmus hyperNEAT je rozšířením algoritmu NEAT. V algoritmu HyperNEAT se topologie sítě zafixuje na začátku (typicky jako hyper-krychle) a váhy se reprezentují pomocí jiné neuronové sítě. Tato neuronová síť dostává na vstupu souřadnice neuronů ve výsledné sítí a vrací pro ně přímo váhy. Síť pro výpočet vah se potom vytváří pomocí algoritmu NEAT.

Výhodou algoritmu HyperNEAT je, že vytváří mnohem pravidelnější sítě než NEAT, které mohou být blíže biologickým neuronovým sítím a navíc je schopen vyvíjet větší sítě.

## Vytváření architektur neuronových sítí

V současnosti jsou velmi populární algoritmy pro hledání celé struktury neuronových sítí, která se později trénuje pomocí běžných gradientních technik. Z hlediska evolučních algoritmů je v takovém případě potřeba zakódovat strukturu sítě (na úrovni vrstev nebo bloků neuronů) do jedince. Pokud bychom chtěli vytvářet pouze vrstvy, situace je docela jednoduchá - jedinec může být např. posloupnost těchto vrstev včetně jejich parametrů. Operátory jsou potom úpravy parametrů těchto vrstev, přidání dalších vrstev, nebo i přidání spojení mezi vrstvami, které spolu nesousedí (skip connections).

Existují ale i algoritmy jako CoDeepNEAT, které kódují jedince podobně jako NEAT. Rozdíl ale je v tom, že jednotlivé uzly neobsahují jednotlivé neurony, ale přímo moduly neuronové sítě (bloky neuronů). Tyto moduly jsou také vytvářeny pomocí NEAT algoritmu. Při vyhodnocení fitness se celkový jedinec vytvoří pomocí kombinace těchto modulů, tak, jak je popsáno v jedinci.

## Novelty Search

Algoritmus Novelty Search se netýká jen evoluce neuronových sítí, ale je obecnější. Nicméně velmi často se používá právě ve spojení s neuroevolucí. Principem novelty search je vynechání fitness funkce, která by přímo hodnotila kvalitu nalezených řešení. Tato fitness funkce je nahrazena funkcí, která porovnává chování vytvořených jedinců (např. při hledání cesty v bludišti se může počítat vzdálenost pozic, kam jedinec došel, od pozic, kam došli jedinci před ním). Může se zdát, že takový algoritmus nebude moc dobře fungovat, ale ukazuje se, že to není pravda. Zvláště v prostředích, kde klasická fitness funkce obsahuje složitá lokální optima se ukazuje, že novelty search dává dobré výsledky i z hlediska kvality nalezených řešení.