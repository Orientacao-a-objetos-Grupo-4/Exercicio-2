
---

## 🧩 O que devo fazer?

Construa as classes acima e implemente os seguintes comportamentos:

1️⃣ **Verificar se um aluno foi aprovado** através da média de duas notas.  

2️⃣ **Aluno do Ensino Médio:** é aprovado com média **≥ 6**.  

3️⃣ **Aluno da Graduação:** é aprovado com média **≥ 7**.  

4️⃣ **Retornar o nome do aluno**, sua **matrícula** e se ele foi **aprovado ou não**.  

5️⃣ **Retornar o nome do professor** e sua **titulação máxima**.  

---

## ⚙️ Estrutura sugerida

### 🧍‍♂️ Classe `Pessoa`
- Atributos: `nome`

---

### 👨‍🏫 Classe `Professor` (herda de Pessoa)
- Atributos: `titulacaoMaxima`  
- Métodos: retornar nome e titulação

---

#Exercicio 2 
## 📊 Olha esse diagrama!

O diagrama apresentado representa a hierarquia de classes abaixo:
<br/>
<img width="191" height="150" alt="image" src="https://github.com/user-attachments/assets/c4065a64-ef19-4d4d-84b9-daee22eaa145" />


### 🎓 Classe `Aluno` (herda de Pessoa)
- Atributos: `matricula`, `nota1`, `nota2`  
- Métodos:  
  - `calcularMedia()`  
  - `verificarAprovacao()` *(método abstrato ou sobrescrito nas subclasses)*

---

### 🏫 Classe `AlunoEnsinoMedio` (herda de Aluno)
- Regra: Aprovado se **média ≥ 6**

---

### 🎓 Classe `AlunoGraduacao` (herda de Aluno)
- Regra: Aprovado se **média ≥ 7**

---

## 📦 Entrega

📅 **Data:** vide exercício anterior  

📨 **Forma de entrega:** conforme instruções anteriores  

🏁 **Pontuação:** igual ao exercício anterior  

❓ **Dúvidas:** mesmas orientações  

📝 **Observação final:** idem  

---

## 🍀 Boa sorte!

> “Programar é transformar lógica em realidade.”  
>
> 🚀 **Mãos à obra e boa codificação!**
