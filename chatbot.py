import pandas as pd
import streamlit as st
import plotly.express as px
from openai import OpenAI

# Configuração inicial da página
st.markdown("""
    <style>
        .stChatInput {
            position: fixed;
            bottom: 20px;
            z-index: 999999;
        }
        .block-container {
            padding-bottom: 120px;
        }
    </style>
""", unsafe_allow_html=True)

st.set_page_config(layout="wide", page_title="Sistema Integrado", page_icon="🌸")

st.write("# 🌸 Sistemas de Vendas 🌸")

# Criação de apenas 2 Abas de navegação
aba1, aba2 = st.tabs([" Sistema e Dashboard", " Chatbot IA"])

# Carrega a tabela de vendas
tabela_vendas = pd.read_csv("vendas.csv")


with aba1:
    st.write("## Cadastrar Vendas")
    
    col1, col2 = st.columns(2)
    with col1:
        data = st.date_input("Data", max_value="today")
        vendedor = st.selectbox("Vendedor", ["Ana", "Bruno", "Carla"])
        produto = st.selectbox("Produto", ["Notebook", "Celular", "Fone"])
    with col2:
        quantidade = st.number_input("Quantidade", step=1)
        valor = st.number_input("Valor")
        
    botao_cadastrar = st.button("Cadastrar Vendas")

    if botao_cadastrar:
        nova_venda = [str(data), vendedor, produto, quantidade, valor] 
        ultima_linha = len(tabela_vendas)
        tabela_vendas.loc[ultima_linha] = nova_venda
        tabela_vendas.to_csv("vendas.csv", index=False)
        st.success("Venda Cadastrada!")

    st.write("## Vendas Cadastradas")
    st.dataframe(tabela_vendas, use_container_width=True)

    st.write("## Dashboard de Faturamento")
    
    faturamento = tabela_vendas["valor"].sum()
    st.metric("Faturamento Total", f"R$ {faturamento:,.2f}")

    cores_rosa_pastel = ["#FFB6C1", "#FF69B4", "#C71585"]
    
    col3, col4 = st.columns(2)
    with col3:
        grafico1 = px.bar(tabela_vendas, x="vendedor", y="valor", color="produto", color_discrete_sequence=cores_rosa_pastel)
        st.plotly_chart(grafico1, use_container_width=True)
        
    with col4:
        grafico2 = px.pie(tabela_vendas, names="produto", values="valor", hole=0.4, color_discrete_sequence=cores_rosa_pastel)
        st.plotly_chart(grafico2, use_container_width=True)


with aba2:
    st.write("### Assistente Virtual")
    
    # Inicializa o modelo
    modelo = OpenAI(
        api_key="[PONHA SUA CHAVE AQ]", 
        base_url="https://generativelanguage.googleapis.com/v1beta/openai"
    )

    
    if "lista_mensagens" not in st.session_state:
        st.session_state["lista_mensagens"] = []

    
    for mensagem in st.session_state["lista_mensagens"]:
        role = mensagem["role"]
        content = mensagem["content"]
        st.chat_message(role).write(content)

    mensagem_usuario = st.chat_input("Escreva sua mensagem aqui...")

    if mensagem_usuario:
        
        st.chat_message("user").write(mensagem_usuario)
        mensagem = {"role": "user", "content": mensagem_usuario}
        st.session_state["lista_mensagens"].append(mensagem)

       
        dados_vendas_texto = tabela_vendas.to_string(index=False)

        
        mensagens_para_ia = st.session_state["lista_mensagens"].copy()
        mensagens_para_ia[-1] = {
            "role": "user", 
            "content": f"Com base nestes dados de vendas:\n{dados_vendas_texto}\n\nResponda: {mensagem_usuario}"
        }

        
        resposta_modelo = modelo.chat.completions.create(
            messages=mensagens_para_ia, 
            model="gemini-flash-lite-latest"
        )
        resposta_ia = resposta_modelo.choices[0].message.content

       
        st.chat_message("assistant").write(resposta_ia)
        mensagem_ia = {"role": "assistant", "content": resposta_ia} 
        st.session_state["lista_mensagens"].append(mensagem_ia)