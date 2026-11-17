from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import datetime

def gerar_relatorio_medico(filename="diagnostico_medico.pdf"):
    # Cria o arquivo PDF com tamanho de página Padrão (Letter)
    # Dimensões aproximadas: 612 x 792 pontos
    c = canvas.Canvas(filename, pagesize=letter)
    largura, altura = letter

    # --- CONFIGURAÇÕES DE LAYOUT (Coordenadas) ---
    margem_esquerda = 50
    linha_atual = altura - 60  # Começa no topo da página

    # 1. CABEÇALHO DO HOSPITAL
    c.setFont("Helvetica-Bold", 16)
    c.drawString(margem_esquerda, linha_atual, "CENTRO MÉDICO HORIZONTE")
    
    c.setFont("Helvetica", 9)
    c.setFillColorRGB(0.3, 0.3, 0.3) # Cor cinza para subtítulos
    linha_atual -= 15
    c.drawString(margem_esquerda, linha_atual, "Av. Principal, 1234 - Contato: (11) 99999-9999")
    
    # Linha divisória do cabeçalho
    linha_atual -= 15
    c.setStrokeColorRGB(0.7, 0.7, 0.7)
    c.setLineWidth(1)
    c.line(margem_esquerda, linha_atual, largura - margem_esquerda, linha_atual)

    # 2. DADOS DO PACIENTE
    c.setFillColorRGB(0, 0, 0) # Retorna para o preto
    linha_atual -= 30
    c.setFont("Helvetica-Bold", 12)
    c.drawString(margem_esquerda, linha_atual, "DADOS DO PACIENTE")
    
    c.setFont("Helvetica", 10)
    linha_atual -= 20
    c.drawString(margem_esquerda, linha_atual, "Paciente: João dos Santos Silva")
    c.drawString(largura / 2, linha_atual, f"Data: {datetime.date.today().strftime('%d/%m/%Y')}")
    
    linha_atual -= 15
    c.drawString(margem_esquerda, linha_atual, "Idade: 45 anos")
    c.drawString(largura / 2, linha_atual, "Cédula de Identidade: 12.345.678-X")

    # Linha divisória
    linha_atual -= 15
    c.line(margem_esquerda, linha_atual, largura - margem_esquerda, linha_atual)

    # 3. CORPO DO DIAGNÓSTICO
    linha_atual -= 30
    c.setFont("Helvetica-Bold", 12)
    c.drawString(margem_esquerda, linha_atual, "DIAGNÓSTICO MÉDICO E CONCLUSÃO")
    
    c.setFont("Helvetica", 10)
    linha_atual -= 25
    
    # Texto longo simulando o relatório clínico
    linhas_texto = [
        "O paciente apresentou quadro clínico compatível com fadiga crônica secundária a distúrbios",
        "do sono e estresse metabólico leve. Os exames laboratoriais de rotina não apresentaram",
        "alterações significativas nas funções hepática ou renal.",
        "",
        "Recomenda-se acompanhamento nutricional, adequação da higiene do sono e retorno",
        "em 60 dias para reavaliação clínica geral."
    ]
    
    for linha in linhas_texto:
        c.drawString(margem_esquerda, linha_atual, linha)
        linha_atual -= 15 # Espaçamento entre as linhas de texto

    # 4. ASSINATURA E FECHAMENTO (No rodapé da página)
    linha_atual = 120 # Fixando uma coordenada próxima ao fundo da página
    c.setStrokeColorRGB(0.5, 0.5, 0.5)
    c.line(largura / 2 - 100, linha_atual, largura / 2 + 100, linha_atual) # Linha da assinatura
    
    linha_atual -= 15
    c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(largura / 2, linha_atual, "Dr. Alexandre Pedrosa")
    
    linha_atual -= 12
    c.setFont("Helvetica", 9)
    c.drawCentredString(largura / 2, linha_atual, "CRM/SP 123456")

    # Salva o arquivo gerado
    c.save()
    print(f"Relatório '{filename}' gerado com sucesso!")

# Executa a função
if __name__ == "__main__":
    gerar_relatorio_medico()