from django.db import models

class reserva(models.Model):
    TAMANHO_OPCOES = (
        (0,'PEQUENO'),
        (1,'MEDIO'),
        (2,'GRANDE')
    )
    TURNO_OPCOES = (
        ('MANHÃ','Manhã'),
        ('TARDE','Tarde')

    )
    nome = models.CharField(verbose_name='nome',max_length=50)
    email = models.EmailField(verbose_name='email')
    data = models.DateField(verbose_name='data',help_text='dd/mm/aaaa')
    turno = models.CharField(verbose_name='turno',max_length=50,choices=TURNO_OPCOES)
    tamanho = models.IntegerField(verbose_name='tamanha',choices=TAMANHO_OPCOES)
    observaçoes = models.TextField(blank=True)

    def __str__(self):
        return f'{self.nome}: {self.data} - {self.turno}'
    class Meta:
        verbose_name = 'Reserva De Banho'
        verbose_name_plural = 'Reservas De Banhos'    
