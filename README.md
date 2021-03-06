# :video_game: Asteroids

Jogo clássico de Asteroids feito com Pygame

## Autores

- Adham Lucas - adhamlucas20@gmail.com
- Edson Barros - edson.limajr@gmail.com
- Tiago Aranha - tiagoweb@gmail.com
- Vitor Simões - vitor6427126@gmail.com
- Wesley Rocha - wesleysr1997@gmail.com

## História

O jogo em questão é um clone do jogo Asteroids. Este é um jogo de arcade com gráficos vetoriais muito popular lançado em 1979 pela Atari. O objetivo do jogo é destruir asteroides sem se deixar ser atingido por seus fragmentos. (Wikipédia)

## Personagens

1. Nave Espacial
2. Asteroide Grande
3. Asteroide Médio
4. Asteroide Pequeno

## Controles
    
1. Movimentação da nave no espaço: A nave pode ser controlada pelo acelarador (tecla UP) que direciona a nave para frente e aumenta a acelaração quando a tecla permance acionada e diminui a aceleração até parar quando a tecla deixa de ser pressionada. A nave também pode girar em seu próprio eixo com a utilização das teclas seta para direita e seta para esquerda, o que fará com que a nave, caso esteja em movimento tenha sua direção modificada de acordo com a telca pressionada (direita ou esqureda)
2. Hiperespaço: A nave pode viajar para o hiperespaço e surgir instantaneamente em qualquer ponto do espaço ao ser acionada a tecla shift do lado esquerdo do teclado.
3. A nave atira misseis caso a tecla barra de espaços seja acionada. Caso a tecla se mantenha acionada, a nave atira sequencialmente misseis até que a tecla deixe de ser pressionada.

Resumo:

- :arrow_up: ou W: propulsiona a nave para frente
- :arrow_left: ou A: gira a nave no sentido anti-horário
- :arrow_right: ou D: gira a nave no sentido horário
- Espaço: atira
- Shift: viaja para hiperespaço

## Câmera

O jogo é mostrado em 2D, sendo o universo ao fundo e a nave vista de cima bem como os asteroides e as patrulhas. O jogo apresenta um efeito circular nas bordas, ou seja, quando a nave atravessa uma das bordas ela reaparece na borda paralela na mesma em direção que sumiu.
   
## Universo do Jogo

O jogo se passa no espaço sideral. 
    
## Inimigos

1. Asteroide Grande
2. Asteroide Médio
3. Asteroide Pequeno

## Interface

1. Inicialmente o Menu onde é mostrado a opção "Play game", "High Socre" e "Creditos". A primeira incia o jogo que é descrito no item 2. e a segunda mostra o máximo de pontos feitos pelos jogadores e o terceiro mostra os nomes dos  desenvolvedores 
2. Fundo preto representando o espaço sideral. As estrelas representadas por pontos minúscolos sobre o fundo preto. No topo à esquerda a pontuação e logo abaixo a quantidade de vidas. As personagens serão desenhadas com figuras geométricas vetoriais.

## Executando (sem build)

Na raíz do diretório, instale as dependências com `pipenv install` e use `pipenv shell && cd src && python main.py` para executar o jogo.
