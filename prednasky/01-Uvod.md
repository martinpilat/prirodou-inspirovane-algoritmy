## Úvod a historie

Oblast umělé inteligence se dá zhruba rozdělit na dvě části - na symbolickou umělou inteligenci a na výpočetní umělou inteligenci. Symbolická umělá inteligence používá symbolický popis světa v nějakém formálním jazyce (např. logice) k řešení problémů např. z oblasti plánování a reprezentace znalostí. Oproti tomu výpočetní inteligence se zaměřuje na učení se chování z dostupných dat a pozorování. Přírodou inspirované algoritmy potom představují velkou část právě výpočetní inteligence.

Přírodou inspirované algoritmy obsahují širokou škálu technik, které v poslední době rychle získávají na popularitě v umělé inteligenci. Mezi nejznámější z nich patří umělé neuronové sítě a evoluční algoritmy. Především umělé neuronové sítě (v podobě tzv. hlubokého učení) dosahují dnes mnoha dobrých výsledků a překonávají tradiční metody v oblasti zpracování obrazu, zpětnovazebního učení, strojového překladu a dalších.

Neuronové sítě jsou inspirované fungováním nervové soustavy. Skládají se z jednoduchých výpočetních jednotek, tzv. neuronů, které jsou propojeny vahami. Při trénování neuronových sítí se právě tyto váhy upravují tak, aby výstupy sítě odpovídaly nějakým požadovaným výstupům. Evoluční algoritmy jsou zase optimalizační algoritmy inspirované Darwinistickou evolucí. Pracují s množinou (populací) kandidátů na řešení (jedinců). Běží v iteracích (generacích) a během každé generace aplikují genetické operátory (křížení a mutaci) na celou populaci. Jedinci, kteří představují kvalitnější řešení, mají větší šanci vytvořit nové potomky.

Zmíněné metody ale rozhodně nejsou nové. První experimenty s umělými neuronovými sítěmi pochází už ze 40. let. V roce 1959 Rosenblatt představuje perceptron, který se později stává základem moderních neuronových sítí. Vývoj neuronových sítí byl ale v 70. a 80. letech poznamenán nedůvěrou v jejich schopnosti, která vycházela především z knihy Perceptrons od Marvina Minského a Seymoura Paperta. Další rozvoj neuronových sítí potom přichází až ve druhé polovině 80. let po (znovu)objevení algoritmu zpětného šíření (backpropagation), který se dodnes používá k trénování neuronových sítí. V současnosti se různé architektury (hlubokých) neuronových sítí objevují v mnoha oblastech strojového učení a dávají nejlepší známé výsledky.

Myšlenka evolučních algoritmů také není nová. Jedny z prvních evolučních strategií (optimalizačních algoritmů pro spojitou optimalizaci, které se vyznačují tím, že automaticky adaptují svoje parametry) pochází už z konce 70. let. Genetický algoritmus jako takový potom z cca poloviny let 80. Dnes se evoluční algoritmy používají kromě samotné optimalizace, např. i k návrhu elektronických obvodů, nebo pro trénování neuronových sítí ve zpětnovazebním učení.

## Strojové učení a optimalizace 

Hlavními oblastmi aplikace přírodou inspirovaný algoritmů jsou strojové učení a optimalizace. Ve skutečnosti, jak uvidíme, mají tyto oblasti mnoho společného, neboť cílem strojového učení je typicky nastavení parametrů nějakého modelu tak, aby co nejlépe odpovídal dostupným datům. Oblast optimalizace je ale o něco obecnější.

Celá oblast strojového učení se dá rozdělit do třech oblastí:

1. V **učení s učitelem** jsou zadané objekty a k nim příslušné výstupy. Cílem je najít model, který, pokud je mu zadaný nějaký objekt, správně přiřadí správný výstup. Výstupy mohou být dvou typů, buď kategorické, nebo číselné. V prvním případě je cílem přiřadit objekt do správné kategorie (např. rozhodnout, jestli je na obrázku pes, nebo kočka) a problém se nazývá klasifikace. Ve druhém případě je cílem na základě vstupních dat předpovědět číselnou hodnotu (např. cenu nemovitosti na základě informací o ní). Takový problém se nazývá regrese.
2. V **učení bez učitele** jsou zadaná pouze objekty, bez požadovaných výstupů. Cílem typicky je např. rozdělit objekty do skupin obsahujících podobné objekty (shlukování), nebo se naučit, jak vstupní objekty vypadají, a generovat nové objekty (generativní modely).
3. Ve **zpětnovazebním učení** je cílem naučit se chování nějakého agenta tak, aby co nejlépe řešil zadaný problém na základě zpětné vazby od prostředí, ve kterém se pohybuje. Můžeme si to představit třeba tak, že se snažíme naučit se novou hru tím, že zkoušíme provádět různé akce a díváme se, jak ovlivňují skóre.

## Aplikace a výsledky

Přírodou inspirované metody dosáhly v posledních letech mnoha zajímavých výsledků. V oblasti evolučních algoritmů jsou každý rok vyhlašovány [Humies awards][1] za výsledky získané pomocí evolučních algoritmů, které mohou svou kvalitou soutěžit s výsledky získanými člověkem. Jedním z pěkných výsledků je také [návrh antény][2] získaný pomocí genetického programování, která byla použita při testovací misi NASA. Evoluční algoritmy se také dají použít k evoluci neuronových sítí, např. pro vytvoření [umělé inteligence pro hru Mario][3].

Neuronové sítě a dnes především hluboké neuronové sítě dosahují velmi dobrých výsledků např. při klasifikaci a zpracování obrazu. Pěkný výsledek je např. [automatické vytváření popisků k obrázkům][4]. Hluboké neuronové sítě ale také dosahují velmi dobrých výsledků ve zpětnovazebním učení a jsou schopny porazit lidské hráče v mnoha hrách, např. v [Go][5], [Starcraftu][6], nebo mnoha [Atari hrách][7]. 

 [1]: http://www.human-competitive.org/awards
 [2]: https://en.wikipedia.org/wiki/Evolved_antenna
 [3]: https://www.youtube.com/watch?v=qv6UVOQ0F44
 [4]: https://cs.stanford.edu/people/karpathy/deepimagesent/
 [5]: https://deepmind.com/research/alphago/
 [6]: https://deepmind.com/blog/alphastar-mastering-real-time-strategy-game-starcraft-ii/
 [7]: https://deepmind.com/research/publications/playing-atari-deep-reinforcement-learning/