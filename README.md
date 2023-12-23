
# MultiPastingBot

## Genel Bakış
Bu Telegram botu, metin veya kod parçalarını paylaşmayı kolaylaştırmak için tasarlanmıştır. Bot, çeşitli hizmetler aracılığıyla metinleri yapıştırma (paste) işlemine tabi tutar ve paylaşılabilir bağlantılar oluşturur.

## Özellikler
1. Metin veya kod parçacığını paylaşmak için ilgili komutları kullanabilirsiniz.
    - Örneğin: `/paste <metin veya dosya_yanıtlama>`.
2. Bot, verilen içeriği seçilen yapıştırma hizmeti ile işleyerek paylaşılabilir bir bağlantı üretir.
3. Oluşturulan bağlantıyı alıp istediğiniz gibi paylaşabilirsiniz.

## Kullanım
1. Varsayılan yapıştırma hizmeti ile metin veya dosya gönderme:
    - `/paste` (spaceb.in)
2. Farklı yapıştırma hizmetlerini kullanma seçenekleri:
    - `/nekobin` (nekobin.com)
    - `/dpaste` (dpaste.org)
    - `/spacebin` (spaceb.in)
    - `/pasty` (pasty.lus.pm)
    - `/centos` (paste.centos.org)

## Kurulum
1. Depoyu klonlayın: `git clone https://github.com/suphiozturk8/MultiPastingBot.git && cd MultiPastingBot`
2. Bağımlılıkları yükleyin: `pip install -r requirements.txt`
3. Telegram bot tokenınızı `config.py` dosyasında ayarlayın.
4. Botu çalıştırın: `python main.py`

## Lisans
Bu proje [MIT Lisansı](LICENSE) altında lisanslanmıştır.