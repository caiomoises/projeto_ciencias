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
        return None, ""
    current = charge / time
    if current > max_current:
        st.warning("Aviso: A corrente está muito alta! Risco de sobrecarga ou curto-circuito.")
    steps = f"\n## Cálculo da Intensidade da Corrente (A)\n" \
            f"\n### Fórmula\n" \
            f"\n$$I = \\frac{{Q}}{{t}}$$\n" \
            f"\n### Substituindo os valores\n" \
            f"\n$$I = \\frac{{{charge}}}{{{time}}}$$\n" \
            f"\n### Resultado\n" \
            f"\n$$I = {current:.2f} \\text{{ A}}$$\n"
    return current, steps

# Função para calcular a quantidade de carga
def calculate_charge(current, time):
    charge = current * time
    steps = f"\n## Cálculo da Quantidade de Carga (C)\n" \
            f"\n### Fórmula\n" \
            f"\n$$Q = I \\cdot t$$\n" \
            f"\n### Substituindo os valores\n" \
            f"\n$$Q = {current} \\cdot {time}$$\n" \
            f"\n### Resultado\n" \
            f"\n$$Q = {charge:.2f} \\text{{ C}}$$\n"
    return charge, steps

# Função para calcular o tempo
def calculate_time(current, charge):
    if current <= 0:
        st.error("A corrente deve ser maior que zero.")
        return None, ""
    time = charge / current
    steps = f"\n## Cálculo do Tempo (s)\n" \
            f"\n### Fórmula\n" \
            f"\n$$t = \\frac{{Q}}{{I}}$$\n" \
            f"\n### Substituindo os valores\n" \
            f"\n$$t = \\frac{{{charge}}}{{{current}}}$$\n" \
            f"\n### Resultado\n" \
            f"\n$$t = {time:.2f} \\text{{ s}}$$\n"
    return time, steps

# Função para calcular as raízes da equação de Bhaskara
def bhaskara(a, b, c):
    delta = b ** 2 - 4 * a * c
    steps = f"\n## Cálculo das Raízes pela Fórmula de Bhaskara\n" \
            f"\n### Cálculo do Delta\n" \
            f"\n$$\\Delta = b^2 - 4ac$$\n" \
            f"\n$$\\Delta = ({b})^2 - 4 \\cdot {a} \\cdot {c}$$\n" \
            f"\n$$\\Delta = {b * b} - {4 * a * c}$$\n" \
            f"\n$$\\Delta = {delta}$$\n"
    if delta < 0:
        steps += "\n### Não existem raízes reais porque \\(\\Delta < 0\\)."
        return (None, None), steps
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    steps += f"\n### Cálculo das Raízes\n" \
             f"\n$$x = \\frac{{-b \\pm \\sqrt{{\\Delta}}}}{{2a}}$$\n" \
             f"\n$$x_1 = \\frac{{-{b} + \\sqrt{{{delta}}}}}{{2 \\cdot {a}}}$$\n" \
             f"\n$$x_1 = {x1:.2f}$$\n" \
             f"\n$$x_2 = \\frac{{-{b} - \\sqrt{{{delta}}}}}{{2 \\cdot {a}}}$$\n" \
             f"\n$$x_2 = {x2:.2f}$$\n"
    return (x1, x2), steps

# Função para calcular o campo elétrico
def calculate_electric_field(q, d):
    if d == 0:
        st.error("A distância não pode ser zero.")
        return None, ""
    field = K * abs(q) / d**2
    steps = f"\n## Cálculo do Campo Elétrico (N/C)\n" \
            f"\n### Fórmula\n" \
            f"\n$$E = \\frac{{K \\cdot |q|}}{{d^2}}$$\n" \
            f"\n### Substituindo os valores\n" \
            f"\n$$E = \\frac{{{K} \\cdot |{q}|}}{{{d}^2}}$$\n" \
            f"\n### Resultado\n" \
            f"\n$$E = {field:.2f} \\text{{ N/C}}$$\n"
    return field, steps

# Função para calcular a força elétrica
def calculate_electric_force(q1, q2, d):
    if d == 0:
        st.error("A distância não pode ser zero.")
        return None, ""
    force = K * abs(q1) * abs(q2) / d**2
    steps = f"\n## Cálculo da Força Elétrica (N)\n" \
            f"\n### Fórmula\n" \
            f"\n$$F = \\frac{{K \\cdot |q_1| \\cdot |q_2|}}{{d^2}}$$\n" \
            f"\n### Substituindo os valores\n" \
            f"\n$$F = \\frac{{{K} \\cdot |{q1}| \\cdot |{q2}|}}{{{d}^2}}$$\n" \
            f"\n### Resultado\n" \
            f"\n$$F = {force:.2f} \\text{{ N}}$$\n"
    return force, steps

# Função para calcular a energia potencial elétrica
def calculate_electric_potential_energy(q, d):
    if d == 0:
        st.error("A distância não pode ser zero.")
        return None, ""
    energy = K * abs(q) / d
    steps = f"\n## Cálculo da Energia Potencial Elétrica (J)\n" \
            f"\n### Fórmula\n" \
            f"\n$$U = \\frac{{K \\cdot |q|}}{{d}}$$\n" \
            f"\n### Substituindo os valores\n" \
            f"\n$$U = \\frac{{{K} \\cdot |{q}|}}{{{d}}}$$\n" \
            f"\n### Resultado\n" \
            f"\n$$U = {energy:.2f} \\text{{ J}}$$\n"
    return energy, steps

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
        result, steps = calculate_current(charge, time)
        if result is not None:
            st.success(f"A intensidade da corrente é: {result:.2f} A")
            st.markdown(steps)
            plot_graph([0, time], [0, result], 'Tempo (s)', 'Corrente (A)', 'Intensidade da Corrente')

elif operation == "Quantidade de Carga (C)":
    current = st.number_input("Insira a intensidade da corrente (A):", step=0.01)
    time = st.number_input("Insira o tempo (s):", step=0.01)
    if st.button("Calcular"):
        result, steps = calculate_charge(current, time)
        st.success(f"A quantidade de carga é: {result:.2f} C")
        st.markdown(steps)
        plot_graph([0, time], [0, result], 'Tempo (s)',
                    'Carga (C)', 'Quantidade de Carga')

elif operation == "Tempo (s)":
    current = st.number_input("Insira a intensidade da corrente (A):", step=0.01)
    charge = st.number_input("Insira a quantidade de carga (C):", step=0.01)
    if st.button("Calcular"):
        result, steps = calculate_time(current, charge)
        if result is not None:
            st.success(f"O tempo é: {result:.2f} s")
            st.markdown(steps)
            plot_graph([0, charge], [0, result], 'Carga (C)', 'Tempo (s)', 'Tempo de Carga')

elif operation == "Fórmula de Bhaskara":
    a = st.number_input("Insira o coeficiente a:", step=0.01)
    b = st.number_input("Insira o coeficiente b:", step=0.01)
    c = st.number_input("Insira o coeficiente c:", step=0.01)
    if st.button("Calcular"):
        (x1, x2), steps = bhaskara(a, b, c)
        if x1 is not None and x2 is not None:
            st.success(f"As raízes são: x1 = {x1:.2f}, x2 = {x2:.2f}")
        st.markdown(steps)
        if x1 is not None and x2 is not None:
            plot_graph([a, b, c], [x1, x2, 0], 'Coeficientes', 'Raízes', 'Raízes da Equação de Bhaskara')

elif operation == "Campo Elétrico (N/C)":
    q = st.number_input("Insira a carga (C):", step=0.01)
    d = st.number_input("Insira a distância (m):", step=0.01)
    if st.button("Calcular"):
        result, steps = calculate_electric_field(q, d)
        if result is not None:
            st.success(f"O campo elétrico é: {result:.2f} N/C")
            st.markdown(steps)
            plot_graph([0, d], [0, result], 'Distância (m)', 'Campo Elétrico (N/C)', 'Campo Elétrico')

elif operation == "Força Elétrica (N)":
    q1 = st.number_input("Insira a carga 1 (C):", step=0.01)
    q2 = st.number_input("Insira a carga 2 (C):", step=0.01)
    d = st.number_input("Insira a distância (m):", step=0.01)
    if st.button("Calcular"):
        result, steps = calculate_electric_force(q1, q2, d)
        if result is not None:
            st.success(f"A força elétrica é: {result:.2f} N")
            st.markdown(steps)
            plot_graph([0, d], [0, result], 'Distância (m)', 'Força Elétrica (N)', 'Força Elétrica')

elif operation == "Energia Potencial Elétrica (J)":
    q = st.number_input("Insira a carga (C):", step=0.01)
    d = st.number_input("Insira a distância (m):", step=0.01)
    if st.button("Calcular"):
        result, steps = calculate_electric_potential_energy(q, d)
        if result is not None:
            st.success(f"A energia potencial elétrica é: {result:.2f} J")
            st.markdown(steps)
            plot_graph([0, d], [0, result], 'Distância (m)', 'Energia Potencial Elétrica (J)', 'Energia Potencial Elétrica')
