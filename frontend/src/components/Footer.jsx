import { Link } from 'react-router-dom'
import { Mail, MapPin, Eye } from 'lucide-react'

function Footer({ visitCount }) {
  return (
    <footer className="bg-gray-900 text-gray-300">
      <div className="container mx-auto px-4 py-12">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {/* Informações da Loja */}
          <div>
            <h3 className="text-white text-lg font-bold mb-4">Tudo do Momento Presentes</h3>
            <p className="text-sm mb-4">
              O que é sucesso, está aqui! Produtos atuais e desejados com praticidade, segurança e o melhor custo-benefício.
            </p>
            <div className="space-y-2">
              <div className="flex items-start space-x-2">
                <MapPin className="w-5 h-5 mt-0.5 flex-shrink-0" />
                <span className="text-sm">
                  Avenida JK, nº 80, Bairro Cidade Nova<br />
                  CEP 39.900-000 – Almenara, MG
                </span>
              </div>
              <div className="flex items-center space-x-2">
                <Mail className="w-5 h-5 flex-shrink-0" />
                <a href="mailto:contato@tudodomomentopresentes.com.br" className="text-sm hover:text-white transition-colors">
                  contato@tudodomomentopresentes.com.br
                </a>
              </div>
            </div>
          </div>

          {/* Links Rápidos */}
          <div>
            <h3 className="text-white text-lg font-bold mb-4">Links Rápidos</h3>
            <ul className="space-y-2">
              <li>
                <Link to="/" className="text-sm hover:text-white transition-colors">
                  Início
                </Link>
              </li>
              <li>
                <Link to="/produtos" className="text-sm hover:text-white transition-colors">
                  Produtos
                </Link>
              </li>
              <li>
                <Link to="/contato" className="text-sm hover:text-white transition-colors">
                  Contato
                </Link>
              </li>
            </ul>
          </div>

          {/* Informações Legais */}
          <div>
            <h3 className="text-white text-lg font-bold mb-4">Informações Legais</h3>
            <ul className="space-y-2">
              <li>
                <Link to="/politica-privacidade" className="text-sm hover:text-white transition-colors">
                  Política de Privacidade
                </Link>
              </li>
              <li>
                <Link to="/termos-uso" className="text-sm hover:text-white transition-colors">
                  Termos de Uso
                </Link>
              </li>
              <li>
                <Link to="/trocas-devolucoes" className="text-sm hover:text-white transition-colors">
                  Política de Trocas e Devoluções
                </Link>
              </li>
            </ul>
            {visitCount > 0 && (
              <div className="mt-4 flex items-center space-x-2 text-sm">
                <Eye className="w-4 h-4" />
                <span>{visitCount.toLocaleString('pt-BR')} visitas</span>
              </div>
            )}
          </div>
        </div>

        {/* Copyright */}
        <div className="border-t border-gray-800 mt-8 pt-8 text-center">
          <p className="text-sm">
            © 2025 Tudo do Momento Presentes – Todos os direitos reservados.
          </p>
          <p className="text-xs mt-2 text-gray-500">
            Proprietário: Paulo Márcio Otoni Silva | CPF: 038.415.216-30
          </p>
          <p className="text-xs mt-1 text-gray-500">
            CNPJ: [A ser registrado]
          </p>
        </div>
      </div>
    </footer>
  )
}

export default Footer

