from django.db import models
import math


class Pessoa(models.Model):

    nome = models.CharField(max_length=100)
    endereco = models.CharField("endereço", max_length=200)
    telefone = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

    def __str__(self):
        return self.nome
    
class Marca(models.Model):

    nome = models.CharField(max_length=50)

    class Meta:
        verbose_name = "marca"
        verbose_name_plural = "marcas"

    def __str__(self):
        return self.nome



class Veiculo(models.Model):

    marca = models.ForeignKey("Marca", on_delete=models.CASCADE)
    placa = models.CharField(max_length=7)
    proprietario = models.ForeignKey("Pessoa", verbose_name="proprietário", on_delete=models.CASCADE)
    cor = models.CharField(max_length=15)
    observacoes = models.TextField("observações")

    class Meta:
        verbose_name = "Veículo"
        verbose_name_plural = "Veículos"

    def __str__(self):
        return self.marca.nome + " - " + self.placa


class Parametro(models.Model):

    valor_hora = models.DecimalField("valor por hora", max_digits=5, decimal_places=2)
    valor_mes = models.DecimalField("valor mensal", max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = "parâmetro"
        verbose_name_plural = "parâmetros"

    def __str__(self):
        return "parâmetros"
    
    
class movRotativo(models.Model):

    checkin = models.DateTimeField(auto_now=False)
    checkout = models.DateTimeField(auto_now=False, null=True, blank=True)
    valor_hora = models.DecimalField("valor da hora", max_digits=5, decimal_places=2)
    veiculo = models.ForeignKey(Veiculo, verbose_name="veículo", on_delete=models.CASCADE)
    pago = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Movimento rotativo"
        verbose_name_plural = "Movimentos rotativos"

    def __str__(self):
        return self.veiculo.placa
    
    def horas_total(self):
        return math.ceil((self.checkout - self.checkin).total_seconds() / 3600)
    
        
    
    
    def total(self):
        return self.valor_hora * self.horas_total()
    

class Mensalista(models.Model):

    veiculo = models.ForeignKey(Veiculo, verbose_name="veículo", on_delete=models.CASCADE)
    inicio = models.DateField("início", auto_now=False, auto_now_add=False)
    valor_mes = models.DecimalField("valor mensal", max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = "mensalista"
        verbose_name_plural = "mensalistas"

    def __str__(self):
        return str(self.veiculo) + " - " + str(self.inicio)

    
class movMensalista(models.Model):

    mensalista = models.ForeignKey("Mensalista", on_delete=models.CASCADE)
    dt_pgto = models.DateField("data de pagamento", auto_now=False, auto_now_add=False)
    total = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = "movimento mensal"
        verbose_name_plural = "movimentos mensais"

    def __str__(self):
        return str(self.mensalista) + " - " + str(self.total)


