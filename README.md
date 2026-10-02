# 🌸 Sistema Integrado de Vendas & Inteligência Artificial

Projeto desenvolvido unindo o aprendizado de duas aulas da **Jornada Python**. Seguindo a dica do professor para consolidar os conhecimentos, decidi juntar o sistema de cadastro e o dashboard de dados com um assistente virtual inteligente alimentado por IA.

---

## 🚀 Funcionalidades da Aplicação

A aplicação utiliza uma interface limpa em Streamlit organizada em **duas abas principais**:

1. **📝 Sistema e Dashboard**:
   - Cadastro em tempo real de novas vendas (Data, Vendedor, Produto, Quantidade e Valor).
   - Salvamento automático dos dados em um arquivo `vendas.csv`.
   - Métricas de faturamento total atualizadas instantaneamente.
   - Gráficos interativos (de barras e de rosca/pizza) criados com Plotly Express utilizando uma identidade visual personalizada em tons de rosa pastel.

2. **🤖 Chatbot IA**:
   - Assistente virtual integrado que lê dinamicamente os dados da tabela de vendas do site.
   - Utiliza a API da OpenAI adaptada para o modelo Gemini (`gemini-flash-lite-latest`) para responder dúvidas sobre o desempenho e os números da empresa de forma inteligente.
   - Mantém o histórico de conversas (`session_state`) para uma experiência de chat fluida.

---

## 🛠️ Tecnologias Utilizadas

* **Python**
* **Streamlit** (Interface web)
* **Pandas** (Manipulação de dados)
* **Plotly Express** (Visualização de dados / Gráficos)
* **OpenAI API / Google Gemini** (Assistente de IA)
