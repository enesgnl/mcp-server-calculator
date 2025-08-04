# Calculator MCP

Bu proje, [MCP (Modular Command Platform)](https://mcp.so/) için geliştirilmiş, temel ve gelişmiş matematiksel işlemleri destekleyen bir hesap makinesi aracıdır.

**Geliştirici:** Enes Gönül  
**Versiyon:** 1.0.0  
**Lisans:** MIT

## Özellikler
- Toplama, çıkarma, çarpma, bölme, üs alma
- Karekök, logaritma, trigonometrik fonksiyonlar, mutlak değer
- MCP platformuna kolay entegrasyon
- Python ile doğrudan kullanılabilirlik

## Kurulum

1. Depoyu klonlayın:
   ```bash
   git clone https://github.com/enesgnl/mcp-server-calculator.git
   cd calculator_mcp
   ```

2. Sanal ortam oluşturun ve aktif edin:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows için: .venv\Scripts\activate
   ```

3. Gerekli paketleri yükleyin:
   ```bash
   pip install -e .
   # veya
   pip install -r requirements.txt
   ```

## Kullanım

### MCP Platformunda
- Projenizi [mcp.so](https://mcp.so/) adresine yükleyin.
- MCP arayüzünden `calculate` ve `advanced_math` araçlarını kullanabilirsiniz.

## Katkı
Katkıda bulunmak için lütfen bir fork oluşturun ve pull request gönderin.

## Lisans
MIT Lisansı ile lisanslanmıştır.

---

Her türlü öneri ve katkı için iletişime geçebilirsiniz.
