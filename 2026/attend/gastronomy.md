---
layout: 2026/attend-page-2026
title: Gastronomy & Local Flavours
permalink: /2026/gastronomy/
---

{% assign flavours_img_path = '/assets/2026/img/bari_puglia/local_flavours/' %}

<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-FQFFZGXF3Y"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-FQFFZGXF3Y');
</script>

<style>
  .gastronomy-hero {
    position: relative;
    min-height: 400px;
    border-radius: 28px;
    overflow: hidden;
    display: flex;
    align-items: flex-end;
    margin-bottom: 3rem;
    background:
      linear-gradient(180deg, rgba(0, 0, 0, 0.08), rgba(0, 0, 0, 0.78)),
      url("{{ flavours_img_path | append: '01_panzerotti.jpg' | relative_url }}") center/cover no-repeat;
    box-shadow: 0 24px 60px rgba(0, 0, 0, 0.18);
  }

  .gastronomy-hero-content {
    color: #fff;
    padding: 3rem;
    max-width: 850px;
  }

  .gastronomy-hero-kicker {
    display: inline-block;
    margin-bottom: 1rem;
    padding: .45rem .85rem;
    border-radius: 999px;
    background: rgba(255, 255, 255, 0.18);
    backdrop-filter: blur(6px);
    font-size: .8rem;
    font-weight: 800;
    letter-spacing: .08em;
    text-transform: uppercase;
  }

  .gastronomy-hero h1 {
    font-size: clamp(2.5rem, 6vw, 5rem);
    font-weight: 900;
    line-height: 1;
    margin-bottom: 1rem;
  }

  .gastronomy-hero p {
    font-size: 1.1rem;
    line-height: 1.65;
    margin-bottom: 0;
  }

  .section-intro {
    max-width: 920px;
    margin: 0 auto 2.4rem;
    text-align: center;
  }

  .section-intro h2 {
    font-weight: 900;
    margin-bottom: 1rem;
  }

  .section-intro p {
    font-size: 1.02rem;
    line-height: 1.75;
    color: #3f3f3f;
  }

  .gastronomy-highlights {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: .85rem;
    margin-bottom: 2.6rem;
  }

  .highlight-box {
    padding: 1rem 1.1rem;
    border-radius: 18px;
    background: #f8f4ee;
    border: 1px solid rgba(0, 0, 0, 0.06);
  }

  .highlight-box strong {
    display: block;
    font-size: 1.45rem;
    line-height: 1;
    margin-bottom: .3rem;
    color: #9c5d12;
  }

  .highlight-box span {
    font-size: .92rem;
    color: #444;
  }

  .food-section-title {
    max-width: 1120px;
    margin: 2.8rem auto 1rem;
  }

  .food-section-title h2 {
    font-weight: 900;
    margin-bottom: .45rem;
  }

  .food-section-title p {
    max-width: 850px;
    color: #444;
    line-height: 1.7;
    margin-bottom: 0;
  }

  .food-list {
    display: grid;
    gap: .9rem;
    max-width: 1120px;
    margin: 0 auto 3.5rem;
  }

  .food-card {
    display: grid;
    grid-template-columns: 220px minmax(0, 1fr);
    overflow: hidden;
    border-radius: 22px;
    background: #fff;
    box-shadow: 0 12px 28px rgba(0, 0, 0, 0.08);
  }

  .food-image {
    margin: 0;
    min-height: 0;
    background: #eee;
  }

  .food-image img {
    width: 100%;
    height: 100%;
    min-height: 0;
    object-fit: cover;
    display: block;
  }

  .food-content {
    padding: 1rem 1.25rem;
  }

  .food-tag {
    display: inline-block;
    width: fit-content;
    margin-bottom: .5rem;
    padding: .25rem .6rem;
    border-radius: 999px;
    background: #fff1db;
    color: #7b470e;
    font-size: .68rem;
    font-weight: 900;
    letter-spacing: .05em;
    text-transform: uppercase;
  }

  .food-card h2 {
    font-size: 1.28rem;
    font-weight: 900;
    margin-bottom: .45rem;
    color: #1f2933;
  }

  .food-card p {
    color: #444;
    font-size: .96rem;
    line-height: 1.48;
    margin-bottom: .6rem;
  }

  .food-card p:last-of-type {
    margin-bottom: .75rem;
  }

  .food-fillings {
    columns: 2;
    column-gap: 2rem;
    margin: .5rem 0 .75rem;
    padding-left: 1.2rem;
    color: #444;
    font-size: .94rem;
    line-height: 1.55;
  }

  .food-meta {
    display: flex;
    flex-wrap: wrap;
    gap: .45rem;
    margin-top: .45rem;
  }

  .food-meta span {
    display: inline-block;
    padding: .38rem .65rem;
    border-radius: 999px;
    background: #f8f4ee;
    color: #444;
    font-size: .84rem;
    line-height: 1.35;
  }

  .food-meta strong {
    color: #222;
  }

  .recommended-box {
    max-width: 1120px;
    margin: 0 auto 3rem;
    padding: 1.35rem 1.5rem;
    border-left: 6px solid #c58b38;
    border-radius: 16px;
    background: #f8f4ee;
    line-height: 1.7;
  }

  .recommended-box h2 {
    font-weight: 900;
    margin-bottom: .85rem;
  }

  .recommended-box p {
    margin-bottom: .8rem;
  }

  .recommended-box p:last-child {
    margin-bottom: 0;
  }

  .cta-link,
  .cta-link:visited {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    margin-top: .6rem;
    padding: .68rem 1rem;
    border-radius: 999px;
    background: #0d7dff;
    color: #fff !important;
    font-weight: 900;
    text-decoration: none;
  }

  .cta-link:hover {
    background: #075fbe;
    color: #fff !important;
    text-decoration: none;
  }

  @media (max-width: 991px) {
    .gastronomy-highlights {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .food-card {
      grid-template-columns: 190px minmax(0, 1fr);
    }
  }

  @media (max-width: 768px) {
    .food-card {
      grid-template-columns: 1fr;
    }

    .food-image img {
      height: 230px;
    }

    .food-fillings {
      columns: 1;
    }
  }

  @media (max-width: 575px) {
    .gastronomy-hero {
      min-height: 360px;
      border-radius: 18px;
      margin-bottom: 2.3rem;
    }

    .gastronomy-hero-content {
      padding: 1.5rem;
    }

    .gastronomy-hero p {
      font-size: 1rem;
    }

    .gastronomy-highlights {
      grid-template-columns: 1fr;
    }

    .food-card {
      border-radius: 18px;
    }

    .food-content {
      padding: 1rem;
    }

    .food-card h2 {
      font-size: 1.18rem;
    }

    .food-card p {
      font-size: .94rem;
    }

    .food-image img {
      height: 210px;
    }
  }
</style>



Bari and Puglia offer a rich food tradition that is easy to enjoy between conference sessions, during a walk through Bari Vecchia or as part of a longer evening meal. This selection highlights some of the most typical local specialities visitors may want to try.



<section class="food-section-title">
  <h2>Street Food and Local Bites</h2>
  <p>These are some of the easiest specialities to enjoy while walking around Bari, especially in the old town or near bakeries, fry shops and casual takeaway places.</p>
</section>

<section class="food-list">

  <article class="food-card">
    <figure class="food-image">
      <img src="{{ flavours_img_path | append: '03_focaccia.jpg' | relative_url }}" alt="Focaccia barese with tomatoes and olives" loading="lazy">
    </figure>

    <div class="food-content">
      <span class="food-tag">Local classic</span>
      <h2>Focaccia Barese</h2>

      <p>Bari-style focaccia is usually round and topped with tomatoes, olives and plenty of olive oil. It can be thin and crispy or thicker and softer depending on the bakery.</p>

      <p><strong>Local note:</strong> watch out for the olive pits.</p>

      <div class="food-meta">
        <span><strong>Best for:</strong> breakfast, snack, casual lunch</span>
        <span><strong>Where to try:</strong> bakeries around Bari</span>
      </div>
    </div>
  </article>

  <article class="food-card">
    <figure class="food-image">
      <img src="{{ flavours_img_path | append: '08_paninopolpo.jpg' | relative_url }}" alt="Panino with octopus and stracciatella" loading="lazy">
    </figure>

    <div class="food-content">
      <span class="food-tag">Seafood sandwich</span>
      <h2>Panino con Polpo e Stracciatella</h2>

      <p>This sandwich combines octopus with stracciatella cheese. It has become very popular and is easy to find in Bari and in other coastal towns.</p>

      <div class="food-meta">
        <span><strong>Best for:</strong> seafood lovers, casual lunch</span>
        <span><strong>Where to try:</strong> Bari and nearby coastal towns</span>
      </div>
    </div>
  </article>

  <article class="food-card">
    <figure class="food-image">
      <img src="{{ flavours_img_path | append: '01_panzerotti.jpg' | relative_url }}" alt="Panzerotti from Bari" loading="lazy">
    </figure>

    <div class="food-content">
      <span class="food-tag">Must try</span>
      <h2>Panzerotti</h2>

      <p>Panzerotti are one of the most popular snacks in Bari, especially for anyone who enjoys fried food. The classic version is filled with tomato sauce and mozzarella, but many other variations are available.</p>

      <p><strong>Try as many as you can.</strong></p>

      <div class="food-meta">
        <span><strong>Best for:</strong> street food, quick lunch, late-night snack</span>
        <span><strong>Where to try:</strong> bakeries, fry shops and Bari Vecchia</span>
      </div>
    </div>
  </article>

  <article class="food-card">
    <figure class="food-image">
      <img src="{{ flavours_img_path | append: '02_scagliozze.jpg' | relative_url }}" alt="Sgagliozze and popizze in Bari" loading="lazy">
    </figure>

    <div class="food-content">
      <span class="food-tag">Bari Vecchia</span>
      <h2>Sgagliozze and Popizze</h2>

      <p>Sgagliozze are fried pieces of maize polenta, while popizze are small pieces of fried dough. They are among the most recognisable snacks of Bari Vecchia.</p>

      <p>You may find them prepared by local frying ladies, including well-known spots such as Maria in Via Carmine and Carmela in Largo Albicocca.</p>

      <div class="food-meta">
        <span><strong>Best for:</strong> walking around the old town</span>
        <span><strong>Style:</strong> simple, fried, traditional</span>
      </div>
    </div>
  </article>

  <article class="food-card">
    <figure class="food-image">
      <img src="{{ flavours_img_path | append: '04_taralli.jpg' | relative_url }}" alt="Traditional taralli from Puglia" loading="lazy">
    </figure>

    <div class="food-content">
      <span class="food-tag">Snack</span>
      <h2>Taralli</h2>

      <p>Taralli are small ring-shaped savoury snacks, usually crunchy or crumbly. They come in many flavours, including onion, garlic, sesame seeds, fennel, black pepper and chilli.</p>

      <div class="food-meta">
        <span><strong>Best for:</strong> aperitivo, travel snack, edible souvenir</span>
        <span><strong>Style:</strong> crunchy and savoury</span>
      </div>
    </div>
  </article>
</section>

<section class="food-section-title">
  <h2>Fresh Dairy, Cheese and Cured Meat</h2>
  <p>Puglia is especially appreciated for fresh dairy products and simple ingredients. These options work well as starters, aperitivo items or part of a shared meal.</p>
</section>

<section class="food-list">

  <article class="food-card">
    <figure class="food-image">
      <img src="{{ flavours_img_path | append: '06_caciocavallo.jpg' | relative_url }}" alt="Caciocavallo cheese from Apulia" loading="lazy">
    </figure>

    <div class="food-content">
      <span class="food-tag">Cheese</span>
      <h2>Caciocavallo</h2>

      <p>Caciocavallo is a traditional local cheese found in many varieties across Apulia. It may be soft, hard, aged in wine or matured in caves.</p>

      <div class="food-meta">
        <span><strong>Best for:</strong> cheese boards and tastings</span>
        <span><strong>Style:</strong> mild to aged, depending on variety</span>
      </div>
    </div>
  </article>

  <article class="food-card">
    <figure class="food-image">
      <img src="{{ flavours_img_path | append: '07_capocollo.jpg' | relative_url }}" alt="Capocollo di Martina Franca" loading="lazy">
    </figure>

    <div class="food-content">
      <span class="food-tag">Cured meat</span>
      <h2>Capocollo di Martina Franca</h2>

      <p>Capocollo di Martina Franca is a local cured meat made from pork neck muscle. It is marinated with spices and cooked wine, lightly smoked and aged.</p>

      <div class="food-meta">
        <span><strong>Best for:</strong> aperitivo and local tastings</span>
        <span><strong>Origin:</strong> Martina Franca area</span>
      </div>
    </div>
  </article>

  <article class="food-card">
    <figure class="food-image">
      <img src="{{ flavours_img_path | append: '05_mozzarella.jpg' | relative_url }}" alt="Mozzarella, burrata and stracciatella from Puglia" loading="lazy">
    </figure>

    <div class="food-content">
      <span class="food-tag">Fresh dairy</span>
      <h2>Mozzarella, Burrata and Stracciatella</h2>

      <p>Puglia is one of Italy’s major producers of cow’s milk mozzarella. Stracciatella is made from strips of mozzarella mixed with fresh cream, while burrata is mozzarella filled with stracciatella.</p>

      <div class="food-meta">
        <span><strong>Best for:</strong> starters, tastings, light meals</span>
        <span><strong>Try with:</strong> tomatoes, olive oil and bread</span>
      </div>
    </div>
  </article>
</section>

<section class="food-section-title">
  <h2>Main Dishes</h2>
  <p>These dishes are especially suitable for a relaxed lunch or dinner, and they show the strong home-cooking tradition of Bari and the wider Puglia region.</p>
</section>

<section class="food-list">

  <article class="food-card">
    <figure class="food-image">
      <img src="{{ flavours_img_path | append: '16_bombette.jpeg' | relative_url }}" alt="Bombette from Puglia" loading="lazy">
    </figure>

    <div class="food-content">
      <span class="food-tag">Grilled meat</span>
      <h2>Bombette</h2>

      <p>Bombette are small pork meat roulades with different fillings. They can be grilled or fried and are commonly found in restaurants, butcher shops and street-food places.</p>

      <div class="food-meta">
        <span><strong>Best for:</strong> meat lovers and informal dinners</span>
        <span><strong>Style:</strong> grilled or fried, filled, savoury</span>
      </div>
    </div>
  </article>

  <article class="food-card">
    <figure class="food-image">
      <img src="{{ flavours_img_path | append: '10_faveecicorie.jpg' | relative_url }}" alt="Fave e cicoria traditional dish from Bari" loading="lazy">
    </figure>

    <div class="food-content">
      <span class="food-tag">Vegetarian</span>
      <h2>Fave e Cicoria</h2>

      <p>One of the most traditional dishes in Bari: mashed broad beans served with boiled chicory. It is simple, vegetarian and usually eaten with bread and good extra virgin olive oil.</p>

      <div class="food-meta">
        <span><strong>Best for:</strong> vegetarian diners and traditional meals</span>
        <span><strong>Style:</strong> simple, rustic, comforting</span>
      </div>
    </div>
  </article>

  <article class="food-card">
    <figure class="food-image">
      <img src="{{ flavours_img_path | append: '13_orecchiette.jpg' | relative_url }}" alt="Orecchiette con le cime di rapa" loading="lazy">
    </figure>

    <div class="food-content">
      <span class="food-tag">Pasta</span>
      <h2>Orecchiette con le Cime di Rapa</h2>

      <p>One of the most famous pasta dishes from Puglia, made with local orecchiette pasta and turnip tops. It is traditionally considered a winter dish.</p>

      <div class="food-meta">
        <span><strong>Best for:</strong> pasta lovers and traditional dining</span>
        <span><strong>Style:</strong> seasonal, simple, iconic</span>
      </div>
    </div>
  </article>

  <article class="food-card">
    <figure class="food-image">
      <img src="{{ flavours_img_path | append: '14_orecchietteragubraciole.jpeg' | relative_url }}" alt="Orecchiette con ragù di braciole" loading="lazy">
    </figure>

    <div class="food-content">
      <span class="food-tag">Sunday dish</span>
      <h2>Orecchiette con Ragù di Braciole</h2>

      <p>A local classic with orecchiette pasta, tomato sauce and meat roulades. It is a typical Sunday dish.</p>

      <div class="food-meta">
        <span><strong>Best for:</strong> hearty meals and local restaurants</span>
        <span><strong>Style:</strong> rich, traditional, meat-based</span>
      </div>
    </div>
  </article>

  <article class="food-card">
    <figure class="food-image">
      <img src="{{ flavours_img_path | append: '12_parmigiana.jpg' | relative_url }}" alt="Parmigiana di melanzane" loading="lazy">
    </figure>

    <div class="food-content">
      <span class="food-tag">Comfort food</span>
      <h2>Parmigiana di Melanzane</h2>

      <p>Fried slices of eggplant layered with cheese and tomato sauce, then baked. It is also common in takeaway places.</p>

      <div class="food-meta">
        <span><strong>Best for:</strong> comfort food and takeaway meals</span>
        <span><strong>Style:</strong> rich, baked, vegetarian</span>
      </div>
    </div>
  </article>

  <article class="food-card">
    <figure class="food-image">
      <img src="{{ flavours_img_path | append: '11_risopatateecozze.jpg' | relative_url }}" alt="Riso patate e cozze from Bari" loading="lazy">
    </figure>

    <div class="food-content">
      <span class="food-tag">Bari classic</span>
      <h2>Riso, Patate e Cozze</h2>

      <p>A traditional baked dish made with rice, potatoes and mussels. Local families often debate the correct recipe, including whether zucchini should be added or not.</p>

      <div class="food-meta">
        <span><strong>Best for:</strong> traditional lunch or dinner</span>
        <span><strong>Style:</strong> baked, savoury, local</span>
      </div>
    </div>
  </article>

  <article class="food-card">
    <figure class="food-image">
      <img src="{{ flavours_img_path | append: '15_spaghettiassassina.jpeg' | relative_url }}" alt="Spaghetti all'assassina from Bari" loading="lazy">
    </figure>

    <div class="food-content">
      <span class="food-tag">Spicy</span>
      <h2>Spaghetti all’Assassina</h2>

      <p>Also known as “killer spaghetti”, this dish is spicy and slightly crunchy because the spaghetti are cooked directly in tomato sauce.</p>

      <div class="food-meta">
        <span><strong>Best for:</strong> adventurous pasta lovers</span>
        <span><strong>Style:</strong> spicy, crispy, very Bari</span>
      </div>
    </div>
  </article>
</section>

<section class="food-section-title">
  <h2>Seafood</h2>
  <p>Bari’s connection with the sea is also part of its food identity. Seafood can be enjoyed in casual sandwiches, restaurants or traditional market settings.</p>
</section>

<section class="food-list">

  <article class="food-card">
    <figure class="food-image">
      <img src="{{ flavours_img_path | append: '09_rawfish.jpg' | relative_url }}" alt="Raw seafood in Bari" loading="lazy">
    </figure>

    <div class="food-content">
      <span class="food-tag">Seafood</span>
      <h2>Raw Fish</h2>

      <p>People from Bari love eating raw seafood. You may find it at the fish market near the old port, in seafood restaurants or in coastal areas such as Savelletri.</p>

      <div class="food-meta">
        <span><strong>Best for:</strong> seafood lovers</span>
        <span><strong>Where to try:</strong> old port, seafood restaurants and coastal towns</span>
      </div>
    </div>
  </article>
</section>

<section class="food-section-title">
  <h2>Puglian Desserts</h2>
  <p>To finish the meal, Puglia offers simple pastries and cream-filled sweets that are easy to find in local pastry shops.</p>
</section>

<section class="food-list">

  <article class="food-card">
    <figure class="food-image">
      <img src="{{ flavours_img_path | append: '17_pasticciotto.jpg' | relative_url }}" alt="Pasticciotto from Lecce" loading="lazy">
    </figure>

    <div class="food-content">
      <span class="food-tag">Pastry</span>
      <h2>Pasticciotti</h2>

      <p>Sweet pastries originally from Lecce, made with shortcrust pastry and filled with custard cream.</p>

      <div class="food-meta">
        <span><strong>Best for:</strong> breakfast or dessert</span>
        <span><strong>Style:</strong> sweet pastry with custard</span>
      </div>
    </div>
  </article>

  <article class="food-card">
    <figure class="food-image">
      <img src="{{ flavours_img_path | append: '19_sporcamousse.jpg' | relative_url }}" alt="Sporcamuss" loading="lazy">
    </figure>

    <div class="food-content">
      <span class="food-tag">Sweet treat</span>
      <h2>Sporcamuss</h2>

      <p>Small pastries made with puff pastry and cream. Their name comes from the local dialect and means “dirty face”, because they are often dusted with powdered sugar.</p>

      <div class="food-meta">
        <span><strong>Best for:</strong> quick dessert or coffee break</span>
        <span><strong>Style:</strong> flaky, creamy, powdered sugar</span>
      </div>
    </div>
  </article>

  <article class="food-card">
    <figure class="food-image">
      <img src="{{ flavours_img_path | append: '18_tette.jpg' | relative_url }}" alt="Tette delle monache pastry from Altamura" loading="lazy">
    </figure>

    <div class="food-content">
      <span class="food-tag">Cream pastry</span>
      <h2>Tette delle Monache</h2>

      <p>Soft pastries filled with cream. They were originally prepared by nuns in monasteries around Altamura and can still be found in some pastry shops.</p>

      <div class="food-meta">
        <span><strong>Best for:</strong> pastry shops and dessert breaks</span>
        <span><strong>Style:</strong> soft, sweet, cream-filled</span>
      </div>
    </div>
  </article>
</section>

<section class="recommended-box">

  <p>For a quick taste of Bari, start with focaccia barese, panzerotti, sgagliozze, popizze or taralli. These are easy options for a short break, a walk through Bari Vecchia or an informal snack between activities.</p>

  <p>For a traditional meal, try orecchiette con le cime di rapa, riso patate e cozze, fave e cicoria, spaghetti all’assassina or orecchiette with ragù di braciole.</p>

  <p>For a shared local experience, fresh mozzarella, burrata, stracciatella, caciocavallo, capocollo and raw seafood are especially good choices for small groups and informal dinners.</p>

  <a class="cta-link" href="https://www.getyourguide.com/s/?q=Bari%20food&lc=721&searchSource=3&src=search_bar" target="_blank" rel="noopener">
    Explore Bari food experiences
  </a>
</section>