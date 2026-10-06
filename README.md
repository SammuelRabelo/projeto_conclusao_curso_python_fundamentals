# 🏦 Sistema Bancário em Python

Projeto simples desenvolvido por mim com o objetivo de consolidar e aplicar na prática os conhecimentos adquiridos ao longo do curso **Formação Python Fundamentals**. 

O sistema simula as operações fundamentais de uma instituição financeira de forma orientada a objetos, focando em boas práticas de arquitetura de software, encapsulamento e persistência de dados.

---

## 🚀 Conceitos e Módulos Aplicados

Durante o desenvolvimento deste projeto, tive a oportunidade de sair da teoria e implementar os principais pilares avançados da linguagem Python abordados no curso:

*   **Programação Orientada a Objetos (POO):** Estruturação do sistema dividida em classes (`Conta`, `Banco` e `Menu`), garantindo a separação de responsabilidades, organização de estados e encapsulamento dos dados.
*   **Decoradores (Decorators):** Criação de um decorador personalizado (`@valida_transacao`) para centralizar regras de negócio e validações de segurança (como impedir saques ou depósitos com valores negativos ou zerados) antes que os métodos principais sejam executados.
*   **Iteradores (Iterators):** Implementação do método mágico `__iter__` na classe `Banco`, permitindo percorrer as instâncias das contas de forma transparente e desacoplada do dicionário interno de armazenamento.
*   **Manipulação de Arquivos (File I/O):** Utilização de gerenciadores de contexto (`with open`) para criar, escrever e persistir históricos de transações e extratos bancários em formato de texto `.txt` de forma segura e automatizada.
*   **Manipulação de Data e Hora (`datetime`):** Registo de logs de auditoria e carimbos de tempo precisos para cada operação financeira realizada nas contas dos clientes.

---

## 🛠️ Tecnologias Utilizadas

*   **Python 3.x** (Linguagem principal)
*   **Git & GitHub** (Controlo de versões e gestão de repositório)

---

## 🎯 Sobre o Projeto
Este projeto faz parte da minha jornada prática em desenvolvimento de software e engenharia de dados, servindo como base sólida para evoluções futuras, como integração com bases de dados relacionais e arquiteturas em camadas.
