from django.db import models

# Create your models here.

class Despesa(models.Model):
    descricao = models.CharField(max_length=100)
    data_despesa = models.DateField()
    valor = models.FloatField(null=False)
    valor_pago = models.FloatField(null=True)
    quitado = models.BooleanField(default=False)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    quantidade_parcela = models.IntegerField(default=1)
    observacao = models.CharField(max_length=300)
    anexo = models.FileField(upload_to='despesas/%d/%m/%Y/', null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now_add=True)


    def transferir(self):
        pass

    def __unicode__(self):
        return '%d: %s' % (self.pk, self.descricao)


class Parcela(models.Model):
    valor = models.FloatField(null=False)
    vencimento = models.DateField()
    numero_parcela = models.IntegerField()
    despesa = models.ForeignKey('Despesa', on_delete=models.CASCADE, related_name='parcelas')

    def pagar(self):
        pass

    def __str__(self):
        return "Parcela nº %d" %(self.numero_parcela)


# será uma app
class Categoria(models.Model):
    descricao = models.CharField(max_length=100)
    is_despesa = models.BooleanField(default=False)
    is_receita = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descricao

# será uma app
class Pagamento(models.Model):
    descricao = models.CharField(max_length=100)
    aceita_parcelamento = models.BooleanField(default=True)
