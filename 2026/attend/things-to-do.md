---
layout: 2026/attend-page-2026
title: Things to Do
permalink: /2026/things-to-do/
---

{% assign things_img_path = '/assets/2026/img/bari_puglia/things_to_do/' %}

<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-FQFFZGXF3Y"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-FQFFZGXF3Y');
</script>

<style>
  .things-hero {
    position: relative;
    min-height: 400px;
    border-radius: 28px;
    overflow: hidden;
    display: flex;
    align-items: flex-end;
    margin-bottom: 3rem;
    background:
      linear-gradient(180deg, rgba(0, 0, 0, 0.08), rgba(0, 0, 0, 0.78)),
      url("{{ things_img_path | append: 'immagine%203.jpg' | relative_url }}") center/cover no-repeat;
    box-shadow: 0 24px 60px rgba(0, 0, 0, 0.18);
  }

  .things-hero-content {
    color: #fff;
    padding: 3rem;
    max-width: 820px;
  }

  .things-hero-kicker {
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

  .things-hero h1 {
    font-size: clamp(2.5rem, 6vw, 5rem);
    font-weight: 900;
    line-height: 1;
    margin-bottom: 1rem;
  }

  .things-hero p {
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

  .things-highlights {
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

  .activities-list {
    display: grid;
    gap: .9rem;
    max-width: 1120px;
    margin: 0 auto 3.5rem;
  }

  .activity-card {
    display: grid;
    grid-template-columns: 220px minmax(0, 1fr);
    overflow: hidden;
    border-radius: 22px;
    background: #fff;
    box-shadow: 0 12px 28px rgba(0, 0, 0, 0.08);
  }

  .activity-image {
    margin: 0;
    min-height: 0;
    background: #eee;
  }

  .activity-image img {
    width: 100%;
    height: 100%;
    min-height: 0;
    object-fit: cover;
    display: block;
  }

  .activity-content {
    padding: 1rem 1.25rem;
  }

  .activity-tag {
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

  .activity-card h2 {
    font-size: 1.28rem;
    font-weight: 900;
    margin-bottom: .45rem;
    color: #1f2933;
  }

  .activity-card p {
    color: #444;
    font-size: .96rem;
    line-height: 1.48;
    margin-bottom: .6rem;
  }

  .activity-card p:last-of-type {
    margin-bottom: .75rem;
  }

  .activity-meta {
    display: flex;
    flex-wrap: wrap;
    gap: .45rem;
    margin-top: .45rem;
  }

  .activity-meta span {
    display: inline-block;
    padding: .38rem .65rem;
    border-radius: 999px;
    background: #f8f4ee;
    color: #444;
    font-size: .84rem;
    line-height: 1.35;
  }

  .activity-meta strong {
    color: #222;
  }

  .activity-link,
  .activity-link:visited {
    color: #9c5d12 !important;
    font-weight: 800;
    text-decoration: none;
  }

  .activity-link:hover {
    color: #6d3d09 !important;
    text-decoration: underline;
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
    .things-highlights {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .activity-card {
      grid-template-columns: 190px minmax(0, 1fr);
    }
  }

  @media (max-width: 768px) {
    .activity-card {
      grid-template-columns: 1fr;
    }

    .activity-image img {
      height: 230px;
    }
  }

  @media (max-width: 575px) {
    .things-hero {
      min-height: 360px;
      border-radius: 18px;
      margin-bottom: 2.3rem;
    }

    .things-hero-content {
      padding: 1.5rem;
    }

    .things-hero p {
      font-size: 1rem;
    }

    .things-highlights {
      grid-template-columns: 1fr;
    }

    .activity-card {
      border-radius: 18px;
    }

    .activity-content {
      padding: 1rem;
    }

    .activity-card h2 {
      font-size: 1.18rem;
    }

    .activity-card p {
      font-size: .94rem;
    }

    .activity-image img {
      height: 210px;
    }
  }
</style>


Bari is a convenient starting point for a wide range of short and half-day experiences. Whether you have a couple of hours after the conference sessions or a free morning or afternoon, you can enjoy authentic local activities without committing to a full-day excursion.

  <a class="cta-link" href="https://www.getyourguide.com/s/?q=Bari&lc=721&et=1109008&searchSource=3&src=search_bar" target="_blank" rel="noopener">
    Find a Guide for these Activities and More
  </a>

<section class="activities-list">

  <article class="activity-card">
    <figure class="activity-image">
      <img src="{{ things_img_path | append: 'immagine%201.jpg' | relative_url }}" alt="Wine and extra virgin olive oil tasting in Puglia" loading="lazy">
    </figure>

    <div class="activity-content">
      <span class="activity-tag">Food and wine</span>
      <h2>Wine and Extra Virgin Olive Oil Tasting</h2>

      <p>A relaxed tasting experience is a great way to discover Puglia through its flavours. Participants can sample local wines, extra virgin olive oils and typical regional products in an informal setting.</p>

      <p>This is a good option for the late afternoon or evening, especially for small groups or networking activities.</p>

      <div class="activity-meta">
        <span><strong>Expected duration:</strong> 1–2 hours</span>
        <span><strong>Best for:</strong> food and wine lovers, informal networking, evening plans</span>
      </div>
    </div>
  </article>

  <article class="activity-card">
    <figure class="activity-image">
      <img src="{{ things_img_path | append: 'immagine%202.jpg' | relative_url }}" alt="Puglia cooking class with local food traditions" loading="lazy">
    </figure>

    <div class="activity-content">
      <span class="activity-tag">Cooking</span>
      <h2>Puglia Cooking Class</h2>

      <p>A hands-on cooking class is an enjoyable way to learn about local food traditions. Typical options include preparing fresh pasta, focaccia barese or other regional specialities.</p>

      <p>This type of activity works well for international guests, as it combines cultural discovery with a practical and social experience.</p>

      <div class="activity-meta">
        <span><strong>Expected duration:</strong> 2–3 hours</span>
        <span><strong>Best for:</strong> small groups, participants interested in local cuisine</span>
      </div>
    </div>
  </article>

  <article class="activity-card">
    <figure class="activity-image">
      <img src="{{ things_img_path | append: 'immagine%203.jpg' | relative_url }}" alt="Boat tour along the Bari coastline" loading="lazy">
    </figure>

    <div class="activity-content">
      <span class="activity-tag">Coast</span>
      <h2>Boat Tour along the Bari Coastline</h2>

      <p>A short boat tour from Bari offers a different perspective on the city and the Adriatic coast. Some options include a light aperitif on board, making it suitable for an informal post-conference activity.</p>

      <p>This is a weather-dependent experience, so it is advisable to keep an indoor alternative in case of wind or rough sea.</p>

      <div class="activity-meta">
        <span><strong>Expected duration:</strong> 1.5–2 hours</span>
        <span><strong>Best for:</strong> small groups, outdoor activities, informal evening plans</span>
      </div>
    </div>
  </article>

  <article class="activity-card">
    <figure class="activity-image">
      <img src="{{ things_img_path | append: 'immagine%204.jpg' | relative_url }}" alt="E-bike experience in the Apulian countryside" loading="lazy">
    </figure>

    <div class="activity-content">
      <span class="activity-tag">Countryside</span>
      <h2>E-bike Experience in the Apulian Countryside</h2>

      <p>
        An e-bike experience outside Bari can be a pleasant way to explore rural landscapes,
        olive groves and small local roads without requiring advanced cycling experience.
        Guided e-bike tours are available in the Bari area and can be suitable for small groups
        (<a class="activity-link" href="https://www.ebikerentalpuglia.it/bike-experiences-puglia/" target="_blank" rel="noopener">E-bike Rental Puglia</a>).
      </p>

      <p>This option is ideal for participants who would like a light outdoor activity combined with local scenery and a slower travel experience.</p>

      <div class="activity-meta">
        <span><strong>Expected duration:</strong> 3–4 hours</span>
        <span><strong>Best for:</strong> active participants, countryside landscapes</span>
      </div>
    </div>
  </article>

  <article class="activity-card">
    <figure class="activity-image">
      <img src="{{ things_img_path | append: 'immagine%205.jpg' | relative_url }}" alt="Dairy farm and burrata experience in Puglia" loading="lazy">
    </figure>

    <div class="activity-content">
      <span class="activity-tag">Local food</span>
      <h2>Dairy Farm and Burrata Experience</h2>

      <p>Puglia is well known for its fresh dairy products. A visit to a local dairy farm or cheese producer can include demonstrations of mozzarella or burrata making, followed by a tasting.</p>

      <p>This is often one of the most memorable experiences for international visitors, especially when combined with a short transfer from Bari.</p>

      <div class="activity-meta">
        <span><strong>Expected duration:</strong> 3–4 hours</span>
        <span><strong>Best for:</strong> food lovers, small groups, authentic local experiences</span>
      </div>
    </div>
  </article>

  <article class="activity-card">
    <figure class="activity-image">
      <img src="{{ things_img_path | append: 'immagine%206.jpg' | relative_url }}" alt="Olive oil mill or olive grove visit in Puglia" loading="lazy">
    </figure>

    <div class="activity-content">
      <span class="activity-tag">Olive oil</span>
      <h2>Olive Oil Mill or Olive Grove Visit</h2>

      <p>October is a particularly interesting period for olive oil experiences in Puglia, as it is close to the olive harvest season. A visit to an olive grove or oil mill can include an introduction to extra virgin olive oil production and a guided tasting.</p>

      <p>This is a good half-day option for those interested in agriculture, food quality and Mediterranean traditions.</p>

      <div class="activity-meta">
        <span><strong>Expected duration:</strong> 3–4 hours</span>
        <span><strong>Best for:</strong> food and sustainability interests, groups, autumn visitors</span>
      </div>
    </div>
  </article>

  <article class="activity-card">
    <figure class="activity-image">
      <img src="{{ things_img_path | append: 'immagine%207.jpg' | relative_url }}" alt="Winery visit in the Bari area" loading="lazy">
    </figure>

    <div class="activity-content">
      <span class="activity-tag">Wine</span>
      <h2>Winery Visit in the Bari Area</h2>

      <p>A winery visit near Bari offers the opportunity to discover Apulian wines and the rural landscape surrounding the city. Experiences may include a guided tasting, a visit to the cellar and, in some cases, a light lunch.</p>

      <p>This can be arranged as a more structured half-day activity with transport from Bari.</p>

      <div class="activity-meta">
        <span><strong>Expected duration:</strong> 3–5 hours</span>
        <span><strong>Best for:</strong> wine lovers, groups, local experiences</span>
      </div>
    </div>
  </article>

  <article class="activity-card">
    <figure class="activity-image">
      <img src="{{ things_img_path | append: 'immagine%208.jpg' | relative_url }}" alt="Kayak, SUP or boat experience near Polignano a Mare" loading="lazy">
    </figure>

    <div class="activity-content">
      <span class="activity-tag">Outdoor activity</span>
      <h2>Kayak, SUP or Boat Experiences</h2>

      <p>For participants looking for an outdoor activity, the coast near Polignano a Mare offers options such as kayaking, stand-up paddleboarding or boat tours along the cliffs and sea caves.</p>

      <p>This is a more active choice and depends on weather and sea conditions, especially in October.</p>

      <div class="activity-meta">
        <span><strong>Expected duration:</strong> 3–5 hours including transfer</span>
        <span><strong>Best for:</strong> active participants, outdoor lovers</span>
      </div>
    </div>
  </article>

</section>

<section class="recommended-box">

  <p>For a short activity after conference sessions, we recommend a wine and olive oil tasting, a cooking class or a boat tour in Bari.</p>

  <p>For a half-day experience, the most suitable options are a dairy farm visit, an olive oil experience, a winery visit, an e-bike experience in the countryside or an outdoor coastal activity near Polignano a Mare.</p>

  <p>As some outdoor activities depend on weather conditions, especially in October, it is advisable to choose an indoor alternative such as a tasting or cooking class.</p>

  <a class="cta-link" href="https://www.getyourguide.com/s/?q=Bari&lc=721&et=1109008&searchSource=3&src=search_bar" target="_blank" rel="noopener">
    Find a Guide for these Activities and More
  </a>
</section>