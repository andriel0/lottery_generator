# lottery_generator

- Não consegui upar o arquivo .exe no repositório, então vou deixar o link aberto do meu drive para quem quiser baixar para testar.
https://drive.google.com/file/d/190k0yLUG-K97OXmuZ16O-hvKXiHG2Y2_/view?usp=sharing

Meu programa de gerador de sena com números de 1 a 60 que não podem se repetir.

- A resolução de Back End foi pequena, perguntei para o usuário se ele tem números da sorte para eu poder adicioná-los na sequência final,
pois vejo que e algo comum querer números aleatórios, mas com um ou mais específicos. Entao adicionado os números da sorte em uma lista,
sorteio o restante até completar o tamanho completo da lista, no caso da sena, 6 números, com a adição de não poder repeti-los. Coloquei 
condição para possível erro de digitação na parte de números de sorte escolhido, caso fosse numero fora do intervalo valido ou caso não
fosse digitado números. Quando clicado o botão, os números aparecem na ordem crescente, sem repetir, com os possíveis números da sorte e 
aparece um texto escrito 'Boa sorte!!!' depois do primeiro clique para gerar.

- A resolução de Front End foi no Qt Designer, coloquei imagem de fundo para ficar algo mais limpo, cores amarelas para douradas nas letras
e bordas das bolinhas, e fiz um botão responsivo que muda de cor quando passa o mouse em cima e quando clica também.

