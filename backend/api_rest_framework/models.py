from django.db import models

class  Occupation(models.Model):
  class Meta:
    db_table = "m_occupation"
  id          = models.BigIntegerField(primary_key=True, auto_created=True)
  name        = models.CharField('職業名',max_length=30, null=True, blank=True, unique=True)
  created_at  = models.DateTimeField(auto_now_add=True)
  updated_at  = models.DateTimeField(auto_now=True)
  deleted_at  = models.DateTimeField(null=True, blank=True)
  def __str__(self):
    name_str = self.name
    return name_str

# 決済方法
class Payment(models.Model):
  class Meta:
    db_table = "m_payment_methods"
  id           = models.BigIntegerField(primary_key=True, auto_created=True)
  name         = models.CharField('決済方法', max_length=30, unique=True)
  created_at   = models.DateTimeField(null=True, blank=True, auto_now_add=True)
  updated_at   = models.DateTimeField(null=True, blank=True, auto_now=True)
  deleted_at   = models.DateTimeField(null=True, blank=True)
  def __str__(self):
    name_str = self.name
    return name_str

# 決済状況
class Status(models.Model):
  class Meta:
    db_table = "m_payment_situations"
  id          = models.BigIntegerField(primary_key=True, auto_created=True)
  name        = models.CharField('決済状況',max_length=30, unique=True)
  created_at  = models.DateTimeField(auto_now_add=True)
  updated_at  = models.DateTimeField(auto_now=True)
  deleted_at  = models.DateTimeField(null=True, blank=True)
  def __str__(self):
    name_str = self.name
    return name_str

# 支払いステータス
class Payment_status(models.Model):
  class Meta:
    db_table = "m_payment_status"
  id          = models.BigIntegerField(primary_key=True, auto_created=True)
  name        = models.CharField(max_length=30, unique=True)
  created_at  = models.DateTimeField(auto_now_add=True)
  updated_at  = models.DateTimeField(auto_now=True)
  deleted_at  = models.DateTimeField(null=True, blank=True)
  def __str__(self):
    name_str = self.name
    return name_str

# 株入会ステータス
class Stock_status(models.Model):
  class Meta:
    db_table = "m_stock_status"
  id          = models.BigIntegerField(primary_key=True, auto_created=True)
  name        = models.CharField(max_length=30, null=True, blank=True, unique=True)
  created_at  = models.DateTimeField(auto_now_add=True)
  updated_at  = models.DateTimeField(auto_now=True)
  deleted_at  = models.DateTimeField(null=True, blank=True)
  def __str__(self):
    name_str = self.name
    return name_str

# サロン生
class Customer(models.Model):
  class Meta:
    db_table = 't_customers'
  fullname          = models.CharField('氏名', max_length=30, null=True, blank=True)
  fullname_kana     = models.CharField('氏名カナ', max_length=30, null=True, blank=True)
  pw                = models.CharField('パスワード', max_length=30, null=True, blank=True)
  mail              = models.EmailField('メール', null=True, blank=True, unique=True)
  tel               = models.CharField('電話', max_length=20, null=True, blank=True)
  age               = models.PositiveIntegerField('年齢', null=True, blank=True)
  occupation_id     = models.ForeignKey(Occupation, null=True, db_column="occupation_id", on_delete=models.CASCADE)
  payment_id        = models.ForeignKey(Payment, null=True, db_column="payment_id", on_delete=models.CASCADE)
  prefecture_id     = models.CharField('都道府県', max_length=5, null=True, blank=True)
  line_name         = models.CharField('LINE', max_length=20, null=True, blank=True)
  discord_name      = models.CharField('ディスコードユーザー名', max_length=30, null=True, blank=True)
  discord_id        = models.CharField('ディスコードID', max_length=30, null=True, blank=True)
  status_id         = models.ForeignKey( Status,null=True, db_column="status_id", on_delete=models.CASCADE)
  fx                = models.PositiveIntegerField('FXサロン生', null=True, blank=True)
  stock             = models.ForeignKey(Stock_status, null=True, db_column="stock", on_delete=models.CASCADE)
  afiliate_code     = models.CharField('紹介者', max_length=20, null=True, blank=True)
  role_state        = models.BooleanField('認証状態', null=True, blank=True)
  payment_status_id = models.ForeignKey(Payment_status, null=True, db_column="payment_status_id", on_delete=models.CASCADE)
  memo              = models.TextField('備考欄', null=True, blank=True)
  join_date         = models.DateField('入会日', null=True, blank=True)
  resigned_at       = models.DateField('退会日', null=True, blank=True)
  created_at        = models.DateTimeField('登録日時', null=True, blank=True, auto_now_add=True)
  updated_at        = models.DateTimeField('更新日時', null=True, blank=True, auto_now=True)
  deleted_at        = models.DateTimeField('削除日時', null=True, blank=True)
  def __str__(self):
    name_str = self.full_name
    return name_str


