from django.db import models

class Matricula(models.Model):
    matricula = models.IntegerField()
    #nome_aluno = models.CharField(max_length=200)
    aluno = models.ForeignKey('comum.Aluno', verbose_name='Aluno', related_name='comum_aluno', on_delete=models.CASCADE)
    curso = models.CharField(max_length=100)
    observacao = models.TextField()
    data_matricula = models.DateField(verbose_name='Data da matrícula', blank=True, auto_now_add=True)

    class Meta:
        verbose_name = 'Matrícula de Aluno'
        verbose_name_plural = 'Matrículas de Aluno'
        #ordering = ['nome_aluno']
        ordering = ['aluno']

    def __str__(self):
        return '{} {}'.format(self.aluno.user.first_name, self.aluno.user.last_name)