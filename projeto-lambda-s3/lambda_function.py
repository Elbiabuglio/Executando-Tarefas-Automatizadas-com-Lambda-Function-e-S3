import json
import boto3
import os
from datetime import datetime
from urllib.parse import unquote_plus

# Cliente S3
s3 = boto3.client('s3')

def lambda_handler(event, context):
    """
    Função Lambda que processa arquivos quando são enviados para o S3
    """
    
    print("🚀 Lambda ativada! Processando arquivo...")
    
    # Bucket de destino (onde vai salvar o arquivo processado)
    output_bucket = os.environ['OUTPUT_BUCKET']
    
    try:
        # Processa cada arquivo que foi enviado
        for record in event['Records']:
            # Pega informações do arquivo
            input_bucket = record['s3']['bucket']['name']
            file_key = unquote_plus(record['s3']['object']['key'])
            file_size = record['s3']['object']['size']
            
            print(f"📁 Arquivo recebido: {file_key}")
            print(f"📊 Tamanho: {file_size} bytes")
            print(f"🗂️ Bucket origem: {input_bucket}")
            
            # Baixa o arquivo do S3
            print("⬇️ Baixando arquivo...")
            response = s3.get_object(Bucket=input_bucket, Key=file_key)
            file_content = response['Body'].read()
            content_type = response.get('ContentType', 'application/octet-stream')
            
            # Processa o arquivo (exemplo: adiciona timestamp)
            processed_content = processar_arquivo(file_content, file_key)
            
            # Cria nome do arquivo processado
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            new_file_name = f"processado_{timestamp}_{file_key}"
            
            # Salva arquivo processado no bucket de output
            print(f"⬆️ Salvando arquivo processado: {new_file_name}")
            s3.put_object(
                Bucket=output_bucket,
                Key=new_file_name,
                Body=processed_content,
                ContentType=content_type,
                Metadata={
                    'arquivo-original': file_key,
                    'processado-em': timestamp,
                    'tamanho-original': str(file_size)
                }
            )
            
            print(f"✅ Sucesso! Arquivo salvo em: {output_bucket}/{new_file_name}")
        
        # Retorna sucesso
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Arquivo processado com sucesso!',
                'arquivos_processados': len(event['Records'])
            })
        }
    
    except Exception as e:
        print(f"❌ Erro ao processar arquivo: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'Erro no processamento',
                'erro': str(e)
            })
        }

def processar_arquivo(conteudo, nome_arquivo):
    """
    Aqui você pode processar o arquivo como quiser!
    Por enquanto, só retorna o conteúdo original.
    """
    
    print("🔄 Processando conteúdo do arquivo...")
    
    # Pega a extensão do arquivo
    extensao = nome_arquivo.split('.')[-1].lower() if '.' in nome_arquivo else ''
    
    # Exemplos de processamento que você pode fazer:
    
    if extensao in ['txt', 'md']:
        # Para arquivos de texto, adiciona um cabeçalho
        print("📝 Processando arquivo de texto...")
        cabecalho = f"=== PROCESSADO EM {datetime.now()} ===\n\n"
        if isinstance(conteudo, bytes):
            conteudo = conteudo.decode('utf-8')
        return (cabecalho + conteudo).encode('utf-8')
    
    elif extensao in ['jpg', 'jpeg', 'png', 'gif']:
        # Para imagens, por enquanto só retorna original
        # Aqui você poderia usar PIL/Pillow para redimensionar, etc.
        print("🖼️ Processando imagem...")
        return conteudo
    
    elif extensao == 'pdf':
        # Para PDFs, por enquanto só retorna original
        # Aqui você poderia extrair texto, etc.
        print("📄 Processando PDF...")
        return conteudo
    
    else:
        # Para outros tipos, apenas retorna original
        print("📦 Processando arquivo genérico...")
        return conteudo

def adicionar_metadados_customizados(conteudo, nome_arquivo):
    """
    Exemplo de função para adicionar metadados
    (você pode criar suas próprias funções de processamento)
    """
    
    # Exemplo: adiciona informações ao final de arquivos de texto
    if nome_arquivo.endswith('.txt'):
        info_extra = f"\n\n--- Processado por Lambda em {datetime.now()} ---"
        return conteudo + info_extra.encode('utf-8')
    
    return conteudo