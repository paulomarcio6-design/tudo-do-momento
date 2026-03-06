import { Link } from 'react-router-dom'
import { ShoppingBag, Menu, X } from 'lucide-react'
import { useState } from 'react'
import { Button } from '@/components/ui/button'

function Header() {
  const [isMenuOpen, setIsMenuOpen] = useState(false)

  const toggleMenu = () => setIsMenuOpen(!isMenuOpen)

  return (
    <header className="bg-gradient-to-r from-blue-600 to-purple-600 text-white shadow-lg sticky top-0 z-50">
      <div className="container mx-auto px-4 py-4">
        <div className="flex items-center justify-between">
          {/* Logo */}
          <Link to="/" className="flex items-center space-x-2 hover:opacity-80 transition-opacity">
            <ShoppingBag className="w-8 h-8" />
            <div className="flex flex-col">
              <span className="text-xl font-bold">Tudo do Momento</span>
              <span className="text-xs opacity-90">Presentes</span>
            </div>
          </Link>

          {/* Desktop Navigation */}
          <nav className="hidden md:flex items-center space-x-6">
            <Link to="/" className="hover:text-yellow-300 transition-colors font-medium">
              Início
            </Link>
            <Link to="/produtos" className="hover:text-yellow-300 transition-colors font-medium">
              Produtos
            </Link>
            <Link to="/produtos/esportivos" className="hover:text-yellow-300 transition-colors font-medium">
              Materiais Esportivos
            </Link>
            <Link to="/produtos/games" className="hover:text-yellow-300 transition-colors font-medium">
              Games & Informática
            </Link>
            <Link to="/produtos/vestuario" className="hover:text-yellow-300 transition-colors font-medium">
              Vestuário
            </Link>
            <Link to="/contato" className="hover:text-yellow-300 transition-colors font-medium">
              Contato
            </Link>
          </nav>

          {/* Mobile Menu Button */}
          <button
            onClick={toggleMenu}
            className="md:hidden p-2 hover:bg-white/10 rounded-lg transition-colors"
            aria-label="Toggle menu"
          >
            {isMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
          </button>
        </div>

        {/* Mobile Navigation */}
        {isMenuOpen && (
          <nav className="md:hidden mt-4 pb-4 space-y-2 animate-fade-in">
            <Link
              to="/"
              onClick={toggleMenu}
              className="block py-2 px-4 hover:bg-white/10 rounded-lg transition-colors"
            >
              Início
            </Link>
            <Link
              to="/produtos"
              onClick={toggleMenu}
              className="block py-2 px-4 hover:bg-white/10 rounded-lg transition-colors"
            >
              Produtos
            </Link>
            <Link
              to="/produtos/esportivos"
              onClick={toggleMenu}
              className="block py-2 px-4 hover:bg-white/10 rounded-lg transition-colors"
            >
              Materiais Esportivos
            </Link>
            <Link
              to="/produtos/games"
              onClick={toggleMenu}
              className="block py-2 px-4 hover:bg-white/10 rounded-lg transition-colors"
            >
              Games & Informática
            </Link>
            <Link
              to="/produtos/vestuario"
              onClick={toggleMenu}
              className="block py-2 px-4 hover:bg-white/10 rounded-lg transition-colors"
            >
              Vestuário
            </Link>
            <Link
              to="/contato"
              onClick={toggleMenu}
              className="block py-2 px-4 hover:bg-white/10 rounded-lg transition-colors"
            >
              Contato
            </Link>
          </nav>
        )}
      </div>
    </header>
  )
}

export default Header

