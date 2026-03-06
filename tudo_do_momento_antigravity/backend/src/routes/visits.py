from flask import Blueprint, request, jsonify
from src.models.user import db
from src.models.visit import Visit

visits_bp = Blueprint('visits', __name__)

@visits_bp.route('/visits', methods=['POST'])
def register_visit():
    """Registrar uma nova visita ao site"""
    try:
        ip_address = request.remote_addr
        user_agent = request.headers.get('User-Agent', '')
        
        visit = Visit(
            ip_address=ip_address,
            user_agent=user_agent
        )
        
        db.session.add(visit)
        db.session.commit()
        
        # Contar total de visitas
        total_visits = Visit.query.count()
        
        return jsonify({
            'success': True,
            'message': 'Visita registrada com sucesso',
            'total_visits': total_visits
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500

@visits_bp.route('/visits/count', methods=['GET'])
def get_visit_count():
    """Obter contagem total de visitas"""
    try:
        total_visits = Visit.query.count()
        
        return jsonify({
            'success': True,
            'total_visits': total_visits
        }), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@visits_bp.route('/visits/stats', methods=['GET'])
def get_visit_stats():
    """Obter estatísticas de visitas"""
    try:
        from datetime import datetime, timedelta
        from sqlalchemy import func
        
        # Total de visitas
        total_visits = Visit.query.count()
        
        # Visitas hoje
        today = datetime.utcnow().date()
        today_visits = Visit.query.filter(
            func.date(Visit.visit_date) == today
        ).count()
        
        # Visitas esta semana
        week_ago = datetime.utcnow() - timedelta(days=7)
        week_visits = Visit.query.filter(
            Visit.visit_date >= week_ago
        ).count()
        
        # Visitas este mês
        month_ago = datetime.utcnow() - timedelta(days=30)
        month_visits = Visit.query.filter(
            Visit.visit_date >= month_ago
        ).count()
        
        return jsonify({
            'success': True,
            'stats': {
                'total': total_visits,
                'today': today_visits,
                'week': week_visits,
                'month': month_visits
            }
        }), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

