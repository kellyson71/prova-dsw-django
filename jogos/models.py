from django.db import models


class Modalidade(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    tipo = models.CharField(choices=[('coletiva', 'Coletiva'), ('individual', 'Individual')], max_length=20)
    max_atletas = models.PositiveIntegerField()

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Tecnico(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    equipe = models.OneToOneField('Equipe', on_delete=models.CASCADE, related_name='tecnico')

    def __str__(self):
        return self.nome


class Equipe(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    curso = models.CharField(max_length=50)
    ano = models.PositiveIntegerField()
    cor = models.CharField(max_length=20)
    criada_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Atleta(models.Model):
    nome = models.CharField(max_length=50)
    matricula = models.CharField(max_length=20, unique=True)
    data_nascimento = models.DateField()
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE, related_name='atletas')
    modalidades = models.ManyToManyField(Modalidade, blank=True, related_name='atletas')

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome
