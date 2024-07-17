# Documento de Visão: Modelo EmpresasJuiniors

## 1. Introdução

Este documento de visão fornece uma visão geral do modelo `EmpresasJuiniors`, que é parte do sistema de gerenciamento de empresas juniores. O modelo é projetado para armazenar informações essenciais sobre as empresas juniores e facilitar a operação e o gerenciamento eficientes.

## 2. Finalidade

O modelo `EmpresasJuiniors` serve como a estrutura de dados central para registrar e manter informações críticas das empresas juniores, incluindo dados legais, representação e área de atuação.
#
## 3. Escopo

O modelo será utilizado pelo sistema para:
- Armazenar dados cadastrais das empresas juniores.
- Associar representantes legais às empresas.
- Gerenciar informações de contato e operacionais.

## 4. Descrição do Modelo

### 4.1. `razao_social`
- **Tipo**: CharField
- **Descrição**: Armazena a razão social da empresa júnior.
- **Restrições**: Máximo de 50 caracteres.

### 4.2. `cnpj`
- **Tipo**: CharField
- **Descrição**: Contém o CNPJ da empresa.
- **Restrições**: Máximo de 18 caracteres.

### 4.3. `inscricao_estadual`
- **Tipo**: CharField
- **Descrição**: Registra a inscrição estadual da empresa.
- **Restrições**: Máximo de 20 caracteres.

### 4.4. `representante_legal`
- **Tipo**: CharField
- **Descrição**: Nome do representante legal da empresa.
- **Restrições**: Máximo de 100 caracteres.

### 4.5. `cpf_representante_lega`
- **Tipo**: CharField
- **Descrição**: CPF do representante legal.
- **Restrições**: Máximo de 11 caracteres.

### 4.6. `area_atuacao`
- **Tipo**: CharField
- **Descrição**: Define a área de atuação da empresa júnior.
- **Restrições**: Máximo de 100 caracteres.

### 4.7. `site`
- **Tipo**: URLField
- **Descrição**: Endereço do site da empresa.
- **Restrições**: Opcional.

### 4.8. `fundacao`
- **Tipo**: DateField
- **Descrição**: Data de fundação da empresa.
- **Restrições**: Nenhuma.

### 4.9. `endereco`
- **Tipo**: ForeignKey (Informacoes)
- **Descrição**: Associa um endereço da tabela `Informacoes` à empresa.
- **Restrições**: Opcional, pode ser nulo.

## 5. Benefícios

O uso deste modelo traz benefícios como:
- Centralização das informações das empresas juniores.
- Facilidade de acesso e atualização dos dados.
- Integração com outros módulos do sistema.

## 6. Conclusão

O modelo `EmpresasJuiniors` é vital para o gerenciamento eficaz das empresas juniores, fornecendo uma base sólida para o armazenamento e manipulação de seus dados.
