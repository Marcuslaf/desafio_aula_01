# Gerenciador de Usuários JSON

Um sistema simples de gerenciamento de usuários que armazena dados em arquivo JSON, desenvolvido em Python.

## Funcionalidades

- Criar arquivo JSON com dados iniciais
- Adicionar novos usuários
- Exibir lista de usuários cadastrados
- Buscar usuários por nome ou email
- Remover usuários pelo nome
- Validações de dados de entrada
- Tratamento de erros robusto

## Requisitos

- Python 3.6 ou superior
- Nenhuma biblioteca externa é necessária (apenas módulos da biblioteca padrão)

## Estrutura dos Dados

Cada usuário é armazenado com os seguintes campos:
```json
{
    "nome": "string",
    "idade": "integer",
    "email": "string"
}
```

## Como Usar

1. Clone ou baixe o arquivo do projeto:
 git clone https://github.com/Marcuslaf/desafio_aula_01.git

2. Execute o script principal:
   ```bash
   python gerenciador_usuarios.py
   ```
3. Siga as opções do menu interativo:
   - 1: Criar arquivo JSON
   - 2: Adicionar usuário
   - 3: Exibir usuários
   - 4: Buscar usuário
   - 5: Remover usuário
   - 6: Sair

## Detalhes das Funcionalidades

### Criar Arquivo JSON
- Cria um novo arquivo JSON com dados iniciais
- Se o arquivo já existir, solicita confirmação antes de sobrescrever

### Adicionar Usuário
- Solicita nome, idade e email do usuário
- Realiza validações:
  - Nome não pode estar vazio
  - Idade deve estar entre 0 e 150
  - Email deve conter "@" e "."
  - Email não pode estar duplicado

### Exibir Usuários
- Mostra todos os usuários cadastrados
- Exibe informações formatadas com separadores
- Mostra o total de usuários cadastrados

### Buscar Usuário
- Busca por nome ou email (parcial ou completo)
- Case insensitive
- Exibe todos os resultados encontrados

### Remover Usuário
- Remove usuário pelo nome
- Se houver múltiplos usuários com o mesmo nome:
  - Exibe lista numerada para escolha
  - Permite cancelar a operação
- Solicita confirmação antes de remover

## Tratamento de Erros

O sistema inclui tratamento para:
- Arquivo JSON corrompido
- Arquivo não encontrado
- Entradas inválidas
- Dados duplicados
- Validações de formato

## Boas Práticas Implementadas

- Orientação a Objetos
- Type hints para melhor documentação
- Métodos privados para operações internas
- Encoding UTF-8 para suporte a caracteres especiais
- Mensagens de erro descritivas
- Validações robustas
- Confirmação para operações críticas

## Contribuição

Sinta-se à vontade para contribuir com melhorias:
1. Fork o projeto
2. Crie uma branch para sua feature
3. Faça commit das alterações
4. Push para a branch
5. Abra um Pull Request

## Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
