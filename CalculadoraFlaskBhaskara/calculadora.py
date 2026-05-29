import math as mt
from flask import Flask, render_template, request

def calcular():
    num1 = float(request.form["num1"])
    operacao = request.form["operacao"]

    if operacao == "sqrt":
        if num1 < 0:
            resultado = "Erro"
            etapas = "Não existe raiz quadrada de número negativo."
        else:
            resultado = mt.sqrt(num1)
            etapas = f"√{num1} = {resultado}"
    
    # CORREÇÃO: Alterado para "BHASKARA" em maiúsculas para coincidir com o HTML
    elif operacao == "BHASKARA":
        if num1 == 0:
            resultado = "Erro"
            etapas = "O coeficiente 'a' não pode ser igual a zero em uma equação do 2º grau."
        else:
            b = float(request.form["num2"])
            c = float(request.form["num3"])

            delta = b**2 - 4*num1*c

            if delta < 0:
                resultado = "Erro"
                etapas = f"Δ = {delta}<br>Delta negativo. Não existem raízes reais."
            else:
                x1 = (-b + mt.sqrt(delta)) / (2 * num1)
                x2 = (-b - mt.sqrt(delta)) / (2 * num1)

                resultado = f"x1 = {x1} | x2 = {x2}"
                etapas = (
                    f"Δ = {b}² - 4 * {num1} * {c} = {delta}<br>"
                    f"x1 = (-({b}) + √{delta}) / (2 * {num1}) = {x1}<br>"
                    f"x2 = (-({b}) - √{delta}) / (2 * {num1}) = {x2}"
                )        

    else:
        num2_raw = request.form.get("num2", "")

        if operacao == "log":
            if num1 <= 0:
                resultado = "Erro"
                etapas = "O logaritmando (num1) deve ser maior que zero."
            else:
                if num2_raw == "":
                    resultado = mt.log(num1)
                    etapas = f"ln({num1}) = {resultado}"
                else:
                    num2 = float(num2_raw)
                    if num2 <= 0 or num2 == 1:
                        resultado = "Erro"
                        etapas = "A base (num2) deve ser maior que zero e diferente de 1."
                    else:
                        resultado = mt.log(num1, num2)
                        etapas = f"log_{num2}({num1}) = {resultado}"

        else:
            num2 = float(num2_raw)

            if operacao == "+":
                resultado = num1 + num2
                etapas = f"{num1} + {num2} = {resultado}"
            elif operacao == "-":
                resultado = num1 - num2
                etapas = f"{num1} - {num2} = {resultado}"
            elif operacao == "*":
                resultado = num1 * num2
                etapas = f"{num1} * {num2} = {resultado}"
            elif operacao == "/":
                if num2 != 0:
                    resultado = num1 / num2
                    etapas = f"{num1} / {num2} = {resultado}"
                else:
                    resultado = "Erro"
                    etapas = "Divisão por zero não é permitida."
            elif operacao == "**":
                resultado = num1**num2
                etapas = f"{num1} ** {num2} = {resultado}"
            else:
                resultado = "Operação inválida"
                etapas = "A operação selecionada é inválida."

    return render_template(
        "calculadora.html", etapas=etapas, resultados=resultado
    )
