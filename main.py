import streamlit as st
import math
import matplotlib.pyplot as plt

# Constante de Coulomb
K = 9e9  # N m²/C²

# Definindo o valor limite de corrente para verificação de segurança
max_current = 10  # Amperes

# Função para calcular a intensidade da corrente
def calculate_current(charge, time):
    if time <= 0:
        st.error("O tempo deve ser maior que zero.")
        return None
    current = charge / time
    if current > max_current:
        st.warning("Aviso: A corrente está muito alta! Risco de sobrecarga ou curto-circuito.")
    return current

# Função para calcular a quantidade de carga
def calculate_charge(current, time):
    return current * time

# Função para calcular o tempo
def calculate_time(current, charge):
    if current <= 0:
        st.error("A corrente deve ser maior que zero.")
        return None
    return charge / current

# Função para calcular as raízes da equação de Bhaskara
def bhaskara(a, b, c):
    delta = b ** 2 - 4 * a * c
    steps = f"\n$$\\Delta = b^2 - 4ac$$\n" \
            f"\n$$\\Delta = ({b})^2 - 4 \\cdot {a} \\cdot {c}$$\n" \
            f"\n$$\\Delta = {b * b} - {4 * a * c}$$\n" \
            f"\n$$\\Delta = {delta}$$\n"
    if delta < 0:
        steps += "Não existem raízes reais porque \\(\\Delta < 0\\)."
        return (None, None), steps
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    steps += f"\n$$x = \\frac{{-b \\pm \\sqrt{{\\Delta}}}}{{2a}}$$\n" \
             f"\n$$x_1 = \\frac{{-{b} + \\sqrt{{delta}}}}{{2 \\cdot {a}}}$$\n" \
             f"\n$$x_1 = {x1:.2f}$$\n" \
             f"\n$$x_2 = \\frac{{-{b} - \\sqrt{{delta}}}}{{2 \\cdot {a}}}$$\n" \
             f"\n$$x_2 = {x2:.2f}$$\n"
    return (x1, x2), steps

# Função para calcular o campo elétrico
def calculate_electric_field(q, d):
    if d == 0:
        st.error("A distância não pode ser zero.")
        return None
    return K * abs(q) / d**2

# Função para calcular a força elétrica
def calculate_electric_force(q1, q2, d):
    if d == 0:
        st.error("A distância não pode ser zero.")
        return None
    return K * abs(q1) * abs(q2) / d**2

# Função para calcular a energia potencial elétrica
def calculate_electric_potential_energy(q, d):
    if d == 0:
        st.error("A distância não pode ser zero.")
        return None
    return K * abs(q) / d

# Função para gerar e exibir gráfico
def plot_graph(x_values, y_values, x_label, y_label, title):
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values, marker='o')
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    st.pyplot(fig)

st.title("Calculadora Multifuncional")

operation = st.selectbox("Escolha a operação:", [
    "Intensidade da Corrente (A)",
    "Quantidade de Carga (C)",
    "Tempo (s)",
    "Fórmula de Bhaskara",
    "Campo Elétrico (N/C)",
    "Força Elétrica (N)",
    "Energia Potencial Elétrica (J)"
])

if operation == "Intensidade da Corrente (A)":
    charge = st.number_input("Insira a quantidade de carga (C):", step=0.01)
    time = st.number_input("Insira o tempo (s):", step=0.01)
    if st.button("Calcular"):
        result = calculate_current(charge, time)
        if result is not None:
            st.success(f"A intensidade da corrente é: {result:.2f} A")
            plot_graph([0, time], [0, result], 'Tempo (s)', 'Corrente (A)', 'Intensidade da Corrente')

elif operation == "Quantidade de Carga (C)":
    current = st.number_input("Insira a intensidade da corrente (A):", step=0.01)
    time = st.number_input("Insira o tempo (s):", step=0.01)
    if st.button("Calcular"):
        result = calculate_charge(current, time)
        st.success(f"A quantidade de carga é: {result:.2f} C")
        plot_graph([0, time], [0, result], 'Tempo (s)', 'Carga (C)', 'Quantidade de Carga')

elif operation == "Tempo (s)":
    current = st.number_input("Insira a intensidade da corrente (A):", step=0.01)
    charge = st.number_input("Insira a quantidade de carga (C):", step=0.01)
    if st.button("Calcular"):
        result = calculate_time(current, charge)
        if result is not None:
            st.success(f"O tempo é: {result:.2f} s")
            plot_graph([0, charge], [0, result], 'Carga (C)', 'Tempo (s)', 'Tempo')

elif operation == "Fórmula de Bhaskara":
    a = st.number_input("Insira o valor de a:", step=0.01)
    b = st.number_input("Insira o valor de b:", step=0.01)
    c = st.number_input("Insira o valor de c:", step=0.01)
    if st.button("Calcular"):
        (x1, x2), steps = bhaskara(a, b, c)
        st.markdown(steps)
        if x1 is None:
            st.error("Não existem raízes reais.")
        else:
            st.success(f"As raízes da equação são: x1 = {x1:.2f}, x2 = {x2:.2f}")

elif operation == "Campo Elétrico (N/C)":
    q = st.number_input("Insira a carga (C):", step=0.01)
    d = st.number_input("Insira a distância (m):", step=0.01)
    if st.button("Calcular"):
        result = calculate_electric_field(q, d)
        if result is not None:
            st.success(f"O campo elétrico é: {result:.2f} N/C")
            plot_graph([0, d], [0, result], 'Distância (m)', 'Campo Elétrico (N/C)', 'Campo Elétrico')

elif operation == "Força Elétrica (N)":
    q1 = st.number_input("Insira a carga 1 (C):", step=0.01)
    q2 = st.number_input("Insira a carga 2 (C):", step=0.01)
    d = st.number_input("Insira a distância (m):", step=0.01)
    if st.button("Calcular"):
        result = calculate_electric_force(q1, q2, d)
        if result is not None:
            st.success(f"A força elétrica é: {result:.2f} N")
            plot_graph([0, d], [0, result], 'Distância (m)', 'Força Elétrica (N)', 'Força Elétrica')

elif operation == "Energia Potencial Elétrica (J)":
    q = st.number_input("Insira a carga (C):", step=0.01)
    d = st.number_input("Insira a distância (m):", step=0.01)
    if st.button("Calcular"):
        result = calculate_electric_potential_energy(q, d)
        if result is not None:
            st.success(f"A energia potencial elétrica é: {result:.2f} J")
            plot_graph([0, d], [0, result], 'Distância (m)', 'Energia Potencial Elétrica (J)', 'Energia Potencial Elétrica')
