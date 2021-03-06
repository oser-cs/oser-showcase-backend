# Generated by Django 2.0.5 on 2018-05-12 12:29

from django.db import migrations, models
import django.utils.timezone
import markdownx.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='titre')),
                ('thumbnail', models.ImageField(blank=True, help_text="Une petite image représentant l'action. Format recommandé : 200x200", null=True, upload_to='actions/', verbose_name='illustration')),
                ('description', markdownx.models.MarkdownxField(help_text="Un texte libre décrivant le point d'action. Markdown est supporté.")),
                ('key_figure', models.TextField(blank=True, default='', help_text="Enoncer un chiffre clé à propos de cette action. Exemple : 'En 2018, 18 sorties ont été organisées dans des lieux tels que…'", verbose_name='chiffre clé')),
                ('highlight', models.BooleanField(default=True, help_text="Cochez pour afficher cette action sur la page d'accueil. Pour un affichage optimal, assurez-vous alors d'avoir renseigné une illustration.", verbose_name='mettre en avant')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='ordre')),
            ],
            options={
                'verbose_name': 'action clé',
                'verbose_name_plural': 'actions clés',
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text="Titre de l'article", max_length=300, verbose_name='titre')),
                ('slug', models.SlugField(help_text="Un court identifiant généré après la création de l'article.", max_length=100, unique=True)),
                ('introduction', models.TextField(blank=True, default='', help_text="Chapeau introductif qui sera affiché sous le titre de l'article. Utilisez-le pour résumer le contenu de l'article ou introduire le sujet.")),
                ('content', markdownx.models.MarkdownxField(help_text="Contenu complet de l'article (Markdown est supporté).", verbose_name='contenu')),
                ('published', models.DateTimeField(auto_now_add=True, verbose_name='publié le')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modifié le')),
                ('image', models.ImageField(blank=True, null=True, upload_to='articles/', verbose_name='illustration')),
                ('display_image', models.BooleanField(default=True, help_text="Cocher pour que l'illustration soit affichée sous le chapeau introductif de l'article.", verbose_name="afficher l'illustration")),
                ('pinned', models.BooleanField(default=False, help_text="Cocher pour que l'article soit épinglé et affiché en priorité.", verbose_name='épinglé')),
                ('active', models.BooleanField(default=True, help_text="Décocher pour que l'article soit archivé. Il ne sera alors plus affiché sur le site.", verbose_name='actif')),
            ],
            options={
                'verbose_name': 'article',
                'ordering': ('-active', '-pinned', '-published'),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='titre')),
            ],
            options={
                'verbose_name': 'catégorie',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='KeyFigure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('figure', models.PositiveIntegerField(help_text='Un nombre entier positif. Exemple : 60', verbose_name='chiffre')),
                ('description', models.CharField(help_text="Une courte description du chiffre (sera convertie en minuscules). Exemple : millions d'amis.", max_length=100)),
                ('order', models.PositiveIntegerField(default=0, verbose_name='ordre')),
            ],
            options={
                'verbose_name': 'chiffre clé',
                'verbose_name_plural': 'chiffres clés',
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='nom')),
                ('website', models.URLField(null=True, verbose_name='site internet')),
                ('logo', models.ImageField(help_text='Image PNG avec arrière-plan transparent. Dimensions recommandées : hauteur = 320px. ', null=True, upload_to='partners/')),
                ('premium', models.BooleanField(default=False, help_text='Cocher si ce partenaire est un partenaire privilégié. Il sera davantage mis en avant sur le site. Exemple : les organismes de subventions peuvent être des partenaires secondaires et les entreprises des partenaires principaux.', verbose_name='partenaire privilégié')),
                ('active', models.BooleanField(default=True, help_text='Cocher si le partenariat est actif. Les partenariats inactifs ne seront pas affichés sur le site.', verbose_name='actif')),
                ('start_date', models.DateField(blank=True, default=django.utils.timezone.now, help_text='Laisser vide si inconnu. (Cette information est stockée pour historique uniquement.)', null=True, verbose_name='début du partenariat')),
            ],
            options={
                'verbose_name': 'partenaire',
                'ordering': ('-active', '-premium', '-start_date', 'name'),
            },
        ),
        migrations.CreateModel(
            name='Testimony',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.TextField(verbose_name='citation')),
                ('source', models.CharField(help_text="Nom et qualité de l'auteur ou de la source de ce témoignage.", max_length=300, verbose_name='source')),
                ('created', models.DateField(auto_now_add=True, verbose_name='ajouté le')),
            ],
            options={
                'verbose_name': 'témoignage',
                'ordering': ('-created', 'source'),
            },
        ),
        migrations.AddField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(blank=True, help_text="Catégories auxquelles rattacher l'article", to='showcase_site.Category', verbose_name='catégories'),
        ),
    ]
