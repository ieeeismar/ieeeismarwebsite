---
layout: 2026/attend-page-2026
title: Visit Bari
permalink: /2026/visit-bari/

---

<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-FQFFZGXF3Y"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-FQFFZGXF3Y');
</script>

<!-- BARI ATTRACTIONS MAP -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.css" />
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">

<style>
  .attractions-guide{
    --ag-paper:#faf6ee;
    --ag-paper2:#f3ebdb;
    --ag-ink:#3a2a1c;
    --ag-muted:#7d6c58;
    --ag-line:#e4d9c4;
    --ag-card:#fffdf8;
    --ag-red:#c1372b;
    --ag-ochre:#d98324;
    --ag-blue:#2a6f97;
    --ag-green:#4f7d45;
    --ag-purple:#7a4e8a;
    --ag-shadow:0 1px 2px rgba(58,42,28,.06),0 10px 30px rgba(58,42,28,.09);
    font-family:'Poppins',system-ui,sans-serif;
    color:var(--ag-ink);
    line-height:1.5;
    max-width:1100px;
    margin:0 auto;
    padding:8px 4px 4px;
  }

  .attractions-guide *{box-sizing:border-box}

  .attractions-guide .ag-intro{
    max-width:78ch;
    margin-bottom:18px;
  }

  .attractions-guide .ag-intro p{
    font-size:16px;
    color:#4a3a2a;
    margin:0 0 12px;
  }

  .attractions-guide .ag-seclabel{
    display:flex;
    align-items:center;
    gap:12px;
    margin:6px 0 18px;
  }

  .attractions-guide .ag-seclabel h2{
    font-family:'Poppins',serif;
    font-weight:600;
    font-size:clamp(22px,3.5vw,30px);
    letter-spacing:-.01em;
    margin:0;
  }

  .attractions-guide .ag-rule{
    height:3px;
    flex:1;
    background:linear-gradient(90deg,var(--ag-red),var(--ag-ochre),var(--ag-blue),var(--ag-green));
    border-radius:2px;
    opacity:.55;
  }

  .attractions-guide .ag-controls{
    display:flex;
    flex-wrap:wrap;
    gap:10px 14px;
    align-items:center;
    margin:0 0 6px;
  }

  .attractions-guide .ag-chips{
    display:flex;
    flex-wrap:wrap;
    gap:7px;
  }

  .attractions-guide .ag-chip{
    font:inherit;
    font-size:13px;
    font-weight:500;
    cursor:pointer;
    border:1px solid var(--ag-line);
    background:var(--ag-card);
    color:var(--ag-ink);
    padding:6px 13px;
    border-radius:999px;
    transition:.15s;
    display:inline-flex;
    align-items:center;
    gap:6px;
  }

  .attractions-guide .ag-chip .ag-dot{
    width:9px;
    height:9px;
    border-radius:50%;
    background:var(--ag-muted);
  }

  .attractions-guide .ag-chip:hover{
    border-color:var(--ag-ink);
  }

  .attractions-guide .ag-chip[aria-pressed="true"]{
    background:var(--ag-ink);
    color:var(--ag-paper);
    border-color:var(--ag-ink);
  }

  .attractions-guide .ag-chip[aria-pressed="true"] .ag-dot{
    outline:2px solid var(--ag-paper);
    outline-offset:1px;
  }

  .attractions-guide .ag-sortwrap{
    margin-left:auto;
    display:flex;
    align-items:center;
    gap:8px;
    font-size:13px;
    color:var(--ag-muted);
  }

  .attractions-guide select{
    font:inherit;
    font-size:13px;
    padding:6px 28px 6px 11px;
    border-radius:8px;
    border:1px solid var(--ag-line);
    background:var(--ag-card);
    color:var(--ag-ink);
    cursor:pointer;
  }

  .attractions-guide .ag-layout{
    display:grid;
    grid-template-columns:minmax(0,1fr) minmax(0,1.05fr);
    gap:22px;
    margin-top:16px;
  }

  @media(max-width:900px){
    .attractions-guide .ag-layout{
      grid-template-columns:1fr;
    }
  }

  .attractions-guide #ag-map{
    height:min(76vh,720px);
    min-height:390px;
    border-radius:14px;
    border:1px solid var(--ag-line);
    box-shadow:var(--ag-shadow);
    position:sticky;
    top:16px;
  }

  @media(max-width:900px){
    .attractions-guide #ag-map{
      position:relative;
      top:0;
      height:54vh;
      order:-1;
    }
  }
.attractions-guide .ag-list{
  display:flex;
  flex-direction:column;
  gap:11px;
  height:min(76vh,720px);
  max-height:min(76vh,720px);
  overflow-y:auto;
  overflow-x:hidden;
  padding-right:8px;
  min-height:0;
}

/* keep the list scrollable on mobile too */
@media(max-width:900px){
  .attractions-guide .ag-list{
    height:60vh;
    max-height:60vh;
    overflow-y:auto;
  }
}
  .attractions-guide .ag-count{
    font-size:13px;
    color:var(--ag-muted);
    margin-bottom:8px;
  }
  .attractions-guide .ag-layout > div{
  min-height:0;
}

  .attractions-guide .ag-card{
    background:var(--ag-card);
    border:1px solid var(--ag-line);
    border-radius:14px;
    overflow:hidden;
    cursor:pointer;
    transition:border-color .15s,box-shadow .15s,transform .1s;
    display:grid;
    grid-template-columns:118px 1fr;
  }

  .attractions-guide .ag-card:hover{
    border-color:var(--ag-ink);
    box-shadow:var(--ag-shadow);
    transform:translateY(-1px);
  }

  .attractions-guide .ag-card.ag-active{
    border-color:var(--ag-red);
    box-shadow:0 0 0 2px rgba(193,55,43,.18);
  }

  .attractions-guide .ag-imgbox{
    position:relative;
    min-height:128px;
    background:var(--ag-paper2);
  }

  .attractions-guide .ag-imgbox img{
    width:100%;
    height:100%;
    min-height:128px;
    object-fit:cover;
    display:block;
  }

  .attractions-guide .ag-num{
    position:absolute;
    top:8px;
    left:8px;
    width:30px;
    height:30px;
    border-radius:50%;
    display:flex;
    align-items:center;
    justify-content:center;
    color:#fff;
    font-weight:800;
    font-size:13px;
    border:2px solid #fff8ee;
    box-shadow:0 2px 8px rgba(0,0,0,.25);
  }

  .attractions-guide .ag-body{
    padding:13px 14px 12px;
  }

  .attractions-guide .ag-ctop{
    display:flex;
    align-items:flex-start;
    justify-content:space-between;
    gap:10px;
  }

  .attractions-guide .ag-name{
    font-weight:700;
    font-size:17px;
    line-height:1.18;
  }

  .attractions-guide .ag-tag{
    display:inline-flex;
    align-items:center;
    gap:6px;
    font-weight:600;
    color:var(--ag-ink);
    border:1px solid var(--ag-line);
    border-radius:999px;
    padding:2px 9px;
    font-size:12px;
    white-space:nowrap;
  }

  .attractions-guide .ag-tag .ag-dot{
    width:8px;
    height:8px;
    border-radius:50%;
  }

  .attractions-guide .ag-desc{
    font-size:13px;
    color:#4a3a2a;
    margin:8px 0 0;
  }

  .attractions-guide .ag-dir{
    display:inline-flex;
    align-items:center;
    gap:6px;
    margin-top:10px;
    font-size:13px;
    font-weight:700;
    color:var(--ag-red);
    text-decoration:none;
  }

  .attractions-guide .ag-dir:hover{
    text-decoration:underline;
  }

  .ag-divicon{
    background:transparent !important;
    border:0 !important;
  }

  .ag-marker{
    width:31px;
    height:31px;
    border-radius:50% 50% 50% 6px;
    transform:rotate(-45deg);
    background:var(--ag-marker-color);
    border:2px solid #fff8ee;
    box-shadow:0 2px 8px rgba(0,0,0,.35);
    display:flex;
    align-items:center;
    justify-content:center;
  }

  .ag-marker span{
    transform:rotate(45deg);
    color:#fff;
    font-weight:800;
    font-size:12px;
    line-height:1;
  }

  .attractions-guide .leaflet-popup-content-wrapper{
    border-radius:12px;
  }

  .attractions-guide .ag-pop-img{
    width:190px;
    height:95px;
    object-fit:cover;
    border-radius:9px;
    display:block;
    margin-bottom:8px;
    background:#f3ebdb;
  }

  .attractions-guide .ag-pop-name{
    font-weight:700;
    font-size:15px;
    margin-bottom:3px;
    color:#3a2a1c;
  }

  .attractions-guide .ag-pop-meta{
    font-size:12.5px;
    color:#7d6c58;
    margin-bottom:8px;
  }

  .attractions-guide .ag-pop-link{
    font-size:13px;
    font-weight:700;
    color:#c1372b;
    text-decoration:none;
  }

  @media(max-width:560px){
    .attractions-guide .ag-card{
      grid-template-columns:1fr;
    }

    .attractions-guide .ag-imgbox img{
      height:170px;
    }

    .attractions-guide .ag-sortwrap{
      width:100%;
      margin-left:0;
    }
  }

  /* =========================================================
     FINAL SCROLL FIX
     Keep this block at the END of the <style> section.
     It forces the attractions list to use its own scrollbar.
     ========================================================= */

  .attractions-guide .ag-layout{
    display:grid !important;
    grid-template-columns:minmax(0,1fr) minmax(0,1.05fr) !important;
    gap:22px !important;
    align-items:start !important;
    margin-top:16px !important;
  }

  .attractions-guide .ag-layout > div{
    min-width:0 !important;
    min-height:0 !important;
  }

  .attractions-guide #ag-list.ag-list{
    display:flex !important;
    flex-direction:column !important;
    gap:11px !important;
    height:min(76vh,720px) !important;
    max-height:min(76vh,720px) !important;
    min-height:0 !important;
    overflow-y:auto !important;
    overflow-x:hidden !important;
    padding-right:10px !important;
    padding-bottom:6px !important;
    -webkit-overflow-scrolling:touch !important;
    overscroll-behavior:contain !important;
    scrollbar-gutter:stable !important;
  }

  .attractions-guide #ag-map{
    height:min(76vh,720px) !important;
    min-height:390px !important;
  }

  .attractions-guide .ag-card{
    flex:0 0 auto !important;
  }

  .attractions-guide #ag-list.ag-list::-webkit-scrollbar{
    width:10px;
  }

  .attractions-guide #ag-list.ag-list::-webkit-scrollbar-track{
    background:#f3ebdb;
    border-radius:999px;
  }

  .attractions-guide #ag-list.ag-list::-webkit-scrollbar-thumb{
    background:#cbbda5;
    border-radius:999px;
    border:2px solid #f3ebdb;
  }

  .attractions-guide #ag-list.ag-list::-webkit-scrollbar-thumb:hover{
    background:#a99677;
  }

  @media(max-width:900px){
    .attractions-guide .ag-layout{
      grid-template-columns:1fr !important;
    }

    .attractions-guide #ag-map{
      position:relative !important;
      top:0 !important;
      order:-1 !important;
      height:54vh !important;
      min-height:320px !important;
    }

    .attractions-guide #ag-list.ag-list{
      height:62vh !important;
      max-height:62vh !important;
      overflow-y:auto !important;
      overflow-x:hidden !important;
    }
  }

  @media(max-width:560px){
    .attractions-guide #ag-list.ag-list{
      height:65vh !important;
      max-height:65vh !important;
    }
  }

</style>

<div class="attractions-guide">
  <div class="ag-seclabel">
    <h2>Explore Bari Attractions</h2>
    <div class="ag-rule"></div>
  </div>

  <div class="ag-intro">
    <p>An interactive map of Bari’s main attractions, historic streets, churches, palaces, museums and seafront spots. Use the filters to explore by category, then click any numbered marker or card for directions.</p>
  </div>

  <div class="ag-controls">
    <div class="ag-chips" id="ag-filters"></div>

    <div class="ag-sortwrap">
      <label for="ag-sort">Sort by</label>
      <select id="ag-sort">
        <option value="route">Suggested route</option>
        <option value="category">Category</option>
        <option value="name">Name A-Z</option>
      </select>
    </div>
  </div>

  <div class="ag-layout">
    <div>
      <div class="ag-count" id="ag-count"></div>
      <div class="ag-list" id="ag-list"></div>
    </div>

    <div id="ag-map"></div>
  </div>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.js"></script>

<script>
(function(){
  function init(){
    if(typeof L === 'undefined'){
      return setTimeout(init,120);
    }

    var CATS = {
      "streets&squares": {
        label: "Streets & Squares",
        color: "#c1372b"
      },
      "palaces": {
        label: "Palaces & Theatres",
        color: "#d98324"
      },
      "museums": {
        label: "Museums & Archaeology",
        color: "#2a6f97"
      },
      "churches": {
        label: "Churches",
        color: "#7a4e8a"
      },
      "natural sites": {
        label: "Seafront & Parks",
        color: "#4f7d45"
      }
    };

    var PLACES = [
      {
        name:"Corso Vittorio Emanuele II",
        desc:"Grand boulevard connecting modern Bari with the edge of the old town.",
        cat:"streets&squares",
        lat:41.126150,
        lng:16.867750,
        img:"https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/340_Teatro_Piccinni_i_Palazzo_di_Citt%C3%A0%2C_Corso_Vittorio_Emanuele_II%2C_84_%28Bari%29.jpg/1920px-340_Teatro_Piccinni_i_Palazzo_di_Citt%C3%A0%2C_Corso_Vittorio_Emanuele_II%2C_84_%28Bari%29.jpg?_=20220922011243"
      },
      {
        name:"City Hall / Comune di Bari",
        desc:"Historic municipal building overlooking one of Bari’s main central boulevards.",
        cat:"palaces",
        lat:41.125781,
        lng:16.867731,
        img:"https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Mostra_Wiki_Loves_Puglia_2021_-_26.jpg/960px-Mostra_Wiki_Loves_Puglia_2021_-_26.jpg"
      },
      {
        name:"Teatro Piccinni",
        desc:"Bari’s oldest theatre, named after local composer Niccolò Piccinni.",
        cat:"palaces",
        lat:41.126275,
        lng:16.867403,
        img:"https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Il_Teatro_Piccinni.jpg/960px-Il_Teatro_Piccinni.jpg"
      },
      {
        name:"Palazzo Fizzarotti",
        desc:"Eclectic palace with Venetian-Gothic details and Oriental-inspired decorative elements.",
        cat:"palaces",
        lat:41.125912,
        lng:16.863472,
        img:"https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Bari_-_Palazzo_Fizzarotti_-_1.jpg/960px-Bari_-_Palazzo_Fizzarotti_-_1.jpg"
      },
      {
        name:"Castello Svevo",
        desc:"Medieval fortress marking the monumental entrance to Bari Vecchia.",
        cat:"museums",
        lat:41.128011,
        lng:16.866997,
        img:"https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Castello_normanno-svevo%2C_Bari_02.jpg/960px-Castello_normanno-svevo%2C_Bari_02.jpg"
      },
      {
        name:"Arco Basso - orecchiette street",
        desc:"Iconic alley where local women prepare handmade orecchiette outdoors.",
        cat:"streets&squares",
        lat:41.127440,
        lng:16.867050,
        img:"https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/ItWikiCon_2023_-_via_delle_orecchiette.jpg/960px-ItWikiCon_2023_-_via_delle_orecchiette.jpg?_=20240617152408"
      },
      {
        name:"Largo Albicocca",
        desc:"Charming evening square known for street food and a village-like atmosphere.",
        cat:"streets&squares",
        lat:41.127370,
        lng:16.867940,
        img:"https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Largo_Albicocca_-_Piazza_degli_Innamorati.jpg/1920px-Largo_Albicocca_-_Piazza_degli_Innamorati.jpg?_=20200921085339"
      },
      {
        name:"Cattedrale di San Sabino",
        desc:"Romanesque cathedral dedicated to Bari’s ancient patron saint.",
        cat:"churches",
        lat:41.128528,
        lng:16.868944,
        img:"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Bari_-_Cattedrale_di_San_Sabino_-_09.jpg/960px-Bari_-_Cattedrale_di_San_Sabino_-_09.jpg"
      },
      {
        name:"Succorpo della Cattedrale",
        desc:"Underground archaeological area revealing the city’s layered religious history.",
        cat:"museums",
        lat:41.128528,
        lng:16.868944,
        img:"https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Bari_-_Cattedrale_di_San_Sabino_-_2023-09-23_21-17-51_001.jpg/960px-Bari_-_Cattedrale_di_San_Sabino_-_2023-09-23_21-17-51_001.jpg"
      },
      {
        name:"Arco delle Meraviglie",
        desc:"Romantic stone arch linked to a famous local lovers’ legend.",
        cat:"streets&squares",
        lat:41.129130,
        lng:16.870240,
        img:"https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Bari%2C_Arco_delle_meraviglie.jpg/960px-Bari%2C_Arco_delle_meraviglie.jpg"
      },
      {
        name:"Strada del Carmine",
        desc:"Old-town street associated with local food traditions, especially sgagliozze.",
        cat:"streets&squares",
        lat:41.129438,
        lng:16.869090,
        img:"https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Bari_BW_2016-10-19_11-57-54.jpg/960px-Bari_BW_2016-10-19_11-57-54.jpg"
      },
      {
        name:"Basilica di San Nicola",
        desc:"Major pilgrimage church and spiritual heart of the old town.",
        cat:"churches",
        lat:41.130261,
        lng:16.870281,
        img:"https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/169_Basilica_di_San_Nicola_%28Bari%29%2C_angle_nord-est%2C_des_de_Via_Venezia.jpg/960px-169_Basilica_di_San_Nicola_%28Bari%29%2C_angle_nord-est%2C_des_de_Via_Venezia.jpg"
      },
      {
        name:"Cripta di San Nicola",
        desc:"Sacred crypt containing the relics of Saint Nicholas.",
        cat:"churches",
        lat:41.130261,
        lng:16.870281,
        img:"https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Bari%2C_san_nicola%2C_interno%2C_cripta%2C_02.jpg/960px-Bari%2C_san_nicola%2C_interno%2C_cripta%2C_02.jpg"
      },
      {
        name:"Santa Maria del Buon Consiglio",
        desc:"Evocative open-air church ruins in one of Bari’s oldest areas.",
        cat:"churches",
        lat:41.131697,
        lng:16.870238,
        img:"https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/158_Ru%C3%AFnes_de_l%27esgl%C3%A9sia_de_Santa_Maria_del_Buon_Consiglio_%28Bari%29.jpg/960px-158_Ru%C3%AFnes_de_l%27esgl%C3%A9sia_de_Santa_Maria_del_Buon_Consiglio_%28Bari%29.jpg"
      },
      {
        name:"Santa Scolastica",
        desc:"Archaeological museum area near Bari’s ancient seafront edge.",
        cat:"museums",
        lat:41.132260,
        lng:16.870830,
        img:"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/163_Muralla_de_Bari%2C_Lungomare_Imperatore_Augusto%2C_basti%C3%B3_de_Santa_Scolastica.jpg/960px-163_Muralla_de_Bari%2C_Lungomare_Imperatore_Augusto%2C_basti%C3%B3_de_Santa_Scolastica.jpg"
      },
      {
        name:"Fortino Sant’Antonio",
        desc:"Panoramic defensive bastion overlooking the old harbour and seafront.",
        cat:"palaces",
        lat:41.128260,
        lng:16.873760,
        img:"https://artbonus.gov.it/assets/components/phpthumbof/cache/d639bad09a5dac4cce058267b98ee0cc2d3bce5e.6f3fbb407888a497592168ea99c861fa.jpg"
      },
      {
        name:"Muraglia di Bari Vecchia",
        desc:"Scenic old city walls with wide views over the Adriatic Sea.",
        cat:"streets&squares",
        lat:41.128211,
        lng:16.873481,
        img:"https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Bari_-_Muraglia_di_Bari_-_2023-09-23_21-56-45_014.jpg/960px-Bari_-_Muraglia_di_Bari_-_2023-09-23_21-56-45_014.jpg"
      },
      {
        name:"Piazza Mercantile",
        desc:"Historic civic square now surrounded by cafés, restaurants and nightlife.",
        cat:"streets&squares",
        lat:41.127411,
        lng:16.872200,
        img:"https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Bari._Piazza_Mercantile.jpg/960px-Bari._Piazza_Mercantile.jpg"
      },
      {
        name:"Piazza del Ferrarese",
        desc:"Lively gateway square between Bari Vecchia and the modern city.",
        cat:"streets&squares",
        lat:41.126969,
        lng:16.871881,
        img:"https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Bari_-_Piazza_del_Ferrarese_-_2023-09-23_23-48-58_019.jpg/960px-Bari_-_Piazza_del_Ferrarese_-_2023-09-23_23-48-58_019.jpg"
      },
      {
        name:"Teatro Margherita",
        desc:"Landmark theatre built over the sea, now used for cultural events.",
        cat:"palaces",
        lat:41.126361,
        lng:16.872811,
        img:"https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Bari_-_Teatro_Margherita_-_1.jpg/960px-Bari_-_Teatro_Margherita_-_1.jpg"
      },
      {
        name:"Molo San Nicola",
        desc:"Old harbour pier with fishing boats, sea views and local life.",
        cat:"natural sites",
        lat:41.125509,
        lng:16.874439,
        img:"https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/040_Port_vell_de_Bari%2C_Molo_San_Nicola%2C_al_fons_el_Teatro_Margherita.jpg/960px-040_Port_vell_de_Bari%2C_Molo_San_Nicola%2C_al_fons_el_Teatro_Margherita.jpg"
      },
      {
        name:"N’ derr’a la lanze",
        desc:"Authentic harbour spot for raw seafood, beer and fishing boats.",
        cat:"streets&squares",
        lat:41.125488,
        lng:16.873653,
        img:"https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Bari_-_Teatro_Margherita_-2025.jpg/960px-Bari_-_Teatro_Margherita_-2025.jpg"
      },
      {
        name:"Palazzo della Provincia",
        desc:"Monumental seafront building hosting Bari’s provincial institutions and art gallery.",
        cat:"palaces",
        lat:41.121472,
        lng:16.881639,
        img:"https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Bari%2C_palazzo_della_provincia%2C_di_luigi_baffa%2C_1935%2C_01.jpg/960px-Bari%2C_palazzo_della_provincia%2C_di_luigi_baffa%2C_1935%2C_01.jpg"
      },
      {
        name:"Pinacoteca Corrado Giaquinto",
        desc:"Bari’s main public art gallery inside Palazzo della Provincia.",
        cat:"museums",
        lat:41.121472,
        lng:16.881639,
        img:"https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Bari_-_Pinacoteca_metropolitana_di_Bari_-_2024-09-26_09-36-36_001.jpg/960px-Bari_-_Pinacoteca_metropolitana_di_Bari_-_2024-09-26_09-36-36_001.jpg"
      },
      {
        name:"Lungomare Nazario Sauro",
        desc:"Elegant seafront promenade with Adriatic views and monumental architecture.",
        cat:"natural sites",
        lat:41.121748,
        lng:16.881459,
        img:"https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/Bari_-_Lungomare_Nazario_Sauro_-_202109141237_3.jpg/960px-Bari_-_Lungomare_Nazario_Sauro_-_202109141237_3.jpg"
      },
      {
        name:"Pane e Pomodoro",
        desc:"Popular city beach close to the centre and seafront promenade.",
        cat:"natural sites",
        lat:41.118540,
        lng:16.892410,
        img:"https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Bari_spiaggia_panepomodoro.JPG/960px-Bari_spiaggia_panepomodoro.JPG"
      },
      {
        name:"Corso Cavour",
        desc:"Central street with theatres, institutions, cafés and shopping opportunities.",
        cat:"streets&squares",
        lat:41.123156,
        lng:16.872609,
        img:"https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Fontana_di_Corso_Cavour_01.jpg/960px-Fontana_di_Corso_Cavour_01.jpg"
      },
      {
        name:"Teatro Petruzzelli",
        desc:"Prestigious opera house and major symbol of Bari’s cultural life.",
        cat:"palaces",
        lat:41.123567,
        lng:16.872838,
        img:"https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Bari_-_Teatro_Petruzzelli_-_Fa%C3%A7ade.jpg/960px-Bari_-_Teatro_Petruzzelli_-_Fa%C3%A7ade.jpg"
      },
      {
        name:"Palazzo dell’acqua",
        desc:"Elegant historic headquarters celebrating Puglia’s aqueduct and water infrastructure.",
        cat:"palaces",
        lat:41.123370,
        lng:16.874023,
        img:"https://www.aqp.it/sites/default/files/2020-05/Palazzo%20dell%27Acqua%20-%20Bari%20-%20Ingresso%20principale.jpg"
      },
      {
        name:"Banca d’Italia",
        desc:"Elegant institutional building located along Corso Cavour.",
        cat:"palaces",
        lat:41.124690,
        lng:16.872690,
        img:"https://catalogo.beniculturali.it/xDamsCMS/2021/07/31/IT-ICCD-CMS-0001-000534/ICCD14168859_334529_F1.jfif"
      },
      {
        name:"Camera di Commercio",
        desc:"Historic institutional building in Bari’s modern commercial centre.",
        cat:"palaces",
        lat:41.124849,
        lng:16.872569,
        img:"https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Bari_2017_by-RaBoe_052.jpg/960px-Bari_2017_by-RaBoe_052.jpg"
      },
      {
        name:"Quartiere Umbertino",
        desc:"Elegant district known for cafés, nightlife and Liberty-style architecture.",
        cat:"streets&squares",
        lat:41.123400,
        lng:16.875800,
        img:"https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Sangiuseppebari.jpg/960px-Sangiuseppebari.jpg?_=20130930074450"
      },
      {
        name:"Kursaal Santa Lucia",
        desc:"Historic seafront theatre in the elegant Umbertino district.",
        cat:"palaces",
        lat:41.123781,
        lng:16.875750,
        img:"https://cobarspa.it/wp-content/uploads/slider/cache/07f8685ee3a4270e86cca7c23001fe87/TeatroKursaalSantalucia68.jpg"
      },
      {
        name:"Quartiere Murattiano",
        desc:"Modern grid district with shopping streets and historic urban palaces.",
        cat:"streets&squares",
        lat:41.123000,
        lng:16.868500,
        img:"https://accademiacittadellanicolaiana.it/wp-content/uploads/2018/06/quartiere_murattiano_1.jpg"
      },
      {
        name:"Palazzo Mincuzzi",
        desc:"Iconic Art Nouveau commercial palace and Via Sparano landmark.",
        cat:"palaces",
        lat:41.123248,
        lng:16.869434,
        img:"https://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Bari_-_Palazzo_Mincuzzi_-_1.jpg/960px-Bari_-_Palazzo_Mincuzzi_-_1.jpg"
      },
      {
        name:"Via Sparano",
        desc:"Bari’s main pedestrian shopping street in the Murattiano district.",
        cat:"streets&squares",
        lat:41.123000,
        lng:16.869100,
        img:"https://visciourbandesign.it/wp-content/uploads/2023/09/Via-Sparano-copia.jpg.webp"
      },
      {
        name:"Piazza Aldo Moro",
        desc:"Main square in front of Bari Centrale railway station.",
        cat:"streets&squares",
        lat:41.119431,
        lng:16.869100,
        img:"https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Bari_Piazza_Aldo_Moro.jpg/960px-Bari_Piazza_Aldo_Moro.jpg"
      },
      {
        name:"Parco 2 Giugno",
        desc:"Bari’s largest urban park, ideal for walking, jogging and relaxing.",
        cat:"natural sites",
        lat:41.102900,
        lng:16.874560,
        img:"https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Scultura_ai_Paracadusti_a_Parco_2_Giugno.jpg/960px-Scultura_ai_Paracadusti_a_Parco_2_Giugno.jpg"
      },
      {
        name:"Faro di San Cataldo",
        desc:"Historic lighthouse overlooking Bari’s northern seafront and harbour area.",
        cat:"natural sites",
        lat:41.139000,
        lng:16.845100,
        img:"https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Faro_di_Bari_%28Punta_San_Cataldo%29.jpg/960px-Faro_di_Bari_%28Punta_San_Cataldo%29.jpg"
      }
    ];

    function escapeHtml(str){
      return String(str).replace(/[&<>"']/g,function(m){
        return {
          "&":"&amp;",
          "<":"&lt;",
          ">":"&gt;",
          '"':"&quot;",
          "'":"&#039;"
        }[m];
      });
    }

    function mapsUrl(place){
      return "https://www.google.com/maps/dir/?api=1&destination=" +
        encodeURIComponent(place.lat + "," + place.lng) +
        "&travelmode=walking";
    }

    function fallbackImage(place){
      var color = CATS[place.cat].color;
      var label = CATS[place.cat].label;
      var svg =
        '<svg xmlns="http://www.w3.org/2000/svg" width="600" height="360" viewBox="0 0 600 360">' +
        '<rect width="600" height="360" fill="#faf6ee"/>' +
        '<rect x="24" y="24" width="552" height="312" rx="22" fill="#f3ebdb" stroke="#e4d9c4"/>' +
        '<circle cx="300" cy="138" r="46" fill="' + color + '"/>' +
        '<text x="300" y="151" text-anchor="middle" font-family="Arial" font-size="34" font-weight="700" fill="#ffffff">IMG</text>' +
        '<text x="300" y="223" text-anchor="middle" font-family="Arial" font-size="24" font-weight="700" fill="#3a2a1c">' + escapeHtml(place.name) + '</text>' +
        '<text x="300" y="260" text-anchor="middle" font-family="Arial" font-size="18" fill="#7d6c58">' + escapeHtml(label) + '</text>' +
        '</svg>';

      return "data:image/svg+xml;charset=UTF-8," + encodeURIComponent(svg);
    }

    function getImage(place){
      if(!place.img || place.img.indexOf("IMAGE_URL_HERE") === 0){
        return fallbackImage(place);
      }
      return place.img;
    }

    var map = L.map("ag-map", {
      scrollWheelZoom:false
    }).setView([41.1258,16.8722],14);

    L.tileLayer("https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png", {
      attribution:"© OpenStreetMap, © CARTO",
      maxZoom:19,
      subdomains:"abcd"
    }).addTo(map);

    var markers = {};

    PLACES.forEach(function(p,i){
      var color = CATS[p.cat].color;

      var icon = L.divIcon({
        className:"ag-divicon",
        html:'<div class="ag-marker" style="--ag-marker-color:'+color+'"><span>'+(i+1)+'</span></div>',
        iconSize:[31,31],
        iconAnchor:[15,31],
        popupAnchor:[0,-28]
      });

      var marker = L.marker([p.lat,p.lng], {
        icon:icon
      }).addTo(map);

      marker.bindPopup(
        '<img class="ag-pop-img" src="'+escapeHtml(getImage(p))+'" alt="'+escapeHtml(p.name)+'">' +
        '<div class="ag-pop-name">'+(i+1)+'. '+escapeHtml(p.name)+'</div>' +
        '<div class="ag-pop-meta">'+escapeHtml(CATS[p.cat].label)+'</div>' +
        '<a class="ag-pop-link" href="'+mapsUrl(p)+'" target="_blank" rel="noopener">Open in Google Maps ↗</a>'
      );

      marker.on("click",function(){
        setActive(i,false);
      });

      markers[i] = marker;
    });

    var ALL = Object.keys(CATS);
    var state = {
      active:new Set(ALL),
      sort:"route",
      selected:null
    };

    var filtersEl = document.getElementById("ag-filters");
    var listEl = document.getElementById("ag-list");
    var countEl = document.getElementById("ag-count");

    var allChip = document.createElement("button");
    allChip.className = "ag-chip";
    allChip.textContent = "All";
    allChip.setAttribute("aria-pressed","true");
    allChip.onclick = function(){
      state.active = new Set(ALL);
      syncChips();
      render();
    };
    filtersEl.appendChild(allChip);

    ALL.forEach(function(cat){
      var button = document.createElement("button");
      button.className = "ag-chip";
      button.setAttribute("aria-pressed","true");
      button.setAttribute("data-cat",cat);
      button.innerHTML = '<span class="ag-dot" style="background:'+CATS[cat].color+'"></span>' + CATS[cat].label;

      button.onclick = function(){
        if(state.active.size === ALL.length){
          state.active = new Set([cat]);
        } else if(state.active.has(cat)){
          state.active.delete(cat);
          if(!state.active.size){
            state.active = new Set(ALL);
          }
        } else {
          state.active.add(cat);
        }

        syncChips();
        render();
      };

      filtersEl.appendChild(button);
    });

    function syncChips(){
      var all = state.active.size === ALL.length;
      allChip.setAttribute("aria-pressed", all ? "true" : "false");

      filtersEl.querySelectorAll("[data-cat]").forEach(function(button){
        var cat = button.getAttribute("data-cat");
        button.setAttribute("aria-pressed", (all || state.active.has(cat)) ? "true" : "false");
      });
    }

    document.getElementById("ag-sort").onchange = function(e){
      state.sort = e.target.value;
      render();
    };

    function clearActive(){
      state.selected = null;
      document.querySelectorAll(".ag-card.ag-active").forEach(function(card){
        card.classList.remove("ag-active");
      });
    }

    function setActive(index,fly){
      if(fly === undefined){
        fly = true;
      }

      clearActive();
      state.selected = index;

      var card = document.querySelector('[data-i="'+index+'"]');
      if(card){
        card.classList.add("ag-active");
        card.scrollIntoView({
          block:"nearest",
          behavior:"smooth"
        });
      }

      if(fly){
        map.flyTo([PLACES[index].lat,PLACES[index].lng],16,{
          duration:.6
        });
      }

      markers[index].openPopup();
    }

    function render(){
      var items = PLACES.map(function(p,i){
        var copy = {};
        for(var key in p){
          copy[key] = p[key];
        }
        copy.i = i;
        return copy;
      }).filter(function(p){
        return state.active.has(p.cat);
      }).sort(function(a,b){
        if(state.sort === "name"){
          return a.name.localeCompare(b.name);
        }

        if(state.sort === "category"){
          return CATS[a.cat].label.localeCompare(CATS[b.cat].label) || a.i - b.i;
        }

        return a.i - b.i;
      });

      var visibleMarkers = {};
      items.forEach(function(p){
        visibleMarkers[p.i] = true;
      });

      Object.keys(markers).forEach(function(i){
        if(visibleMarkers[i]){
          if(!map.hasLayer(markers[i])){
            markers[i].addTo(map);
          }
        } else {
          if(map.hasLayer(markers[i])){
            map.removeLayer(markers[i]);
          }
        }
      });

      if(state.selected !== null && !visibleMarkers[state.selected]){
        state.selected = null;
      }

      countEl.textContent = items.length + " attraction" + (items.length !== 1 ? "s" : "") + " shown";
      listEl.innerHTML = "";

      items.forEach(function(p){
        var color = CATS[p.cat].color;

        var card = document.createElement("div");
        card.className = "ag-card" + (state.selected === p.i ? " ag-active" : "");
        card.setAttribute("data-i",p.i);

        card.innerHTML =
          '<div class="ag-imgbox">' +
            '<img src="'+escapeHtml(getImage(p))+'" alt="'+escapeHtml(p.name)+'">' +
            '<span class="ag-num" style="background:'+color+'">'+(p.i+1)+'</span>' +
          '</div>' +
          '<div class="ag-body">' +
            '<div class="ag-ctop">' +
              '<div class="ag-name">'+escapeHtml(p.name)+'</div>' +
              '<span class="ag-tag"><span class="ag-dot" style="background:'+color+'"></span>'+escapeHtml(CATS[p.cat].label)+'</span>' +
            '</div>' +
            '<p class="ag-desc">'+escapeHtml(p.desc)+'</p>' +
            '<a class="ag-dir" href="'+mapsUrl(p)+'" target="_blank" rel="noopener" onclick="event.stopPropagation()">Open in Google Maps ↗</a>' +
          '</div>';

        card.onclick = function(){
          setActive(p.i);
        };

        listEl.appendChild(card);
      });
    }

    map.on("click",clearActive);

    render();

    setTimeout(function(){
      map.invalidateSize();

      var bounds = L.latLngBounds(PLACES.map(function(p){
        return [p.lat,p.lng];
      }));

      map.fitBounds(bounds,{
        padding:[28,28],
        maxZoom:14
      });
    },200);
  }

  if(document.readyState !== "loading"){
    init();
  } else {
    document.addEventListener("DOMContentLoaded",init);
  }
})();
</script>