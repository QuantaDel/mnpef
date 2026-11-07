'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
import streamlit as st
import time

# Configuração da página para dispositivos móveis
st.set_page_config(
    page_title="Operação Sinal de Prata - Desafio Cripto",
    page_icon="🔒",
    layout="centered"
)

# Estilização CSS personalizada para estética de Cibersegurança
st.markdown(
    """
    <style>
    .main { background-color: #0e1117; }
    h1 { color: #f39c12; text-align: center; }
    .stButton>button { width: 100%; background-color: #f39c12; color: black; font-weight: bold; }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🔒 OPERAÇÃO SINAL DE PRATA")
st.markdown("<p style='text-align: center; color: #aaa;'>Módulo de Teste de Vulnerabilidade de Senhas</p>", unsafe_allow_html=True)

# Inicialização segura do estado da sessão
if 'fase' not in st.session_state:
    st.session_state.fase = 1

# ---------------------------------------------------------
# FASE 1: DESAFIO INICIAL (Cifra de Substituição / César)
# ---------------------------------------------------------
if st.session_state.fase == 1:
    st.markdown("### Nível 1: Cifra de Substituição Simples")
    st.write("Crie uma senha inicial para testar o sistema de proteção por deslocamento de caracteres.")
    
    senha1 = st.text_input("Digite sua senha Nível 1:", type="password", key="input_s1")
    
    if st.button("Testar Resistência da Senha 1", key="btn_s1"):
        if senha1:
            with st.spinner("Analisando padrões estatísticos de frequência..."):
                time.sleep(1.5)
            st.session_state.res_s1 = senha1
        else:
            st.warning("Digite uma senha válida primeiro.")

    if 'res_s1' in st.session_state:
        st.error(f"❌ SENHA QUEBRADA EM 0.4 SEGUNDOS! A sua senha é: **{st.session_state.res_s1}**")
        
        # Explicação Didática do Nível 1
        st.info("""
        💡 **Diagnóstico de Segurança (Cifra de Substituição / César):**
        * **Como o sistema quebrou:** O algoritmo usou **Análise de Frequência Estatística**. Na língua portuguesa, letras como 'A', 'E' e 'O' aparecem muito mais do que 'Z' ou 'X'.
        * **A falha clássica:** Trocar letras por símbolos ou deslocar o alfabeto (ex: A vira C) **não esconde o padrão da linguagem humana**. O computador descobre o segredo em milissegundos contando as repetições.
        """)
        
        if st.button("Avançar para o Nível 2 ➔", key="next_to_2"):
            st.session_state.fase = 2
            st.rerun()

# ---------------------------------------------------------
# FASE 2: CHAVE SIMÉTRICA REUTILIZADA (Vigenère / XOR)
# ---------------------------------------------------------
elif st.session_state.fase == 2:
    st.markdown("### Nível 2: Criptografia por Chave Reutilizável")
    st.write("Sua primeira senha caiu rápido. Agora crie uma senha mais complexa misturando letras, números e símbolos.")
    
    senha2 = st.text_input("Digite sua senha Nível 2:", type="password", key="input_s2")
    
    if st.button("Testar Resistência da Senha 2", key="btn_s2"):
        if senha2:
            status = st.empty()
            progress = st.progress(0)
            
            status.text("Detectando padrão de repetibilidade da chave...")
            progress.progress(30)
            time.sleep(1)
            
            status.text("Aplicando eliminação lógica via XOR...")
            progress.progress(70)
            time.sleep(1)
            
            progress.progress(100)
            status.empty()
            st.session_state.res_s2 = senha2
        else:
            st.warning("Digite uma senha válida primeiro.")

    if 'res_s2' in st.session_state:
        st.error(f"❌ SENHA QUEBRADA EM 3.2 SEGUNDOS! A sua senha é: **{st.session_state.res_s2}**")
        
        # Explicação Didática do Nível 2
        st.info("""
        💡 **Diagnóstico de Segurança (Chave Simétrica / Vigenère):**
        * **Como o sistema quebrou:** O algoritmo utilizou detecção de **repetição de chave simétrica** e operações lógicas como a porta **XOR**.
        * **A falha clássica:** Se a mesma chave secreta é reutilizada para cifrar várias mensagens ou transmitir dados pelo canal, uma espiã (Eva) que interceptar o fluxo consegue cancelar a chave matematicamente por força bruta e extrair o texto original.
        """)
        
        if st.button("Avançar para o Nível 3 (Segurança Bancária) ➔", key="next_to_3"):
            st.session_state.fase = 3
            st.rerun()

# ---------------------------------------------------------
# FASE 3: CRIPTOGRAFIA ASSIMÉTRICA MODERNA (RSA)
# ---------------------------------------------------------
elif st.session_state.fase == 3:
    st.markdown("### Nível 3: Criptografia Assimétrica Moderna (RSA / Bancos)")
    st.write("Esta é a criptografia que protege o WhatsApp e transações bancárias. Crie a senha definitiva 'inquebrável'.")
    
    senha3 = st.text_input("Digite sua senha Nível 3:", type="password", key="input_s3")
    
    if st.button("Iniciar Teste de Invasão de Alta Complexidade", key="btn_s3"):
        if senha3:
            status = st.empty()
            bar = st.progress(0)
            
            etapas = [
                ("Iniciando algoritmo de fatoração de números primos...", 15, 1.5),
                ("Mapeando par de chaves pública e privada...", 35, 1.5),
                ("Simulando processamento massivo paralelo...", 60, 2),
                ("Aplicando estimativa de Shor em ambiente quântico simulado...", 85, 2),
                ("Finalizando extração da chave...", 100, 1)
            ]
            
            for texto, pct, espera in etapas:
                status.text(texto)
                bar.progress(pct)
                time.sleep(espera)
                
            status.empty()
            st.session_state.res_s3 = senha3
        else:
            st.warning("Digite uma senha válida primeiro.")

    if 'res_s3' in st.session_state:
        st.error(f"💥 SISTEMA INVASOR VENCEU! Sua senha inquebrável é: **{st.session_state.res_s3}**")
        
        # Explicação Didática do Nível 3
        st.info("""
        💡 **Diagnóstico de Segurança (Criptografia Assimétrica / RSA):**
        * **Como o sistema quebrou:** O RSA baseia sua segurança na **dificuldade de fatorar a multiplicação de dois números primos gigantescos**.
        * **A falha conceitual:** A segurança do RSA é baseada em *tempo de processamento*, e não em uma lei inviolável da natureza. Com o avanço de supercomputadores ou a chegada dos **Computadores Quânticos (Algoritmo de Shor)**, o que levaria bilhões de anos para ser fatorado pode ser resolvido em poucos minutos.
        """)
        
        st.markdown("---")
        st.warning("""
        ### ⚠️ A Conclusão da Investigação
        Todas as senhas baseadas puramente em **complexidade matemática** podem ser quebradas se o invasor possuir tempo e poder computacional suficientes.
        
        **Como garantir a segurança da informação se a matemática clássica sempre pode ser derrotada?**
        
        *A resposta não está na Matemática... está na **Física Quântica**.*
        """)
        
        if st.button("🔄 Reiniciar Investigação", key="restart"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
