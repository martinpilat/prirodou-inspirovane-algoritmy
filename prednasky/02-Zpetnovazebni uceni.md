Jednou z oblastí, kde se přírodou inspirované techniky často používají je zpětnovazební učení. Cílem zpětnovazebního učení je naučit se takové chování agenta, které maximalizuje jeho celkovou odměnu, kterou získá z prostředí, pokud bude dané chování používat. Předpokládáme, že agent se vyskytuje v nějakém prostředí, jehož stav může pozorovat a ovlivňovat. Agent běží v cyklech, v každé iteraci $t$ pozoruje stav prostředí $s_t$, na základě pozorování provede akci $a_t$ a tím převede prostředí do nového stavu $s_{t+1}$. Za provedení akce dostane od prostředí odměnu $r_t$.

Jedním z typických ukázkových problémů pro zpětnovazební učení je Mountain Car. Jde o auto, které je v  údolí a snaží se z něj dostat ven, má ale slabý motor, takže přímo vyjet nemůže a musí se "rozhoupat". Stav je v tomto případě vektor dvou čísel udávajících polohu a rychlost auta. Auto může provádět tři akce - jet zrychlovat, zpomalovat, nebo nic. Pokud chceme, aby z údolí vyjelo co možná nejrychleji, dostává typicky odměnu -1 za každý krok v údolí a 0 v kroku, kdy vyjede.

## Markovské rozhodovací procesy

Prostředí můžeme formálně popsat jako markovský rozhodovací proces (MDP), který je zadaný čtveřicí $(S, A, P, R)$, kde $S$ je konečná množina stavů prostředí, $A$ je (konečná) množina akcí (případě může být nahrazena množinami $A_s$ akcí aplikovatelných ve stavu $s$), $P_a(s, s')$ je přechodová funkce, která udává pravděpodobnost, že aplikací akce $a$ ve stavu $s$ přejde prostředí do stavu $s'$ a $R_a(s, s')$ je funkce odměn, která udává okamžitou odměnu, kterou agent dostane od prostředí, pokud ve stavu $s$ provede akci $a$ a převede tím prostředí do stavu $s'$. U přechodové funkce je důležité, že splňuje tzv. markovskou podmínku, tj. že závisí pouze na aktuálním stavu $s$ a akci $a$ a nikoliv na akcích a stavech předcházejících. 

Chování agenta potom můžeme popsat pomocí strategie (policy) $\pi: S \times A \to [0,1]$, kde $\pi(s,a)$ udává pravděpodobnost provedení akce $a$ ve stavu $s$. Cílem zpětnovazebního učení je potom najít strategii $\pi$ takovou, že maximalizuje celkovou odměnu, kterou agent získá $\sum_{t=0}^\infty \gamma^tR_{a_t}(s_t, s_{t+1})$, kde $a_t = \pi(s_t)$ je akce provedená agentem v kroku $t$ a $\gamma < 1$ je diskontní faktor, který zajišťuje, že suma je konečná.

## Hodnota stavu a hodnota akce

Hodnota $V^\pi(s)$ stavu $s$ při použití strategie $\pi$ se dá definovat jako $V^\pi(s) = \mathrm{E}[R] = \mathrm{E}[\sum_{t=0}^\infty \gamma^t r_t|s_0 = s]$, kde $R$ značí celkovou získanou diskontovanou odměnu a $r_t$ značí odměnu obdrženou v čase $t$. Kromě hodnoty stavu se velmi často hodí uvažovat také hodnotu $Q^\pi(s, a)$ akce $a$ provedené ve stavu $s$ pokud budeme dále sledovat strategii $\pi$. Výhodou tohoto modelu je, že agent nepotřebuje mít model prostředí, který popisuje, jakým způsobem akce ovlivňují prostředí a učí se tento model za běhu.

Cílem agenta potom tedy je najít optimální strategii $\pi^\star$ takovou, že $V^{\pi^\star}(s) = \max_\pi V^\pi(s)$. Hodnotu stavů (akcí) pro optimální strategii budeme značit jako $V^\star (s)$ ($Q^\star(s, a)$).

## Strategie prohledávání

Hodnotu obou výše zmíněných funkcí může agent použít k tomu, aby vylepšil svojí strategii. Je třeba si uvědomit, že agent má relativně složitou úlohu - musí se snažit maximalizovat svůj celkový zisk $R$, k tomu se musí naučit vhodnou strategii, která ale zpětně ovlivňuje hodnoty stavů odhadovaných agentem. Agent by mohl sledovat takovou strategii, která vždy přejde do stavu, který slibuje největší užitek. Problém je, že agent se hodnoty jednotlivých stavů předem nezná a musí se je učit za běhu. Pokud tedy bude mít špatný (moc nízký) odhad hodnoty některého stavu, nemusí ho nikdy navštívit i přes to, že při použití jiné strategie by jeho hodnota byla o hodně lepší (například přes něj vede zkratka do cíle, kterou agent ještě neobjevil). Agent, který vždy vybírá nejlepší akci (hladový, nebo greedy, agent) tedy špatně prohledává prostředí a akce v něm dostupné. Výběr vhodné strategie pro učení je složitý problém, je potřeba vyvažovat prohledávání prostoru (exploraci) a využívání známého (exploataci). Jednou z populárních metod výběru akce ve zpětnovazebním učení je tzv. $\epsilon$-hladová ($\epsilon$-greedy) strategie. Ta s pravděpodobností $(1-\epsilon)$ vybere nejlepší akci a s pravděpodobností $\epsilon$ vybere akci náhodnou.  Tím kombinuje jak využívání naučených znalostí, tak prohledávání nových stavů. 

## Monte-Carlo metody 

Zpětnovazební učení si lze představit ve dvou krocích - zlepšení strategie a vyhodnocení strategie. Vyhodnocení strategie lze dělat pomocí Monte-Carlo metod, které počítají hodnoty funkce $Q^\pi(s,a)$. Provedeme ve stavu $s$ akci $a$ a potom začneme provádět strategii $\pi$, dokud se nedostaneme do nějakého cíle. Obdrženou odměnu potom zaznamenáme. Vylepšení strategie se potom dělá tak, že se spočítá nová (hladová) strategie na základě právě nových hodnot $Q(s,a)$. 

Takto popsaná metoda nefunguje moc dobře. Pokud jsou rozptyly odměn pro akce a stavy velké, může konvergovat velmi pomalu. Navíc v jednom běhu ohodnocení upravíme hodnotu pouze pro jednu dvojici stavu a akce, nelze ji tedy použít pro větší markovské rozhodovací procesy. 

## Q-učení 

Některé výše zmíněné problémy řeší tzv. temporal-difference (TD) metody. Ty jsou založen na tzv. Bellmanových rovnicích, které říkají, že $V^\pi(s)=E_{\pi}[r_0 + \gamma V^\pi(s_1)|s_0=s]$. Aktualizace hodnotové funkce se potom po každém kroku vyhodnocení strategie (každém kroku agenta) provede jako $ V(s) \leftarrow V(s) + \alpha(r + \gamma V(s') - V(s) )$, kde $r + \gamma V(s')$ je nová cílová hodnota pro $V(s)$. Výhodou oproti Monte Carlo metodám je, že se při jednom ohodnocení upraví hodnota více stavů. TD metody si můžeme představovat i tak, že se v nich informace o odměnách propaguje z cílových stavů (kde může být známa) do stavů předcházejících. Navíc tyto metody řeší problém rozdělení odměny v čase. Pokud agent dostane odměnu jen při dosažení cíle, TD metoda tuto odměnu rozdělí postupně mezi akce, které k tomuto cíli vedly.

Specifickým algoritmem založeným na TD metodách je Q-učení. To se přímo učí funkci $Q(s,a)$. V tradičních případech je $Q$ reprezentována jako matice, na začátku inicializovaná samými nulami. Potom v každém kroku agent postupně pozoruje stav $s_t,$ provede akci $a_t$, dostane odměnu $r_t$ a pozoruje nový stav $s_{t+1}$. Na základě těchto informací upraví matici $Q$ takto:

$$ Q^{new}(s_{t},a_{t}) \leftarrow (1-\alpha) \cdot Q(s_{t},a_{t}) + \alpha \cdot  \bigg( r_{t} + \gamma\cdot \max_{a}Q(s_{t+1}, a) \bigg), $$

kde $\alpha$ je parametr učení a akce $a_t$ může být vybírána libovolnou z metod zmíněných výše.

## SARSA

Algoritmus Q-učení je tzv. off-policy algoritmus, nezávisí totiž na žádné konkrétní strategii, kterou agent sleduje. Algoritmus SARSA je obdobný, výpočet $Q$ se ale provádí podle vztahu $$ Q(s_t,a_t) \leftarrow Q(s_t,a_t) + \alpha [r_{t} + \gamma Q(s_{t+1}, a_{t+1})-Q(s_t,a_t)],$$ kde akce $a_t$ a $a_{t+1}$ jsou založené na strategii používané agentem. 

## Problémy ve zpětnovazebním učení

Tradiční implementace Q-učení pomocí matice má ten problém, že funguje jen v diskrétních prostorech a s diskrétními akcemi. První omezení se dá obejít tím, že stavy diskretizujeme, např. v příkladu na Mountain Car můžeme hodnoty polohy a rychlosti rozdělit do intervalů a stav reprezentovat jen intervalem, místo konkrétní hodnoty. Podobně můžeme řešit i problém se spojitými akcemi. Dalším problémem je, že stavové prostory mohou být hodně velké, to potom vede k tomu, že matice jsou také velké a algoritmus se učí pomalu, nebo vůbec.

Později uvidíme i metody, které se učí strategii přímo jako mapování ze stavu na akci - takové se spojitými akcemi problém mít nemusí a typicky nemají problémy ani s velikostí stavu.

## Multi-agentní zpětnovazební učení

Zpětnovazební učení se dá použít i v případech, kdy je agentů více. Jedním z jednoduchých způsobů, jak algoritmy zobecnit je místo akce uvažovat $n$-tice akcí, v takovém případě ale složitost celého problému výrazně zvyšuje. Často používanou metodou je také tzv. self-learning, kde agent předpokládá, že ostatní agenti se chovají stejně jako on. Existují ale i metody založené na modelování chování ostatních agentů. 

Jedním z hlavních problémů zpětnovazebního učení s více agenty je to, jak určit, komu přiřadit jakou část odměny. Odměna od prostředí je totiž stále jen jedna. Jednou z možností je určit odměnu daného agenta tak, že se podíváme, jakou odměnu bychom dostali, kdyby tento agent nic nedělal a jakou jsme dostali díky jeho akci - rozdíl mezi těmito dvěma čísly je odměna pro tohoto agenta.