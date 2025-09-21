# 📁 Projeto Lambda + S3 - Automação 

> **Projeto básico para aprendizado de AWS Lambda e S3 com CloudFormation**

## 🎯 O que este projeto faz?

1. **Você faz upload** de um arquivo no bucket S3
2. **Lambda é ativada automaticamente** quando o arquivo chega
3. **Lambda processa** o arquivo (adiciona timestamp no nome)
4. **Arquivo processado** é salvo em outro bucket

Simples assim! 🚀

## 📋 Pré-requisitos

- Conta AWS (pode usar free tier)
- AWS CLI instalado
- Conhecimento básico de AWS

## 🏗️ Arquitetura

```
Arquivo → S3 Bucket Input → Lambda → S3 Bucket Output
```

## 📁 Estrutura do Projeto

```
meu-projeto-lambda-s3/
├── README.md
├── cloudformation.yaml    (cria tudo na AWS)
├── lambda_function.py     (código da função)
└── deploy.sh             (script para subir tudo)
```

## 🚀 Como usar

### Passo 1: Baixar os arquivos
```bash
git clone seu-repositorio
cd meu-projeto-lambda-s3
```

### Passo 2: Fazer deploy
```bash
chmod +x deploy.sh
./deploy.sh
```

### Passo 3: Testar
1. Vá no console AWS → S3
2. Procure o bucket `meu-bucket-input-[números]`
3. Faça upload de qualquer arquivo
4. Vá no bucket `meu-bucket-output-[números]`
5. Veja seu arquivo processado com timestamp!

## 📝 O que aprendi

### AWS Lambda
- ✅ Como criar função serverless
- ✅ Como configurar triggers do S3
- ✅ Como processar arquivos automaticamente

### Amazon S3
- ✅ Como criar buckets
- ✅ Como configurar eventos
- ✅ Como mover arquivos entre buckets

### CloudFormation
- ✅ Como criar infraestrutura como código
- ✅ Como conectar Lambda com S3
- ✅ Como configurar permissões (IAM)

## 🔧 Personalizações que fiz

```python
# No código Lambda, mudei:
- Nome do arquivo processado
- Localização de output
- Logs personalizados
```

## 💡 Próximos passos

- [ ] Adicionar processamento de imagens
- [ ] Criar notificações por email
- [ ] Monitorar com CloudWatch
- [ ] Adicionar mais tipos de arquivos

## 🐛 Problemas que encontrei

1. **Erro de permissão**: Esqueci de dar permissão para Lambda acessar S3
2. **Bucket já existe**: Mudei o nome para único
3. **Função não ativa**: Configurei o trigger corretamente

## 📚 Links úteis

- [AWS Lambda Docs](https://docs.aws.amazon.com/lambda/)
- [S3 Event Notifications](https://docs.aws.amazon.com/s3/latest/userguide/NotificationHowTo.html)
- [CloudFormation Tutorial](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/GettingStarted.Walkthrough.html)

## 🏆 Resultado

**Antes**: Upload manual de arquivos
**Depois**: Processamento automático com Lambda! ⚡

---

⭐ **Projeto simples mas funcional para portfólio!** ⭐

*Feito com ❤️ durante o bootcamp DIO*
