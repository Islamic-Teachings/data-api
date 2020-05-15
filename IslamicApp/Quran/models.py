from django.db import models

class QuranModel(models.Model):
    type = models.CharField(max_length=100)

class SurahModel(models.Model):
    quran = models.ForeignKey(QuranModel, on_delete=models.CASCADE, related_name='surahs')
    juza = models.CharField(max_length=250)
    surah_order = models.IntegerField(default=1)
    ayah_count = models.IntegerField()
    arabic_name = models.CharField(max_length=250)
    english_name = models.CharField(max_length=250)

class AyahModel(models.Model):
    surah = models.ForeignKey(SurahModel, on_delete=models.CASCADE, related_name='ayat')
    ayah_number = models.IntegerField()
    ayah_text = models.TextField(blank=False, null=False)
    ayah_relative_number = models.IntegerField()

class AyahRecitation(models.Model):
    ayah = models.ForeignKey(AyahModel, on_delete=models.CASCADE, related_name='recitations')
    reciter_name = models.CharField(max_length=250)
    reciter_media = models.TextField(blank=True, null=True)

class TafseerModel(models.Model):
    ayah = models.ForeignKey(AyahModel, on_delete=models.CASCADE, related_name='tafseers')
    language = models.CharField(max_length=250)
    audio_url = models.CharField(max_length=250)
    audio = models.TextField(blank=True, null=True)
    source = models.CharField(max_length=250)
