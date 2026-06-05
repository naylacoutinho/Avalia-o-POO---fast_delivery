# FastDelivery Express

## Autor

Nayla Coutinho Lopes

Disciplina: Programação Orientada a Objetos com Python

Professor: Evandro de Lima Rodrigues

## 1. Descrição do Projeto

O FastDelivery Express é um sistema de gerenciamento de entregas desenvolvido em Python utilizando os principais conceitos da Programação Orientada a Objetos (POO).

O sistema permite cadastrar clientes e entregadores, criar pedidos de entrega, calcular fretes de acordo com o tipo de serviço escolhido e acompanhar o status dos pedidos.

Este projeto foi desenvolvido como atividade avaliativa da disciplina de Programação Orientada a Objetos com Python.



## 2. Tecnologias Utilizadas

* Python 3
* Git
* Github



## 3. Estrutura de Pastas

```text
FastDeliveryExpress/
│
├── modelos/
│   ├── pessoa.py
│   ├── cliente.py
│   ├── entregador.py
│   ├── pedido.py
│   ├── entrega_comum.py
│   ├── entrega_expressa.py
│   └── entrega_premium.py
│
├── interfaces/
│   └── calculo_frete_interface.py
│
├── services/
│   ├── cliente_service.py
│   ├── pedido_service.py
│   ├── entrega_service.py
│   └── entregador_service.py
│
├── util/
│   ├── menu.py
│   └── formatador.py
│
├── main.py
└── README.md
```

### Funcionalidades

#### Clientes

* Cadastro de clientes
* Listagem de clientes cadastrados
* Busca de clientes por CPF

#### Entregadores

* Cadastro de entregadores
* Listagem de entregadores
* Busca de entregadores por CNH

#### Pedidos

* Criação de pedidos
* Cálculo automático do frete
* Listagem de pedidos
* Atualização do status do pedido

#### Tipos de Entrega

* Entrega Comum
* Entrega Expressa
* Entrega Premium



## 4. Conceitos de POO Utilizados

### Encapsulamento

Os atributos das classes foram protegidos utilizando atributos privados e métodos de acesso (`@property` e setters).

### Herança

A classe `Pessoa` é utilizada como classe base para:

* Cliente
* Entregador

### Polimorfismo

As classes de entrega implementam o método `calcular_frete()` de formas diferentes:

* EntregaComum
* EntregaExpressa
* EntregaPremium

### Interface

Foi utilizada a interface `CalculoFreteInterface`, garantindo que todas as classes de entrega implementem o método `calcular_frete()`.


## 5. Como Executar

1. Abra o terminal na pasta do projeto.
2. Execute o arquivo principal:

```bash
python main.py
```

3. Utilize os menus para cadastrar clientes, entregadores e criar pedidos.


## 6. Exemplos de Uso

## Demonstração

### Menu Principal e Cadastro do Cliente
<img src="imagens/14.png" width="700">

### Lista de Clientes
<img src="imagens/11.png" width="700">

### Lista de Clientes
<img src="imagens/11.png" width="700">

### Busca de Clientes
<img src="imagens/10.png" width="700">

### Menu e Criação de Pedidos
<img src="imagens/9.png" width="700">

### Lista de Pedidos
<img src="imagens/7.png" width="700">

### Atualização de Status
<img src="imagens/6.png" width="700">

### Lista de Pedidos com Exemplo Atualizado
<img src="imagens/5.png" width="700">

### Cadastro de Entregador
<img src="imagens/4.png" width="700">

### Lista de Entregadores
<img src="imagens/2.png" width="700">

### Busca de Entregador e Finalização
<img src="imagens/11.png" width="700">