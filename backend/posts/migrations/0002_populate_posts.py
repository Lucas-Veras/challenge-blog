from django.contrib.auth.hashers import make_password
from django.db import migrations
from users.constants import GroupUserEnum


def populate(apps, schema_editor):
    posts = [
        {
            "title": "Deixe o useEffect em paz!",
            "content": "Como desenvolvedor full-stack na Melio, trabalhando em aplicativos web baseados em React, vi em primeira mão que o desenvolvimento frontend é tão complexo quanto o trabalho backend. Gerenciar o estado, garantir a responsividade e otimizar o desempenho contribuem para os desafios intrincados do frontend.Eu vi em primeira mão que o desenvolvimento frontend é tão complexo quanto o trabalho backend. Gerenciar o estado, garantir a capacidade de resposta e otimizar o desempenho contribuem para os desafios complexos do frontend.</br>Cada framework frontend tem seu funcionamento interno, desafios e nuances, e o React não é diferente. Algumas de suas mecânicas exigem um nível de entendimento para serem usadas corretamente, como o famoso hook useEffect .</br>useEffect é um dos hooks mais populares fornecidos pelo React; ele nos permite sincronizar o componente com fatores/serviços externos, incluindo busca de dados, assinaturas, alterações manuais, etc., mas também é facilmente abusado. Nesta postagem do blog, discutirei alguns cenários que todo desenvolvedor deve evitar e como a equipe do React coloca tudo na mesa nos novos documentos do React",
        },
        {
            "title": "Modernizando o Django REST Framework com visualizações assíncronas e middleware.",
            "content": "Modernizando o Django REST Framework com visualizações assíncronas e middleware. À medida que os aplicativos da web exigem cada vez mais interações em tempo real e arquiteturas escaláveis, alavancar a programação assíncrona se tornou essencial. O Django, com seus recursos assíncronos, agora oferece mais flexibilidade e desempenho, particularmente quando combinado com o Django REST Framework (DRF). Este artigo o guiará pelo processo de modernização de suas APIs do Django REST Framework implementando visualizações assíncronas e middleware. <br/>Por que programação assíncrona? A programação assíncrona permite que seu aplicativo manipule várias tarefas simultaneamente sem bloquear o thread de execução principal. Isso é especialmente benéfico para operações vinculadas a E/S, como consultas de banco de dados, chamadas de API ou tarefas de longa duração. Ao implementar visualizações assíncronas e middleware no Django, você pode obter: <b/>Melhor desempenho : melhor tratamento de solicitações simultâneas.<b/>Escalabilidade : Uso eficiente de recursos sob carga pesada.<b/>APIs responsivas : tempo de resposta reduzido para endpoints.<b/>Configurando visualizações assíncronas no Django REST Framework",
        },
        {
            "title": "Como criar um aplicativo de chat em tempo real com Django Channels",
            "content": "Como criar um aplicativo de chat em tempo real com Django Channels. O desenvolvimento de aplicativos de chat em tempo real é uma tarefa complexa, especialmente quando você deseja que os usuários se comuniquem instantaneamente. O Django Channels é uma extensão do Django que permite a criação de aplicativos de chat em tempo real, notificações push, atualizações em tempo real e muito mais. Neste artigo, você aprenderá a criar um aplicativo de chat em tempo real com Django Channels, incluindo: <br/>Configurando o Django Channels: instalação e configuração.<br/>Criando um aplicativo de chat em tempo real: implementando salas de chat e mensagens.<br/>Adicionando funcionalidades avançadas: autenticação de usuário, notificações push e muito mais.<br/>Implantando o aplicativo de chat em tempo real: hospedagem e escalabilidade. <br/>Pronto para criar um aplicativo de chat em tempo real com Django Channels? Vamos começar!",
        },
        {
            "title": "Como criar um aplicativo de chat em tempo real com Django Channels",
            "content": "Como criar um aplicativo de chat em tempo real com Django Channels. O desenvolvimento de aplicativos de chat em tempo real é uma tarefa complexa, especialmente quando você deseja que os usuários se comuniquem instantaneamente. O Django Channels é uma extensão do Django que permite a criação de aplicativos de chat em tempo real, notificações push, atualizações em tempo real e muito mais. Neste artigo, você aprenderá a criar um aplicativo de chat em tempo real com Django Channels, incluindo: <br/>Configurando o Django Channels: instalação e configuração.<br/>Criando um aplicativo de chat em tempo real: implementando salas de chat e mensagens.<br/>Adicionando funcionalidades avançadas: autenticação de usuário, notificações push e muito mais.<br/>Implantando o aplicativo de chat em tempo real: hospedagem e escalabilidade. <br/>Pronto para criar um aplicativo de chat em tempo real com Django Channels? Vamos começar!",
        },
        {
            "title": "Como criar um aplicativo de chat em tempo real com Django Channels",
            "content": "Como criar um aplicativo de chat em tempo real com Django Channels. O desenvolvimento de aplicativos de chat em tempo real é uma tarefa complexa, especialmente quando você deseja que os usuários se comuniquem instantaneamente. O Django Channels é uma extensão do Django que permite a criação de aplicativos de chat em tempo real, notificações push, atualizações em tempo real e muito mais. Neste artigo, você aprenderá a criar um aplicativo de chat em tempo real com Django Channels, incluindo: <br/>Configurando o Django Channels: instalação e configuração.<br/>Criando um aplicativo de chat em tempo real: implementando salas de chat e mensagens.<br/>Adicionando funcionalidades avançadas: autenticação de usuário, notificações push e muito mais.<br/>Implantando o aplicativo de chat em tempo real: hospedagem e escalabilidade. <br/>Pronto para criar um aplicativo de chat em tempo real com Django Channels? Vamos começar!",
        },
        {
            "title": "Como criar um aplicativo de chat em tempo real com Django Channels",
            "content": "Como criar um aplicativo de chat em tempo real com Django Channels. O desenvolvimento de aplicativos de chat em tempo real é uma tarefa complexa, especialmente quando você deseja que os usuários se comuniquem instantaneamente. O Django Channels é uma extensão do Django que permite a criação de aplicativos de chat em tempo real, notificações push, atualizações em tempo real e muito mais. Neste artigo, você aprenderá a criar um aplicativo de chat em tempo real com Django Channels, incluindo: <br/>Configurando o Django Channels: instalação e configuração.<br/>Criando um aplicativo de chat em tempo real: implementando salas de chat e mensagens.<br/>Adicionando funcionalidades avançadas: autenticação de usuário, notificações push e muito mais.<br/>Implantando o aplicativo de chat em tempo real: hospedagem e escalabilidade. <br/>Pronto para criar um aplicativo de chat em tempo real com Django Channels? Vamos começar!",
        },
        {
            "title": "Como criar um aplicativo de chat em tempo real com Django Channels",
            "content": "Como criar um aplicativo de chat em tempo real com Django Channels. O desenvolvimento de aplicativos de chat em tempo real é uma tarefa complexa, especialmente quando você deseja que os usuários se comuniquem instantaneamente. O Django Channels é uma extensão do Django que permite a criação de aplicativos de chat em tempo real, notificações push, atualizações em tempo real e muito mais. Neste artigo, você aprenderá a criar um aplicativo de chat em tempo real com Django Channels, incluindo: <br/>Configurando o Django Channels: instalação e configuração.<br/>Criando um aplicativo de chat em tempo real: implementando salas de chat e mensagens.<br/>Adicionando funcionalidades avançadas: autenticação de usuário, notificações push e muito mais.<br/>Implantando o aplicativo de chat em tempo real: hospedagem e escalabilidade. <br/>Pronto para criar um aplicativo de chat em tempo real com Django Channels? Vamos começar!",
        },
        {
            "title": "Como criar um aplicativo de chat em tempo real com Django Channels",
            "content": "Como criar um aplicativo de chat em tempo real com Django Channels. O desenvolvimento de aplicativos de chat em tempo real é uma tarefa complexa, especialmente quando você deseja que os usuários se comuniquem instantaneamente. O Django Channels é uma extensão do Django que permite a criação de aplicativos de chat em tempo real, notificações push, atualizações em tempo real e muito mais. Neste artigo, você aprenderá a criar um aplicativo de chat em tempo real com Django Channels, incluindo: <br/>Configurando o Django Channels: instalação e configuração.<br/>Criando um aplicativo de chat em tempo real: implementando salas de chat e mensagens.<br/>Adicionando funcionalidades avançadas: autenticação de usuário, notificações push e muito mais.<br/>Implantando o aplicativo de chat em tempo real: hospedagem e escalabilidade. <br/>Pronto para criar um aplicativo de chat em tempo real com Django Channels? Vamos começar!",
        },
        {
            "title": "Como criar um aplicativo de chat em tempo real com Django Channels",
            "content": "Como criar um aplicativo de chat em tempo real com Django Channels. O desenvolvimento de aplicativos de chat em tempo real é uma tarefa complexa, especialmente quando você deseja que os usuários se comuniquem instantaneamente. O Django Channels é uma extensão do Django que permite a criação de aplicativos de chat em tempo real, notificações push, atualizações em tempo real e muito mais. Neste artigo, você aprenderá a criar um aplicativo de chat em tempo real com Django Channels, incluindo: <br/>Configurando o Django Channels: instalação e configuração.<br/>Criando um aplicativo de chat em tempo real: implementando salas de chat e mensagens.<br/>Adicionando funcionalidades avançadas: autenticação de usuário, notificações push e muito mais.<br/>Implantando o aplicativo de chat em tempo real: hospedagem e escalabilidade. <br/>Pronto para criar um aplicativo de chat em tempo real com Django Channels? Vamos começar!",
        },
        {
            "title": "Como adicionar o modo escuro ao seu site usando apenas CSS",
            "content": "Quer fazer seu site passar de “brilhante e ensolarado” para “escuro e melancólico” sem nenhuma mágica do JavaScript? Perfeito! O CSS sozinho pode lidar com essa tarefa respondendo às configurações do sistema do seu usuário. No artigo a seguir, configuraremos um site que alterna entre o Modo Claro e o Modo Escuro com base nas configurações do dispositivo — sem necessidade de JavaScript! Vamos mergulhar!",
        },
        {
            "title": "Controle de acesso baseado em função (RBAC) no Django",
            "content": "Role-Based Access Control (RBAC) é um modelo de segurança que restringe o acesso a recursos com base em funções de usuário. No Django, você pode implementar o RBAC aproveitando as estruturas de autenticação e autorização integradas, que permitem definir funções, atribuir permissões e controlar o acesso a partes específicas do seu aplicativo. Este artigo fornece um guia abrangente sobre como implementar RBAC complexo no Django usando permissões, grupos e middleware personalizados.",
        },
        {
            "title": "Como criar um aplicativo de chat em tempo real com Django Channels",
            "content": "Como criar um aplicativo de chat em tempo real com Django Channels. O desenvolvimento de aplicativos de chat em tempo real é uma tarefa complexa, especialmente quando você deseja que os usuários se comuniquem instantaneamente. O Django Channels é uma extensão do Django que permite a criação de aplicativos de chat em tempo real, notificações push, atualizações em tempo real e muito mais. Neste artigo, você aprenderá a criar um aplicativo de chat em tempo real com Django Channels, incluindo: <br/>Configurando o Django Channels: instalação e configuração.<br/>Criando um aplicativo de chat em tempo real: implementando salas de chat e mensagens.<br/>Adicionando funcionalidades avançadas: autenticação de usuário, notificações push e muito mais.<br/>Implantando o aplicativo de chat em tempo real: hospedagem e escalabilidade. <br/>Pronto para criar um aplicativo de chat em tempo real com Django Channels? Vamos começar!",
        },
        {
            "title": "As 10 principais extensões do Chrome para desenvolvedores",
            "content": "O Chrome é o navegador mais preferido do mundo. A maioria dos desenvolvedores também usa o Chrome por causa de suas ferramentas de desenvolvimento. As extensões do Chrome podem melhorar sua experiência de navegação e desenvolvimento. As extensões também podem economizar muito tempo e custo gratuitamente. Por exemplo, o LastPass pode armazenar todas as suas senhas, e você pode usá-lo sempre que necessário.",
        },
        {
            "title": "Depois de revisar mais de 500 componentes do React, aqui está o que aprendi",
            "content": "Ao longo dos anos, escrevi e analisei centenas de componentes React para uma startup GenAI de US$ 1,7 bilhão . Eu examinei códigos de desenvolvedores juniores e engenheiros experientes ex-FAANG. Embora esse conselho possa parecer óbvio para componentes pequenos, ele se torna crucial conforme sua base de código front-end cresce. Seguindo essas diretrizes, você garantirá que seu código esteja entre os mais compreensíveis e fáceis de manter em qualquer base de código.",
        },
        {
            "title": "Hoje fui entrevistado para uma vaga de líder de front-end",
            "content": "Meu amigo é um líder de front-end que tem mais de 10 anos de experiência e quer mudar de emprego. Recentemente, ele fez entrevistas em algumas empresas.'Hoje, meu entrevistador mergulhou fundo em algumas perguntas básicas sobre a linguagem JavaScript e o framework ReactJS em si. Foi a primeira vez que alguém me fez esse tipo de pergunta', disse meu amigo, a quem chamarei de 'A'. “Talvez eles vejam que você está buscando um papel de liderança e queiram testar sua compreensão de conceitos fundamentais. Você conseguiu responder a todas as perguntas?”, perguntei. “Só alguns deles. Nunca me preparei tanto”, ele respondeu.",
        },
        {
            "title": "Implante o backend Node.js gratuitamente no Vercel",
            "content": "Implantar qualquer frontend de graça não é grande coisa. Você tem muitas opções como Vercel , Firebase , GitHub Pages e muito mais. Até mesmo implantar frontends é possível com seu Google Drive também. Mas quando você implanta suas APIs de backend, você tem um número limitado de opções 🥲 e hoje vou apresentar a você a implantação do backend de graça no Vercel.",
        },
    ]

    model_post = apps.get_model("posts", "Post")
    model_user = apps.get_model("users", "User")

    try:
        for post_data in posts:
            user_instance = model_user.objects.all().order_by("?").first()
            post_instance = model_post.objects.create(
                title=post_data["title"],
                content=post_data["content"],
                author=user_instance,
            )
            post_instance.save()
    except Exception as e:
        print(e)


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_populate_users"),
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(
            code=populate,
            atomic=True,
        )
    ]
