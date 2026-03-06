"""
Agente de IA para Pesquisa de Mercado - Tudo do Momento Presentes
Este script realiza pesquisas de mercado semanais em sites de dropshipping
e atualiza automaticamente o catálogo de produtos.
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from openai import OpenAI
import json
from datetime import datetime
from src.models.user import db
from src.models.product import Product
from flask import Flask

# Configurar Flask app para acesso ao banco de dados
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(os.path.dirname(__file__), 'database', 'app.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Inicializar cliente OpenAI
client = OpenAI()

# Categorias de produtos
CATEGORIES = {
    'esportivos': 'Materiais esportivos para todas as idades e gêneros',
    'games': 'Produtos de informática voltados a games',
    'vestuario': 'Vestuário esportivo e social para adolescentes e adultos'
}

# Sites de dropshipping conhecidos (exemplos)
DROPSHIPPING_SITES = [
    'AliExpress',
    'Oberlo',
    'Spocket',
    'Modalyst',
    'SaleHoo',
    'Wholesale2B'
]


def generate_market_research_prompt():
    """Gerar prompt para pesquisa de mercado"""
    return f"""
Você é um especialista em pesquisa de mercado para dropshipping. 
Sua tarefa é gerar uma lista de produtos mais vendidos atualmente nas seguintes categorias:

1. Materiais esportivos (para todas as idades e gêneros)
2. Produtos de informática voltados a games
3. Vestuário esportivo e social (para adolescentes e adultos)

Para cada categoria, forneça 5 produtos populares com as seguintes informações:
- Nome do produto
- Descrição detalhada (2-3 frases)
- Categoria (esportivos, games, ou vestuario)
- Preço de compra estimado (em reais)
- Preço de venda sugerido (com margem de lucro de 30-50%)
- Fornecedor sugerido (escolha entre: {', '.join(DROPSHIPPING_SITES)})
- URL do fornecedor (formato: https://exemplo.com/produto)
- Estoque inicial sugerido

Retorne os dados em formato JSON válido com a seguinte estrutura:
{{
  "products": [
    {{
      "name": "Nome do Produto",
      "description": "Descrição detalhada do produto",
      "category": "esportivos|games|vestuario",
      "purchase_price": 100.00,
      "sale_price": 150.00,
      "supplier": "Nome do Fornecedor",
      "supplier_url": "https://exemplo.com/produto",
      "stock": 50,
      "image_url": "https://exemplo.com/imagem.jpg"
    }}
  ]
}}

Importante:
- Os preços devem ser realistas para o mercado brasileiro
- As descrições devem ser atrativas e informativas
- Foque em produtos que estão em alta no mercado atual
- Use URLs fictícias mas realistas para os fornecedores
"""


def call_ai_for_market_research():
    """Chamar a IA para realizar pesquisa de mercado"""
    try:
        print("Iniciando pesquisa de mercado com IA...")
        
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": "Você é um especialista em e-commerce e pesquisa de mercado para dropshipping."
                },
                {
                    "role": "user",
                    "content": generate_market_research_prompt()
                }
            ],
            temperature=0.7,
            max_tokens=3000
        )
        
        # Extrair resposta
        content = response.choices[0].message.content
        
        # Tentar extrair JSON da resposta
        # A IA pode retornar o JSON dentro de ```json ... ```
        if "```json" in content:
            json_start = content.find("```json") + 7
            json_end = content.find("```", json_start)
            content = content[json_start:json_end].strip()
        elif "```" in content:
            json_start = content.find("```") + 3
            json_end = content.find("```", json_start)
            content = content[json_start:json_end].strip()
        
        # Parse JSON
        data = json.loads(content)
        
        print(f"Pesquisa concluída! {len(data.get('products', []))} produtos encontrados.")
        return data
        
    except Exception as e:
        print(f"Erro ao realizar pesquisa de mercado: {str(e)}")
        return None


def update_product_catalog(products_data):
    """Atualizar catálogo de produtos no banco de dados"""
    if not products_data or 'products' not in products_data:
        print("Nenhum dado de produto para atualizar.")
        return
    
    with app.app_context():
        try:
            updated_count = 0
            new_count = 0
            
            for product_data in products_data['products']:
                # Verificar se o produto já existe (por nome)
                existing_product = Product.query.filter_by(
                    name=product_data['name']
                ).first()
                
                if existing_product:
                    # Atualizar produto existente
                    existing_product.description = product_data.get('description', existing_product.description)
                    existing_product.purchase_price = product_data.get('purchase_price', existing_product.purchase_price)
                    existing_product.sale_price = product_data.get('sale_price', existing_product.sale_price)
                    existing_product.stock = product_data.get('stock', existing_product.stock)
                    existing_product.image_url = product_data.get('image_url', existing_product.image_url)
                    existing_product.supplier = product_data.get('supplier', existing_product.supplier)
                    existing_product.supplier_url = product_data.get('supplier_url', existing_product.supplier_url)
                    existing_product.is_active = True
                    updated_count += 1
                else:
                    # Criar novo produto
                    new_product = Product(
                        name=product_data['name'],
                        description=product_data['description'],
                        category=product_data['category'],
                        purchase_price=product_data['purchase_price'],
                        sale_price=product_data['sale_price'],
                        stock=product_data.get('stock', 0),
                        image_url=product_data.get('image_url'),
                        supplier=product_data.get('supplier'),
                        supplier_url=product_data.get('supplier_url'),
                        is_active=True
                    )
                    db.session.add(new_product)
                    new_count += 1
            
            db.session.commit()
            print(f"Catálogo atualizado: {new_count} novos produtos, {updated_count} produtos atualizados.")
            
        except Exception as e:
            db.session.rollback()
            print(f"Erro ao atualizar catálogo: {str(e)}")


def remove_unavailable_products():
    """Remover produtos indisponíveis (exemplo: estoque zerado há muito tempo)"""
    with app.app_context():
        try:
            # Por enquanto, apenas marcar produtos com estoque 0 como inativos
            # Em uma implementação real, verificaríamos com os fornecedores
            products = Product.query.filter_by(stock=0, is_active=True).all()
            
            for product in products:
                product.is_active = False
            
            db.session.commit()
            print(f"{len(products)} produtos com estoque zerado foram desativados.")
            
        except Exception as e:
            db.session.rollback()
            print(f"Erro ao remover produtos indisponíveis: {str(e)}")


def run_weekly_market_research():
    """Executar pesquisa de mercado semanal completa"""
    print("=" * 60)
    print("PESQUISA DE MERCADO SEMANAL - TUDO DO MOMENTO PRESENTES")
    print(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("=" * 60)
    
    # 1. Realizar pesquisa de mercado com IA
    products_data = call_ai_for_market_research()
    
    if products_data:
        # 2. Atualizar catálogo de produtos
        update_product_catalog(products_data)
        
        # 3. Remover produtos indisponíveis
        remove_unavailable_products()
        
        print("\nPesquisa de mercado concluída com sucesso!")
        print("=" * 60)
        return True
    else:
        print("\nFalha na pesquisa de mercado.")
        print("=" * 60)
        return False


if __name__ == '__main__':
    # Executar pesquisa de mercado
    run_weekly_market_research()

