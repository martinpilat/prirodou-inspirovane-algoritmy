V dnešní přednášce se podíváme na dva různé typy neuronových sítí. Napřed si představíme architekturu, která používá lokální jednotky ve vstupní vrstvě a potom se podíváme na rekurentní neuronové sítě, tedy takové, kde váhy mezi neurony mohou tvořit cykly.

## RBF sítě

Neuronové funkce s lokálními jednotkami založenými na Radial Basis Functions (RBF sítě) představují zajímavou alternativu k perceptronovým neuronovým sítím. Hlavní rozdíl mezi nimi je v tom, že neurony ve vstupní vrstvě místo skalárního součinu počítají nějakou funkci závislou na vzdálenosti od svého "váhového" vektoru (slovo "váhového" je v uvozovkách, protože se váhy nejedná - typicky se tomuto vektoru říká "střed"). Výpočet těchto neuronů tedy můžeme vyjádřit jako  $y = \rho(||x-c||)$, kde $\rho$ je nějaká aktivační funkce (kernel), $c_i$ je střed neuronu, $x_i$ je vstup a $||\cdot||$ je nějaká norma - často Euklidovská vzdálenost, ale může být i jiná. Jako kernel se často používá např. Gaussova funkce $\rho(x) = e^{-\beta x^2}$.

Typická RBF síť má po RBF vrstvě už jen jednu vrstvu neuronů (perceptronového typu). Celá síť tedy počítá funkci 
$$ \varphi(x) = \sum_{i=1}^N w_i \rho(x, c), $$
kde $w_i$ jsou váhy pro výstupní vrstvu (v případě více výstupních neuronů máme zase matici vah).

Všimněte si, že aktivační funkce v RBF síti je lokální, tj. má největší hodnotu pro vstupy, které jsou blízko středu neuronu a pro vstupy dále od středu jejich aktivace klesá až k 0.

Trénování RBF sítí typicky probíhá ve dvou fázích, napřed se pomocí nějakého shlukovacího algoritmu (např. $k$-means, viz níže) nastaví středy neuronů ve vstupní vrstvě, potom se spočítá parametr $\beta$ v každém neuronu jako 
$$ \beta = \frac{1}{2\sigma^2},$$
kde $\sigma$ je průměrná vzdálenost objektů v příslušném shluku od jeho středu. Nakonec se natrénují váhy výstupní vrstvy. Zde stačí postupně předložit vstupy z trénovací množiny, spočítat aktivace vstupní vrstvy a následně použít algoritmy pro lineární regresi. Výstupní vrstva totiž počítá pouze lineární kombinaci aktivací vstupní vrstvy. 

Alternativou k popsanému postupu trénování může být použití gradientní metody pro nastavení středů neuronů i vah ve výstupní vrstvě. 

### Algoritmus $k$-means

Zmínili jsme, že pro hledání středů neuronů ve vstupní vrstvě se používají shlukovací algoritmy, nejčastěji tzv. algoritmus $k$-means. Je to algoritmus, který se snaží ve vstupních datech najít shluky - skupiny dat, které jsou blízko k sobě, ale zároveň daleko od ostatních skupin. Jde o algoritmus učení bez učitele, nepoužívá tedy žádné cílové hodnoty $y$. Algoritmus dostane na vstupu vektory dat $x_i$ a číslo $k$, které označuje požadovaný počet shluků. Algoritmus začne tak, že náhodně zvolí $k$ středů shluků $m_j$ (často jako $k$ vzorků ze vstupních dat). Potom opakuje fáze přiřazování a přepočítávání středů. Ve fázi přiřazování je každý vzorek ze vstupních dat přiřazen do toho shluku, jehož střed je k němu nejblíž. Ve fázi přepočítání středů se každý střed přepočítá jako střed shluku dat, které k němu patří. Tyto dvě fáze se opakují, dokud algoritmus nezkonverguje, nebo po zadaný počet iterací.

## Rekurentní neuronové sítě

V neuronových sítí, které jsme zatím zmiňovali, vedou váhy vždy jen jedním směrem a celá neuronová síť tedy tvoří acyklický graf. Takové neuronové sítě se chovají zcela reaktivně a jejich přechozí vstupy nijak neovlivňují vstupy následující. To se hodí pro mnoho běžných problémů, jako jsou např. klasifikace obrázků apod., ale pokud mají být vstupem neuronové sítě posloupnosti různých délek, kde se jednotlivé položky ovlivňují, je vhodnější neuronové síti přidat nějaký vnitřní stav, reprezentovaný typicky pomocí spoje, který vede zpět. Sítě s takovými spoji se nazývají rekurentní a používají se např. pro předpovídání časových řad, strojový překlad, nebo generování textu.

Nejjednodušší rekurentní sítí může být síť pouze s jedním vstupem, jedním výstupem a jedním neuronem v jediné skryté vrstvě. Tento neuron potom bude mít rekurentní spojení sám do sebe. Význam tohoto spoje je takový, že při předložení vzoru neuron dostane kromě svého běžného vstupu ještě svojí aktivaci v předchozím kroku (při předložení předcházejícího vstupu). Neuron tedy vlastě počítá svou aktuální aktivaci jako vážený součet svého vstupu a svého předchozího výstupu. V obecnějších rekurentních sítích je význam podobný - rekurentní váhy předávají stav z předcházejícího časového kroku.

Výpočet rekurentní sítě tedy probíhá tak, že ji postupně předkládáme vzory a ona na jejich základě (a na základě svých aktivací v předchozích krocích) počítá výstupy. S výstupy zacházíme podle toho, co chceme se sítí dělat. Pokud má např. předpovídat hodnotu časové řady, předložíme napřed všechny vstupy a až potom se podíváme na výstup. Při překladu předložíme napřed větu v jednom jazyce a potom teprve počkáme, až síť vygeneruje větu v jazyce cílovém. Při generování textu necháme síť generovat samostatně a dáváme jí na vstup její předchozí výstupy. Každopádně na posloupnost vstupů dostaneme posloupnost výstupů, kterou můžeme při trénování porovnat s nějakou požadovanou posloupností. 

### Trénování rekurentních neuronových sítí

Trénování probíhá pomocí algoritmu back-propagation, který jsme si ukazovali minule, jen je potřeba síť rozvinout v čase, tj. zkopírovat ji pro každý krok vstupu (a výstupu). Takto upravené verzi algoritmu se říká backpropagation through time (algoritmus zpětného šíření v čase).

S trénováním rekurentních vah ale mohou být problémy. Když si uvědomíte, jak algoritmus zpětného šíření funguje, uvidíte, že se v něm gradient z předchozí vždy násobí vahou. Pokud je toto rekurentní váha, tak se opakovaně násobí tou samou hodnotou. V případě, že je tato hodnota větší než 1, tak gradienty nekontrolovaně rostou (explodující gradienty), pokud je menší než 1, tak naopak klesají k 0 (mizející gradienty). Obě situace vedou k tomu, že algoritmus nefunguje moc dobře. 

Tento problém se dá řešit dvěma způsoby - buď se rekurentní část sítě neučí vůbec, jako v tzv. Echo state networks, nebo se rekurentní váha zafixuje na 1 a práce se stavem sítě se provádí explicitně jako v tzv. Long-short term memory sítích.

### Echo state sítě

Echo state sítě (ESN) fungují tak, že hned na vstupu mají velkou rekurentní vrstvu, která má váhy inicializované náhodně, a tyto se dál nijak netrénují. Typicky je tato vrstva implementovaná jako jediná matice $k \times m$, kde $k = n + m$, $m$ je velikost rekurentní vrstvy a $n$ je počet vstupů. Síť funguje tak, že na vstup dostává vektory délky $n$ a připojí k nim svůj vnitřní stav délky $m$. Na ten aplikuje svou rekurentní vrstvu a tím dostane nový vnitřní stav. Rekurentní vrstva typicky obsahuje nějakou aktivační funkci, aby byla nelineární (ta se aplikuje po složkách na všechny aktivace - výsledky násobení náhodnou maticí). Tradiční ESN po rekurentní vrstvě obsahují už jen jednu vrstvu, kterou podobně jako u RBF sítí můžeme trénovat pomocí lineární regrese, nebo pomocí gradientní metody.

ESN může na první pohled vypadat zvláštně, proč by měla náhodná matice dávat rozumné výsledky? Důležitým pozorováním je, že díky velikosti vnitřního stavu (který je často větší než počet vstupů), matice vlastně náhodně transformuje informaci ze vstupu do prostoru s větší dimenzí. Další vrstvy se potom vlastně snaží tuto informaci rozkódovat a dostat z ní potřebné informace. Uvědomte si také, že vnitřní stav sítě závisí na všech předcházejících vstupech, nejen na tom posledním, a obsahuje tedy informace o všech z nich.

### Long short term memory

Long short term memory (LSTM) sítě řeší problém s trénováním trochu jinak. Nahrazují každý neuron tzv. LSTM buňkou, která explicitně pracuje se svým stavem (pamětí) a rekurentní spoje mezi jednotlivými buňkami potom mají váhu zafixovanou na 1. 

Vstupem každé buňky je její stav $c_{t-1}$ z předcházejícího kroku a spojení jejích výstupů v předcházejícím stavu a nových vstupů $[h_{t-1}, x_{t}]$. Na základě vstupů se napřed spočítají hodnoty tzv. bran (gates) - zapomínací $f_t$ (forget) a vstupní $i_t$ (input). Obě se počítají podobně a to jako 
$$ \begin{aligned}
    f_t &= \sigma(W_f[h_{t-1}, x_t] + b_f) \\  
    i_t &= \sigma(W_i[h_{t-1}, x_t] + b_i), \\
    \end{aligned}
$$
kde $W_f, W_i, b_f$ a $b_i$ jsou váhy a prahy pro zapomínací a vstupní bránu a $\sigma$ je sigmoida. Z těch samých hodnot zároveň spočítáme i kandidáta na nový vnitřní stav jako 
$$
    \bar{C_t} = \tanh(W_c[h_{t-1}, x_t] + b_c), 
$$
kde opět $W_c$ jsou váhy a $b_c$ jsou prahy pro výpočet stavu. Nový stav buňky se potom spočítá jako 
$$
    C_t = f_t \ast C_{t-1} + i_t \ast \bar{C_t}, 
$$
kde operace $\ast$ značí násobení po složkách.

Nakonec ještě spočítáme výstup buňky $h_t$. Ten se spočítá z aktuálního stavu buňky a jejího vstupu pomocí výstupní (output) brány $o_t$, jako
$$
\begin{aligned}
    o_t &= \sigma(W_o[h_{t-1}, x_t] + b_o) \\
    h_t &= o_t \ast \tanh(C_t),
\end{aligned}
$$
kde opět $W_o$ a $b_o$ jsou váhy a prahy pro výstupní bránu.

Přenos informace mezi jednotlivými časovými kroky u LSTM sítí probíhá pomocí stavu. S tím není přímo spojena žádná váha a tak se při propagaci chyby v síti můžeme vyhnout problémům s explodujícími a mizícími gradienty. LSTM sítě si díky této vlastnosti umí zapamatovat delší posloupnosti vstupů než základní typu rekurentních sítí. 
