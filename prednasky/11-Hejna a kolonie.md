V dnešní přednášce se podíváme na další přírodou inspirované algoritmy pro optimalizaci. Konkrétně na algoritmus Particle Swarm Optimization (PSO), který je inspirovaný pohybem hejn ptáků, a na And Colony Optimization (ACO), který je inspirovaný chováním mravenců. Nakonec se stručně podíváme i na další přírodou inspirované algoritmy.

## Particle Swarm Optimization (PSO)

Optimalizace hejnem částic (PSO) je optimalizační algoritmus inspirovaný chováním hejn ryb nebo ptáků. Je to algoritmus určený pro spojitou optimalizaci, který používá množinu (populaci) částic. Každá částice je reprezentována jako dva vektory v $\mathbb{R}^n$ -- jeden z nich je její pozice ($x$) a druhý je její rychlost ($v$). Navíc si každá částice pamatuje pozici (vektor) v prostoru, kde měla nejlepší hodnotu fitness ($p_{best}$) a místo, kde je nejlepší hodnota fitness pro celou populaci ($g_{best}$).

Celý algoritmus PSO je potom velmi jednoduchý. Je založený na tom, že každá částice se pohybuje v prostoru a přitom je přitahována k místům, kde sama našla své nejlepší řešení, a kde je zatím nejlepší globální řešení. Na počátku se pozice částic inicializují náhodně v prohledávaném prostoru a potom algoritmus iterativně aktualizuje rychlosti a pozice všech částic podle rovnic
$$ v \gets \omega v  + \varphi_p r_p (p_{best} - x) + \varphi_b r_b (g_{best} - x)$$

$$ x \gets x + v,$$

kde $r_p, r_b$ jsou náhodná čísla mezi 0 a 1 (často různá pro různé souřadnice) a $\omega, \varphi_p, \varphi_b$ jsou parametry, které určují setrvačnost a jak moc je jedinec přitahován ke svému a globálnímu nejlepšímu řešení.

Takto popsaný algoritmus PSO používá tzv. globální topologii, tj. všechny částice mohou přímo komunikovat se všemi (a sdílet tak informaci o globálním optimu). Existují i varianty PSO, které používají jen lokální topologii, tedy částice mohou komunikovat jen s nějakou podmnožinou hejna, ta potom sdílí lokální nejlepší řešení. Pro výběr topologie existují v zásadě dvě možnosti - buď geometrická, kde spolu komunikují částice, které jsou blízko u sebe, nebo sociální, kde je topologie určena předem, bez ohledu na pozice částic. Ve druhém případě se často používá kruhová topologie, kde každá částice má jen dva sousedy.

PSO se typicky používá pro spojitou optimalizaci a pro tento případ není nutné algoritmus nijak upravovat - pozice částic přímo reprezentují kandidáty na řešení a jejich kvalita je určena podle hodnoty optimalizované funkce. Algoritmus se ale dá použít i pro řešení jiných typů problémů - diskrétních a kombinatorických. Pro celočíselnou optimalizaci se často počítá s reálnými čísly a výsledky se potom zaokrouhlí. Pro obecnější kombinatorickou optimalizaci je potřeba nějakým způsobem definovat operace, které se používají v rovnicích. Jednou z možností je např. použít množinové operace.

## Ant Colony Optimization (ACO)

Ant Colony Optimization (optimalizace kolonií mravenců), je algoritmu založený na chování mravenců. Ti jsou schopni hledat krátké cesty mezi mraveništěm a potravou na základě pokládání feromonu do prostředí. Při vyhledávání potravy mravenci cestou od mraveniště kladou malé množství feromonu. Po nalezení potravy se vrací do mraveniště a cestou kladou mnohem větší množství feromonu. Pokud mravenci při svém pohybu (hledání potravy) narazí na feromonovou stopu, mají tendenci ji sledovat - šance, že po ní půjdou je vyšší, pokud je stopa silnější.

Algoritmus ACO je založen právě na této metafoře. Typicky se používá pro řešení problémů, které lze reprezentovat jako hledání cest v grafu, např. problém obchodního cestujícího, nebo směrování v počítačových sítích. Algoritmus běží iterativně a opakuje dvě části - vygenerování řešení a update feromonu.

Vygenerování řešení každým mravencem probíhá tak, že mravenec začne v některém (náhodném) vrcholu grafu a rozhoduje se, do jakého vrcholu půjde dál. Pravděpodobnost přechodu z vrcholu $x$ do vrcholu $y$ je závisí na množství feromonu $\tau_{xy}$ mezi těmito dvěma vrcholy a na atraktivitě (v zásadě heuristické hodnotě) $\nu_{xy}$ přechodu mezi těmito vrcholy (v obou případech je vyšší hodnota lepší). Pravděpodobnost přechodu je potom úměrná hodnotě $(\tau_{xy}^\alpha)(\nu_{xy}^\beta)$, kde $\alpha$ a $\beta$ jsou konstanty,které určují poměr mezi vlivem obou proměnných.

Update feromonu má dva kroky - v prvním kroku se část feromonu vypaří, ve druhém kroku je na hrany, po kterých se pohyboval některý z mravenců, položen feromon v množství, které odpovídá kvalitě řešení nalezených mravenci. Konkrétně, po těchto dvou krocích se množství feromonu upraví podle vztahu 
$$ \tau_{xy} \gets (1-\rho)\tau_{xy} + \rho \sum_k \tau_{xy}^k,$$ 
kde $\rho$ je konstanta, která určuje rychlost vypařování feromonu, $Q$ je vhodně zvolená konstanta, $L_k$ je kvalita řešení nalezeného mravencem $k$ a $\tau_{xy}^k = Q/L_k$ pokud mravenec $k$ prošel přes hranu $(x,y)$ a 0 jinak.

Při použití ACO pro řešení TSP je $L_k$ typicky délka cesty a $\nu_{xy}$ převrácená hodnota délky hrany $(x, y)$. 

Při aplikaci na jiné problémy je typicky rozdíl hlavně v generování cesty mravencem. Například tzv. Vehicle Routing Problem (VRP) je problém, kde je cílem naplánovat trasu pro rozvoz zboží ze skladu k zákazníkům. Cílem je minimalizovat počet vozidel potřebných pro rozvoz a najetou vzdálenost. Vozidla jsou omezena kapacitou (a např. i dobou strávenou na cestě). Při generování cesty tedy mravenci (vozidla) vybírají podle výše zmíněného vztahu dalšího zákazníka k navštívení dokud to je možné (zboží se vejde do auta a cesta není moc dlouhá). Pokud to možné není, vrací se do skladu. Zbytek algoritmu je potom stejný jako u TSP.

## Artificial Bee Colony

Umělé včelí kolonie (ABC) jsou optimalizační algoritmus založený na chování včel při hledání potravy. Včely jsou rozděleny do třech skupin - na dělnice, vyčkávající včely a průzkumníky. Každá dělnice opracovává jeden zdroj jídla (pozice těchto zdrojů kódují řešení). Při opracování dělnice navštíví zdroje jídla v okolí, a pokud je kvalitnější (má lepší fitness) nahradí svůj zdroj tímto novým zdrojem. Potom se všechny dělnice sejdou v úle, vymění si informace o kvalitě zdrojů a vyčkávající včely si vyberou některé z těchto zdrojů pomocí ruletové selekce. Dělnice si zároveň pamatují, jak dlouho už opracovávají daný zdroj, a pokud přesáhne tato doba nastavený limit, zdroj opustí a stane se z ní průzkumník. Průzkumníci prohledávají prostor náhodně a hledají nové zdroje potravy. 

## Artificial Immune Systems

Umělé imunitní systémy (AIS) modelují různé procesy, které probíhají při práci imunitního systému u savců. Použité techniky se zde různí, nicméně typická aplikace AIS je ve strojovém učení, konkrétně pro klasifikaci, nebo detekci anomálií.

Například negativní selekce je inspirovaná pozitivní a negativní selekcí T-lymfocytů, která probíhá v brzlíku při jejich dozrávání. Při negativní selekci se lymfocyty, které reagují na vlastí buňky odstraňují. Algoritmy založené na negativní selekci se typicky používají pro detekci anomálií, nebo jednotřídní (one-class) klasifikaci. V obou případech jde o to poznat, jestli dané vzory jsou normální (patří do trénovacích dat), nebo ne. Algoritmus generuje množství různých pravidel a odstraňuje ta, která reagují na data z trénovací množiny. 

Klonální selekce (clonal selection) se na druhou stranu snaží vytvořit pravidla, která dobře rozpoznávají nějaké vzory. Napřed se vygeneruje množina možných pravidel, z těch se potom ta, které lépe odpovídají požadovaným vzorům (mají vyšší afinitu), naklonují a v závislosti na jejich afinitě se na ně aplikuje tzv. hyper-mutace. Celý algoritmus klonální selekce vlastně připomíná evoluční algoritmus bez křížení.

## Kritika přírodou inspirovaných heuristik

V současnosti se objevuje celá řada nových přírodou inspirovaných heuristik. Toto je velmi často kritizováno, neboť navržené algoritmy často používají komplikované metafory k tomu, aby zakryly to, že nejsou až tak nové. Při studiu těchto algoritmů je tedy vždy dobré se zamyslet, co je v nich opravdu nové a jestli náhodou metafora nemá za úkol jen zkomplikovat popis algoritmu, aby vypadal nově a zajímavě. 