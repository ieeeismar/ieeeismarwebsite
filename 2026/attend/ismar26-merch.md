---
layout: 2026/attend-page-2026
title: Purchase ISMAR 2026 Conference Merch
permalink: /2026/ismar26-merch/
---
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-FQFFZGXF3Y"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-FQFFZGXF3Y');
</script>

## ISMAR 2026 Conference Official Merch

The official ISMAR 2026 conference merch are now available to the whole community!
<div class="venue-button-wrap">
  <a href="https://ismar-2026-official-items.printify.me/" target="_blank" rel="noopener" class="venue-button" style="font-size: 18px; padding: 12px 28px; border-radius: 999px;">Purchase Merch</a>
</div>

Orders are open to both conference participants and non-participants. Production, payment, and shipping are managed through an external fulfillment platform.
The collection currently includes t-shirts, hooded sweatshirts, hats, and more.
The collection is constantly expanding, so stay tuned for more merch!

### Notes:

- Merchandise is optional and is not included in the conference registration fee.
- Prices are set by the print-on-demand platform, which requires a minimum 15% profit margin. Proceeds from this margin will be used to support ISMAR 2026 conference activities, including diversity initiatives.
- There will be no physical merchandise shop at the conference. However, the online shop will fulfill orders locally within the country of purchase, helping to reduce the carbon footprint associated with shipping.

## Some of the Merch

<style>
  .merch-products {
    position: relative;
    margin: 2rem 0;
  }

  .merch-slider-viewport {
    overflow: hidden;
  }

  .merch-slider-track {
    display: flex;
    gap: 1rem;
    animation: merch-scroll 18s linear infinite;
    will-change: transform;
  }

  @keyframes merch-scroll {
    from {
      transform: translateX(0);
    }
    to {
      transform: translateX(calc(var(--merch-slide-distance) * -5));
    }
  }

  .merch-product {
    flex: 0 0 calc((100% - 2rem) / 3);
    margin: 0;
    text-align: center;
  }

  .merch-product img {
    display: block;
    width: min(100%, 420px);
    height: auto;
    margin: 0 auto 0.75rem;
  }

  .merch-product figcaption {
    line-height: 1.5;
  }

  @media (max-width: 600px) {
    .merch-product {
      flex-basis: calc((100% - 1rem) / 2);
    }
  }

  @media (max-width: 420px) {
    .merch-product {
      flex-basis: 100%;
    }
  }
</style>

<div class="merch-products">
  <div class="merch-slider-viewport" aria-live="polite">
    <div class="merch-slider-track">
  <figure class="merch-product">
    <a href="https://ismar-2026-official-items.printify.me/product/32375398" target="_blank" rel="noopener noreferrer">
      <img src="{{ '/assets/2026/img/Merch/ismar-2026-water-bottle.jpg' | relative_url }}" alt="ISMAR 2026 Water Bottle">
    </a>
    <figcaption>
      <a href="https://ismar-2026-official-items.printify.me/product/32375398" target="_blank" rel="noopener noreferrer">ISMAR 2026 Water Bottle</a>
    </figcaption>
  </figure>

  <figure class="merch-product">
    <a href="https://ismar-2026-official-items.printify.me/product/32375079" target="_blank" rel="noopener noreferrer">
      <img src="{{ '/assets/2026/img/Merch/ismar-2026-pin-button.jpg' | relative_url }}" alt="ISMAR 2026 Pin Button">
    </a>
    <figcaption>
      <a href="https://ismar-2026-official-items.printify.me/product/32375079" target="_blank" rel="noopener noreferrer">ISMAR 2026 Pin Button</a>
    </figcaption>
  </figure>

  <figure class="merch-product">
    <a href="https://ismar-2026-official-items.printify.me/product/31796354" target="_blank" rel="noopener noreferrer">
      <img src="{{ '/assets/2026/img/Merch/ismar-2026-denim-hat.jpg' | relative_url }}" alt="ISMAR 2026 Denim Hat">
    </a>
    <figcaption>
      <a href="https://ismar-2026-official-items.printify.me/product/31796354" target="_blank" rel="noopener noreferrer">ISMAR 2026 Denim Hat</a>
    </figcaption>
  </figure>

  <figure class="merch-product">
    <a href="https://ismar-2026-official-items.printify.me/product/31796207" target="_blank" rel="noopener noreferrer">
      <img src="{{ '/assets/2026/img/Merch/ismar-2026-unisex-tshirt.jpg' | relative_url }}" alt="ISMAR 2026 Unisex T-Shirt">
    </a>
    <figcaption>
      <a href="https://ismar-2026-official-items.printify.me/product/31796207" target="_blank" rel="noopener noreferrer">ISMAR 2026 Unisex T-Shirt</a>
    </figcaption>
  </figure>

  <figure class="merch-product">
    <a href="https://ismar-2026-official-items.printify.me/product/31759737" target="_blank" rel="noopener noreferrer">
      <img src="{{ '/assets/2026/img/Merch/ismar-2026-hooded-sweatshirt.jpg' | relative_url }}" alt="ISMAR 2026 Hooded Sweatshirt">
    </a>
    <figcaption>
      <a href="https://ismar-2026-official-items.printify.me/product/31759737" target="_blank" rel="noopener noreferrer">ISMAR 2026 Hooded Sweatshirt</a>
    </figcaption>
  </figure>
    </div>
  </div>
</div>

<script>
  (() => {
    const slider = document.querySelector('.merch-products');
    const track = slider.querySelector('.merch-slider-track');
    const originalSlides = [...track.children];

    originalSlides.slice(0, 3).forEach((slide) => {
      track.appendChild(slide.cloneNode(true));
    });

    const updateSlideDistance = () => {
      const slideDistance = originalSlides[0].offsetWidth + parseFloat(getComputedStyle(track).gap);
      track.style.setProperty('--merch-slide-distance', `${slideDistance}px`);
    };

    updateSlideDistance();
    window.addEventListener('resize', updateSlideDistance);
  })();
</script>
