import streamlit as st
from chempy import Substance

def CalcularMassa(formula):
  try:
    return Substance.from_formula(formula).mass
  except:
    return None
st.title(Calculadora de Massa Molar)
st.write(Digite a fórmula para ver o resultado!)

while True:
  entrada = st.text_input("\nDigite a fórmula (ou sair para encerrar o programa: ")
  if entrada.lower =='sair':
    break

  resultado = CalcularMassa(entrada)

  if resultado:
    st.success(f'A massa molar de {entrada} é aproximadamente {resultado:.2f} g/mol')
  else:
    st.error("Ops! Fórmula escrita errada. Tente novamente!")
