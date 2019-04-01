V minulých přednáškách jsme se věnovali evolučním algoritmům jako přírodou inspirované optimalizační technice. Teď necháme evoluční algoritmy na chvíli stranou a podíváme se na techniku inspirovanou fungováním nervové soustavy - na neuronové sítě.

Neuronové sítě zažívají v současnosti bouřlivý rozmach v oblasti hlubokého učení a dosahují velmi dobrých výsledků v mnoha problémech strojového učení. Velmi populární jsou především tzv. konvoluční sítě, které se používají ke zpracování obrazu. Než se dostaneme k popisu těchto složitějších modelů, podíváme se na úplné základy. Dnes si popíšeme perceptron a vícevrstvý perceptron. 

## Strojové učení a příprava dat

Neuronové sítě se používají velmi často pro klasifikaci nebo regresi ve strojovém učení. Než se tedy dostaneme k tomu, co neuronové sítě jsou, podívejme se stručně na to, v jaké formě můžeme mít data a jak s nimi pracovat jako se vstupy nebo výstupy modelu strojového učení. 

Datové množiny typicky obsahují příznaky ve formě vektorů (budeme je značit $x = (x_1, \dots, x_n)$) a požadované výstupy jako (typicky) jednu hodnotu ($y$). Různé datové množiny se ale liší typem dat pro jednotlivé příznaky $x_i$ a cílovou hodnotu $y$. Příznaky i výstupy obecně mohou být třech typů - číselné, ordinální a kategorické. 

Číselné příznaky mohou být použity přímo jako vstupy většiny modelů. Nicméně, pokud mají různé příznaky rozdílné rozsahy, bývá lepší data nějakým způsobem přeškálovat. Mezi typické přístupy patří škálování každého příznaku do intervalu $[0,1]$, nebo tzv. normalizace, tj. odečtení průměru a vydělení směrodatnou odchylkou. V prvním případě je potřeba nespoléhat na to, že hodnoty budou vždy mezi 0 a 1 - můžeme například později dostat hodnotu větší, než bylo maximum v trénovací množině, potom bude hodnota po naškálování větší než 1.

Kategorické příznaky (např. textové popisy) jsou příznaky, kterou mohou mít hodnotu z nějaké konečné množiny. Zároveň mezi hodnotami není žádné uspořádání. Takové příznaky je potřeba před jejich použitím převést na číselné. Pokud může mít daný kategorický příznak $n$ hodnot, tak se typicky kóduje pomocí vektoru $n$ hodnot z množiny $\{0, 1\}$, přičemž na 1 je nastavena jen ta pozice ve vektoru, která odpovídá dané hodnotě příznaku (např. pokud má příznak $i$-tou hodnotu z množiny, je pouze $i$-tá souřadnice vektoru nastavena na 1).

Ordinální příznaky jsou někde mezi číselnými a kategorickými a dají se kódovat pomocí libovolné z metod. 

Typ cílových hodnot určuje typ problému, který budeme řešit - kategorické cílové hodnoty vedou na klasifikaci (určení do jaké ze tříd objekt patří), číselné hodnoty na regresi (předpověď hodnoty). Jejich kódování při trénování je stejné jako u příznaků, jen je potřeba myslet na to, že je třeba kódování zase invertovat při odpovědi tak, aby výsledek dával smysl.

## Perceptron

Základní jednotkou v neuronové síti je jeden neuron. Perceptron je potom algoritmem (neuronovou sítí) s jediným takovým neuronem - perceptronem. Tento umělý neuron je vzdáleně inspirován přírodními neurony. Má několik vstupů $x_i$ a jeden výstup. Každý ze vstupů má přiřazenu váhu $w_i$. Perceptron nejdříve spočítá svojí aktivaci jako vážený součet vstupů $\xi = b + \sum_{i=1}^n w_i x_i $. $b$ je tzv. práh (bias) a ovlivňuje nakolik musí být vážený součet větší než 0, aby se peceptron aktivoval. Pokud je tato aktivace větší než práh $0$, je výstup perceptronu $1$, jinak je $0$.

Explicitní práce s prahem $b$ není potřeba a velmi často se upravují vstupy tak, že se k nim přidá jedna souřadnice s konstantní hodnotou $1$. Prahy jsou potom přímo součástí vah. Výpočet perceptronu se pak dá zapsat jako $f(\sum_{i=0}^n w_i f_i)$, kde $f$ je funkce, která pro $x < 0$ vrací 0 a jinak 1.

Kromě varianty, která vrací binární hodnoty $0$ a $1$ se často používá i varianta, která vrací tzv. bipolární hodnoty $-1$ a $1$. Rozdíl je jen ve funkci $f$. 

Trénování perceptronu je velmi jednoduché - postupně se předkládají vstupy $(x, y)$ z trénovací množiny a aktualizují se váhy podle rovnice $$w_i = w_i + r (y - f(x))x_i,$$ kde $r$ je parametr učení, který určuje, jak rychle se mění váhový vektor. Všimněte si, že výraz v závorce je 0, pokud perceptron odpověděl správně a 1, nebo -1, pokud odpověděl nesprávně.

Dá se ukázat, že takto popsaný algoritmus konverguje pokud jsou třídy v datech tzv. lineárně separabilní, tj. lze je oddělit nadrovinou ve vstupním prostoru.

V některých případech se třídy pro perceptron kódují jako $-1$ a $1$. Potom se na trénování perceptronu dá dívat i jako na gradientní optimalizaci chybové funkce $-\sum y_i(x_i^Tw_i)$.

## Vícevrstvé perceptrony (dopředné neuronové sítě)

Spojením několika perceptronů vznikne nejznámější typ neuronové sítě, tzv. vícevrstvý perceptron, nebo dopředná neuronová sít (feedforward network). Ta se skládá z vrstev perceptronů popsaných výše, přičemž vstupy první (vstupní) vrstvy jsou přímo data z trénovací (testovací) množiny a vstupy dalších (skrytých a výstupní) vrstev jsou výstupy z vrstvy předcházející.

Ve vícevrstvých sítích se zpravidla používají jiné aktivační funkce $f$ než ty zmiňované výše. Hlavní důvod je, že neuronové sítě se typicky trénují pomocí gradientních algoritmů a funkce zmíněné výše mají skoro všude gradient 0. Místo toho se používá tradičně tzv. logistická sigmoida - $f(x) = \frac{1}{1+e^{-\lambda x}}$. V současnosti se také velmi často používá funkce ReLU (rectified linear unit) definovaná jako $f(x) = \max(0, x)$.

Pro trénování se používá gradientní metoda. Chybová funkce $L(x,y|w)$ neuronové sítě (typicky MSE) se zderivuje podle vah v síti a váhy se potom upraví podle vztahu $$ w_i = w_i - \alpha\frac{\partial L(x,y|w)}{\partial w_i},$$ kde $\alpha$ je parametr učení.

V současnosti se pro výpočet gradientu nejčastěji používají knihovny, které ho umí spočítat symbolicky. Prakticky tedy je potřeba napsat jen dopředný výpočet sítě a implementovat chybovou funkci. O výpočet gradientu se postarají existující nástroje. Nicméně, pro lepší pochopení neuronových sítí se vyplatí si gradient alespoň v tomto jednoduchém případě zkusit spočítat.

Začneme s výpočtem pro výstupní vrstvu. Označme jako $w_{jk}$ váhu mezi $j$-tým neuronem v poslední skryté vrstvě a $k$-tým neuronem ve výstupní vrstvě. Výstup tohoto neuronu je $y_k = f(\xi_k)$, kde $x_j$ je výstup $j$-tého neuronu v poslední skryté vrstvě a $\xi_k = \sum w_{jk} x_j$. Uvažujeme-li chybovou funkci $E(x,t|w) = \frac{1}{2}\sum_k (y_k - t_k)^2$ ($t$ označuje vektor požadovaných výstupů, $y$ označuje výstup sítě), je její derivace podle váhy $w^L_{jk}$ dána pomocí výpočtu níže (aplikovali jsme pravidlo pro derivaci složené funkce).

$$ \frac{\partial E}{\partial w^L_{jk}}=\frac{\partial E}{\partial y_{k}}\frac{\partial y_{k}}{\partial\xi_{k}}\frac{\partial\xi_{k}}{\partial w^L_{jk}}=(y_{k}-t_{k})x_{j}\frac{\partial f(\xi_j)}{\partial\xi_{j}}.$$

Pro výpočet derivace chybové funkce podle vah ve skrytých vrstvách neuronové sítě je užitečné představit si, co přesně počítají poslední dvě vrstvy této sítě. Budeme označovat indexem $k$ neurony ve výstupní vrstvě, indexem $j$ neurony v poslední skryté vrstvě a indexem $i$ neurony ve skryté vrstvě před poslední skrytou vrstvou. Vstupy těchto neuronů budou označeny jako $x_k$, $x_j$, a $x_i$, jejich aktivace budou zase značeny jako $\xi$ s příslušným indexem a aktivační funkce jako $f$ s tímto indexem. Váhy mezi poslední skrytou a výstupní vrstvou označíme jako $w^L$ a váhy mezi posledními dvěma skrytými vrstvami jako $w^{L-1}$. Poslední dvě vrstvy tedy počítají výraz $y_{k}=f_{k}(\sum_{j}w_{jk}^L f_{j} (\sum_i w_{ij}^{L-1} x_{i}))$. Pokud zase budeme uvažovat stejnou chybovou funkci, dostaneme její derivaci opět podle pravidla pro derivaci složené funkce jako 

$$ \frac{\partial E}{\partial w_{ij}^{L-1}}=\left[\sum_{k}\frac{\partial E}{\partial\xi_{k}}\frac{\partial\xi_{k}}{\partial y_{j}}\right]\frac{\partial y_j}{\partial\xi_{j}}\frac{\partial\xi_{j}}{\partial w_{ij}^{L-1}}=\left[\sum_{k}\delta_{k}w_{jk}^{L}\right]y_{i}\frac{\partial f_{j}(\xi_{j})}{\partial\xi_{j}}.$$

Můžeme si všimnout, že první část sumy ($\frac{\partial E}{\partial\xi_{k}}$) jsem spočítali již při výpočtu pro výstupní vrstvu. Označíme ji tedy $\delta_k$ a tím dostaneme zjednodušenou verzi výrazu za posledním $=$. Nyní si stačí uvědomit, že jsme nikde nepoužili informaci o tom, že $k$ značí výstupní vrstvu a můžeme tedy použít stejný výraz pro všechny skryté vrstvy. Pokud ještě i zde definujeme $$\delta_{j}=\frac{\partial E_{v}}{\partial\xi_{j}}=\frac{\partial f_{j}(\xi_{j})}{\partial\xi_{j}}\sum\delta_{k}w_{jk}$$, dostaneme známé adaptační pravidlo pro trénování vah neuronové sítě (definice $\delta_j$ se liší podle toho, jestli jde o skrytou nebo výstupní vrstvu): $$w_{ij}^{k+1}=w_{ij}^{k}-\alpha\delta_{j}y_{i}.$$ 

Zatím jsme se nebavili o tom, jaká je derivace aktivační funkce podle jejího vstupu. Dá se ukázat, že například pro sigmoidu to je $\lambda y_{j}(1-y_{j})$. Také jsme zatím počítali derivaci jen pro jeden vstupní vzor - pro více vzorů ale dostaneme jen součet těchto derivací.