#!/bin/bash

echo "🚀 Fazendo deploy do projeto Lambda + S3..."

# Nome da stack no CloudFormation
STACK_NAME="meu-projeto-lambda-s3"

# Verificar se AWS CLI está configurado
if ! aws sts get-caller-identity > /dev/null 2>&1; then
    echo "❌ AWS CLI não configurado. Execute: aws configure"
    exit 1
fi

echo "📋 Criando/atualizando stack CloudFormation..."

# Deploy da stack
aws cloudformation deploy \
    --template-file cloudformation.yaml \
    --stack-name $STACK_NAME \
    --capabilities CAPABILITY_IAM \
    --region us-east-1

if [ $? -eq 0 ]; then
    echo "✅ Deploy realizado com sucesso!"
    
    # Mostrar os outputs da stack
    echo ""
    echo "📊 Recursos criados:"
    aws cloudformation describe-stacks \
        --stack-name $STACK_NAME \
        --query 'Stacks[0].Outputs[*].[OutputKey,OutputValue]' \
        --output table
    
    echo ""
    echo "🎉 Pronto! Agora você pode:"
    echo "1. Ir no console AWS → S3"
    echo "2. Procurar o bucket input e fazer upload de um arquivo"
    echo "3. Verificar o bucket output para ver o arquivo processado"
    
else
    echo "❌ Erro no deploy!"
    exit 1
fi