define hector = Character(("Hector"), color="#FFFFFF")
define elsa = Character(("Elsa"), color="#FFFFFF")
define xu = Character(("Xu"), color="#FFFFFF")
define guardas = Character(("Guardas"), color="#FFFFFF")

label start:

    play music "audio/musicaGame.mp3"
    scene telapreta
    show text "Nossa história começa no século XV em uma cidade ao norte de Zarandi chamada Dowblin, onde morava um ferreiro conhecido como Hector que fabricava armas e armaduras para a guarda real. Dowblin e Zarandi se localizavam em uma ilha próximo ao Oriente Médio, eram dominadas por cachorros e não recebiam invasões há muito tempo, por serem consideradas impenetráveis." at truecenter
    with Dissolve(2.0)
    pause
    hide text
    with Dissolve(2.0)
    show text "O maior sonho de Hector era se tornar um cavaleiro e proteger o rei, porém, pelo seu tamanho relativamente pequeno e seu jeito atrapalhado, nunca era convocado para se tornar um. Mesmo não sendo convocado Hector treinava dia e noite, esperando que um dia o seu sonho se tornasse realidade." at truecenter
    with Dissolve(2.0)
    pause
    hide text
    with Dissolve(2.0)
    show text "Draxon Malavak, o Capitão de uma organização de piratas gatos chamada Sea Cats, que saqueavam e dominavam todas as cidades que passavam, recolhendo ouro e tornando todos escravos tomou as cidades de Zarandi e Dowblin, tornando todos prisioneiros." at truecenter
    with Dissolve(2.0)
    pause
    hide text
    with Dissolve(2.0)
    show text "10 Anos depois..." at truecenter
    with Dissolve(2.0)
    pause
    hide text
    with Dissolve(2.0)

    scene cutscene01
    "Hector depois de muitos anos na prisão, não suportava mais os odores e gritos dos seus amigos que foram feitos prisioneiros."
    scene cutscene02
    with Dissolve(2.0)
    "Os dias passavam e uma pequena arvore crescia atrás de onde Hector era feito prisioneiro."
    scene cutscene03
    with Dissolve(2.0)
    "Depois de varios dias analisando os movimentos do carcereiro, Hector percebeu que ele sempre se ausentava próximo ao pôr do sol."
    scene cutscene04
    with Dissolve(2.0)
    "Essa seria a hora perfeita para armar uma fuga, então Hector pegou um galho da arvore e esticou o seu braço para alcançar a chave que ficava na mesa em frente a sua cela."
    scene cutscene05
    with Dissolve(2.0)
    "O coração de Hector acelerado dificultava pegar a chave com o galho. A qualquer momento o carcereiro poderia chegar e perder para sempre a sua possibilide de fuga."
    scene cutscene06
    with Dissolve(2.0)
    "Assim que conseguiu pegar a chave, Hector rapidamente puxou ela para dentro da cela e escondeu o galho embaixo de sua cama."
    scene cutscene07
    with Dissolve(2.0)
    "Hector abriu a sua cela e ficou de cara para as celas de dois de seus amigos que moravam no mesmo vilarejo que ele."
    scene cutscene08
    with Dissolve(2.0)
    scene salvarpersonagem
    show expression "hector.png"
    hector "Preciso fazer uma decisão rápida, quem salvarei?"

    $ vidas = 3
    $ armadura = ""
    $ machado = ""
    $ lanca = ""
    $ sangue = ""

    call screen salvarPersonagem

    if _return == "xu":
        $ personagem = xu
        $ posicao = left
        $ imagemPersonagem = "xu"
        jump salvarXu

    if _return == "sozinho":
        $ personagem = ""
        $ posicao = right
        $ imagemPersonagem = "sozinho"
        jump continuarSozinho

    if _return == "elsa":
        $ personagem = elsa
        $ posicao = right
        $ imagemPersonagem = "elsa"
        $ vidas = 4
        jump salvarElsa

screen salvarPersonagem:
    imagemap:
        ground "salvarPersonagem.png"
        hover "salvarPersonagemE.png"
        hotspot(75,156,358,366) action Return("xu")
        hotspot(462,156,358,366) action Return("sozinho")
        hotspot(851,156,358,366) action Return("elsa")

label salvarXu:
    scene resgate
    show expression "vidas"+str(vidas)+".png"
    show expression "hector.png"
    show expression "xuA.png" at posicao
    personagem "Olá Hector, meu nome é Xu, obrigado por me salvar."
    hector "Vamos, Vamos, precisamos sair daqui rápido, a qualquer momento o carcereiro pode chegar."
    scene portaxu
    with Dissolve(2.0)
    show expression "vidas"+str(vidas)+".png"
    show expression "hector.png"
    show expression "xuA.png" at posicao
    personagem "Só vou pegar meu arco e flecha."
    hector "Para onde vamos, pela esquerda ou direita?"

    call screen escolherPortaXu

    if _return == "esquerda":
        jump ladoEsquerdo

    if _return == "direita":
        jump ladoDireitoXu

screen escolherPortaXu:
    imagemap:
        ground "portaXu.png"
        hover "portaXuE.png"
        hotspot(308,254,210,396) action Return("esquerda")
        hotspot(757,254,210,396) action Return("direita")

label continuarSozinho:
    scene portasozinho
    show expression "vidas"+str(vidas)+".png"
    show expression "hector.png"
    "Essa prisão é enorme, para onde irei?"

    call screen escolherPortaSozinho

    if _return == "esquerda":
        jump ladoEsquerdo

    if _return == "direita":
        jump ladoDireito

screen escolherPortaSozinho:
    imagemap:
        ground "portaSozinho.png"
        hover "portaSozinhoE.png"
        hotspot(308,254,210,396) action Return("esquerda")
        hotspot(757,254,210,396) action Return("direita")

label salvarElsa:
    scene resgate
    show expression "vidas"+str(vidas)+".png"
    show expression "hector.png"
    show expression "elsaA.png" at posicao
    personagem "Olá Hector, meu nome é Elsa, obrigado por me salvar."
    hector "Olá Elsa, o carcereiro já está a muito tempo sem ser visto, precisamos nos apressar."
    "Hector ganha uma companheira e também um ponto de vida."
    scene portaelsa
    with Dissolve(2.0)
    show expression "vidas"+str(vidas)+".png"
    show expression "hector.png"
    show expression "elsaA.png" at posicao
    personagem "Tudo bem, só vou pegar meu jaleco."
    hector "Para onde vamos, pela esquerda ou direita?"

    call screen escolherPortaElsa

    if _return == "esquerda":
        jump ladoEsquerdoElsa

    if _return == "direita":
        jump ladoDireito

screen escolherPortaElsa:
    imagemap:
        ground "portaElsa.png"
        hover "portaElsaE.png"
        hotspot(308,254,210,396) action Return("esquerda")
        hotspot(757,254,210,396) action Return("direita")

label ladoEsquerdo:
    scene guarda01
    show expression "vidas"+str(vidas)+".png"
    show expression "hector.png"
    show expression imagemPersonagem+".png" at posicao
    if imagemPersonagem == "xu":
        scene telapreta
        with Dissolve(2.0)
        play sound "audio/espada.mp3"
        "Quando Hector e Xu entram na porta, se deparam com um dos guardas do castelo, porém Xu com apenas uma flechada mata o guarda."
        play sound "audio/espada.mp3"
    else:
        scene telapreta
        with Dissolve(2.0)
        play sound "audio/espada.mp3"
        "Hector entra sozinho na porta e se depara com um guarda armado."
        "Mesmo sem armas Hector mata o guarda porém lhe custa uma vida."
        play sound "audio/espada.mp3"
    if personagem != xu:
        $ vidas = vidas - 1
    scene guarda01m
    with Dissolve(2.0)
    $ sangue = "S"
    show expression "vidas"+str(vidas)+".png"
    show expression "hector" + armadura + lanca + machado + sangue + ".png"
    show expression imagemPersonagem + sangue + ".png" at posicao
    hector "Temos que ir para sairmos logo dessa prisão e completarmos nossa missão."
    jump escolherPortas

label ladoDireito:
    scene armadilhas01
    show expression "hector.png"
    show expression "vidas"+str(vidas)+".png"
    show expression imagemPersonagem at posicao
    if imagemPersonagem == "elsa":
        elsa "Uma sala vazia, vamos Hector não aguento mais esse lugar."
        hector "Cuidado Elsa, essa sala possui armadilhas letais."
    else:
        hector "Uma sala vazia, certamente existe alguma coisa escondida."
    scene armadilhas02
    with Dissolve(0.2)
    scene armadilhas03
    with Dissolve(0.2)
    scene armadilhas04
    with Dissolve(0.2)
    scene armadilhas05
    with Dissolve(0.2)
    scene armadilhas06
    with Dissolve(0.2)
    scene armadilhas07
    with Dissolve(0.2)
    scene armadilhas08
    with Dissolve(0.2)
    scene armadilhas09
    with Dissolve(0.2)
    show expression "hector.png"
    show expression "vidas"+str(vidas)+".png"
    show expression imagemPersonagem at posicao
    "Hector usa uma pedra para desarmar as armadilhas e seguir em frente."
    jump escolherPortas

label ladoEsquerdoElsa:
    scene resgate
    show expression "vidas"+str(vidas)+".png"
    show expression "hector.png"
    show expression "elsaA.png" at posicao
    hector "Não foi uma boa escolha essa porta"
    personagem "Agora não sairemos mais da prisão, por sua causa."
    jump gameOver

label ladoDireitoXu:
    scene resgate
    show expression "vidas"+str(vidas)+".png"
    show expression "hector.png"
    show expression "xuA.png" at posicao
    hector "Não foi uma boa escolha essa porta"
    personagem "É voltamos para a prisão"
    jump gameOver

label escolherPortas:
    scene portas
    show expression "vidas"+str(vidas)+".png"
    show expression "hector" + armadura + lanca + machado + sangue + ".png"
    show expression imagemPersonagem + sangue + ".png" at posicao
    if imagemPersonagem == "xu":
        hector "Precisamos escolher entre esses três caminhos."
        xu "O caminho mais longe deve ser o mais fácil, mas irei com você onde quer que vá."
    elif imagemPersonagem == "elsa":
        hector "Precisamos escolher entre esses três caminhos."
        elsa "Eu escolheria o curto, não aguento mais tantas coisas que podem nos matar."
    else:
        hector "Preciso escolher com sabedoria, um passo infalso posso morrer."

    call screen escolherPortas

    if _return == "primeiraPorta":
        jump primeiraPorta

    if _return == "segundaPorta":
        jump segundaPorta

    if _return == "terceiraPorta":
        jump terceiraPorta

screen escolherPortas:
    imagemap:
        ground "portas.png"
        hover "portasE.png"
        hotspot(230,253,211,394) action Return("primeiraPorta")
        hotspot(531,253,211,394) action Return("segundaPorta")
        hotspot(836,253,211,394) action Return("terceiraPorta")

screen escolherPortasMar:
    imagemap:
        ground "portasMar.png"
        hover "portasE.png"
        hotspot(230,253,211,394) action Return("primeiraPorta")
        hotspot(531,253,211,394) action Return("segundaPorta")
        hotspot(836,253,211,394) action Return("terceiraPorta")

screen escolherPortasFloresta:
    imagemap:
        ground "portasFloresta.png"
        hover "portasE.png"
        hotspot(230,253,211,394) action Return("primeiraPorta")
        hotspot(531,253,211,394) action Return("segundaPorta")
        hotspot(836,253,211,394) action Return("terceiraPorta")

screen escolherPortasDeserto:
    imagemap:
        ground "portasDeserto.png"
        hover "portasE.png"
        hotspot(230,253,211,394) action Return("primeiraPorta")
        hotspot(531,253,211,394) action Return("segundaPorta")
        hotspot(836,253,211,394) action Return("terceiraPorta")

label primeiraPorta:
    scene armadilhas09
    show expression "vidas"+str(vidas)+".png"
    show expression "hector" + armadura + lanca + machado + sangue + ".png"
    show expression imagemPersonagem + sangue + ".png" at posicao
    if imagemPersonagem == "xu":
        hector "Vamos Xu, temos que sair daqui."
        xu "Cuidado com as armadilhas Hector."
    elif imagemPersonagem == "elsa":
        hector "Cuidado Elsa, temos que ter cuidado com possíveis armadilhas."
    else:
        hector "Essa sala está muito calma."
    scene armadilhas08
    with Dissolve(0.2)
    scene armadilhas07
    with Dissolve(0.2)
    scene armadilhas06
    with Dissolve(0.2)
    scene armadilhas05
    with Dissolve(0.2)
    scene armadilhas04
    with Dissolve(0.2)
    scene armadilhas03
    with Dissolve(0.2)
    scene armadilhas02
    with Dissolve(0.2)
    scene armadilhas01
    with Dissolve(0.2)
    show expression "vidas"+str(vidas)+".png"
    show expression "hector" + armadura + lanca + machado + sangue + ".png"
    show expression imagemPersonagem + sangue + ".png" at posicao
    if imagemPersonagem == "xu":
        "Xu usa seu arco e flecha para desarmar as armadilhas."
        xu "Agora com elas desarmadas podemos ir para nossa missão."
    elif imagemPersonagem == "elsa":
        hector "Precisamos tomar mais cuidado, não podemos morrer antes de salvarmos Dowblin e Zarandi."
    else:
        hector "Preciso tomar cuidado, não posso morrer antes de salvar o rei."
    scene guarda02
    show expression "vidas"+str(vidas)+".png"
    show expression "hector" + armadura + lanca + machado + sangue + ".png"
    show expression imagemPersonagem + sangue + ".png" at posicao
    if imagemPersonagem == "xu":
        hector "E eu imaginando que esse seria o caminho mais fácil."
        xu "Eu pego o da direita e você o da esquerda"
    elif imagemPersonagem == "elsa":
        elsa "Ai meu Deus, eu não quero morrer hoje."
    else:
        hector "Venham, vingarei todos que vocês torturaram."
    scene telapreta
    play sound "audio/espada.mp3"
    "E o som das espadas mostrava a difícil batalha."
    play sound "audio/espada.mp3"

    if armadura != "A":
        $ vidas = vidas - 1
        if vidas == 0:
            scene guarda02
            show morto
            show expression imagemPersonagem + "M.png" at posicao
            "Acabou as suas vidas, você perdeu."
            jump gameOver

    scene guarda02m
    with Dissolve(2.0)
    $ sangue = "S"
    show expression "vidas"+str(vidas)+".png"
    show expression "hector" + armadura + lanca + machado + sangue + ".png"
    show expression imagemPersonagem + sangue + ".png" at posicao
    if imagemPersonagem == "xu":
        hector "Draxon Malavak, o próximo será você."
    elif imagemPersonagem == "elsa":
        elsa "Dessa nós escapamos."
    else:
        hector "Que venham mais, preciso acabar com todos."

    scene portasecreta

    if imagemPersonagem == "xu":
        hector "Precisamos fazer uma escolha, qual porta seguiremos?"
        xu "Acredito que o difícil será o mais fácil."
    elif imagemPersonagem == "elsa":
        hector "Precisamos fazer uma escolha, qual porta seguiremos?"
        elsa "Vamos pelo mais fácil, eu não sou um gato para ter sete vidas."
    else:
        hector "Precisamos fazer uma escolha, qual porta seguiremos?"

    call screen portaSecreta

    if _return == "facil":
        jump facil

    if _return ==  "dificil":
        jump dificil

    if _return == "passagemSecreta":
        jump passagemSecreta

screen portaSecreta:
    imagemap:
        ground "portaSecreta.png"
        hover "portaSecretaE.png"
        hotspot(512,248,216,400) action Return("facil")
        hotspot(774,248,216,400) action Return ("dificil")
        hotspot(289,311,93,98) action Return("passagemSecreta")

label facil:
    scene salamachado
    show expression "vidas"+str(vidas)+".png"
    show expression "hector" + armadura + lanca + machado + sangue + ".png"
    show expression imagemPersonagem + sangue + ".png" at posicao
    if imagemPersonagem == "xu":
        hector "Um machado, facilitará a nossa fuga."
        xu "Agora podemos matar os guardas mais rápido."
    elif imagemPersonagem == "elsa":
        hector "Uma machado, isso me ajudará a lutar."
        elsa "Você pode ficar com seu machado, eu só quero o ouro."
    else:
        hector "Preciso ter cuidado, mesmo com esse machado ainda sou uma presa fácil."
    $ machado = "M"
    jump decisaoMar

label dificil:
    scene guarda04
    show expression "vidas"+str(vidas)+".png"
    show expression "hector" + armadura + lanca + machado + sangue + ".png"
    show expression imagemPersonagem + sangue + ".png" at posicao
    if imagemPersonagem == "xu":
        hector "Quatro guardas, teremos que lutar com a cabeça."
        xu "Espere eles virem para nós atacarmos."
    elif imagemPersonagem == "elsa":
        hector "Cuidado Elsa, fique atrás de mim."
        elsa "Ai meu Deus, todos esses esqueletos, não quero morrer hoje."
    else:
        hector "Que venham todos, não será hoje que morrerei."
    scene telapreta
    play sound "audio/espada.mp3"
    "E o som das espadas mostrava a difícil batalha."
    play sound "audio/espada.mp3"
    if armadura != "A":
        $ vidas = vidas - 1
        if vidas == 0:
            scene guarda02
            show morto
            show expression imagemPersonagem + "M.png" at posicao
            "Acabou as suas vidas, você perdeu."
            jump gameOver
    scene guarda04m
    with Dissolve(2.0)
    $ sangue = "S"
    show expression "vidas"+str(vidas)+".png"
    show expression "hector" + armadura + lanca + machado + sangue + ".png"
    show expression imagemPersonagem + sangue + ".png" at posicao
    "Depois de matar todos os guardas, Hector partiu para achar a saída daquele lugar."
    jump decisaoMar

label passagemSecreta:
    scene salaarmadura
    show expression "vidas"+str(vidas)+".png"
    show expression "hector" + armadura + lanca + machado + sangue + ".png"
    show expression imagemPersonagem + sangue + ".png" at posicao
    if imagemPersonagem == "xu":
        hector "Minha armadura, agora estou invulnerável."
        xu "Agora nem Draxon Malavak nos imperirá de salvar nossa cidade."
    elif imagemPersonagem == "elsa":
        hector "Minha armadura, agora estou invulnerável."
    else:
        hector "Minha armadura, agora estou invulnerável."
    $ armadura = "A"
    jump decisaoMar

label decisaoMar:
    scene portasmar
    show expression "vidas"+str(vidas)+".png"
    show expression "hector" + armadura + lanca + machado + sangue + ".png"
    show expression imagemPersonagem + sangue + ".png" at posicao
    if imagemPersonagem == "xu":
        hector "Chegamos na saída, podemos salvar nossas cidades."
        xu "Parece que estou ouvindo gaivotas, será que estamos na praia?"
    elif imagemPersonagem == "elsa":
        hector "Chegamos na saída, podemos salvar nossas cidades."
        elsa "Parece que estou ouvindo gaivotas, será que estamos na praia?"
    else:
        hector "Parece que estou ouvindo gaivotas, será que estamos na praia?"

    call screen escolherPortasMar

    if _return == "primeiraPorta":
        jump fimMar

    if _return == "segundaPorta":
        jump terceiraPorta

    if _return == "terceiraPorta":
        jump segundaPorta

label segundaPorta:
    scene salalanca
    show expression "vidas"+str(vidas)+".png"
    show expression "hector" + armadura + lanca + machado + sangue + ".png"
    show expression imagemPersonagem + sangue + ".png" at posicao
    if imagemPersonagem == "xu":
        hector "Uma lança, facilitará a nossa fuga."
        xu "Agora podemos matar os guardas mais rápido."
    elif imagemPersonagem == "elsa":
        hector "Uma lança, facilitará a nossa fuga."
        elsa "Você pode ficar com sua lança, eu só quero um colar de ouro."
    else:
        hector "Preciso ter cuidado, mesmo com essa lança ainda sou um alvo fácil."
    $ lanca = "L"
    scene guarda03
    show expression "vidas"+str(vidas)+".png"
    show expression "hector" + armadura + lanca + machado + sangue + ".png"
    show expression imagemPersonagem + sangue + ".png" at posicao
    if imagemPersonagem == "xu":
        hector "Três guardas, acho que daremos conta."
        xu "Venham todos, estou com sede de sangue."
    elif imagemPersonagem == "elsa":
        hector "Cuidado Elsa, fique atrás de mim."
        elsa "Ai meu Deus, estamos tão perto de sair, não podemos morrer agora."
    else:
        hector "Venham todos, estou com sede de sangue."
    scene telapreta
    scene telapreta
    play sound "audio/espada.mp3"
    "E o som das espadas mostrava a difícil batalha."
    play sound "audio/espada.mp3"

    if armadura != "A":
        $ vidas = vidas - 1
        if vidas == 0:
            scene guarda04
            show morto
            show expression imagemPersonagem + "M.png" at posicao
            "Acabou as suas vidas, você perdeu."
            jump gameOver

    scene guarda03m
    with Dissolve(2.0)
    show expression "vidas"+str(vidas)+".png"
    show expression "hector" + armadura + lanca + machado + sangue + ".png"
    show expression imagemPersonagem + sangue + ".png" at posicao
    "Depois de matar todos os guardas, Hector pegou a chave com um dos guardas e saiu pela porta."

    scene portasmar
    show expression "vidas"+str(vidas)+".png"
    show expression "hector" + armadura + lanca + machado + sangue + ".png"
    show expression imagemPersonagem + sangue + ".png" at posicao
    if imagemPersonagem == "xu":
        hector "Chegamos na saída, podemos salvar nossas cidades."
        xu "Consigo até ouvir o canto dos pássaros, e o som das árvores."
    elif imagemPersonagem == "elsa":
        hector "Chegamos na saída, podemos salvar nossas cidades."
        elsa "Consigo até ouvir o canto dos pássaros, e o som das árvores."
    else:
        hector "Consigo até ouvir o canto dos pássaros, e o som das árvores."

    call screen escolherPortasFloresta

    if _return == "primeiraPorta":
        jump terceiraPorta

    if _return == "segundaPorta":
        jump primeiraPorta

    if _return == "terceiraPorta":
        jump fimFloresta

label terceiraPorta:
    scene guarda04
    show expression "vidas"+str(vidas)+".png"
    show expression "hector" + armadura + lanca + machado + sangue + ".png"
    show expression imagemPersonagem + sangue + ".png" at posicao
    if imagemPersonagem == "xu":
        hector "Quatro guardas, teremos que lutar com a cabeça."
        xu "Espere eles virem para nós atacarmos."
    elif imagemPersonagem == "elsa":
        hector "Cuidado Elsa, fique atrás de mim."
        elsa "Ai meu Deus, todos esses esqueletos, não quero morrer hoje."
    else:
        hector "Que venham todos, não será hoje que morrerei."
    scene telapreta
    play sound "audio/espada.mp3"
    "E o som das espadas mostrava a difícil batalha."
    play sound "audio/espada.mp3"

    if armadura != "A":
        $ vidas = vidas - 1
        if vidas == 0:
            scene guarda03
            show morto
            show expression imagemPersonagem + "M.png" at posicao
            "Acabou as suas vidas, você perdeu."
            jump gameOver

    scene guarda04m
    with Dissolve(2.0)
    show expression "vidas"+str(vidas)+".png"
    show expression "hector" + armadura + lanca + machado + sangue + ".png"
    show expression imagemPersonagem + sangue + ".png" at posicao
    "Hector estava mais próximo do seu objetivo."

    scene portasdeserto
    show expression "vidas"+str(vidas)+".png"
    show expression "hector" + armadura + lanca + machado + sangue + ".png"
    show expression imagemPersonagem + sangue + ".png" at posicao
    if imagemPersonagem == "xu":
        hector "Chegamos na saída, podemos salvar nossas cidades."
        xu "Que vento seco, está muito calor aqui."
    elif imagemPersonagem == "elsa":
        hector "Chegamos na saída, podemos salvar nossas cidades."
        elsa "Que vento seco, está muito calor aqui."
    else:
        hector "Que vento seco, está muito calor aqui."

    call screen escolherPortasDeserto

    if _return == "primeiraPorta":
        jump segundaPorta

    if _return == "segundaPorta":
        jump primeiraPorta

    if _return == "terceiraPorta":
        jump fimDeserto

label fimMar:
    scene mar
    play music "audio/mar.mp3"
    pause 1.0
    if imagemPersonagem == "xu":
        show expression "hector" + armadura + lanca + machado + sangue + ".png"
        show expression imagemPersonagem + sangue + ".png" at posicao
        "Hector e Xu chegam na praia, ouvem os cantos das gaivotas e la no horizonte se deparam com alguma coisa se aproximando."
        "Eles não se importam muito com o que está vindo, só querem aproveitar a maresia que já não sentiam a um bom tempo."
        hector "Fazia tempo que não sentia um vento, preciso logo tomar um banho na praia."
        personagem "Temos que tomar cuidado, as coisas estão muito calmas por aqui."
        scene marguardas
        show expression "hector" + armadura + lanca + machado + sangue + ".png"
        show expression imagemPersonagem + sangue + ".png" at posicao
        "A coisa coisa que estava la no horizonte, começou a se aproximar. Hector e Xu perceberam que era um navio, mas não um navio qualquer e sim um navio de Draxon Malavak."
        hector "Xu, o navio é de Malavak, precisamos acabar com eles."
        scene telapreta
        play sound "audio/espada.mp3"
        "E o som das espadas mostrava a difícil batalha."
        play sound "audio/espada.mp3"
        if armadura == "A":
            scene marguardasm
            with Dissolve(2.0)
            show expression "hector" + armadura + lanca + machado + sangue + ".png"
            show expression imagemPersonagem + sangue + ".png" at posicao
            hector "Conseguimos destruir o navio de Malavak, temos que resgatar nossos amigos e voltar para conquistar nossa ilha novamente."
            scene telapreta
            with Dissolve(2.0)
            show text "O tempo passou, Hector e Xu conquistaram toda a prisão e resgataram os moradores de Dowblin e Zarandi, Draxon Malavak foi mantido refém na prisão que ele mesmo construiu." at truecenter
            with Dissolve(2.0)
            hide text
            with Dissolve(2.0)
            pause
            jump vitoria
        else:
            scene marguardasm
            with Dissolve(2.0)
            show expression "morto.png"
            show expression imagemPersonagem + sangue + ".png" at posicao
            "Hector e Xu conseguiram derrotar o navio de Draxon Malavak, porém uma flecha atinge as costas de Hector."
            "Ferido gravemente Hector pede nas suas ultimas palavras para salvar o rei e resgatar as cidades de Dowblin e Zarandi."
            scene telapreta
            with Dissolve(2.0)
            show text "50 anos após o resgate da ilha e a morte de Hector, os jovens ainda ouvem a história de coragem e se espelham nele para defender o rei." at truecenter
            with Dissolve(2.0)
            hide text
            with Dissolve(2.0)
            pause
            jump gameOver
    elif imagemPersonagem == "elsa":
        show expression "hector" + armadura + lanca + machado + sangue + ".png"
        show expression imagemPersonagem + sangue + "ArcoIris.png" at posicao
        "Hector e Elsa chegam na praia, os ventos estão fortes e a brisa do mar cria para eles uma sensação de liberdade que a muitos anos não sentiam."
        "Elsa muito emocionada começa a chorar, as lagrimas no vento criam um arco-íris nunca visto antes por Hector."
        hector "Elsa, veja que bonito o arco-íris criado pelas suas lágrimas."
        scene marguardas
        show expression "hector" + armadura + lanca + machado + sangue + ".png"
        show expression imagemPersonagem + sangue + ".png" at posicao
        "Desatentos com a situação, Hector e Elsa nem percebem que o navio de Draxon Malavak se aproximava."
        personagem "Cuidado Hector, são os guardas de Malavak."
        "Hector com a sede de vingança para destruir Malavak, parte para uma batalha contra tudo e contra todos."
        scene telapreta
        with Dissolve(2.0)
        play sound "audio/espada.mp3"
        "E o som das espadas mostrava a difícil batalha."
        play sound "audio/espada.mp3"
        if armadura ==  "A":
            scene marguardasm
            with Dissolve(2.0)
            show expression "hector" + armadura + lanca + machado + sangue + ".png"
            show expression imagemPersonagem + sangue + ".png" at posicao
            "Hector consegue destruir o navio de Draxon Malavak, e com Elsa parte para o resgate de seus outros amigos."
            hector "Elsa, precisamos resgatar o rei e salvar nossas cidades, preciso que seja forte e me medique sempre que eu precise."
            if lanca == "L":
                scene telapreta
                with Dissolve(2.0)
                show text "Hector e Elsa passaram semanas próximo a praia, antes do resgate da ilha, Hector saia para pescar com sua lança, enquanto Elsa cuidava do fogo para assar o peixe." at truecenter
                with Dissolve(2.0)
                pause
                hide text
                with Dissolve(2.0)
                show text "O tempo passou e Hector e Elsa se casam na cidade de Dowblin, 10 anos depois do resgate do rei, hoje Hector possui 2 filhos e 1 filha com Elsa e gerencia todos os cavaleiros do rei." at truecenter
                with Dissolve(2.0)
                pause
                hide text
                with Dissolve(2.0)
                jump vitoria
            else:
                scene telapreta
                with Dissolve(2.0)
                show text "A noite chegou e a procura de comida ficou difícil, Hector tentou pescar, porém, a sua espada era muito pesada e os peixes fugiam." at truecenter
                with Dissolve(2.0)
                pause
                hide text
                with Dissolve(2.0)
                show text "Varios dias sem comer, Hector e Elsa morrem de fome." at truecenter
                with Dissolve(2.0)
                pause
                hide text
                with Dissolve(2.0)
                jump gameover
        else:
            scene marguardas
            with Dissolve(2.0)
            show expression "morto.png"
            "Hector sem armas para se defender, tenta lutar contra todo o navio, porém, com uma espada em suas costas um dos guardas mata Hector."
            "Elsa aos prantos, não consegue sair de perto do corpo de Hector. Um dos guardas leva ela a força para a mesma cela de onde ela saiu."
            jump gameOver
    else:
        show expression "hector" + armadura + lanca + machado + sangue + ".png"
        "Hector, ouvindo os cantos das gaivotas e olha para o horizonte se deparam com alguma coisa se aproximando."
        "Depois de ter visto tantas barbaridades, Hector imagina que aquilo que se aproxima possa ser um navio de Draxon Malavak."
        hector "Preciso me preparar para qualquer coisa que possa acontecer."
        scene marguardas
        with Dissolve(2.0)
        show expression "hector" + armadura + lanca + machado + sangue + ".png"
        hector "Draxon Malavak, eu estava esperando você, venha e lute comigo, pela liberdade da minha ilha."
        scene telapreta
        with Dissolve(2.0)
        play sound "audio/espada.mp3"
        "E o som das espadas mostrava a difícil batalha."
        play sound "audio/espada.mp3"
        if armadura ==  "A":
            scene marguardasm
            with Dissolve(2.0)
            show expression "hector" + armadura + lanca + machado + sangue + ".png"
            "Sem piedade Hector mata todos do navio e o afunda."
            hector "Preciso agora salvar o rei e a cidades que foram tomadas, ainda tenho um grande caminho pela frente."
            if lanca == "L":
                scene telapreta
                with Dissolve(2.0)
                show text "Os dias passaram e Hector sobrevivia pescando, até que meses depois a cidade de Dowblin e Zarandi foram resgatadas por Hector e o exército que ele tinha formado." at truecenter
                with Dissolve(2.0)
                pause
                hide text
                with Dissolve(2.0)
                jump vitoria
            else:
                scene telapreta
                with Dissolve(2.0)
                show expression "Após a morte de Malavak, Hector se perdeu na região onde foi preso, próximo a costa, sem uma lança para pescar ficou dias e dias sem poder se alimentar." at truecenter
                with Dissolve(2.0)
                pause
                hide text
                with Dissolve(2.0)
                show expression "Hector morre de fome e até hoje ninguém sabe o paradeiro do seu corpo." at truecenter
                with Dissolve(2.0)
                pause
                hide text
                with Dissolve(2.0)
                jump gameOver
        else:
            scene marguardas
            with Dissolve(2.0)
            show expression "morto.png"
            "Com muita coragem, Hector parte para cima de varios guardas no navio, porém, antes mesmo de chegar próximo, Hector toma uma flechada nas costas e morre no mesmo lugar."
            jump gameOver

label fimFloresta:
    scene floresta
    play music "audio/floresta.mp3"
    pause 1.0
    if imagemPersonagem == "xu":
        show expression "hector" + armadura + lanca + machado + sangue + ".png"
        show expression imagemPersonagem + sangue + ".png" at posicao
        "Hector e Xu se deparam com um lugar calmo, com muitas arvores e pássaros cantando."
        hector "Enfim estamos do lado de fora da prisão, que lugar bonito, podemos passar alguns dias caçando e pescando nessa floresta."
        personagem "Temos que tomar cuidado, podem ter guardas de Draxon Malavak por aqui."
        stop music fadeout 1.0
        "De uma hora para outra os pássaros pararam de cantar e o silêncio contaminou toda a floresta."
        hector "Tem algo de errado, todos os passaros pararam de cantar."
        scene florestaguardas
        with Dissolve(2.0)
        show expression "hector" + armadura + lanca + machado + sangue + ".png"
        show expression imagemPersonagem + sangue + ".png" at posicao
        personagem "Cuidado Hector, são os guardas do Draxon Malavak, teremos que lutar contra eles."
        guardas "De hoje vocês não escapam, iremos vingar todos aqueles que vocês mataram."
        scene telapreta
        with Dissolve(2.0)
        play sound "audio/espada.mp3"
        "E o som das espadas mostrava a difícil batalha."
        play sound "audio/espada.mp3"
        if armadura == "A":
            scene florestaguardasm
            with Dissolve(2.0)
            show expression "hector" + armadura + lanca + machado + sangue + ".png"
            show expression imagemPersonagem + sangue + ".png" at posicao
            hector "Conseguimos derrotar os guardas de Malavak, podemos seguir nosso caminho para salvar nossas cidades."
            if machado == "M":
                scene telapreta
                with Dissolve(2.0)
                show text "E assim Hector e Xu partiram para salvar Dowblin e Zarandi, com seu machado Hector conseguiu fazer fogo para sobreviverem do frio e da fome." at truecenter
                with Dissolve(2.0)
                pause
                hide text
                with Dissolve(2.0)
                jump vitoria
            else:
                scene telapreta
                with Dissolve(2.0)
                show text "Porém..." at truecenter
                with Dissolve(2.0)
                pause
                hide text
                with Dissolve(2.0)
                show text "A noite chegou, Hector e Xu estavam no meio da floresta, o rangir dos dentes e o ronco dos seus estomagos mostrava que mesmo depois de todos os desafios, o maior deles ainda estaria por vir." at truecenter
                with Dissolve(2.0)
                pause
                hide text
                with Dissolve(2.0)
                show text "Hector e Xu sobreviveram alguns dias e depois de uma semana morreram de frio e fome." at truecenter
                with Dissolve(2.0)
                pause
                hide text
                with Dissolve(2.0)
                jump gameOver
        else:
            scene florestaguardasm
            with Dissolve(2.0)
            show expression "morto.png"
            show expression imagemPersonagem + sangue + ".png" at posicao
            "Mesmo matando todos os guardas, Hector sofre um grave ferimento que causa a sua morte."
            personagem "Hector seguirei meu caminho e vingarei a sua morte."
            jump gameOver
    elif imagemPersonagem == "elsa":
        show expression "hector" + armadura + lanca + machado + sangue + ".png"
        show expression imagemPersonagem + sangue + ".png" at posicao
        "Hector e Elsa se deparam com um lugar calmo, com muitas arvores e pássaros cantando."
        hector "Estamos fora da prisão, aqui posso até respirar novamente, podemos seguir nosso caminho para salvar Dowblin e Zarandi."
        personagem "Precisamos mesmo, preciso voltar para casa, não suporto os mosquitos dessa floresta."
        "De uma hora para outra os pássaros pararam de cantar e o silêncio contaminou toda a floresta."
        stop music fadeout 1.0
        hector "Tem algo de errado, todos a floresta de repente ficou silenciosa, para onde foram os pássaros?"
        scene florestaguardas
        with Dissolve(2.0)
        show expression "hector" + armadura + lanca + machado + sangue + ".png"
        show expression imagemPersonagem + sangue + ".png" at posicao
        personagem "Cuidado Hector, são os guardas do Draxon Malavak, preciso me esconder, não posso deixar eles me levarem novamente para prisão."
        guardas "De hoje vocês não escapam, iremos vingar todos aqueles que vocês mataram."
        personagem "Eu não matei ninguém, só tentei sair daquele lugar nojento."
        scene telapreta
        with Dissolve(2.0)
        play sound "audio/espada.mp3"
        "E o som das espadas mostrava a difícil batalha."
        play sound "audio/espada.mp3"
        if armadura ==  "A":
            scene florestaguardasm
            with Dissolve(2.0)
            show expression "hector" + armadura + lanca + machado + sangue + ".png"
            show expression imagemPersonagem + sangue + ".png" at posicao
            hector "Conseguimos derrotar os guardas de Malavak, podemos seguir nosso caminho para salvar nossas cidades."
            if machado == "M":
                scene telapreta
                with Dissolve(2.0)
                show text "E assim Hector e Elsa partiram para salvar Dowblin e Zarandi, com seu machado Hector conseguiu fazer fogo para sobreviverem do frio e da fome." at truecenter
                with Dissolve(2.0)
                pause
                hide text
                with Dissolve(2.0)
                jump vitoria
            else:
                scene telapreta
                with Dissolve(2.0)
                show text "Porém..." at truecenter
                with Dissolve(2.0)
                pause
                hide text
                with Dissolve(2.0)
                show text "A noite chegou, Hector e Elsa estavam no meio da floresta, o rangir dos dentes e o ronco dos seus estomagos mostrava que mesmo depois de todos os desafios, o maior deles ainda estaria por vir." at truecenter
                with Dissolve(2.0)
                pause
                hide text
                with Dissolve(2.0)
                show text "Elsa não parava de falar, dizia que preferiria passar a vida na prisão que naquela mata cheia de mosquitos." at truecenter
                with Dissolve(2.0)
                pause
                hide text
                with Dissolve(2.0)
                show text "Hector e Elsa sobreviveram alguns dias e depois de uma semana morreram de frio e fome." at truecenter
                with Dissolve(2.0)
                pause
                hide text
                with Dissolve(2.0)
                jump gameOver
        else:
            scene florestaguardas
            show expression "morto.png"
            show expression imagemPersonagem + sangue + ".png" at posicao
            "Elsa percebendo que Hector não teria chance contra os guardas de Draxon Malavak, bateu na sua cabeça com um pedaço de madeira que estava no chão, que o deixou desacordado."
            "Para não ter que voltar para prisão, ela trocou o corpo de Hector pela sua liberdade."
            jump gameOver
    else:
        show expression "hector" + armadura + lanca + machado + sangue + ".png"
        "Hector se deparam com um lugar calmo, com muitas arvores e pássaros cantando."
        hector "Enfim estou fora da prisão, aqui posso até respirar novamente, posso seguir meu caminho para salvar o rei."
        "De uma hora para outra os pássaros pararam de cantar e o silêncio contaminou toda a floresta."
        stop music fadeout 1.0
        hector "Tem algo de errado, todos a floresta de repente ficou silenciosa, para onde foram os pássaros?"
        scene florestaguardas
        with Dissolve(2.0)
        show expression "hector" + armadura + lanca + machado + sangue + ".png"
        guardas "De hoje você não escapa, iremos vingar todos aqueles que você matou."
        hector "E eu irei vingar o meu rei, e trarei a cabeça de Draxon Malavak para vocês."
        scene telapreta
        with Dissolve(2.0)
        play sound "audio/espada.mp3"
        "E o som das espadas mostrava a difícil batalha."
        play sound "audio/espada.mp3"
        if armadura ==  "A":
            scene florestaguardasm
            with Dissolve(2.0)
            hector "Consegui derrotar os guardas de Malavak, agora posso seguir meu caminho para salvar minha ilha."
            if machado == "M":
                scene telapreta
                with Dissolve(2.0)
                show text "E assim Hector partiu para salvar Dowblin, Zarandi e o rei, com seu machado Hector conseguiu fazer fogo para sobreviver ao frio e a fome." at truecenter
                with Dissolve(2.0)
                pause
                hide text
                with Dissolve(2.0)
                jump vitoria
            else:
                scene telapreta
                with Dissolve(2.0)
                show text "Porém..." at truecenter
                with Dissolve(2.0)
                pause
                hide text
                with Dissolve(2.0)
                show text "A noite chegou, Hector no meio da floresta, o rangir dos dentes e o ronco do seu estomago mostrava que mesmo depois de todos os desafios, o maior deles ainda estaria por vir." at truecenter
                with Dissolve(2.0)
                pause
                hide text
                with Dissolve(2.0)
                show text "Hector mesmo depois de varios dias sem se alimentar direito, conseguia seguir sua jornada, até que em uma noite, sem ter com o que fazer fogo, uma cobra ataca Hector e o mata." at truecenter
                with Dissolve(2.0)
                pause
                hide text
                with Dissolve(2.0)
                jump gameOver
        else:
            scene florestaguardas
            with Dissolve(2.0)
            show expression "morto.png"
            "Hector não tendo como se defender contra tantos guardas, morre lutando."
            jump gameOver

label fimDeserto:
    scene deserto
    play music "audio/deserto.mp3"
    pause 1.0
    if imagemPersonagem == "xu":
        show expression "hector" + armadura + lanca + machado + sangue + ".png"
        show expression imagemPersonagem + sangue + ".png" at posicao
        "Hector e Xu chegam a um lugar deserto, olham para todos os lados e não há um sinal de vida."
        "No horizonte, alguns corvos comiam o resto dos ultimos animais que sobreviviam naquela área."
        hector "Precisamso encontrar um lugar com água e alimentos para passarmos a noite."
        personagem "Sim, os desertos possuem dias muito quentes e noites muito frias, podemos morrer em menos de 24 horas."
        if armadura == "A":
            scene telapreta
            with Dissolve(2.0)
            show text "Hector e Xu partiram para procurar abrigo, sua armadura em meio ao sol do deserto, fez com que Hector em menos de 5 horas morresse de desidratação." at truecenter
            with Dissolve(2.0)
            pause
            hide text
            with Dissolve(2.0)
            show text "Xu, desidratado e quase sem esperança de encontrar água, avista em meio ao sol, um pequeno camelo indo ao encontro de um oasis para beber água." at truecenter
            with Dissolve(2.0)
            pause
            hide text
            with Dissolve(2.0)
            show text "Chegando lá, Xu se hidrata e pega o camelo para cumprir sua missão de salvar Dowblin e Zarandi." at truecenter
            with Dissolve(2.0)
            pause
            hide text
            with Dissolve(2.0)
            jump gameOver
        else:
            scene telapreta
            with Dissolve(2.0)
            show text "Hector e Xu partiram na busca de um abrigo, depois de uma longa caminhada, avistaram uma região com uma pequena arvore nascendo." at truecenter
            with Dissolve(2.0)
            pause
            hide text
            with Dissolve(2.0)
            show text "Foi ai que Xu teve a brilhante ideia, vamos cavar para ver se achamos um fluxo de água para bebermos." at truecenter
            with Dissolve(2.0)
            pause
            hide text
            with Dissolve(2.0)
            show text "Assim, depois de cavar por alguns dias, encontraram água suficiente para sobreviver e partiram para salvar o rei das garras de Draxon Malavak." at truecenter
            with Dissolve(2.0)
            pause
            hide text
            with Dissolve(2.0)
            jump vitoria
    elif imagemPersonagem == "elsa":
        show expression "hector" + armadura + lanca + machado + sangue + ".png"
        show expression imagemPersonagem + sangue + ".png" at posicao
        "Chegando no deserto, Elsa, criada por uma família rica, odiava sentir aquele calor insuportável."
        elsa "Hector, precisamos sair daqui logo, o sol está muito quente para a minha pele."
        "Encantado pela beleza de Elsa, Hector nem imaginava o que estava por vir."
        hector "Claro, vamos procurar uma sombra até a noite, e partimos para salvar nossas cidades."
        "Elsa não estava se importando em salvar a cidade, a vida dela era o mais importante."
        "Elsa arquitetou um plano para sair viva."
        "Entregar o corpo de Hector para Draxon Malavak em troca de sua liberdade."
        if armadura ==  "A":
            "Quando Hector se abaixou, Elsa com uma pedra o golpeou na cabeça."
            "Hector ficou meio tonto, porém, o que Elsa não esperava era que o seu capacete o protegeria contra a pedrada."
            hide expression imagemPersonagem + sangue + ".png" at posicao
            show expression imagemPersonagem + "M.png" at posicao
            with Dissolve(2.0)
            "Hector com muito ódio, sacou a espada e a matou."
            scene telapreta
            with Dissolve(2.0)
            show text "Mesmo eliminando um de seus obstáculos, Hector ainda estava em meio ao deserto sem água nem comida." at truecenter
            with Dissolve(2.0)
            pause
            hide text
            with Dissolve(2.0)
            show text "Depois de algumas horas, devido a sua armadura muito quente, Hector desmaia e acaba morrendo desidratado." at truecenter
            with Dissolve(2.0)
            pause
            hide text
            with Dissolve(2.0)
            jump gameOver
        elif lanca == "L" or machado == "M":
            "Hector observando os corvos devorando os restos de um animal no deserto, quase não percebeu quando Elsa pegou uma pedra no chão."
            "Porém, a sombra de Elsa quando se aproximava de Hector, fez com que ele percebesse a verdadeira intenção da enfermeira."
            hide expression imagemPersonagem + sangue + ".png" at posicao
            show expression imagemPersonagem + "M.png" at posicao
            with Dissolve(2.0)
            "Rapidamente Hector retira sua arma e mata Elsa."
            scene telapreta
            with Dissolve(2.0)
            show text "Hector mesmo depois de ter matado Elsa, seguiu friamente seu caminha para cumprir seu objetivo de salvar Dowblin e Zarandi." at truecenter
            with Dissolve(2.0)
            pause
            hide text
            with Dissolve(2.0)
            jump vitoria
        else:
            "Sem ter como se defender, Hector recebe uma pedrada de Elsa na cabeçam, que cai no chão desacordado."
            "Elsa enquanto você está desacordado no chão, te entrega para os guardas de Malavak."
            hide expression "hector" + armadura + lanca + machado + sangue + ".png"
            show expression "morto.png"
            with Dissolve(2.0)
            show telapreta
            with Dissolve(2.0)
            show text "Porém como o sol estava muito quente, antes que os guardas cheguem, Hector já estava morto por desidratação." at truecenter
            with Dissolve(2.0)
            pause
            hide text
            with Dissolve(2.0)
            jump gameOver
    else:
        "Hector chega em um lugar desértico, nenhum sinal de vida, a única coisa vista são alguns corvos que comiam o resto dos ultimos animais que sobreviviam naquela área."
        "Os ventos fortes transformava o local diariamente, tornando o lugar muito fácil para se perder, e difícil de se achar."
        hector "Preciso encontrar água para sobreviver nesse deserto."
        if armadura ==  "A":
            "O calor escaldante, e sua armadura, fizeram com que Hector ficasse alucinado, perdendo a noção do seu objetivo"
            hide expression "hector" + armadura + lanca + machado + sangue + ".png"
            show expression "morto.png"
            with Dissolve(2.0)
            show telapreta
            with Dissolve(2.0)
            show text "Em pouco tempo Hector já perdeu boa parte do líquido do seu corpo, morrendo desidratado no meio do deserto." at truecenter
            with Dissolve(2.0)
            pause
            hide text
            with Dissolve(2.0)
            jump gameOver
        else:
            show telapreta
            with Dissolve(2.0)
            show text "Hector mesmo com sede manteve o foco no seu objetivo, rapidamente encontrou um oasis onde vários camelos bebiam água" at truecenter
            with Dissolve(2.0)
            pause
            hide text
            with Dissolve(2.0)
            show text "Hector montou em um camelo e partiu para salvar o rei e sua cidade natal." at truecenter
            with Dissolve(2.0)
            pause
            hide text
            with Dissolve(2.0)
            jump vitoria

label gameOver:
    play music "audio/gameover.mp3"
    scene gameover
    with Dissolve(2.0)
    pause
    return

label vitoria:
    play music "audio/vitoria.mp3"
    scene vitoria
    with Dissolve(2.0)
    pause
    return
