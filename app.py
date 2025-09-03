from fasthtml.common import *

# Estilo com Pico CSS (igual ao site do FastHTML)
css = Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css")

app, rt = fast_app(hdrs=[css])

# Componente reutilizável: Card de serviço
def Card(title: str, body: str):
    return Article(
        Header(H3(title)),
        P(body),
        style="margin-bottom: 1.5rem; padding: 1.5rem; border: 1px solid #e5e5e5; border-radius: 0.5rem;"
    )

# Página inicial
@rt("/")
def get():
    return Html(
        Head(Title("EditData Soluções Inteligentes"), css),
        Body(
            Main(
                H1("EditData Soluções Inteligentes"),
                P("Automação de planilhas, tratamento de dados e integração com APIs — tudo com Python e tecnologia de ponta."),

                H2("Serviços"),
                Card("Automação de Planilhas", "Elimine tarefas repetitivas. Automatizamos Excel e Google Sheets com Python e integração de APIs."),
                Card("Tratamento de Dados", "Limpeza, padronização e análise de dados para empresas que querem agilidade e precisão."),
                Card("Integração com Sistemas", "Conectamos sua planilha ou sistema interno com APIs externas de ERP, CRM, e-commerce e mais."),

                H2("Por que automatizar?"),
                Ul(
                    Li("Reduza horas de trabalho manual"),
                    Li("Evite erros humanos"),
                    Li("Integre sistemas sem complicação"),
                    Li("Tenha relatórios automáticos e atualizados")
                ),

                H2("Contato"),
                P(
                    A("📲 WhatsApp: (11) 98235-4531", href="https://wa.me/5511982354531", cls="button"),
                    " ",
                    A("📧 contato@editdata.com.br", href="mailto:contato@editdata.com.br", cls="button outline")
                ),

                Footer(
                    P("© 2025 EditData Soluções Inteligentes – Todos os direitos reservados."),
                    style="margin-top: 3rem; text-align: center; font-size: 0.9rem; color: #666;"
                ),

                style="max-width: 800px; margin: auto; padding: 2rem;"
            )
        )
    )

# Rodar localmente (opcional)
if __name__ == "__main__":
    serve()