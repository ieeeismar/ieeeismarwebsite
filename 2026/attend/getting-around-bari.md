---
layout: 2026/attend-page-2026
title: Getting Around Bari
permalink: /2026/getting-around-bari/
---

<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-FQFFZGXF3Y"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-FQFFZGXF3Y');
</script>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.css" />

{% assign transport_img_path = '/assets/2026/img/bari_puglia/' %}

<style>
  .travel-note {
    font-size: 0.95rem;
    color: #555;
    margin-top: 1rem;
  }

  .quick-links {
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem;
    margin: 1.5rem 0 2rem 0;
  }

  .quick-links a,
  .route-button {
    display: inline-block;
    padding: 0.75rem 1rem;
    border-radius: 8px;
    background: #0057a8;
    color: #fff;
    text-decoration: none;
    font-weight: 600;
    text-align: center;
  }

  .quick-links a:hover,
  .route-button:hover {
    background: #003f7a;
    color: #fff;
  }

  .transport-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1rem;
    margin: 1.5rem 0;
  }

  .transport-card {
    border: 1px solid #ddd;
    border-radius: 12px;
    padding: 1rem;
    background: #fff;
  }

  .transport-card h3 {
    display: block;
    margin-top: 0;
    margin-bottom: 0.35rem;
    color: #0057a8;
  }

  .transport-card p {
    margin-bottom: 0.5rem;
  }

  .transport-section {
    margin: 1.5rem 0 2.5rem 0;
  }

  .transport-image {
    float: left;
    width: 360px;
    margin: 0 2rem 1rem 0;
  }

  .transport-image img {
    width: 100%;
    height: 240px;
    object-fit: cover;
    border-radius: 12px;
    display: block;
  }

  .transport-section::after {
    content: "";
    display: block;
    clear: both;
  }

  .venue-section {
    display: flex;
    flex-wrap: wrap;
    gap: 2rem;
    align-items: flex-start;
    margin: 2rem 0;
  }

  .venue-details {
    flex: 1 1 280px;
  }

  .venue-name {
    font-size: 1.15rem;
  }

  .google-map {
    flex: 1 1 360px;
  }

  .google-map iframe {
    width: 100%;
    max-width: 100%;
    border-radius: 12px;
  }

  .routes-intro {
    margin: 2.5rem 0 1.25rem 0;
    padding: 1.25rem 1.5rem;
    border-radius: 16px;
    background: #f5f8fb;
    border: 1px solid #e4d9c4;
  }

  .routes-intro h2 {
    margin-top: 0;
  }

  .routes-accordion {
    display: grid;
    gap: 1.2rem;
    margin: 1.5rem 0 3rem 0;
  }

  .route-panel {
    overflow: hidden;
    border-radius: 22px;
    background: #fff;
    border: 1px solid #ddd;
    box-shadow: 0 12px 30px rgba(0, 0, 0, 0.08);
  }

  .route-panel.recommended-route-panel {
    border: 2px solid #0057a8;
  }

  .route-panel summary {
    display: grid;
    grid-template-columns: 1fr auto;
    align-items: stretch;
    cursor: pointer;
    list-style: none;
  }

  .route-panel summary::-webkit-details-marker {
    display: none;
  }

  .route-summary-content {
    padding: 1.35rem 1.5rem;
  }

  .route-label {
    display: inline-block;
    width: fit-content;
    margin-bottom: 0.75rem;
    padding: 0.28rem 0.65rem;
    border-radius: 999px;
    background: #0057a8;
    color: #fff;
    font-size: 0.78rem;
    font-weight: 800;
    letter-spacing: 0.04em;
    text-transform: uppercase;
  }

  .route-label.secondary {
    background: #eef4fa;
    color: #0057a8;
  }

  .route-panel h3 {
    margin-top: 0;
    margin-bottom: 0.55rem;
    color: #0057a8;
    font-size: 1.35rem;
  }

  .route-panel p {
    color: #444;
    line-height: 1.65;
  }

  .route-meta-line {
    display: grid;
    grid-template-columns: 1fr;
    gap: 0.35rem;
    margin-top: 0.75rem;
    font-size: 0.95rem;
    color: #555;
  }

  .route-meta-line span {
    display: block;
  }

  .route-meta-line strong {
    color: #222;
  }

  .route-toggle {
    display: flex;
    align-items: center;
    justify-content: center;
    min-width: 120px;
    padding: 1rem;
    background: #eef4fa;
  }

  .route-toggle::after {
    content: "";
    width: 14px;
    height: 14px;
    border-right: 3px solid #0057a8;
    border-bottom: 3px solid #0057a8;
    transform: rotate(45deg);
    transition: transform 0.25s ease;
  }

  .route-panel[open] .route-toggle::after {
    transform: rotate(-135deg);
  }

  .route-panel-body {
    padding: 1.5rem;
    border-top: 1px solid #eee;
  }

  .route-flow {
    display: grid;
    gap: 0.5rem;
    margin: 0 0 1.5rem 0;
    text-align: center;
  }

  .route-step {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    padding: 0.75rem 1rem;
    border-radius: 10px;
    background: #eef4fa;
    border: 1px solid #cdddea;
    font-weight: 600;
  }

  .route-icon {
    font-size: 1.35rem;
    line-height: 1;
  }

  .route-arrow {
    font-size: 1.5rem;
    line-height: 1.5;
    color: #0057a8;
    font-weight: 700;
  }

  .route-table {
    width: 100%;
    margin: 1rem 0 1.5rem 0;
    border-collapse: collapse;
  }

  .route-table th,
  .route-table td {
    padding: 0.75rem;
    border: 1px solid #ddd;
    vertical-align: top;
  }

  .route-table th {
    background: #eef4fa;
    color: #1f2933 !important;
    font-weight: 800;
  }

  .route-table td {
    color: #222;
  }

  .route-table a,
  .route-table a:visited {
    color: #0057a8;
    font-weight: 800;
    text-decoration: none;
  }

  .route-table a:hover {
    color: #003f7a;
    text-decoration: underline;
  }

  .useful-links-title {
    margin-top: 1.5rem;
    margin-bottom: 0.75rem;
    font-size: 1rem;
    font-weight: 800;
  }

  .photo-gallery {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
    margin: 1.5rem auto 2rem auto;
    max-width: 900px;
  }

  .photo-gallery img {
    width: 100%;
    height: 160px;
    object-fit: cover;
    border-radius: 12px;
    display: block;
  }

  .photo-gallery-title {
    margin-top: 2rem;
    text-align: center;
  }

  .orientation-map-section {
    margin: 2rem 0 3rem 0;
  }

  .orientation-map-intro {
    margin-bottom: 1rem;
    max-width: 900px;
  }

  .orientation-map-intro p {
    color: #444;
    line-height: 1.65;
  }

  .orientation-layout {
    display: grid;
    grid-template-columns: 320px minmax(0, 1fr);
    gap: 1.25rem;
    align-items: stretch;
  }

  .orientation-list {
    display: grid;
    gap: 0.75rem;
    max-height: 680px;
    overflow: auto;
    padding-right: 0.25rem;
  }

  .orientation-card {
    display: grid;
    grid-template-columns: 44px minmax(0, 1fr);
    gap: 0.75rem;
    align-items: start;
    padding: 0.9rem;
    border: 1px solid #ddd;
    border-radius: 16px;
    background: #fff;
    cursor: pointer;
    text-align: left;
    font: inherit;
    width: 100%;
    transition: border-color 0.15s ease, box-shadow 0.15s ease, transform 0.1s ease;
  }

  .orientation-card:hover,
  .orientation-card.active {
    border-color: #0057a8;
    box-shadow: 0 8px 22px rgba(0, 87, 168, 0.14);
    transform: translateY(-1px);
  }

  .orientation-card-icon {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 42px;
    height: 42px;
    border-radius: 999px;
    color: #fff;
    font-size: 1.25rem;
    border: 3px solid #fff;
    box-shadow: 0 3px 10px rgba(0, 0, 0, 0.18);
  }

  .orientation-card h3 {
    margin: 0 0 0.25rem 0;
    font-size: 1rem;
    color: #1f2933;
  }

  .orientation-card p {
    margin: 0;
    font-size: 0.9rem;
    color: #555;
    line-height: 1.45;
  }

  .orientation-card-tag {
    display: inline-block;
    margin-top: 0.45rem;
    font-size: 0.75rem;
    font-weight: 800;
    color: #0057a8;
  }

  #bari-orientation-map {
    height: 680px;
    min-height: 560px;
    border-radius: 22px;
    border: 1px solid #ddd;
    box-shadow: 0 12px 30px rgba(0, 0, 0, 0.08);
    overflow: hidden;
  }

  .orientation-marker {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 36px;
    height: 36px;
    border-radius: 999px;
    color: #fff;
    border: 3px solid #fff;
    box-shadow: 0 3px 10px rgba(0, 0, 0, 0.28);
    font-size: 18px;
  }

  .orientation-popup strong {
    display: block;
    margin-bottom: 0.35rem;
    color: #1f2933;
  }

  .orientation-popup p {
    margin: 0 0 0.55rem 0;
    color: #444;
    line-height: 1.45;
  }

  .orientation-popup a {
    color: #0057a8;
    font-weight: 800;
    text-decoration: none;
  }

  .orientation-popup a:hover {
    text-decoration: underline;
  }

  @media (max-width: 900px) {
    .orientation-layout {
      grid-template-columns: 1fr;
    }

    .orientation-list {
      max-height: none;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      padding-right: 0;
    }

    #bari-orientation-map {
      height: 520px;
      min-height: 420px;
    }
  }

  @media (max-width: 768px) {
    .transport-image {
      float: none;
      width: 100%;
      margin: 0 0 1.25rem 0;
    }

    .transport-image img {
      height: auto;
      max-height: 300px;
    }

    .route-panel summary {
      grid-template-columns: 1fr;
    }

    .route-toggle {
      min-width: 0;
      padding: 0.75rem;
    }

    .route-table {
      display: block;
      overflow-x: auto;
      white-space: normal;
    }

    .photo-gallery {
      grid-template-columns: 1fr;
      max-width: 420px;
    }

    .photo-gallery img {
      height: 180px;
    }
  }
</style>


This page provides practical information for participants travelling around Bari during the conference. It explains the main transport options, the location of the conference venue, and the recommended routes from the airport, Bari Centrale Railway Station, and the city centre. The circles show approximate areas and are intended only to help participants understand where the main parts of Bari are located.

<section class="orientation-map-section" id="orientation-map">
  <div class="orientation-map-intro">
    <h2>Orientation Map</h2>
    <p>
      This map shows the main areas participants may need during the conference.
      Select an item from the list to locate it on the map and open Google Maps directions.
    </p>
  </div>

  <div class="orientation-layout">
    <div class="orientation-list" id="orientation-list"></div>
    <div id="bari-orientation-map"></div>
  </div>

</section>

---

## Main Transport Options in Bari {#main-transport-options}

### Urban Transport

<div class="transport-section">
  <figure class="transport-image">
    <img src="{{ transport_img_path | append: 'AMTAB.jpg' | relative_url }}" alt="AMTAB urban bus service in Bari" loading="lazy">
  </figure>

  <p>
    Bari’s urban bus network connects the city centre, Bari Centrale Railway Station, and the Poggiofranco district, where The Nicolaus Hotel is located.
  </p>

  <p>
    For travel between Bari Centrale and The Nicolaus Hotel, participants can check Bus Line 6 and live directions before departure.
  </p>

  <p>
    Tickets can usually be purchased at authorized retailers, tobacconists, kiosks, through local mobility apps, or on board where available. A standard urban ticket usually costs around €1.00–€1.50.
  </p>

  <p>
    Further information is available on the
    <a href="https://www.amtab.it/it/" target="_blank" rel="noopener noreferrer">AMTAB website</a>,
    through the
    <a href="https://www.mycicero.it/muvt/TPWebPortal/en/" target="_blank" rel="noopener noreferrer">MUVT travel planner</a>,
    or on
    <a href="https://moovitapp.com/" target="_blank" rel="noopener noreferrer">Moovit</a>.
  </p>
</div>
### Taxi, Uber and Ride-hailing

<div class="transport-section">
  <figure class="transport-image">
    <img
      src="{{ transport_img_path | append: 'Bari-Taxi.webp' | relative_url }}"
      alt="Taxi service in Bari"
      loading="lazy">
  </figure>

  <p>
    Participants can use official taxis throughout Bari, especially when travelling with luggage,
    arriving late, transferring from the airport or railway station, or returning from the Banquet
    in the evening.
  </p>

  <p>
    Taxis are available at Bari Karol Wojtyła Airport, Bari Centrale Railway Station, and in the
    main areas of the city. Participants are advised to use official licensed taxis or reliable
    transport services, especially late in the evening.
  </p>

  <p>
    For taxi information and booking, participants can check the
    <a href="https://bariintaxi.it/" target="_blank" rel="noopener noreferrer">Bari InTaxi website</a>
    or use the
    <a href="https://play.google.com/store/apps/details?id=it.ud.microtek.InTaxi&hl=en" target="_blank" rel="noopener noreferrer">InTaxi app</a>.
  </p>

  <p>
    Participants may also use
    <a href="https://www.uber.com/it/en/ride/" target="_blank" rel="noopener noreferrer">Uber</a>
    or other NCC / app-based ride-hailing services, subject to driver availability and waiting times.
    These services may be convenient for trips within the city, while taxis are usually easier directly
    from the airport arrivals area.
  </p>
</div>

### Shared Mobility

<div class="transport-section">
  <figure class="transport-image">
    <img src="{{ transport_img_path | append: 'vaimoo.jpg' | relative_url }}" alt="Vaimoo shared mobility service in Bari" loading="lazy">
  </figure>

  <p>
    Bari offers electric bike, scooter, and car-sharing services. These may be useful for short trips within the city, depending on availability, weather, luggage, and the participant’s comfort with local traffic.
  </p>

  <p>
    Available services include
    <a href="https://www.vaimoo.app/it/bari-bike-sharing/" target="_blank" rel="noopener noreferrer">Vaimoo</a>,
    <a href="https://bitmobility.it/en/app-bit-mobility-electric-scooter-bari/" target="_blank" rel="noopener noreferrer">Bit Mobility</a>,
    and
    <a href="https://www.pikyrent.com/en/sharing/" target="_blank" rel="noopener noreferrer">Pikyrent</a>.
  </p>
</div>

<div class="venue-button-wrap">
  <a href="{{ '/2026/visit-bari/' | relative_url }}" class="venue-button">
    Explore Bari Attractions
  </a>
</div>

---

## How to Reach the Conference Venue {#conference-venue}

The conference will take place at **The Nicolaus Hotel**, located in the Poggiofranco district of Bari.

The hotel is approximately 5 km from Bari Centrale Railway Station and about 16–17 km from Bari Karol Wojtyła Airport.

<div class="venue-section">
  <div class="venue-details">
    <p class="venue-name"><strong>The Nicolaus Hotel</strong></p>
    <p>Via Cardinale Agostino Ciasca 27, 70124 Bari, Italy</p>
    <p>
      <a href="https://www.thenicolaushotel.com" target="_blank" rel="noopener noreferrer">
        www.thenicolaushotel.com
      </a>
    </p>
    <p>+39 080 568 2111</p>
  </div>

  <div class="google-map">
    <iframe
      src="https://www.google.com/maps?q=The+Nicolaus+Hotel+Bari&output=embed"
      width="450"
      height="280"
      style="border:0;"
      allowfullscreen
      loading="lazy"
      referrerpolicy="no-referrer-when-downgrade">
    </iframe>
  </div>
</div>


<section class="routes-accordion">

  <details class="route-panel recommended-route-panel">
    <summary>
      <div class="route-summary-content">
        <span class="route-label">Recommended</span>
        <h3>Route 1: Bari Airport to The Nicolaus Hotel</h3>
        <p>
          The simplest and most direct option for participants staying at The Nicolaus Hotel, travelling with luggage, or arriving late.
        </p>
        <div class="route-meta-line">
          <span><strong>Approx. time:</strong> 20–30 minutes</span>
          <span><strong>Best option:</strong> Taxi or hotel shuttle</span>
        </div>
      </div>
      <span class="route-toggle" aria-hidden="true"></span>
    </summary>

    <div class="route-panel-body">
      <div class="route-flow">
        <div class="route-step">
          <span class="route-icon">✈️</span>
          <span>Bari Karol Wojtyła Airport</span>
        </div>
        <div class="route-arrow">↓</div>
        <div class="route-step">
          <span class="route-icon">🏨</span>
          <span>The Nicolaus Hotel</span>
        </div>
      </div>

      <table class="route-table">
        <thead>
          <tr>
            <th>Option</th>
            <th>Approx. time</th>
            <th>Notes</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>
              <strong>
                <a href="https://www.thenicolaushotel.com/en/hotel/services" target="_blank" rel="noopener noreferrer">
                  Nicolaus Hotel shuttle
                </a>
              </strong>
            </td>
            <td>20–30 minutes</td>
            <td>
              Free service for hotel guests, subject to availability. Book at least 24 hours before arrival or departure.
            </td>
          </tr>
          <tr>
            <td>
              <strong>
                <a href="https://bari.airports.aeroportidipuglia.it/da-e-per-gli-aeroporti/type/taxi/" target="_blank" rel="noopener noreferrer">
                  Taxi
                </a>
              </strong>
            </td>
            <td>20–30 minutes</td>
            <td>
              Usually the easiest airport option. Taxis are available outside the arrivals terminal. Fixed fare around €28.00.
              You can also check
              <a href="https://bariintaxi.it/" target="_blank" rel="noopener noreferrer">Bari InTaxi</a>.
            </td>
          </tr>
          <tr>
            <td>
              <strong>
                <a href="https://www.uber.com/it/en/ride/" target="_blank" rel="noopener noreferrer">
                  Uber or ride-hailing
                </a>
              </strong>
            </td>
            <td>20–30 minutes</td>
            <td>
              Subject to driver availability and waiting times. From the airport, taxis are usually more convenient.
            </td>
          </tr>
          <tr>
            <td>
              <strong>
                <a href="https://bari.airports.aeroportidipuglia.it/en/da-e-per-gli-aeroporti/type/noleggio-auto/" target="_blank" rel="noopener noreferrer">
                  Rental car
                </a>
              </strong>
            </td>
            <td>20–30 minutes</td>
            <td>
              Car rental services are available at Bari Airport. Follow signs for Bari Tangenziale, direction Brindisi, then take Exit 11, Bari-Poggiofranco.
            </td>
          </tr>
        </tbody>
      </table>

      <h4 class="useful-links-title">Parking near The Nicolaus Hotel</h4>
      <p>
        Parking is available in the area surrounding the conference venue. Free public parking spaces are usually available along Viale Gandhi Mohandas and in nearby streets.
      </p>
      <p>
        Paid parking is also available, particularly in Via Salvatore Matarrese. Participants should always check local signage and parking regulations before leaving their car.
      </p>
      <p>
        Where available, paid parking can be managed through the
        <a href="https://www.easypark.com/en-it" target="_blank" rel="noopener noreferrer">EasyPark</a>
        app.
      </p>
    </div>
  </details>

  <details class="route-panel">
    <summary>
      <div class="route-summary-content">
        <span class="route-label secondary">Public transport option</span>
        <h3>Route 2: Bari Airport to Bari Centrale to The Nicolaus Hotel</h3>
        <p>
          Useful for participants staying in the city centre or wishing to use public transport before continuing to the conference venue.
        </p>
        <div class="route-meta-line">
          <span><strong>Approx. time:</strong> 35–65 minutes, depending on connections</span>
          <span><strong>Best option:</strong> Train to Bari Centrale, then taxi or Bus Line 6</span>
        </div>
      </div>
      <span class="route-toggle" aria-hidden="true"></span>
    </summary>

    <div class="route-panel-body">
      <div class="route-flow">
        <div class="route-step">
          <span class="route-icon">✈️</span>
          <span>Bari Karol Wojtyła Airport</span>
        </div>
        <div class="route-arrow">↓</div>
        <div class="route-step">
          <span class="route-icon">🚉</span>
          <span>Bari Centrale Railway Station</span>
        </div>
        <div class="route-arrow">↓</div>
        <div class="route-step">
          <span class="route-icon">🏨</span>
          <span>The Nicolaus Hotel</span>
        </div>
      </div>

      <h4>Step 1: Bari Airport to Bari Centrale Railway Station</h4>

      <table class="route-table">
        <thead>
          <tr>
            <th>Option</th>
            <th>Approx. time</th>
            <th>Ticket</th>
            <th>Notes</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>
              <strong>
                <a href="https://www.ferrotramviaria.it/en/home" target="_blank" rel="noopener noreferrer">
                  Train
                </a>
              </strong>
            </td>
            <td>20 minutes</td>
            <td>€5.30</td>
            <td>
              The train station is inside the airport. Follow the signs from the arrivals area.
            </td>
          </tr>
          <tr>
            <td>
              <strong>
                <a href="https://www.autoservizitempesta.it/_wp_/servizi-orari-bus-navetta/" target="_blank" rel="noopener noreferrer">
                  Airport shuttle bus
                </a>
              </strong>
            </td>
            <td>30 minutes</td>
            <td>€5.00</td>
            <td>
              Operated by Tempesta Autolinee. The city-centre stop is in Piazza Aldo Moro, near Bari Centrale.
            </td>
          </tr>
          <tr>
            <td>
              <strong>
                <a href="https://www.mycicero.it/muvt/TPWebPortal/en/" target="_blank" rel="noopener noreferrer">
                  City Bus Line 16
                </a>
              </strong>
            </td>
            <td>40 minutes</td>
            <td>Around €1.00 on board</td>
            <td>
              Less recommended with luggage or if you are in a hurry.
            </td>
          </tr>
        </tbody>
      </table>

      <h4>Step 2: Bari Centrale Railway Station to The Nicolaus Hotel</h4>

      <table class="route-table">
        <thead>
          <tr>
            <th>Option</th>
            <th>Approx. time</th>
            <th>Notes</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>
              <strong>
                <a href="https://bariintaxi.it/" target="_blank" rel="noopener noreferrer">
                  Taxi
                </a>
                or
                <a href="https://www.uber.com/it/en/ride/" target="_blank" rel="noopener noreferrer">
                  Uber
                </a>
              </strong>
            </td>
            <td>5–10 minutes</td>
            <td>
              Easiest option with luggage. Taxi fare is approximately €10–15.
            </td>
          </tr>
          <tr>
            <td>
              <strong>
                <a href="https://moovitapp.com/" target="_blank" rel="noopener noreferrer">
                  Bus
                </a>
              </strong>
            </td>
            <td>15–25 minutes</td>
            <td>
              Check Bus Line 6 and live directions before travelling. You can also use the
              <a href="https://www.mycicero.it/muvt/TPWebPortal/en/" target="_blank" rel="noopener noreferrer">MUVT travel planner</a>.
            </td>
          </tr>
          <tr>
            <td><strong>Shared mobility</strong></td>
            <td>Varies</td>
            <td>
              Useful for short city trips, depending on availability and luggage.
              Services include
              <a href="https://www.vaimoo.app/it/bari-bike-sharing/" target="_blank" rel="noopener noreferrer">Vaimoo</a>,
              <a href="https://bitmobility.it/en/app-bit-mobility-electric-scooter-bari/" target="_blank" rel="noopener noreferrer">Bit Mobility</a>,
              and
              <a href="https://www.pikyrent.com/en/sharing/" target="_blank" rel="noopener noreferrer">Pikyrent</a>.
            </td>
          </tr>
          <tr>
            <td><strong>Walking</strong></td>
            <td>40–60 minutes</td>
            <td>
              Approximately 3–4 km. Possible, but not recommended with luggage.
            </td>
          </tr>
        </tbody>
      </table>

      <p>
        For those who wish to walk, the route can follow the tree-lined avenues of
        <a href="https://maps.app.goo.gl/36Bw5hog1WLfTP6J6" target="_blank" rel="noopener noreferrer">Viale della Repubblica</a>
        and
        <a href="https://maps.app.goo.gl/KfWFSny24HupiZpHA" target="_blank" rel="noopener noreferrer">Viale Giovanni XXIII</a>,
        which intersect near
        <a href="https://maps.app.goo.gl/8DZ3v4zMocDv13Bt6" target="_blank" rel="noopener noreferrer">Parco 2 Giugno</a>.
      </p>

      <p>
        Participants may then continue toward Poggiofranco through
        <a href="https://maps.app.goo.gl/qRHMcfrg99NfLHZy9" target="_blank" rel="noopener noreferrer">Via Mazzitelli</a>,
        an area with restaurants and new buildings.
      </p>
    </div>
  </details>

</section>


---

## How to Reach the Banquet Venue {#banquet-venue}

The Banquet will take place at **Villa Romanazzi Carducci**, a historic venue located close to Bari Centrale Railway Station and the city centre.

<div class="venue-section">
  <div class="venue-details">
    <p class="venue-name"><strong>Villa Romanazzi Carducci</strong></p>
    <p>Via G. Capruzzi 326, 70124 Bari, Italy</p>
    <p><strong>Parking entrance:</strong> Via Nicola Di Tullio 82, Bari</p>
    <p>
      <a href="https://www.villaromanazzi.com" target="_blank" rel="noopener noreferrer">
        www.villaromanazzi.com
      </a>
    </p>
    <p>+39 080 542 7400</p>
  </div>

  <div class="google-map">
    <iframe
      src="https://www.google.com/maps?q=Villa+Romanazzi+Carducci+Bari&output=embed"
      width="450"
      height="280"
      style="border:0;"
      allowfullscreen
      loading="lazy"
      referrerpolicy="no-referrer-when-downgrade">
    </iframe>
  </div>
</div>

<h2 class="photo-gallery-title">Villa Romanazzi Carducci</h2>

<div class="photo-gallery">
  <img
    src="{{ '/assets/2026/img/venue/Villa_Romanazzi.jpg' | relative_url }}"
    alt="Villa Romanazzi Carducci exterior">

  <img
    src="{{ '/assets/2026/img/venue/Villa_Romanazzi2.jpg' | relative_url }}"
    alt="Villa Romanazzi Carducci garden and pool">

  <img
    src="{{ '/assets/2026/img/venue/Villa_Romanazzi3.jpg' | relative_url }}"
    alt="Villa Romanazzi Carducci Banquet hall">
</div>


<section class="routes-accordion">

  <details class="route-panel recommended-route-panel">
    <summary>
      <div class="route-summary-content">
        <span class="route-label">Recommended</span>
        <h3>Route 1: The Nicolaus Hotel to Villa Romanazzi Carducci</h3>
        <p>
          Recommended for participants going to the Banquet from the conference hotel.
        </p>
        <div class="route-meta-line">
          <span><strong>Approx. time:</strong> 10–15 minutes by taxi or Uber</span>
          <span><strong>Best option:</strong> Taxi or Uber, especially for the evening transfer</span>
        </div>
      </div>
      <span class="route-toggle" aria-hidden="true"></span>
    </summary>

    <div class="route-panel-body">
      <div class="route-flow">
        <div class="route-step">
          <span class="route-icon">🏨</span>
          <span>The Nicolaus Hotel</span>
        </div>
        <div class="route-arrow">↓</div>
        <div class="route-step">
          <span class="route-icon">🍽️</span>
          <span>Villa Romanazzi Carducci</span>
        </div>
      </div>

      <p>
        Villa Romanazzi Carducci is approximately 3 km from The Nicolaus Hotel.
      </p>

      <table class="route-table">
        <thead>
          <tr>
            <th>Option</th>
            <th>Approx. time</th>
            <th>Notes</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>
              <strong>
                <a href="https://bariintaxi.it/" target="_blank" rel="noopener noreferrer">
                  Taxi
                </a>
                or
                <a href="https://www.uber.com/it/en/ride/" target="_blank" rel="noopener noreferrer">
                  Uber
                </a>
              </strong>
            </td>
            <td>10–15 minutes</td>
            <td>
              Recommended for the evening transfer and for returning after dinner.
            </td>
          </tr>
          <tr>
            <td>
              <strong>
                <a href="https://moovitapp.com/" target="_blank" rel="noopener noreferrer">
                  Bus
                </a>
              </strong>
            </td>
            <td>Varies</td>
            <td>
              Bus Line 6 may connect the area near The Nicolaus Hotel with stops close to Villa Romanazzi Carducci.
              Check live directions before travelling.
            </td>
          </tr>
          <tr>
            <td><strong>Shared mobility</strong></td>
            <td>Varies</td>
            <td>
              Useful for short city trips, depending on availability and weather.
              Services include
              <a href="https://www.vaimoo.app/it/bari-bike-sharing/" target="_blank" rel="noopener noreferrer">Vaimoo</a>,
              <a href="https://bitmobility.it/en/app-bit-mobility-electric-scooter-bari/" target="_blank" rel="noopener noreferrer">Bit Mobility</a>,
              and
              <a href="https://www.pikyrent.com/en/sharing/" target="_blank" rel="noopener noreferrer">Pikyrent</a>.
            </td>
          </tr>
          <tr>
            <td><strong>Walking</strong></td>
            <td>35–45 minutes</td>
            <td>
              Possible, but taxi, Uber, or public transport may be more comfortable in the evening.
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </details>

  <details class="route-panel">
    <summary>
      <div class="route-summary-content">
        <span class="route-label secondary">City-centre option</span>
        <h3>Route 2: Bari Centrale Railway Station to Villa Romanazzi Carducci</h3>
        <p>
          Useful for participants staying in the city centre or arriving from Bari Centrale Railway Station.
        </p>
        <div class="route-meta-line">
          <span><strong>Approx. time:</strong> 15–20 minutes walking, or 5–10 minutes by taxi</span>
          <span><strong>Best option:</strong> Walk or taxi, depending on time of day and luggage</span>
        </div>
      </div>
      <span class="route-toggle" aria-hidden="true"></span>
    </summary>

    <div class="route-panel-body">
      <div class="route-flow">
        <div class="route-step">
          <span class="route-icon">🚉</span>
          <span>Bari Centrale Railway Station</span>
        </div>
        <div class="route-arrow">↓</div>
        <div class="route-step">
          <span class="route-icon">🍽️</span>
          <span>Villa Romanazzi Carducci</span>
        </div>
      </div>

      <p>
        Villa Romanazzi Carducci is close to Bari Centrale Railway Station and can be reached quickly from the station area.
      </p>

      <table class="route-table">
        <thead>
          <tr>
            <th>Option</th>
            <th>Approx. time</th>
            <th>Notes</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Walking</strong></td>
            <td>15–20 minutes</td>
            <td>
              Walk along Via Giuseppe Capruzzi toward Villa Romanazzi Carducci.
            </td>
          </tr>
          <tr>
            <td>
              <strong>
                <a href="https://bariintaxi.it/" target="_blank" rel="noopener noreferrer">
                  Taxi
                </a>
                or
                <a href="https://www.uber.com/it/en/ride/" target="_blank" rel="noopener noreferrer">
                  Uber
                </a>
              </strong>
            </td>
            <td>5–10 minutes</td>
            <td>
              Taxis are available in Piazza Aldo Moro, in front of Bari Centrale.
            </td>
          </tr>
          <tr>
            <td>
              <strong>
                <a href="https://www.ferrotramviaria.it/en/home" target="_blank" rel="noopener noreferrer">
                  Metropolitan train
                </a>
              </strong>
            </td>
            <td>Varies</td>
            <td>
              Take Ferrotramviaria Line FR2 from Bari Centrale toward the airport and get off at Quintino Sella, then walk about 6 minutes.
            </td>
          </tr>
          <tr>
            <td>
              <strong>
                <a href="https://www.mycicero.it/muvt/TPWebPortal/en/" target="_blank" rel="noopener noreferrer">
                  City bus
                </a>
              </strong>
            </td>
            <td>Varies</td>
            <td>
              Urban bus lines 6, 10, and D stop near Via Quintino Sella. Check live schedules before travelling.
              You can also check directions on
              <a href="https://moovitapp.com/" target="_blank" rel="noopener noreferrer">Moovit</a>.
            </td>
          </tr>
        </tbody>
      </table>

      <h4 class="useful-links-title">Parking at the Banquet Venue</h4>
      <p>
        Villa Romanazzi Carducci has private parking with entrance from Via Nicola Di Tullio 82.
      </p>
      <p>
        Participants arriving by car should follow the signs for the hotel parking entrance and check on-site instructions on arrival.
      </p>
    </div>
  </details>

</section>


<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.js"></script>

<script>
(function () {
  function initOrientationMap() {
    if (typeof L === "undefined") {
      return setTimeout(initOrientationMap, 120);
    }

    var mapEl = document.getElementById("bari-orientation-map");
    var listEl = document.getElementById("orientation-list");

    if (!mapEl || !listEl) return;

    var map = L.map("bari-orientation-map", {
      scrollWheelZoom: false
    }).setView([41.1178, 16.8635], 13);

    L.tileLayer("https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png", {
      attribution: "© OpenStreetMap, © CARTO",
      maxZoom: 19,
      subdomains: "abcd"
    }).addTo(map);

    function mapsLink(query) {
      return "https://www.google.com/maps/search/?api=1&query=" + encodeURIComponent(query);
    }

    function popup(title, text, query) {
      return (
        '<div class="orientation-popup">' +
        "<strong>" + title + "</strong>" +
        "<p>" + text + "</p>" +
        '<a href="' + mapsLink(query) + '" target="_blank" rel="noopener noreferrer">Open in Google Maps ↗</a>' +
        "</div>"
      );
    }

    function markerIcon(symbol, color) {
      return L.divIcon({
        className: "",
        html:
          '<div class="orientation-marker" style="background:' + color + ';">' +
          symbol +
          "</div>",
        iconSize: [36, 36],
        iconAnchor: [18, 18],
        popupAnchor: [0, -18]
      });
    }

    var places = [
      // Airport first
      {
        id: "airport",
        title: "Bari Karol Wojtyła Airport",
        shortTitle: "Airport",
        text: "Arrival airport for most international participants.",
        query: "Bari Karol Wojtyła Airport, Bari, Italy",
        lat: 41.1389,
        lng: 16.7606,
        symbol: "✈️",
        color: "#ef4444",
        type: "point",
        radius: 1200,
        zoom: 13
      },

      // Bari Centrale / Piazza Aldo Moro transport area
      {
        id: "station",
        title: "Bari Centrale Railway Station / Piazza Aldo Moro",
        shortTitle: "Bari Centrale / Piazza Aldo Moro",
        text: "Main railway station. Piazza Aldo Moro is the main front entrance.",
        query: "Bari Centrale Railway Station, Piazza Aldo Moro, Bari, Italy",
        lat: 41.1174,
        lng: 16.8707,
        symbol: "🚉",
        color: "#0057a8",
        type: "point",
        radius: 350,
        zoom: 16
      },
      {
        id: "amtab",
        title: "Bari Centrale AMTAB urban bus stops",
        shortTitle: "AMTAB urban buses",
        text: "Urban bus stops near Bari Centrale for city buses, including connections toward the Poggiofranco area.",
        query: "Piazza Aldo Moro Bari AMTAB bus stop",
        lat: 41.1172,
        lng: 16.8714,
        symbol: "🚍",
        color: "#0ea5e9",
        type: "point",
        radius: 300,
        zoom: 16
      },
      {
        id: "fs-park-terminal",
        title: "FS Park Bari Terminal, Via Capruzzi",
        shortTitle: "FS Park bus terminal",
        text: "New Via Capruzzi terminal for extraurban and long-distance buses, separate from the AMTAB urban bus stops.",
        query: "FS Park Bari Terminal Via Capruzzi Bari",
        lat: 41.117126,
        lng: 16.866713,
        symbol: "🚌",
        color: "#2563eb",
        type: "point",
        radius: 280,
        zoom: 16
      },

      // Conference venue area
      {
        id: "nicolaus",
        title: "The Nicolaus Hotel",
        shortTitle: "Conference venue",
        text: "Conference venue in the Poggiofranco district.",
        query: "The Nicolaus Hotel, Bari, Italy",
        lat: 41.1036,
        lng: 16.8427,
        symbol: "🏨",
        color: "#0057a8",
        type: "point",
        zoom: 15
      },
      {
        id: "poggiofranco",
        title: "Poggiofranco district",
        shortTitle: "Poggiofranco",
        text: "District of the conference venue. Useful reference area for hotels near The Nicolaus Hotel.",
        query: "Poggiofranco, Bari, Italy",
        lat: 41.1028,
        lng: 16.8455,
        symbol: "📍",
        color: "#8b5cf6",
        type: "zone",
        radius: 850,
        zoom: 14
      },

      // City areas last
      {
        id: "bari-vecchia",
        title: "Bari Vecchia",
        shortTitle: "Bari Vecchia",
        text: "Historic old town, useful for sightseeing, restaurants, and evening walks.",
        query: "Bari Vecchia, Bari, Italy",
        lat: 41.1290,
        lng: 16.8696,
        symbol: "🏛️",
        color: "#f59e0b",
        type: "zone",
        radius: 520,
        zoom: 15
      },
      {
        id: "modern-centre",
        title: "Modern city centre",
        shortTitle: "Modern city centre",
        text: "Murattiano and Umbertino districts: shopping streets, cafés, theatres, and hotels.",
        query: "Via Sparano Bari, Italy",
        lat: 41.1230,
        lng: 16.8705,
        symbol: "🏙️",
        color: "#10b981",
        type: "zone",
        radius: 450,
        zoom: 15
      }

      ,{
        id: "banquet",
        title: "Villa Romanazzi Carducci",
        shortTitle: "Banquet venue",
        text: "Banquet venue near Bari Centrale and the city centre.",
        query: "Villa Romanazzi Carducci, Bari, Italy",
        lat: 41.1168,
        lng: 16.8597,
        symbol: "🍽️",
        color: "#0057a8",
        type: "point",
        zoom: 15
      }
      
    ];

    var markers = {};
    var cards = {};

    function setActive(id, fly) {
      var p = places.find(function (item) {
        return item.id === id;
      });

      if (!p) return;

      Object.keys(cards).forEach(function (key) {
        cards[key].classList.remove("active");
      });

      if (cards[id]) {
        cards[id].classList.add("active");
        cards[id].scrollIntoView({
          behavior: "smooth",
          block: "nearest"
        });
      }

      if (fly !== false) {
        map.flyTo([p.lat, p.lng], p.zoom || 15, {
          duration: 0.6
        });
      }

      if (markers[id]) {
        markers[id].openPopup();
      }
    }

    places.forEach(function (p) {
      if (p.radius) {
        var circle = L.circle([p.lat, p.lng], {
          radius: p.radius,
          color: p.color,
          fillColor: p.color,
          weight: 2,
          opacity: 0.9,
          fillOpacity: p.type === "zone" ? 0.16 : 0.12
        }).addTo(map);

        circle.bindPopup(popup(p.title, p.text, p.query));
        circle.on("click", function () {
          setActive(p.id, false);
        });
      }

      var marker = L.marker([p.lat, p.lng], {
        icon: markerIcon(p.symbol, p.color)
      }).addTo(map);

      marker.bindPopup(popup(p.title, p.text, p.query));
      marker.on("click", function () {
        setActive(p.id, false);
      });

      markers[p.id] = marker;

      var card = document.createElement("button");
      card.type = "button";
      card.className = "orientation-card";
      card.innerHTML =
        '<span class="orientation-card-icon" style="background:' + p.color + ';">' + p.symbol + "</span>" +
        "<span>" +
          "<h3>" + p.shortTitle + "</h3>" +
          "<p>" + p.text + "</p>" +
          '<span class="orientation-card-tag">Open on map</span>' +
        "</span>";

      card.onclick = function () {
        setActive(p.id, true);
      };

      listEl.appendChild(card);
      cards[p.id] = card;
    });

    setTimeout(function () {
      map.invalidateSize();
    }, 250);
  }

  if (document.readyState !== "loading") {
    initOrientationMap();
  } else {
    document.addEventListener("DOMContentLoaded", initOrientationMap);
  }
})();
</script>