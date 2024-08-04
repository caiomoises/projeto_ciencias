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
    # Plotar gráfico
    plt.figure(figsize=(10, 5))
    plt.plot([0, time], [0, current], marker='o')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Corrente (A)')
    plt.title('Gráfico da Intensidade da Corrente')
    plt.grid(True)
    plt.savefig('current_plot.png')
    plt.close()
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
    # Plotar gráfico
    plt.figure(figsize=(10, 5))
    plt.plot([0, time], [0, charge], marker='o')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Carga (C)')
    plt.title('Gráfico da Quantidade de Carga')
    plt.grid(True)
    plt.savefig('charge_plot.png')
    plt.close()
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
    # Plotar gráfico
    plt.figure(figsize=(10, 5))
    plt.plot([0, current], [0, time], marker='o')
    plt.xlabel('Corrente (A)')
    plt.ylabel('Tempo (s)')
    plt.title('Gráfico do Tempo')
    plt.grid(True)
    plt.savefig('time_plot.png')
    plt.close()
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
    # Plotar gráfico
    x_vals = [x1, x2]
    y_vals = [0, 0]
    plt.figure(figsize=(10, 5))
    plt.scatter(x_vals, y_vals)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Gráfico das Raízes da Equação de Bhaskara')
    plt.grid(True)
    plt.savefig('bhaskara_plot.png')
    plt.close()
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
    # Plotar gráfico
    d_vals = list(range(1, 11))  # Distância de 1 a 10 metros
    e_vals = [K * abs(q) / (d_val**2) for d_val in d_vals]
    plt.figure(figsize=(10, 5))
    plt.plot(d_vals, e_vals, marker='o')
    plt.xlabel('Distância (m)')
    plt.ylabel('Campo Elétrico (N/C)')
    plt.title('Gráfico do Campo Elétrico')
    plt.grid(True)
    plt.savefig('electric_field_plot.png')
    plt.close()
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
    # Plotar gráfico
    d_vals = list(range(1, 11))  # Distância de 1 a 10 metros
    f_vals = [K * abs(q1) * abs(q2) / (d_val**2) for d_val in d_vals]
    plt.figure(figsize=(10, 5))
    plt.plot(d_vals, f_vals, marker='o')
    plt.xlabel('Distância (m)')
    plt.ylabel('Força Elétrica (N)')
    plt.title('Gráfico da Força Elétrica')
    plt.grid(True)
    plt.savefig('electric_force_plot.png')
    plt.close()
    return force, steps

# Função para calcular a velocidade média
def calculate_average_velocity(distance, time):
    if time <= 0:
        st.error("O tempo deve ser maior que zero.")
        return None, ""
    velocity = distance / time
    steps = f"\n## Cálculo da Velocidade Média (m/s)\n" \
            f"\n### Fórmula\n" \
            f"\n$$v = \\frac{{d}}{{t}}$$\n" \
            f"\n### Substituindo os valores\n" \
            f"\n$$v = \\frac{{{distance}}}{{{time}}}$$\n" \
            f"\n### Resultado\n" \
            f"\n$$v = {velocity:.2f} \\text{{ m/s}}$$\n"
    # Plotar gráfico
    x_values = [0, time]
    y_values = [0, velocity]
    plt.figure(figsize=(10, 5))
    plt.plot(x_values, y_values, marker='o')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Velocidade (m/s)')
    plt.title('Gráfico da Velocidade Média')
    plt.grid(True)
    plt.savefig('average_velocity_plot.png')
    plt.close()
    return velocity, steps

# Função para calcular a posição no movimento uniforme
def calculate_position_uniform_motion(velocity, time):
    position = velocity * time
    steps = f"\n## Cálculo da Posição (m)\n" \
            f"\n### Fórmula\n" \
            f"\n$$x = v \\cdot t$$\n" \
            f"\n### Substituindo os valores\n" \
            f"\n$$x = {velocity} \\cdot {time}$$\n" \
            f"\n### Resultado\n" \
            f"\n$$x = {position:.2f} \\text{{ m}}$$\n"
    # Plotar gráfico
    x_values = [0, time]
    y_values = [0, position]
    plt.figure(figsize=(10, 5))
    plt.plot(x_values, y_values, marker='o')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Posição (m)')
    plt.title('Gráfico da Posição no Movimento Uniforme')
    plt.grid(True)
    plt.savefig('uniform_motion_position_plot.png')
    plt.close()
    return position, steps

# Função para calcular a aceleração no movimento uniformemente acelerado
def calculate_acceleration_uniformly_accelerated_motion(initial_velocity, final_velocity, time):
    if time <= 0:
        st.error("O tempo deve ser maior que zero.")
        return None, ""
    acceleration = (final_velocity - initial_velocity) / time
    steps = f"\n## Cálculo da Aceleração (m/s²)\n" \
            f"\n### Fórmula\n" \
            f"\n$$a = \\frac{{v_f - v_i}}{{t}}$$\n" \
            f"\n### Substituindo os valores\n" \
            f"\n$$a = \\frac{{{final_velocity} - {initial_velocity}}}{{{time}}}$$\n" \
            f"\n### Resultado\n" \
            f"\n$$a = {acceleration:.2f} \\text{{ m/s²}}$$\n"
    # Plotar gráfico
    x_values = [0, time]
    y_values = [initial_velocity, final_velocity]
    plt.figure(figsize=(10, 5))
    plt.plot(x_values, y_values, marker='o')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Velocidade (m/s)')
    plt.title('Gráfico da Velocidade no Movimento Uniformemente Acelerado')
    plt.grid(True)
    plt.savefig('uniformly_accelerated_motion_plot.png')
    plt.close()
    return acceleration, steps

# Função para calcular o deslocamento no movimento uniformemente acelerado
def calculate_displacement_uniformly_accelerated_motion(initial_velocity, acceleration, time):
    displacement = initial_velocity * time + 0.5 * acceleration * time**2
    steps = f"\n## Cálculo do Deslocamento (m)\n" \
            f"\n### Fórmula\n" \
            f"\n$$x = v_i \\cdot t + \\frac{1}{2} a \\cdot t^2$$\n" \
            f"\n### Substituindo os valores\n" \
            f"\n$$x = {initial_velocity} \\cdot {time} + \\frac{1}{2} \\cdot {acceleration} \\cdot {time}^2$$\n" \
            f"\n### Resultado\n" \
            f"\n$$x = {displacement:.2f} \\text{{ m}}$$\n"
    # Plotar gráfico
    x_values = [0, time]
    y_values = [0, displacement]
    plt.figure(figsize=(10, 5))
    plt.plot(x_values, y_values, marker='o')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Deslocamento (m)')
    plt.title('Gráfico do Deslocamento no Movimento Uniformemente Acelerado')
    plt.grid(True)
    plt.savefig('displacement_plot.png')
    plt.close()
    return displacement, steps

# Função principal
def main():
    st.title("Calculadora de Física e Matemática")
    
    calculation_type = st.selectbox(
        "Escolha o tipo de cálculo:",
        ["Intensidade da Corrente", "Quantidade de Carga", "Tempo", "Raízes da Equação de Bhaskara",
         "Campo Elétrico", "Força Elétrica", "Velocidade Média", "Movimento Uniforme",
         "Movimento Uniformemente Acelerado"]
    )
    
    if calculation_type == "Intensidade da Corrente":
        charge = st.number_input("Digite a carga (C)", value=0.0)
        time = st.number_input("Digite o tempo (s)", value=0.0)
        if st.button("Calcular Corrente"):
            current, steps = calculate_current(charge, time)
            if current is not None:
                st.write(f"Intensidade da Corrente: {current:.2f} A")
                st.markdown(steps)
                st.image('current_plot.png')

    elif calculation_type == "Quantidade de Carga":
        current = st.number_input("Digite a corrente (A)", value=0.0)
        time = st.number_input("Digite o tempo (s)", value=0.0)
        if st.button("Calcular Carga"):
            charge, steps = calculate_charge(current, time)
            if charge is not None:
                st.write(f"Quantidade de Carga: {charge:.2f} C")
                st.markdown(steps)
                st.image('charge_plot.png')

    elif calculation_type == "Tempo":
        current = st.number_input("Digite a corrente (A)", value=0.0)
        charge = st.number_input("Digite a carga (C)", value=0.0)
        if st.button("Calcular Tempo"):
            time, steps = calculate_time(current, charge)
            if time is not None:
                st.write(f"Tempo: {time:.2f} s")
                st.markdown(steps)
                st.image('time_plot.png')

    elif calculation_type == "Raízes da Equação de Bhaskara":
        a = st.number_input("Digite o valor de a", value=1.0)
        b = st.number_input("Digite o valor de b", value=0.0)
        c = st.number_input("Digite o valor de c", value=0.0)
        if st.button("Calcular Raízes"):
            roots, steps = bhaskara(a, b, c)
            if roots[0] is not None:
                st.write(f"Raízes: x1 = {roots[0]:.2f}, x2 = {roots[1]:.2f}")
                st.markdown(steps)
                st.image('bhaskara_plot.png')

    elif calculation_type == "Campo Elétrico":
        charge = st.number_input("Digite a carga (C)", value=0.0)
        distance = st.number_input("Digite a distância (m)", value=0.0)
        if st.button("Calcular Campo Elétrico"):
            field, steps = calculate_electric_field(charge, distance)
            if field is not None:
                st.write(f"Campo Elétrico: {field:.2f} N/C")
                st.markdown(steps)
                st.image('electric_field_plot.png')

    elif calculation_type == "Força Elétrica":
        charge1 = st.number_input("Digite a carga 1 (C)", value=0.0)
        charge2 = st.number_input("Digite a carga 2 (C)", value=0.0)
        distance = st.number_input("Digite a distância (m)", value=0.0)
        if st.button("Calcular Força Elétrica"):
            force, steps = calculate_electric_force(charge1, charge2, distance)
            if force is not None:
                st.write(f"Força Elétrica: {force:.2f} N")
                st.markdown(steps)
                st.image('electric_force_plot.png')

    elif calculation_type == "Velocidade Média":
        distance = st.number_input("Digite a distância (m)", value=0.0)
        time = st.number_input("Digite o tempo (s)", value=0.0)
        if st.button("Calcular Velocidade Média"):
            velocity, steps = calculate_average_velocity(distance, time)
            if velocity is not None:
                st.write(f"Velocidade Média: {velocity:.2f} m/s")
                st.markdown(steps)
                st.image('average_velocity_plot.png')

    elif calculation_type == "Movimento Uniforme":
        velocity = st.number_input("Digite a velocidade (m/s)", value=0.0)
        time = st.number_input("Digite o tempo (s)", value=0.0)
        if st.button("Calcular Posição"):
            position, steps = calculate_position_uniform_motion(velocity, time)
            if position is not None:
                st.write(f"Posição: {position:.2f} m")
                st.markdown(steps)
                st.image('uniform_motion_position_plot.png')

    elif calculation_type == "Movimento Uniformemente Acelerado":
        initial_velocity = st.number_input("Digite a velocidade inicial (m/s)", value=0.0)
        final_velocity = st.number_input("Digite a velocidade final (m/s)", value=0.0)
        time = st.number_input("Digite o tempo (s)", value=0.0)
        if st.button("Calcular Aceleração"):
            acceleration, steps = calculate_acceleration_uniformly_accelerated_motion(initial_velocity, final_velocity, time)
            if acceleration is not None:
                st.write(f"Aceleração: {acceleration:.2f} m/s²")
                st.markdown(steps)
                st.image('uniformly_accelerated_motion_plot.png')

        if st.button("Calcular Deslocamento"):
            acceleration, steps = calculate_acceleration_uniformly_accelerated_motion(initial_velocity, final_velocity, time)
            displacement, steps = calculate_displacement_uniformly_accelerated_motion(initial_velocity, acceleration, time)
            if displacement is not None:
                st.write(f"Deslocamento: {displacement:.2f} m")
                st.markdown(steps)
                st.image('displacement_plot.png')

if __name__ == "__main__":
    main()
