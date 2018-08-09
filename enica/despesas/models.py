from django.db import models

# Create your models here.

class Despesa(models.Model):
    descricao = models.CharField(max_length=100)
    data_despesa = models.DateField()
    valor = models.FloatField(null=False)
    pago = models.BooleanField(default=False)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    parcelas = models.ManyToManyField('self')
    observacao = models.CharField(max_length=300)
    anexo = models.FileField(upload_to='despesas/%d/%m/%Y/', blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now_add=True)

    def valor_aberto(self):
        pass

    def pagar(self):
        self.pago = True

    def transferir(self):
        pass

    def parcelar(self, parcela):
        self.parcelas.add(parcela)



class Categoria(models.Model):
    descricao = models.CharField(max_length=100)
    is_despesa = models.BooleanField(default=False)
    is_receita = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)