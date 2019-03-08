Jednou z nejznámějších přírodou inspirovaných technik jsou evoluční algoritmy. Jsou to obecné optimalizační heuristiky, které mají široké uplatnění v mnoha oblastech, od optimalizace reálných funkcí, přes kombinatorickou optimalizaci, až po vývoj elektronických obvodů, nebo neuronových sítí.

Evoluční algoritmy jsou inspirované (typicky) Darwinovou evoluční teorií. Dalo by se i říct, že evoluční algoritmy simulují život mnoha generací a to, jak je ovlivní selekční tlak prostředí. V evolučních algoritmech pracujeme s množinou kandidátů na řešení daného problému. Každý kandidát se nazývá jedinec a celé množině se říká populace. Evoluční algoritmus běží v iteracích (generacích) a v každé iteraci provede výběr jedinců, které nějak upraví (pomocí tzv. genetických operátorů) a následně vybere, kteří jedinci přežijí do další generace. Přednostně jsou vždy vybíráni jedinci, kteří lépe řeší zadaný problém. Kvalita řešení problému je daná tzv. fitness funkcí. Populace na začátku generace se označuje jako rodiče a populace na konci (po aplikaci genetických operátorů) jako potomci. 

## Jednoduchý genetický algoritmus

Klasickým příkladem evolučního algoritmu může být tzv. jednoduchý genetický algoritmus. V tom jsou jedinci kódováni jako posloupnosti bitů pevné délky. Fitness funkce (jako vždy) záleží na konkrétním řešeném problému. Na začátku algoritmu jsou jedinci v populaci inicializováni náhodně a je spočítána jejich fitness. Tito jedinci potom tvoří první populaci rodičů. Následně jsou vybrání rodiče, na které budou aplikovány genetické operátory. Výběr se provádí tak, že pravděpodobnost výběru daného jedince je přímo úměrná jeho fitness - tento způsob výběru se nazývá ruletová selekce. Výběr se provádí s opakováním, někteří jedinci tedy mohou být vybrání vícekrát, zatímco jiní nejsou vybráni vůbec. Potom jsou na tyhle vybrané jedince aplikovány genetické operátory - křížení  a mutace. Křížení ma za úkol zkombinovat dvě řešení a vytvořit tak řešení nové. Zde se typicky používá tzv. jednobodové křížení - náhodně se vybere jeden bod v jedinci a nový potomek vznikne tak, že se překopíruje část z jednoho rodiče před tímto bodem a z druhého od tohoto bodu dále. Po křížení se ještě aplikuje mutace. V jednoduchém genetickém algoritmu to je typicky mutace, která náhodně změní některé bity v jedinci. Cílem mutace je zlepšit různorodost (diverzitu) populace. Nově vytvoření potomci potom nahradí původní rodiče a algoritmus pokračuje další generací. 

Algoritmus může být popsán pomocí pseudokódu níže:

    P_0 <- náhodně inicializuj populaci
    t <- 0
    dokud není konec
        vyhodnoť fitness jedinců v P_t
        M_t <- vyber rodiče pro aplikaci operátorů pomocí ruletové selekce z P_t
        O_t <- vytvoř populaci potomků aplikováním genetických operátorů na M_t
        P_{t+1} <- O_t
        t <- t+1

Fitness funkce je daná problémem, který chceme řešit a evoluční algoritmy ji vždy maximalizují. Typickým příkladem je tzv. problém OneMAX, kde chceme, aby jedinec reprezentovaný jako binární řetězec obsahoval co nejvíce jedniček. V takovém případě můžeme fitness definovat jako počet jedniček v jedinci. Tento příklad není prakticky moc užitečný, stejným způsobem ale můžeme reprezentovat i známý problém nalezení podmnožiny nějaké zadané množiny, takové, že součet prvků v této podmnožině je nějaké zadané číslo. Jednička v jedinci na pozici $i$ potom znamená, že $i$-tý předmět je vybraný do podmnožiny. Fitness se pak dá počítat jako rozdíl součtu všech čísel v množině a absolutní hodnoty rozdílu požadované hodnoty a součtu prvků v podmnožině (chceme minimalizovat absolutní hodnotu rozdílu, protože evoluční algoritmy maximalizují fitness, musíme ji odečíst od nějakého vhodně velkého čísla - např. součtu všech čísel).

## Varianty evolučních algoritmů

Jednoduchý genetický algoritmus je jen jedním příkladem evolučních algoritmů. Můžeme si všimnout, že mnoho jeho částí jde snadno nahradit nějakou jinou variantou. Například můžeme změnit selekci, genetické operátory a způsob jakým vzniká nová populace ze staré. Kromě toho můžeme změnit i způsob kódování řešení v jedinci.

### Selekce

Zatím jsme zmínili ruletovou selekci, kde pravděpodobnost výběru jedince je přímo úměrná jeho fitness - formálněji pravděpodobnost $p_i$ výběru jedince $i$ se spočítá jako $$p_i = \frac{f_t}{\sum_{j=1}^N f_j},$$ kde $f_j$ je fitness jedince $j$. Velkou nevýhodou této selekce je, že záleží přímo na hodnotách fitness, pokud tedy fitness změníme tak, že k ní přičteme nějakou velkou konstantu, rozdíly mezi jedinci se zmenší a selekce se začne chovat náhodně. Toho se samozřejmě dá i využít, pokud chceme zesílit/zeslabit vliv selekce. 

Alternativ k ruletové selekci existuje celá řada. My zmíníme teď jen jednu a to je turnajová selekce - v té se napřed náhodně vybere několik (typicky 2) jedinci, porovná se jejich fitness a selekce potom s velkou pravděpodobností (třeba 80 %) vybere toho lepšího z nich. Výhodou turnajové selekce je, že její výsledek záleží jen na pořadí jedinců podle fitness, navíc funguje i pro záporné hodnoty fitness.

### Genetické operátory

Genetické operátory úzce souvisí s tím, jak je jedinec zakódovaný. Pro binární kódování a jiná kódování založená na posloupnostech konstantní délky se často používá např. již zmíněné jednobodové křížení. Do se dá zobecnit na $n$-bodové křížení, kde se místo jednoho bodu pro křížení jich zvolí $n$ a potomci potom vznikají tak, že se alternuje, z jakého rodiče je vybrána jaká část. Kromě toho se ještě občas uvažuje tzv. uniformní křížení, kde se u každé pozice znovu náhodně rozhodujeme, ze kterého rodiče dosadíme hodnotu do potomka.

### Přenos jedinců do další generace

V jednoduchém genetickém operátoru je další generace tvořena přímo potomky vytvořenými v generaci předcházející. Z toho důvodu také musí být počet rodičů a potomků stále stejný. Nevýhodou je i to, že genetické operátory mohou rozbít nejlepší zatím nalezené řešení. Ztrátě nejlepšího řešení se zabraňuje pomocí techniky, které se říká elitismus. V algoritmech s elitismem se typicky malá část nejlepších rodičů rovnou zkopíruje do další generace. Z potomků je potom potřeba vybrat jen tolik, aby se populace naplnila. K výběru se mohou používat stejné selekce jako k výběru před aplikací genetických operátorů.

Je také možné generovat jiný počet potomků, než kolik je rodičů. Práci s populací potom můžeme popsat pomocí notace z evolučních strategií (budou později) jako $(\mu, \lambda)$ nebo $(\mu + \lambda)$. Zápis značí, že z populace $\mu$ rodičů se vygeneruje $\lambda$ potomků. V prvním případě se potom další populace vybírá jako $\mu$ nejlepších z $\lambda$ potomků (a tedy nutně $\lambda > \mu$), ve druhém případě se další populace vybírá jako $\mu$ nejlepších z rodičů i potomků (a někdy dokonce $\lambda = 1$ - v tzv. stead-state algoritmech).

V příští přednášce se podíváme na další možnosti kódování jedince a s tím související genetické operátory.