import { Link } from 'react-router-dom'
import { Button } from '@/components/ui/button'
import { ShoppingBag, TrendingUp, Shield, Clock } from 'lucide-react'

function HomePage() {
  const categories = [
    {
      title: 'Materiais Esportivos',
      description: 'Equipamentos e acessórios para todas as idades e estilos',
      image: '🏃',
      link: '/produtos/esportivos',
      color: 'from-green-500 to-emerald-600'
    },
    {
      title: 'Games & Informática',
      description: 'O melhor em tecnologia para gamers',
      image: '🎮',
      link: '/produtos/games',
      color: 'from-purple-500 to-pink-600'
    },
    {
      title: 'Vestuário',
      description: 'Moda esportiva e social para todos',
      image: '👕',
      link: '/produtos/vestuario',
      color: 'from-blue-500 to-cyan-600'
    }
  ]

  const features = [
    {
      icon: <TrendingUp className="w-8 h-8" />,
      title: 'Produtos em Alta',
      description: 'Atualizações semanais com as tendências do momento'
    },
    {
      icon: <Shield className="w-8 h-8" />,
      title: 'Compra Segura',
      description: 'Segurança e transparência em todas as transações'
    },
    {
      icon: <Clock className="w-8 h-8" />,
      title: 'Entrega Confiável',
      description: 'Parceiros de confiança para entrega dos produtos'
    },
    {
      icon: <ShoppingBag className="w-8 h-8" />,
      title: 'Melhor Custo-Benefício',
      description: 'Preços competitivos e produtos de qualidade'
    }
  ]

  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="bg-gradient-to-br from-blue-600 via-purple-600 to-pink-600 text-white py-20">
        <div className="container mx-auto px-4">
          <div className="max-w-4xl mx-auto text-center">
            <h1 className="text-5xl md:text-6xl font-bold mb-6 animate-fade-in">
              Bem-vindo à Tudo do Momento Presentes!
            </h1>
            <p className="text-xl md:text-2xl mb-8 opacity-95 animate-fade-in-up">
              Aqui, você encontra os produtos mais atuais e desejados do mercado, com praticidade, segurança e o melhor custo-benefício.
            </p>
            <p className="text-lg mb-8 opacity-90">
              Trabalhamos no modelo dropshipping, oferecendo uma ampla variedade de materiais esportivos, produtos de informática voltados a games, e vestuário esportivo e social para todas as idades e estilos.
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Link to="/produtos">
                <Button size="lg" className="bg-white text-purple-600 hover:bg-gray-100 text-lg px-8 py-6">
                  Ver Produtos
                </Button>
              </Link>
              <Link to="/contato">
                <Button size="lg" variant="outline" className="border-2 border-white text-white hover:bg-white/10 text-lg px-8 py-6">
                  Entre em Contato
                </Button>
              </Link>
            </div>
          </div>
        </div>
      </section>

      {/* Slogan */}
      <section className="bg-yellow-400 py-8">
        <div className="container mx-auto px-4 text-center">
          <h2 className="text-3xl md:text-4xl font-bold text-gray-900">
            Tudo do Momento Presentes — o que é sucesso, está aqui!
          </h2>
        </div>
      </section>

      {/* Categories Section */}
      <section className="py-16 bg-gray-50">
        <div className="container mx-auto px-4">
          <h2 className="text-4xl font-bold text-center mb-12 text-gray-900">
            Nossas Categorias
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {categories.map((category, index) => (
              <Link
                key={index}
                to={category.link}
                className="group"
              >
                <div className="bg-white rounded-xl shadow-lg overflow-hidden hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-2">
                  <div className={`bg-gradient-to-br ${category.color} p-8 text-center`}>
                    <div className="text-7xl mb-4">{category.image}</div>
                  </div>
                  <div className="p-6">
                    <h3 className="text-2xl font-bold mb-2 text-gray-900 group-hover:text-purple-600 transition-colors">
                      {category.title}
                    </h3>
                    <p className="text-gray-600">{category.description}</p>
                  </div>
                </div>
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-16 bg-white">
        <div className="container mx-auto px-4">
          <h2 className="text-4xl font-bold text-center mb-4 text-gray-900">
            Por que escolher a Tudo do Momento?
          </h2>
          <p className="text-center text-gray-600 mb-12 max-w-2xl mx-auto">
            Nosso compromisso é trazer para você as tendências do momento, com atualizações semanais e um atendimento simples e eficiente.
          </p>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            {features.map((feature, index) => (
              <div
                key={index}
                className="text-center p-6 rounded-xl hover:bg-gray-50 transition-colors"
              >
                <div className="inline-flex items-center justify-center w-16 h-16 bg-gradient-to-br from-blue-500 to-purple-600 text-white rounded-full mb-4">
                  {feature.icon}
                </div>
                <h3 className="text-xl font-bold mb-2 text-gray-900">{feature.title}</h3>
                <p className="text-gray-600">{feature.description}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="bg-gradient-to-r from-purple-600 to-pink-600 text-white py-16">
        <div className="container mx-auto px-4 text-center">
          <h2 className="text-4xl font-bold mb-4">
            Pronto para descobrir o que há de melhor?
          </h2>
          <p className="text-xl mb-8 opacity-90">
            Na Tudo do Momento Presentes, você compra fácil, recebe com tranquilidade e tem a certeza de estar adquirindo o que há de melhor em cada categoria.
          </p>
          <Link to="/produtos">
            <Button size="lg" className="bg-white text-purple-600 hover:bg-gray-100 text-lg px-8 py-6">
              Explorar Produtos
            </Button>
          </Link>
        </div>
      </section>
    </div>
  )
}

export default HomePage

