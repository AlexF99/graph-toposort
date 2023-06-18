# graph-toposort

Programa desenvolvido em Python que recebe como entrada um grafo direcionado e retorna uma ordenação topológica deste grafo.

## Como rodar

- Estando no diretório do projeto, rode `make`;
- Rode `./toposort < [arquivo.dot]`

## Grafo

Representamos o grafo com uma matriz de adjacência, além de uma lista de símbolos representando os vértices.

## Ordenação topológica

Primeiro, colocamos os graus de entrada de todos os vértices em uma lista indexada de maneira idêntica a lista original de vértices. Os vértices com grau de entrada 0 (fontes) são colocados em uma fila, o que é possível pois todo grafo direcionado acíclico possui ao menos uma fonte.
Depois, enquanto a fila não estiver vazia:
- Removemos um vértice da fila;
- Colocamos ele na lista de ordenação topológica;
- Para cada um de seus vizinhos:
    - diminui seu grau de entrada em 1;
    - se seu grau de entrada for 0, coloca na fila de fontes;
