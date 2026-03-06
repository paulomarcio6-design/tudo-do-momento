import React from 'react';

function PrivacyPolicyPage() {
  return (
    <div className="min-h-screen bg-gray-50 py-12">
      <div className="container mx-auto px-4">
        <div className="bg-white rounded-lg shadow-lg p-8">
          <h1 className="text-4xl font-bold text-gray-900 mb-6">Política de Privacidade</h1>
          <p className="text-gray-700 mb-4">
            Bem-vindo à Tudo do Momento Presentes. A sua privacidade é de extrema importância para nós. Esta Política de Privacidade descreve como coletamos, usamos, processamos e protegemos suas informações pessoais, em conformidade com a Lei Geral de Proteção de Dados (LGPD) - Lei nº 13.709/2018.
          </p>

          <h2 className="text-2xl font-bold text-gray-900 mt-8 mb-4">1. Coleta de Informações Pessoais</h2>
          <p className="text-gray-700 mb-4">
            Coletamos informações pessoais que você nos fornece diretamente ao interagir com nossa loja virtual, tais como:
          </p>
          <ul className="list-disc list-inside text-gray-700 mb-4 ml-4">
            <li><strong>Dados de Cadastro:</strong> Nome completo, CPF, endereço de e-mail, endereço de entrega e cobrança, número de telefone, data de nascimento, ao criar uma conta ou realizar uma compra.</li>
            <li><strong>Dados de Pagamento:</strong> Informações de cartão de crédito/débito ou outros dados financeiros, processados por gateways de pagamento seguros. Não armazenamos dados completos de cartão de crédito em nossos servidores.</li>
            <li><strong>Dados de Comunicação:</strong> Informações fornecidas ao entrar em contato conosco via formulário, e-mail ou chat, incluindo nome, e-mail, assunto e conteúdo da mensagem.</li>
          </ul>
          <p className="text-gray-700 mb-4">
            Também coletamos automaticamente certas informações quando você visita nosso site:
          </p>
          <ul className="list-disc list-inside text-gray-700 mb-4 ml-4">
            <li><strong>Dados de Navegação:</strong> Endereço IP, tipo de navegador, sistema operacional, páginas visitadas, tempo de permanência, cliques e outras interações com o site.</li>
            <li><strong>Cookies e Tecnologias Semelhantes:</strong> Utilizamos cookies para melhorar sua experiência de navegação, personalizar conteúdo, analisar tráfego e para fins de marketing.</li>
          </ul>

          <h2 className="text-2xl font-bold text-gray-900 mt-8 mb-4">2. Uso das Informações Pessoais</h2>
          <p className="text-gray-700 mb-4">
            Utilizamos suas informações pessoais para as seguintes finalidades:
          </p>
          <ul className="list-disc list-inside text-gray-700 mb-4 ml-4">
            <li>Processar e gerenciar seus pedidos, incluindo pagamento, entrega e suporte pós-venda.</li>
            <li>Personalizar sua experiência de compra e oferecer produtos e serviços relevantes.</li>
            <li>Melhorar nossos produtos, serviços e a funcionalidade do site.</li>
            <li>Comunicar-nos com você sobre seu pedido, promoções, novidades e informações importantes.</li>
            <li>Realizar análises de mercado e estatísticas para entender o comportamento do consumidor.</li>
            <li>Garantir a segurança do site e prevenir fraudes.</li>
            <li>Cumprir obrigações legais e regulatórias.</li>
          </ul>

          <h2 className="text-2xl font-bold text-gray-900 mt-8 mb-4">3. Compartilhamento de Informações Pessoais</h2>
          <p className="text-gray-700 mb-4">
            Suas informações pessoais podem ser compartilhadas com:
          </p>
          <ul className="list-disc list-inside text-gray-700 mb-4 ml-4">
            <li><strong>Parceiros de Dropshipping:</strong> Para que possam processar e enviar os produtos que você adquiriu.</li>
            <li><strong>Provedores de Serviços:</strong> Empresas que nos auxiliam em operações como processamento de pagamentos, entrega, marketing, análise de dados e hospedagem de site.</li>
            <li><strong>Autoridades Legais:</strong> Quando exigido por lei ou para proteger nossos direitos, propriedade ou segurança.</li>
          </ul>
          <p className="text-gray-700 mb-4">
            Exigimos que todos os terceiros com quem compartilhamos dados respeitem a segurança de suas informações pessoais e as tratem de acordo com a lei.
          </p>

          <h2 className="text-2xl font-bold text-gray-900 mt-8 mb-4">4. Direitos do Titular dos Dados (LGPD)</h2>
          <p className="text-gray-700 mb-4">
            De acordo com a LGPD, você possui os seguintes direitos em relação aos seus dados pessoais:
          </p>
          <ul className="list-disc list-inside text-gray-700 mb-4 ml-4">
            <li><strong>Confirmação e Acesso:</strong> Confirmar a existência de tratamento e acessar seus dados.</li>
            <li><strong>Correção:</strong> Solicitar a correção de dados incompletos, inexatos ou desatualizados.</li>
            <li><strong>Anonimização, Bloqueio ou Eliminação:</strong> Solicitar a anonimização, bloqueio ou eliminação de dados desnecessários, excessivos ou tratados em desconformidade com a LGPD.</li>
            <li><strong>Portabilidade:</strong> Solicitar a portabilidade dos dados a outro fornecedor de serviço ou produto.</li>
            <li><strong>Eliminação:</strong> Solicitar a eliminação dos dados pessoais tratados com o seu consentimento.</li>
            <li><strong>Informação:</strong> Obter informações sobre as entidades públicas e privadas com as quais compartilhamos seus dados.</li>
            <li><strong>Revogação do Consentimento:</strong> Revogar o consentimento a qualquer momento.</li>
            <li><strong>Oposição:</strong> Opor-se a tratamento realizado com fundamento em uma das hipóteses de dispensa de consentimento, em caso de descumprimento à LGPD.</li>
          </ul>
          <p className="text-gray-700 mb-4">
            Para exercer qualquer um desses direitos, entre em contato conosco através do e-mail: <a href="mailto:contato@tudodomomentopresentes.com.br" className="text-purple-600 hover:underline">contato@tudodomomentopresentes.com.br</a>.
          </p>

          <h2 className="text-2xl font-bold text-gray-900 mt-8 mb-4">5. Segurança dos Dados</h2>
          <p className="text-gray-700 mb-4">
            Implementamos medidas de segurança técnicas e administrativas para proteger suas informações pessoais contra acesso não autorizado, alteração, divulgação ou destruição. Isso inclui criptografia, firewalls e controles de acesso. No entanto, nenhum sistema é 100% seguro, e não podemos garantir a segurança absoluta de suas informações.
          </p>

          <h2 className="text-2xl font-bold text-gray-900 mt-8 mb-4">6. Retenção de Dados</h2>
          <p className="text-gray-700 mb-4">
            Retemos suas informações pessoais pelo tempo necessário para cumprir as finalidades descritas nesta Política de Privacidade, a menos que um período de retenção mais longo seja exigido ou permitido por lei.
          </p>

          <h2 className="text-2xl font-bold text-gray-900 mt-8 mb-4">7. Alterações a Esta Política de Privacidade</h2>
          <p className="text-gray-700 mb-4">
            Podemos atualizar nossa Política de Privacidade periodicamente. Notificaremos você sobre quaisquer alterações publicando a nova política nesta página. Aconselhamos que você revise esta Política de Privacidade regularmente para quaisquer alterações.
          </p>

          <h2 className="text-2xl font-bold text-gray-900 mt-8 mb-4">8. Contato</h2>
          <p className="text-gray-700 mb-4">
            Se tiver alguma dúvida sobre esta Política de Privacidade, entre em contato conosco:
          </p>
          <ul className="list-disc list-inside text-gray-700 mb-4 ml-4">
            <li>E-mail: <a href="mailto:contato@tudodomomentopresentes.com.br" className="text-purple-600 hover:underline">contato@tudodomomentopresentes.com.br</a></li>
            <li>Endereço: Avenida JK, nº 80, Bairro Cidade Nova, CEP 39.900-000 – Almenara, MG</li>
          </ul>

          <p className="text-gray-700 mt-8 text-sm">
            Última atualização: 16 de Outubro de 2025
          </p>
        </div>
      </div>
    </div>
  );
}

export default PrivacyPolicyPage;

