from flask import Blueprint, request, jsonify
from src.models.user import db
from src.models.product import Product
from src.models.sale import Sale
from src.models.visit import Visit
from datetime import datetime, timedelta
from sqlalchemy import func
import threading

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin/stats', methods=['GET'])
def get_stats():
    """Obter estatísticas gerais do dashboard"""
    try:
        # Total de vendas
        total_sales = Sale.query.count()
        
        # Receita total
        total_revenue = db.session.query(func.sum(Sale.sale_price)).scalar() or 0
        
        # Lucro total
        total_profit = db.session.query(func.sum(Sale.profit)).scalar() or 0
        
        # Total de visitas
        total_visits = Visit.query.count()
        
        # Produtos com estoque baixo (<=5)
        low_stock_products = Product.query.filter(
            Product.is_active == True,
            Product.stock <= 5
        ).count()
        
        return jsonify({
            'totalSales': total_sales,
            'totalRevenue': float(total_revenue),
            'totalProfit': float(total_profit),
            'totalVisits': total_visits,
            'lowStockProducts': low_stock_products
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@admin_bp.route('/admin/sales-data', methods=['GET'])
def get_sales_data():
    """Obter dados de vendas por período"""
    try:
        # Últimos 7 dias
        sales_data = []
        for i in range(6, -1, -1):
            date = datetime.utcnow().date() - timedelta(days=i)
            
            daily_sales = Sale.query.filter(
                func.date(Sale.sale_date) == date
            ).all()
            
            sales_count = len(daily_sales)
            revenue = sum(sale.sale_price for sale in daily_sales)
            
            sales_data.append({
                'period': date.strftime('%d/%m'),
                'sales': sales_count,
                'revenue': float(revenue)
            })
        
        return jsonify({
            'data': sales_data
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@admin_bp.route('/admin/top-products', methods=['GET'])
def get_top_products():
    """Obter produtos mais vendidos"""
    try:
        # Agrupar vendas por produto
        top_products = db.session.query(
            Sale.product_id,
            Sale.product_name,
            func.count(Sale.id).label('sales'),
            func.sum(Sale.sale_price).label('revenue')
        ).group_by(Sale.product_id, Sale.product_name)\
         .order_by(func.count(Sale.id).desc())\
         .limit(5)\
         .all()
        
        products_data = []
        for product in top_products:
            # Obter estoque atual
            product_obj = Product.query.get(product.product_id)
            stock = product_obj.stock if product_obj else 0
            
            products_data.append({
                'name': product.product_name,
                'sales': product.sales,
                'revenue': float(product.revenue),
                'stock': stock
            })
        
        return jsonify({
            'products': products_data
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@admin_bp.route('/admin/generate-report', methods=['POST'])
def generate_report():
    """Gerar relatório de vendas"""
    try:
        # Obter dados para o relatório
        total_sales = Sale.query.count()
        total_revenue = db.session.query(func.sum(Sale.sale_price)).scalar() or 0
        total_profit = db.session.query(func.sum(Sale.profit)).scalar() or 0
        
        # Produtos mais vendidos
        top_products = db.session.query(
            Sale.product_name,
            func.count(Sale.id).label('sales')
        ).group_by(Sale.product_name)\
         .order_by(func.count(Sale.id).desc())\
         .limit(10)\
         .all()
        
        # Produtos com estoque baixo
        low_stock = Product.query.filter(
            Product.is_active == True,
            Product.stock <= 5
        ).all()
        
        report = {
            'generated_at': datetime.utcnow().isoformat(),
            'summary': {
                'total_sales': total_sales,
                'total_revenue': float(total_revenue),
                'total_profit': float(total_profit)
            },
            'top_products': [
                {'name': p.product_name, 'sales': p.sales}
                for p in top_products
            ],
            'low_stock_products': [
                {'name': p.name, 'stock': p.stock}
                for p in low_stock
            ]
        }
        
        return jsonify({
            'success': True,
            'message': 'Relatório gerado com sucesso',
            'report': report
        }), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@admin_bp.route('/admin/send-report', methods=['POST'])
def send_report():
    """Enviar relatório por e-mail"""
    try:
        # Gerar relatório
        from src.routes.contact import send_email
        
        total_sales = Sale.query.count()
        total_revenue = db.session.query(func.sum(Sale.sale_price)).scalar() or 0
        total_profit = db.session.query(func.sum(Sale.profit)).scalar() or 0
        total_visits = Visit.query.count()
        
        email_body = f"""
        <html>
        <body>
            <h2>Relatório Automático - Tudo do Momento Presentes</h2>
            <p><strong>Data:</strong> {datetime.utcnow().strftime('%d/%m/%Y %H:%M')}</p>
            
            <h3>Resumo</h3>
            <ul>
                <li>Total de Vendas: {total_sales}</li>
                <li>Receita Total: R$ {total_revenue:.2f}</li>
                <li>Lucro Total: R$ {total_profit:.2f}</li>
                <li>Total de Visitas: {total_visits}</li>
            </ul>
            
            <p>Este é um relatório automático gerado pelo sistema.</p>
        </body>
        </html>
        """
        
        send_email(
            'contato@tudodomomentopresentes.com.br',
            f'Relatório Automático - {datetime.utcnow().strftime("%d/%m/%Y")}',
            email_body
        )
        
        return jsonify({
            'success': True,
            'message': 'Relatório enviado por e-mail com sucesso'
        }), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

def run_market_research_async():
    """Executar pesquisa de mercado em thread separada"""
    try:
        from src.ai_market_research import run_weekly_market_research
        run_weekly_market_research()
    except Exception as e:
        print(f"Erro ao executar pesquisa de mercado: {str(e)}")

@admin_bp.route('/admin/run-market-research', methods=['POST'])
def run_market_research():
    """Executar pesquisa de mercado com agente de IA"""
    try:
        # Executar em thread separada para não bloquear a requisição
        thread = threading.Thread(target=run_market_research_async)
        thread.daemon = True
        thread.start()
        
        return jsonify({
            'success': True,
            'message': 'Pesquisa de mercado iniciada com sucesso! O catálogo será atualizado em breve.'
        }), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

