import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { useState, useEffect } from 'react'

// Pages
import HomePage from './pages/HomePage'
import ProductsPage from './pages/ProductsPage'
import ContactPage from './pages/ContactPage'
import AdminPage from './pages/AdminPage'
import PrivacyPolicyPage from './pages/PrivacyPolicyPage'
import TermsOfUsePage from './pages/TermsOfUsePage'
import ReturnsPage from './pages/ReturnsPage'

// Components
import Header from './components/Header'
import Footer from './components/Footer'

function App() {
  const [visitCount, setVisitCount] = useState(0)

  useEffect(() => {
    // Registrar visita ao carregar a página
    fetch('/api/visits', {
      method: 'POST',
    })
      .then(res => res.json())
      .then(data => setVisitCount(data.total_visits))
      .catch(err => console.error('Erro ao registrar visita:', err))
  }, [])

  return (
    <Router>
      <div className="min-h-screen flex flex-col">
        <Header />
        <main className="flex-grow">
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/produtos" element={<ProductsPage />} />
            <Route path="/produtos/:categoria" element={<ProductsPage />} />
            <Route path="/contato" element={<ContactPage />} />
            <Route path="/admin" element={<AdminPage />} />
            <Route path="/politica-privacidade" element={<PrivacyPolicyPage />} />
            <Route path="/termos-uso" element={<TermsOfUsePage />} />
            <Route path="/trocas-devolucoes" element={<ReturnsPage />} />
          </Routes>
        </main>
        <Footer visitCount={visitCount} />
      </div>
    </Router>
  )
}

export default App

