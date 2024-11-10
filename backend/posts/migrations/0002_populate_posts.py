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
        ("posts", "0001_initial"),
        ("users", "0004_populate_users"),
    ]

    operations = [
        migrations.RunPython(
            code=populate,
            atomic=True,
        )
    ]
