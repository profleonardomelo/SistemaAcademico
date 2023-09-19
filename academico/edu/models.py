from django.db import models

class Matricula(models.Model):
    matricula = models.IntegerField()
    nome_aluno = models.CharField(max_length=200)
    curso = models.CharField(max_length=100)
    observacao = models.TextField()
    data_matricula = models.DateField(verbose_name='Data da matrícula', blank=True, auto_now_add=True)

    class Meta:
        verbose_name = 'Matrícula de Aluno'
        verbose_name_plural = 'Matrículas de Aluno'
        ordering = ['nome_aluno']