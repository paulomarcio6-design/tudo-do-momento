from flask import Blueprint, request, jsonify
from src.models.user import db
from src.models.product import Product

products_bp = Blueprint('products', __name__)

@products_bp.route('/products', methods=['GET'])
def get_products():
    """Obter lista de produtos com filtros opcionais"""
    try:
        category = request.args.get('category')
        search = request.args.get('search')
        
        query = Product.query.filter_by(is_active=True)
        
        if category and category != 'todos':
            query = query.filter_by(category=category)
        
        if search:
            query = query.filter(
                db.or_(
                    Product.name.ilike(f'%{search}%'),
                    Product.description.ilike(f'%{search}%')
                )
            )
        
        products = query.order_by(Product.created_at.desc()).all()
        
        return jsonify({
            'success': True,
            'products': [product.to_dict() for product in products],
            'total': len(products)
        }), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@products_bp.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Obter detalhes de um produto específico"""
    try:
        product = Product.query.get(product_id)
        if not product:
            return jsonify({'success': False, 'error': 'Produto não encontrado'}), 404
        
        return jsonify({
            'success': True,
            'product': product.to_dict()
        }), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@products_bp.route('/products', methods=['POST'])
def create_product():
    """Criar um novo produto"""
    try:
        data = request.json
        
        product = Product(
            name=data['name'],
            description=data['description'],
            category=data['category'],
            purchase_price=float(data['purchase_price']),
            sale_price=float(data['sale_price']),
            stock=int(data.get('stock', 0)),
            image_url=data.get('image_url'),
            supplier=data.get('supplier'),
            supplier_url=data.get('supplier_url')
        )
        
        db.session.add(product)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Produto criado com sucesso',
            'product': product.to_dict()
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500

@products_bp.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """Atualizar um produto existente"""
    try:
        product = Product.query.get(product_id)
        if not product:
            return jsonify({'success': False, 'error': 'Produto não encontrado'}), 404
        
        data = request.json
        
        if 'name' in data:
            product.name = data['name']
        if 'description' in data:
            product.description = data['description']
        if 'category' in data:
            product.category = data['category']
        if 'purchase_price' in data:
            product.purchase_price = float(data['purchase_price'])
        if 'sale_price' in data:
            product.sale_price = float(data['sale_price'])
        if 'stock' in data:
            product.stock = int(data['stock'])
        if 'image_url' in data:
            product.image_url = data['image_url']
        if 'supplier' in data:
            product.supplier = data['supplier']
        if 'supplier_url' in data:
            product.supplier_url = data['supplier_url']
        if 'is_active' in data:
            product.is_active = data['is_active']
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Produto atualizado com sucesso',
            'product': product.to_dict()
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500

@products_bp.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Desativar um produto (soft delete)"""
    try:
        product = Product.query.get(product_id)
        if not product:
            return jsonify({'success': False, 'error': 'Produto não encontrado'}), 404
        
        product.is_active = False
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Produto desativado com sucesso'
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500

@products_bp.route('/products/low-stock', methods=['GET'])
def get_low_stock_products():
    """Obter produtos com estoque baixo (<=5)"""
    try:
        products = Product.query.filter(
            Product.is_active == True,
            Product.stock <= 5
        ).all()
        
        return jsonify({
            'success': True,
            'products': [product.to_dict() for product in products],
            'total': len(products)
        }), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

