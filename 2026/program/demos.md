---
layout: 2026/program-page-2026
title: Demos
permalink: /2026/demos/
---

<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-FQFFZGXF3Y"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-FQFFZGXF3Y');
</script>

## Demos

**Room:** Sala Expositiva

<div class="day-nav">
  <a href="#day-1" class="day-btn"><span class="day-full">Wednesday</span><span class="day-short">Wed</span> <span class="day-date">Oct 7</span></a>
  <a href="#day-2" class="day-btn"><span class="day-full">Thursday</span><span class="day-short">Thur</span> <span class="day-date">Oct 8</span></a>
  <a href="#day-3" class="day-btn"><span class="day-full">Friday</span><span class="day-short">Fri</span> <span class="day-date">Oct 9</span></a>
</div>

{% assign demos = site.data["2026"]["program"].demos %}
{% assign day1_demos = demos | where: "Session", "07-Oct-26" %}
{% assign day2_demos = demos | where: "Session", "08-Oct-26" %}
{% assign day3_demos = demos | where: "Session", "09-Oct-26" %}

<section id="day-1" class="demo-day">
  <h3 class="demo-day-title">Wednesday - October 7, 2026</h3>

<div class="demo-day-map">
  <img src="{{ '/assets/2026/img/venue/map/demo/Demo-7-oct.png' | relative_url }}" alt="Map of demo locations for Wednesday, October 7" loading="lazy">
</div>

<section class="demo-session">
<h4 class="demo-session-title"><span>Demos</span><span class="demo-session-room">Sala Expositiva</span></h4>
<ul class="demo-list">
{% for demo in day1_demos %}
<li class="demo-item">
  <details class="demo-details" id="{{ demo['Title'] | slugify }}">
    <summary class="demo-summary">
      <span class="demo-id">Demo {{ demo["Demo ID"] }}</span>
      <span class="demo-title">{{ demo["Title"] }}</span>
      <span class="demo-authors">{{ demo["Authors"] }}</span>
    </summary>
    <div class="demo-expanded">
      <p><strong>Session:</strong> {{ demo["Session"] }}</p>
      {% if demo["Affiliations"] and demo["Affiliations"] != "" %}
      <h4>Affiliations</h4>
      <p>{{ demo["Affiliations"] | newline_to_br }}</p>
      {% endif %}
      <h4>Abstract</h4>
      <p>{{ demo["Abstract"] }}</p>
    </div>
  </details>
</li>
{% endfor %}
</ul>
</section>
</section>

<section id="day-2" class="demo-day">
  <h3 class="demo-day-title">Thursday - October 8, 2026</h3>

<div class="demo-day-map">
  <img src="{{ '/assets/2026/img/venue/map/demo/Demo-8-oct.png' | relative_url }}" alt="Map of demo locations for Thursday, October 8" loading="lazy">
</div>

<section class="demo-session">
<h4 class="demo-session-title"><span>Demos</span><span class="demo-session-room">Sala Expositiva</span></h4>
<ul class="demo-list">
{% for demo in day2_demos %}
<li class="demo-item">
  <details class="demo-details" id="{{ demo['Title'] | slugify }}">
    <summary class="demo-summary">
      <span class="demo-id">Demo {{ demo["Demo ID"] }}</span>
      <span class="demo-title">{{ demo["Title"] }}</span>
      <span class="demo-authors">{{ demo["Authors"] }}</span>
    </summary>
    <div class="demo-expanded">
      <p><strong>Session:</strong> {{ demo["Session"] }}</p>
      {% if demo["Affiliations"] and demo["Affiliations"] != "" %}
      <h4>Affiliations</h4>
      <p>{{ demo["Affiliations"] | newline_to_br }}</p>
      {% endif %}
      <h4>Abstract</h4>
      <p>{{ demo["Abstract"] }}</p>
    </div>
  </details>
</li>
{% endfor %}
</ul>
</section>
</section>

<section id="day-3" class="demo-day">
  <h3 class="demo-day-title">Friday - October 9, 2026</h3>

<div class="demo-day-map">
  <img src="{{ '/assets/2026/img/venue/map/demo/Demo-9-oct.png' | relative_url }}" alt="Map of demo locations for Friday, October 9" loading="lazy">
</div>

<section class="demo-session">
<h4 class="demo-session-title"><span>Demos</span><span class="demo-session-room">Sala Expositiva</span></h4>
<ul class="demo-list">
{% for demo in day3_demos %}
<li class="demo-item">
  <details class="demo-details" id="{{ demo['Title'] | slugify }}">
    <summary class="demo-summary">
      <span class="demo-id">Demo {{ demo["Demo ID"] }}</span>
      <span class="demo-title">{{ demo["Title"] }}</span>
      <span class="demo-authors">{{ demo["Authors"] }}</span>
    </summary>
    <div class="demo-expanded">
      <p><strong>Session:</strong> {{ demo["Session"] }}</p>
      {% if demo["Affiliations"] and demo["Affiliations"] != "" %}
      <h4>Affiliations</h4>
      <p>{{ demo["Affiliations"] | newline_to_br }}</p>
      {% endif %}
      <h4>Abstract</h4>
      <p>{{ demo["Abstract"] }}</p>
    </div>
  </details>
</li>
{% endfor %}
</ul>
</section>
</section>

<style>
.day-nav { display:flex; flex-wrap:nowrap; gap:10px; padding:12px 10px; margin:-8px -10px 8px; position:sticky; top:70px; background:#F4E8D4; z-index:11; }
.day-btn { display:inline-flex; align-items:center; justify-content:center; gap:8px; padding:10px 18px; border-radius:8px; font-size:0.9rem; font-weight:600; text-decoration:none; background:#3A8BF3; color:#fff !important; box-shadow:0 2px 4px rgba(0,0,0,.12); flex:1 1 0; min-width:0; }
.day-btn:hover { background:#2878DB; transform:translateY(-1px); box-shadow:0 3px 8px rgba(0,0,0,.18); text-decoration:none !important; color:#fff !important; }
.day-date { font-size:0.75rem; font-weight:500; opacity:0.85; }
.day-short { display:none; }
.demo-day { margin-bottom:26px; scroll-margin-top:130px; }
.demo-day-title { margin:0; font-size:1.35rem; border-bottom:none; padding:8px 10px 6px; position:sticky; top:128px; background:#F4E8D4; z-index:10; margin-left:-10px; margin-right:-10px; }
.demo-day-map { margin:12px 0 20px; }
.demo-day-map img { display:block; width:100%; max-width:420px; height:auto; margin:0 auto; border-radius:8px; }
.demo-session { margin-bottom:20px; padding:12px 14px 14px; border-radius:10px; background:rgba(58,139,243,.18); border-left:4px solid #3A8BF3; }
.demo-session-title { margin:0 0 10px; font-size:1rem; font-weight:600; display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; gap:4px 12px; color:#2878DB; }
.demo-session-room { font-size:.75rem; font-weight:500; background:#f0f0f0; padding:2px 8px; border-radius:12px; color:#555; }
.page-content ul.demo-list { list-style:none; margin:0; padding:0; }
.demo-item { margin:0 0 6px; padding:0; background:#fff; border:1px solid #e1e4e7; border-radius:8px; box-shadow:0 1px 1px rgba(0,0,0,.03); }
.demo-details { width:100%; }
.demo-summary { display:block; padding:6px 9px 6px 22px; cursor:pointer; list-style:none; position:relative; }
.demo-summary::-webkit-details-marker, .demo-summary::marker { display:none; }
.demo-summary::before { content:""; position:absolute; left:8px; top:10px; width:0; height:0; border-left:6px solid #2878DB; border-top:4px solid transparent; border-bottom:4px solid transparent; transition:transform .2s ease; }
.demo-details[open] .demo-summary::before { transform:rotate(90deg); }
.demo-details[open] .demo-summary { border-bottom:1px solid #e8eaed; }
.demo-id { display:inline-block; background:#2878DB; color:#fff; font-size:.6rem; font-weight:600; padding:5px 6px; border-radius:6px; margin:0 8px 3px 0; vertical-align:middle; line-height:1; }
.demo-title { display:inline; font-weight:600; color:#2878DB; font-size:.9rem; line-height:1.2; }
.demo-authors { display:block; font-size:.66rem; line-height:1.25; margin:3px 0 0; color:#444; }
.demo-expanded { padding:10px 12px; font-size:.82rem; line-height:1.5; color:#333; background:#f8f9fa; border-radius:0 0 7px 7px; }
.demo-expanded p { margin:0 0 8px; }
.demo-expanded h4 { margin:10px 0 4px; font-size:.9rem; }
@media (max-width:600px) {
  .day-nav { gap:4px; padding:6px 10px; }
  .day-btn { padding:5px 8px; font-size:0.65rem; gap:4px; }
  .day-date { font-size:.55rem; }
  .day-short { display:inline; }
  .day-full { display:none; }
  .demo-day-title { top:100px; font-size:1.22rem; }
  .demo-authors { font-size:.64rem; }
}
</style>
