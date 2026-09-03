---
layout: 2026/program-page-2026
title: Posters
permalink: /2026/posters/
---
---
*Last updated: 2026-08-28 7:14PM EDT*

---

All accepted posters, including those invited from the Doctoral Consortium and TVCG Journal papers, are assigned to a specific day, which has multiple presentation timeslots throughout that day. We **highly recommend being at your posters** during the allocated timeslots! This is a great opportunity to network and talk to other conference attendees.

This year, there are **no traditional poster fast-forward sessions.** Instead, fast-forward poster videos that you submitted will be showcased at the exhibition hall. 

** Please put your poster on the board in the exhibition hall *before* the first presentation timeslot and clean up your poster *after* the last presentation timeslot.

<div class="day-nav">
  <a href="#day-1" class="day-btn"><span class="day-full">Wednesday</span><span class="day-short">Wed</span> <span class="day-date">Oct 7</span></a>
  <a href="#day-2" class="day-btn"><span class="day-full">Thursday</span><span class="day-short">Thur</span> <span class="day-date">Oct 8</span></a>
  <a href="#day-3" class="day-btn"><span class="day-full">Friday</span><span class="day-short">Fri</span> <span class="day-date">Oct 9</span></a>
</div>

----

{% comment %}
Automatically generated posters listing.
Data source: _data/2026/program/posters.csv
Poster ID format: Poster [day][session] (e.g. Poster 3B)
{% endcomment %}

{% assign y2026 = site.data['2026'] %}
{% assign posters = y2026.program.posters %}

{% assign day1A = posters | where_exp:'p','p["Session"] contains "Poster 1A"' %}
{% assign day1B = posters | where_exp:'p','p["Session"] contains "Poster 1B"' %}
{% assign day2A = posters | where_exp:'p','p["Session"] contains "Poster 2A"' %}
{% assign day2B = posters | where_exp:'p','p["Session"] contains "Poster 2B"' %}
{% assign day3A = posters | where_exp:'p','p["Session"] contains "Poster 3A"' %}
{% assign day3B = posters | where_exp:'p','p["Session"] contains "Poster 3B"' %}

<div class="posters-wrapper">
  {% if day1A.size > 0 or day1B.size > 0 %}
  <section id="day-1" class="poster-day">
    <h3 class="poster-day-title"><strong>Wednesday</strong> – October 7, 2026 </h3>
    <div class="session-nav">
      <a href="#day-1-session-a" class="session-btn session-btn-a">Visualization, Rendering & Immersive Experience <span class="session-time">10:30–12:45</span></a>
      <a href="#day-1-session-b" class="session-btn session-btn-b">XR Training, Education & Responsible Use <span class="session-time">13:45–16:00</span></a>
    </div>
    {% if day1A.size > 0 %}
    <div id="day-1-session-a" class="poster-session session-a">
      <h4 class="session-title session-title-a"><span class="session-label-row"><span class="session-label">Posters 1A</span><span class="session-room">Cassiopea</span></span>Visualization, Rendering & Immersive Experience <span class="session-title-datetime"><span class="session-title-day">Wednesday</span><span class="session-title-time">10:30–12:45</span></span></h4>
      <ul class="poster-list">
        {% for p in day1A %}
        <li class="poster-item">
          <details class="poster-details">
            <summary class="poster-summary">
              <span class="poster-id">{{ p["Poster ID"] }}</span>
              <span class="poster-title">{{ p["Title"] }}</span>
              <span class="poster-authors">{% assign authors = "" %}{% for i in (1..15) %}{% assign key = "Author " | append: i %}{% if p[key] and p[key] != "" %}{% if authors != "" %}{% assign authors = authors | append: ", " %}{% endif %}{% assign authors = authors | append: p[key] %}{% endif %}{% endfor %}{{ authors }}</span>
            </summary>
            {% if p["abstract"] and p["abstract"] != "" %}
            <div class="poster-abstract">{{ p["abstract"] }}</div>
            {% endif %}
          </details>
        </li>
        {% endfor %}
      </ul>
    </div>
    {% endif %}
    {% if day1B.size > 0 %}
    <div id="day-1-session-b" class="poster-session session-b">
      <h4 class="session-title session-title-b"><span class="session-label-row"><span class="session-label">Posters 1B</span><span class="session-room">Cassiopea</span></span>XR Training, Education & Responsible Use <span class="session-title-datetime"><span class="session-title-day">Wednesday</span><span class="session-title-time">13:45–16:00</span></span></h4>
      <ul class="poster-list">
        {% for p in day1B %}
        <li class="poster-item">
          <details class="poster-details">
            <summary class="poster-summary">
              <span class="poster-id">{{ p["Poster ID"] }}</span>
              <span class="poster-title">{{ p["Title"] }}</span>
              <span class="poster-authors">{% assign authors = "" %}{% for i in (1..15) %}{% assign key = "Author " | append: i %}{% if p[key] and p[key] != "" %}{% if authors != "" %}{% assign authors = authors | append: ", " %}{% endif %}{% assign authors = authors | append: p[key] %}{% endif %}{% endfor %}{{ authors }}</span>
            </summary>
            {% if p["abstract"] and p["abstract"] != "" %}
            <div class="poster-abstract">{{ p["abstract"] }}</div>
            {% endif %}
          </details>
        </li>
        {% endfor %}
      </ul>
    </div>
    {% endif %}
  </section>
  {% endif %}
  <div class="poster-separator" aria-hidden="true"></div>
  {% if day2A.size > 0 or day2B.size > 0 %}
  <section id="day-2" class="poster-day">
    <h3 class="poster-day-title"><strong>Thursday</strong> – October 8, 2026</h3>
    <div class="session-nav">
      <a href="#day-2-session-a" class="session-btn session-btn-a">Human Perception, Cognition & XR Methods <span class="session-time">11:15–13:45</span></a>
      <a href="#day-2-session-b" class="session-btn session-btn-b">Collaborative XR, Avatars & Navigation <span class="session-time">14:15–16:30</span></a>
    </div>
    {% if day2A.size > 0 %}
    <div id="day-2-session-a" class="poster-session session-a">
      <h4 class="session-title session-title-a"><span class="session-label-row"><span class="session-label">Posters 2A</span><span class="session-room">Cassiopea</span></span>Human Perception, Cognition & XR Methods <span class="session-title-datetime"><span class="session-title-day">Thursday</span><span class="session-title-time">11:15–13:45</span></span></h4>
      <ul class="poster-list">
        {% for p in day2A %}
        <li class="poster-item">
          <details class="poster-details">
            <summary class="poster-summary">
              <span class="poster-id">{{ p["Poster ID"] }}</span>
              <span class="poster-title">{{ p["Title"] }}</span>
              <span class="poster-authors">{% assign authors = "" %}{% for i in (1..15) %}{% assign key = "Author " | append: i %}{% if p[key] and p[key] != "" %}{% if authors != "" %}{% assign authors = authors | append: ", " %}{% endif %}{% assign authors = authors | append: p[key] %}{% endif %}{% endfor %}{{ authors }}</span>
            </summary>
            {% if p["abstract"] and p["abstract"] != "" %}
            <div class="poster-abstract">{{ p["abstract"] }}</div>
            {% endif %}
          </details>
        </li>
        {% endfor %}
      </ul>
    </div>
    {% endif %}
    {% if day2B.size > 0 %}
    <div id="day-2-session-b" class="poster-session session-b">
      <h4 class="session-title session-title-b"><span class="session-label-row"><span class="session-label">Posters 2B</span><span class="session-room">Cassiopea</span></span>Collaborative XR, Avatars & Navigation <span class="session-title-datetime"><span class="session-title-day">Thursday</span><span class="session-title-time">14:15–16:30</span></span></h4>
      <ul class="poster-list">
        {% for p in day2B %}
        <li class="poster-item">
          <details class="poster-details">
            <summary class="poster-summary">
              <span class="poster-id">{{ p["Poster ID"] }}</span>
              <span class="poster-title">{{ p["Title"] }}</span>
              <span class="poster-authors">{% assign authors = "" %}{% for i in (1..15) %}{% assign key = "Author " | append: i %}{% if p[key] and p[key] != "" %}{% if authors != "" %}{% assign authors = authors | append: ", " %}{% endif %}{% assign authors = authors | append: p[key] %}{% endif %}{% endfor %}{{ authors }}</span>
            </summary>
            {% if p["abstract"] and p["abstract"] != "" %}
            <div class="poster-abstract">{{ p["abstract"] }}</div>
            {% endif %}
          </details>
        </li>
        {% endfor %}
      </ul>
    </div>
    {% endif %}
  </section>
  {% endif %}
  <div class="poster-separator" aria-hidden="true"></div>
  {% if day3A.size > 0 or day3B.size > 0 %}
  <section id="day-3" class="poster-day">
    <h3 class="poster-day-title"><strong>Friday</strong> – October 9, 2026 </h3>
    <div class="session-nav">
      <a href="#day-3-session-a" class="session-btn session-btn-a">Embodied Interaction, Multimodal Control & Assistive Systems <span class="session-time">11:15–13:45</span></a>
      <a href="#day-3-session-b" class="session-btn session-btn-b">Interaction & XR Interfaces <span class="session-time">14:15–16:30</span></a>
    </div>
    {% if day3A.size > 0 %}
    <div id="day-3-session-a" class="poster-session session-a">
      <h4 class="session-title session-title-a"><span class="session-label-row"><span class="session-label">Posters 3A</span><span class="session-room">Cassiopea</span></span>Embodied Interaction, Multimodal Control & Assistive Systems <span class="session-title-datetime"><span class="session-title-day">Friday</span><span class="session-title-time">11:15–13:45</span></span></h4>
      <ul class="poster-list">
        {% for p in day3A %}
        <li class="poster-item">
          <details class="poster-details">
            <summary class="poster-summary">
              <span class="poster-id">{{ p["Poster ID"] }}</span>
              <span class="poster-title">{{ p["Title"] }}</span>
              <span class="poster-authors">{% assign authors = "" %}{% for i in (1..15) %}{% assign key = "Author " | append: i %}{% if p[key] and p[key] != "" %}{% if authors != "" %}{% assign authors = authors | append: ", " %}{% endif %}{% assign authors = authors | append: p[key] %}{% endif %}{% endfor %}{{ authors }}</span>
            </summary>
            {% if p["abstract"] and p["abstract"] != "" %}
            <div class="poster-abstract">{{ p["abstract"] }}</div>
            {% endif %}
          </details>
        </li>
        {% endfor %}
      </ul>
    </div>
    {% endif %}
    {% if day3B.size > 0 %}
    <div id="day-3-session-b" class="poster-session session-b">
      <h4 class="session-title session-title-b"><span class="session-label-row"><span class="session-label">Posters 3B</span><span class="session-room">Cassiopea</span></span>Interaction & XR Interfaces <span class="session-title-datetime"><span class="session-title-day">Friday</span><span class="session-title-time">14:15–16:30</span></span></h4>
      <ul class="poster-list">
        {% for p in day3B %}
        <li class="poster-item">
          <details class="poster-details">
            <summary class="poster-summary">
              <span class="poster-id">{{ p["Poster ID"] }}</span>
              <span class="poster-title">{{ p["Title"] }}</span>
              <span class="poster-authors">{% assign authors = "" %}{% for i in (1..15) %}{% assign key = "Author " | append: i %}{% if p[key] and p[key] != "" %}{% if authors != "" %}{% assign authors = authors | append: ", " %}{% endif %}{% assign authors = authors | append: p[key] %}{% endif %}{% endfor %}{{ authors }}</span>
            </summary>
            {% if p["abstract"] and p["abstract"] != "" %}
            <div class="poster-abstract">{{ p["abstract"] }}</div>
            {% endif %}
          </details>
        </li>
        {% endfor %}
      </ul>
    </div>
    {% endif %}
  </section>
  {% endif %}
</div>

For questions, contact: posters2026@ieeeismar.net

ISMAR 2026 Poster Chairs:
Mohammed Safayet Arefin, Andrea Boensch, Francesco Ferrise, Cassidy Nelson

<style>
/* Day navigation buttons */
.day-nav { display:flex; flex-wrap:nowrap; gap:10px; padding:12px 10px; margin:-8px -10px 8px; position:sticky; top:70px; background:#F4E8D4; z-index:11; animation:none !important; }
.day-btn { display:inline-flex; align-items:center; justify-content:center; gap:8px; padding:10px 18px; border-radius:8px; font-size:0.9rem; font-weight:600; text-decoration:none; background:#3A8BF3; color:#fff !important; box-shadow:0 2px 4px rgba(0,0,0,.12); animation:none !important; flex:1 1 0; min-width:0; }
.day-btn:hover { background:#2878DB; transform:translateY(-1px); box-shadow:0 3px 8px rgba(0,0,0,.18); text-decoration:none !important; color:#fff !important; }
.day-date { font-size:0.75rem; font-weight:500; opacity:0.85; }
.day-short { display:none; }

.posters-wrapper { max-width: 1050px; margin: 8px 0 28px 0; }
.poster-day { margin-bottom: 26px; scroll-margin-top: 130px; }
.poster-day-title { margin: 0; font-size: 1.35rem; border-bottom: none; padding: 8px 10px 6px; position:sticky; top:128px; background:#F4E8D4; z-index:10; margin-left:-10px; margin-right:-10px; }
.session-nav { display:flex; flex-wrap:wrap; gap:8px; margin:0 -10px 16px; position:sticky; top:168px; background:#F4E8D4; z-index:9; padding:0 10px 12px; box-shadow: 0 -30px 0 #F4E8D4; }
.poster-day-title .count { font-size: 0.72rem; font-weight: 500; color: #666; }
.poster-day-title .weekday { font-size:0.75rem; font-weight:500; color:#777; margin-left:4px; }
.poster-day-title .count { background:var(--blue); color:#fff; padding:2px 6px; border-radius:12px; display:inline-block; line-height:1; }

/* Session navigation buttons */
.session-btn { display:inline-flex; align-items:center; gap:8px; padding:8px 14px; border-radius:8px; font-size:0.8rem; font-weight:600; text-decoration:none; transition: all 0.2s ease; box-shadow:0 1px 3px rgba(0,0,0,.1); }
.session-btn:hover { transform:translateY(-1px); box-shadow:0 2px 6px rgba(0,0,0,.15); text-decoration:none; }
.session-btn-a, .session-btn-a:link, .session-btn-a:visited { background:#3A8BF3; color:#fff !important; }
.session-btn-a:hover { background:#2878DB; color:#fff !important; }
.session-btn-b, .session-btn-b:link, .session-btn-b:visited { background:#F28C28; color:#fff !important; }
.session-btn-b:hover { background:#D96F08; color:#fff !important; }
.session-time { font-size:0.68rem; font-weight:500; opacity:0.9; }

/* Session containers */
.poster-session { margin-bottom:20px; padding:12px 14px 14px; border-radius:10px; scroll-margin-top:240px; }
.session-a { background:rgba(58, 139, 243, 0.18); border-left:4px solid #3A8BF3; }
.session-b { background:rgba(242, 140, 40, 0.12); border-left:4px solid #F28C28; }

/* Session titles */
.session-title { margin:0 0 10px 0; font-size:1rem; font-weight:600; display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; gap:4px 12px; }
.session-title-a { color:#2878DB; }
.session-title-b { color:#D96F08; }
.session-label-row { display:flex; width:100%; justify-content:space-between; align-items:center; margin-bottom:2px; }
.session-label { font-size:1.1rem; font-weight:700; }
.session-title-datetime { display:flex; flex-direction:column; align-items:flex-end; flex-shrink:0; line-height:1.3; }
.session-title-day { }
.session-title-time { }
.session-room { font-size:0.75rem; font-weight:500; background:#f0f0f0; padding:2px 8px; border-radius:12px; color:#555; }

.page-content ul.poster-list { list-style: none; margin: 0; padding: 0; }
.poster-item { margin: 0 0 6px 0; padding: 0; background: #fff; border:1px solid #e1e4e7; border-radius:8px; box-shadow:0 1px 1px rgba(0,0,0,.03); position:relative; }
.poster-item:hover { box-shadow:0 1px 4px rgba(0,0,0,.07); border-color:#d2d7db; }

/* Expandable poster details */
.poster-details { width:100%; }
.poster-summary { display:block; padding:6px 9px 6px 10px; cursor:pointer; list-style:none; position:relative; padding-left:22px; }
.poster-summary::-webkit-details-marker { display:none; }
.poster-summary::marker { display:none; }
.poster-summary::before { content:""; position:absolute; left:8px; top:10px; width:0; height:0; border-left:6px solid #2878DB; border-top:4px solid transparent; border-bottom:4px solid transparent; transition:transform 0.2s ease; }
.session-b .poster-summary::before { border-left-color:#F28C28; }
.poster-details[open] .poster-summary::before { transform:rotate(90deg); }
.poster-title { display:inline; font-weight:600; color: #2878DB; font-size:0.9rem; line-height:1.2; cursor:pointer; }
.poster-title:hover { text-decoration:underline; }
.session-b .poster-title { color: #D96F08; }
.poster-details[open] .poster-summary { border-bottom:1px solid #e8eaed; }
.poster-abstract { padding:10px 12px; font-size:0.82rem; line-height:1.5; color:#333; background:#f8f9fa; border-radius:0 0 7px 7px; }
.session-b .poster-abstract { background:#fef8f4; }

.poster-id { display:inline-block; background: #2878DB; color:#fff; font-size:0.60rem; letter-spacing:.45px; font-weight:600; padding:5px 6px 5px; border-radius:6px; margin:0 8px 3px 0; vertical-align:middle; box-shadow:0 1px 2px rgba(0,0,0,.15); line-height:1; }
.session-b .poster-id { background: #F28C28; }
.poster-authors { display:block; font-size:0.66rem; line-height:1.15; margin:3px 0 0 0; color:#444; }

@media (max-width: 640px){
  .day-nav { gap:4px; padding:6px 10px; }
  .day-btn { padding:5px 8px; font-size:0.65rem; gap:4px; }
  .day-btn:hover, .day-btn:active { background:#3A8BF3; transform:none; box-shadow:0 2px 4px rgba(0,0,0,.12); }
  .day-date { font-size:0.55rem; }
  .day-full { display:none; }
  .day-short { display:inline; }
  .poster-day-title { top:100px; }
  .session-nav { top:138px; }
  .poster-title { display:inline; margin-top:0; }
  .poster-authors { font-size:0.64rem; }
  .poster-day-title { font-size:1.22rem; }
  .session-nav { gap:6px; flex-direction:column; }
  .session-btn { padding:8px 12px; font-size:0.75rem; min-height:52px; width:100%; justify-content:space-between; }
  .session-btn .session-time { margin-left:auto; text-align:right; flex-shrink:0; }
  .session-time { font-size:0.62rem; }
  .poster-session { padding:10px 10px 12px; scroll-margin-top:300px; }
  .session-title { font-size:0.9rem; }
}
</style>

