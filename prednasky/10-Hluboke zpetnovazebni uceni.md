Zatím jsme se na přednášce bavili o zpětnovazebním učení, evolučních algoritmech a neuronových sítí. Minule jsme spojili evoluci a neuronové sítě, dnes se podíváme na použití neuronových sítí ve zpětnovazebním učení - na hluboké zpětnovazební učení. Tímto tématem také uzavřeme všechny tři tyto kapitoly.

Připomeňme si napřed terminologii a značení (kopie textu z kapitoly o zpětnovazebním učení):

> Prostředí můžeme formálně popsat jako markovský rozhodovací proces (MDP), který je zadaný čtveřicí $(S, A, P, R)$, kde $S$ je konečná množina stavů prostředí, $A$ je (konečná) množina akcí (případě může být nahrazena množinami $A_s$ akcí aplikovatelných ve stavu $s$), $P_a(s, s')$ je přechodová funkce, která udává pravděpodobnost, že aplikací akce $a$ ve stavu $s$ přejde prostředí do stavu $s'$ a $R_a(s, s')$ je funkce odměn, která udává okamžitou odměnu, kterou agent dostane od prostředí, pokud ve stavu $s$ provede akci $a$ a převede tím prostředí do stavu $s'$. U přechodové funkce je důležité, že splňuje tzv. markovskou podmínku, tj. že závisí pouze na aktuálním stavu $s$ a akci $a$ a nikoliv na akcích a stavech předcházejících. 

> Chování agenta potom můžeme popsat pomocí strategie (policy) $\pi: S \times A \to [0,1]$, kde $\pi(s,a)$ udává pravděpodobnost provedení akce $a$ ve stavu $s$. Cílem zpětnovazebního učení je potom najít strategii $\pi$ takovou, že maximalizuje celkovou odměnu, kterou agent získá $\sum_{t=0}^\infty \gamma^tR_{a_t}(s_t, s_{t+1})$, kde $a_t = \pi(s_t)$ je akce provedená agentem v kroku $t$ a $\gamma < 1$ je diskontní faktor, který zajišťuje, že suma je konečná.

> Hodnota $V^\pi(s)$ stavu $s$ při použití strategie $\pi$ se dá definovat jako $V^\pi(s) = \mathrm{E}[R] = \mathrm{E}[\sum_{t=0}^\infty \gamma^t r_t|s_0 = s]$, kde $R$ značí celkovou získanou diskontovanou odměnu a $r_t$ značí odměnu obdrženou v čase $t$. Kromě hodnoty stavu se velmi často hodí uvažovat také hodnotu $Q^\pi(s, a)$ akce $a$ provedené ve stavu $s$ pokud budeme dále sledovat strategii $\pi$. Výhodou tohoto modelu je, že agent nepotřebuje mít model prostředí, který popisuje, jakým způsobem akce ovlivňují prostředí a učí se tento model za běhu.

> Cílem agenta potom tedy je najít optimální strategii $\pi^\star$ takovou, že $V^{\pi^\star}(s) = \max_\pi V^\pi(s)$. Hodnotu stavů (akcí) pro optimální strategii budeme značit jako $V^\star (s)$ ($Q^\star(s, a)$).

Z těchto definici můžeme snadno odvodit tzv. Bellmanovy rovnice, které jsou nutnou podmínkou optimality pro strategii $\pi$. 
$$ Q^\pi (s, a) = \sum_{s'}P_a(s, s')\big[ R_a(s, s') + \gamma \sum_{a'}\pi(s', a')Q^\pi(s', a') \big]$$
$$ V^\pi(s) = \sum_{a} \pi(s, a)\sum_{s'}P_a(s, s')\big[ R_a(s, s') + \gamma V^\pi(s') \big]$$

## Hluboké Q-učení

Hluboké Q-učení je založeno na stejné myšlence jako Q-učení, tj. chceme pro každý stav $s$ a každou akci $a$ odhadnout jakou diskontovanou odměnu bychom dostali, pokud bychom akci $a$ ve stavu $s$ provedli. V tradičním Q-učení jsou tyto hodnoty reprezentovány jako matice Q. Tato reprezentace je ale problematická, pokud je hodně stavů, nebo hodně různých akcí. V hlubokém Q-učení se tedy pro reprezentaci této matice používá neuronová síť, která pro každý stav vrací ohodnocení všech akcí. 

Trénování neuronové sítě se provádí podle Bellmanovy rovnice pro $Q$, takovým způsobem, že se porovnává aktuální odměna od prostředí $R_a(s, s')$ s hodnotou spočítanou pomocí Bellmanových rovnic z $Q$ a minimalizuje se střední čtvercová chyba jejich rozdílu. Naším cílem tedy je minimalizovat rozdíl mezi $Q(s, a)$ a $R_a(s, s') + \gamma max_{a'}Q_k(s', a')$. Všimněte si, že stejně jako v standardním Q-učení uvažujeme, že v dalším stavu vybereme nejlepší akci podle aktuálního odhadu $Q$. Chybová funkce tedy je 

$$ \mathbb E_{s' \sim P_a(s, s')}\big[ (R_a(s, s') + \gamma max_{a'}Q_\theta(s', a') - Q_\theta(s, a))^2 \big]|{\theta = \theta_k} $$

kde $Q_\theta$ jsou parametry neuronové sítě reprezentující matici $Q$.  

Pro výpočet chybové funkce tedy potřebujeme znát stav $s$, vybranou akci $a$, získanou odměnu $R_a(s, s')$ a následující stav $s'$. Všechny tyto údaje snadno získáme, pokud necháme agenta provádět akce v prostředí. Při trénování se ale často objevuje problém s tím, že měníme přímo funkci, která odhaduje Q a tím měníme i chování agenta a odhady zároveň, je ale vidět, že oba tyto aspekty spolu úzce souvisí - vlastně se snažíme učit funkci, kde se pořád mění vstupy i výstupy. Pro zachování větší stability trénování se používají dva triky - cílová síť (target network) a přehrávání zkušeností (experience replay).

Podstatou triku s cílovou sítí je, že oddělíme síť pro výběr akce a síť pro odhad hodnoty. Typicky jen tak, že se zafixují parametry sítě, podle které se vybírá akce a měníme jen parametry sítě, která se učí ohodnocení. Po daném počtu iterací se parametry obou sítí nastaví na stejné hodnoty a pokračuje se se trénováním podle stejného postupu. Chybová funkce tedy v tomto případě vypadá jako 
$$ \mathbb E_{s' \sim P_a(s, s')}\big[ (R_a(s, s') + \gamma max_{a'}Q_{\theta^-}(s', a') - Q_\theta(s, a))^2 \big]|_{\theta = \theta_k}, $$
kde $\theta^-$ jsou právě parametry sítě pro výběr akce, které se aktualizují méně často, než parametry $\theta$, které odhadují hodnotu Q.

Podstatou experience replay je, že si pamatujeme čtveřice $(s, a, r, s')$ stavu, akce, odměny a následujícího stavu a při trénování náhodně vybíráme přechody z této paměti místo toho, abychom vždy používali poslední přechod. Tím se zbavíme závislostí mezi po sobě jdoucími vstupy.

Hluboké Q-učení se proslavilo jako technika, která je schopná naučit se hrát Atari hry na podobné úrovni jako lidští hráči s tím, že vstupem je pouze obrazová informace a změny odměny se počítají jako změny skóre hry.

## DDPG

Hluboké Q-učení vyžaduje počítání maxima přes všechny akce - tato operace je ale složitá, pokud je prostor akcí spojitý (představte si třeba řízení auta, kde akce je úhel otočení volantu a sešlápnutí plynu/brzdy). Z tohoto důvodu algoritmus DDPG (Deep Deterministic Policy Gradient) nahrazuje tuto operaci novou sítí, která přímo vrací akci, která se má provést. Označme tuto funkci s parametry $\theta$ jako $\mu_\theta$. Jde o funkci z prostoru stavů do prostoru akcí. Označme zároveň funkci počítající hodnotu $Q$ s parametry $\phi$ jako $Q_\phi$. DDPG používá oba triky zmíněné výše, označme tedy pomocí $\theta^-$ a $\phi^-$ parametry cílových sítí pro $\theta$ a $\phi$.

Aktualizace parametrů $\phi$ sítě pro $Q$ se potom počítá pomocí upravené chybové funkce 
$$ \mathbb E_{s' \sim P_a(s, s')}\big[ (R_a(s, s') + \gamma Q_{\phi^-}(s', \mu_{\theta^-}(s')) - Q_\phi(s, a))^2 \big]| \theta = \theta_k. $$
Myšlenka trénování sítě $\mu$ je velmi jednoduchá - chceme aby vracela akce, které maximalizují $Q_\theta(s, a)$ ve stavu $s$. Maximalizujeme tedy pomocí gradientní metody výraz 
$$ \mathbb E_s\big[ Q_\phi(s, \mu_\theta(s)) \big]. $$


## Policy gradient metody

Na zpětnovazební učení se také můžeme dívat tak, že cílem je najít policy parametrizovanou pomocí $\theta$, která bude maximalizovat celkovou odměnu $J(\theta) = \mathbb{E}[\sum_{t=0}^{T-1}r_{t+1}]$, tj. součet odměn, které agent získá při následování policy v prostředí. Při troše snahy a derivování se dá ukázat, že gradient této celkové odměny je $\nabla_\theta J(\theta) = \sum_{t=0}^{T-1}\nabla_\theta \log \pi_\theta(a_t|s_t)G_t$, kde $\pi_\theta(a | s)$ je pravděpodobnost výběru akce $a$ ve stavu $s$ pomocí policy $\pi$ parametrizované $\theta$ a $G_t$ jsou kumulované (diskontované) odměny od času $t$ do $T-1$.

## Actor-critic

Nevýhodou tohoto popisu učení je, že při velkých odměnách $G_t$ můžeme dostávat velké rozptyly hodnot gradientu. Z toho důvodu se $G_t$ často nahrazuje jinými výrazy - jednou z možností je přímo hodnota $Q(s, a)$, která se potom učí podobně jako Q hodnoty v DQN. Populární je ale i tzv. advantage (výhoda), ta se spočítá jako rozdíl mezi provedením akce $a_t$ ve stavu $s_t$ (tj. hodnotu $Q(s_t, a_t)$) a hodnotou stavu $V(s_t)$ - $A(s_t, a_t) = Q(s_t, a_t) - V(s_t)$. Počítáme tedy, o kolik lepší je provést akci $s_t$ oproti nějaké obecné akci. Pro určení advantage nepotřebujeme trénovat sítě pro $Q$ a $V$, stačí jedna síť pro $V$, ze vztahů mezi $Q$ a $V$ lze odvodit, že advantage se dá spočítat i jako $A(s_t, a_t) = R_a(s_t, s_{t+1}) + \gamma V(s_{t+1}) - V(s_t)$. Takto implementovaná metoda se nazývá advantage actor-critic. Síť pro $V$ hraje roli kritika a říká, jak dobré jsou stavy, kdo kterých se agent dostal, síť pro policy $\pi$ potom vybírá prováděné akce.

Existuje i velmi populární metoda A3C - Asynchronous Advantage Actor-Critic. Ta nahrazuje použití experience replay tím, že se hraje více her najednou, aktualizace vah se potom průměrují přes aktualizace spočítané ve všech nezávislých hrách.