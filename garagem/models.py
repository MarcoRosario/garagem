from django.db import models

class Marca(models.Model):
    nome = models.CharField(max_length=50)
    nacionalidade = models.CharField(max_length=50,blank=True,null=True)
    ano = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nome.upper()      
  

class Categoria(models.Model):
    descricao = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.descricao.upper()



class Acessório(models.Model):
    descricao = models.CharField(max_length=100)
  

    def __str__(self):
        return self.descricao

class Cor(models.Model):
    descricao = models.CharField(max_length=100)
  
    def __str__(self):
        return self.descricao

class Veiculo(models.Model):
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="Veiculo"
)   
    cor = models.ForeignKey(
        Cor, on_delete=models.PROTECT, related_name="Veiculo"
)   
    marca = models.ForeignKey(
        Marca, on_delete=models.PROTECT, related_name="Veiculo"
)   
    descricao = models.CharField(max_length=50)
    
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    def __str__(self):
        return f"{self.marca} ({self.cor} ({self.descricao})"
 