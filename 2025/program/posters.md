---
layout: 2025/page
title: Posters
---

*Last updated: 2025-09-26 5:53AM GMT*

All accepted posters, including those invited from the Doctoral Consortium and TVCG Journal papers, are assigned to a specific day, which has multiple presentation timeslots throughout that day. We **highly recommend being at your posters** during the allocated timeslots! This is a great opportunity to network and talk to other conference attendees.

This year, there are **no traditional poster fast-forward sessions.** Instead, fast-forward poster videos that you submitted will be showcased at the exhibition hall. 

** Please put your poster on the board in the exhibition hall *before* the first presentation timeslot and clean up your poster *after* the last presentation timeslot.

----

{% comment %}
Automatically generated posters listing.
Data source: _data/2025/program/posters.csv
Poster ID format: D[day]-[sequence] (e.g., D1-12) used to split by day.
{% endcomment %}

{% assign y2025 = site.data['2025'] %}
{% assign posters = y2025.program.posters %}

{% assign day1 = posters | where_exp:'p','p["Poster ID"] contains "D1-"' %}
{% assign day2 = posters | where_exp:'p','p["Poster ID"] contains "D2-"' %}
{% assign day3 = posters | where_exp:'p','p["Poster ID"] contains "D3-"' %}

<div class="posters-wrapper">
  {% if day1 and day1.size > 0 %}
  <section id="day-1" class="poster-day">
    <h3 class="poster-day-title"><strong>Day 1</strong>: October 9, 2025 (Thursday) | Time: (Morning) 10:00 ~ 10:30, 11:30 ~ 12:00, (Lunch) 13:00 ~ 14:30, (Afternoon) 15:30 ~ 16:00, 17:00 ~ 17:30 | Exhibition Hall (1F) <span class="count">({{ day1.size }})</span></h3>
    <ul class="poster-list">
      {% for p in day1 %}
      <li class="poster-item">
        <span class="poster-id">{{ p["Poster ID"] }}</span>
        <span class="poster-title">{{ p["Poster Title"] }}</span>
        <span class="poster-authors">{{ p["Poster Authors"] }}</span>
      </li>
      {% endfor %}
    </ul>
  </section>
  {% endif %}
  <hr>
  {% if day2 and day2.size > 0 %}
  <section id="day-2" class="poster-day">
    <h3 class="poster-day-title"><strong>Day 2</strong>: October 10, 2025 (Friday) | Time: (Morning) 10:00 ~ 10:30, 11:30 ~ 12:00, (Lunch) 13:00 ~ 14:30, (Afternoon) 15:30 ~ 16:00, 17:00 ~ 18:00  | Exhibition Hall (1F) <span class="count">({{ day2.size }})</span></h3>
    <ul class="poster-list">
      {% for p in day2 %}
      <li class="poster-item">
        <span class="poster-id">{{ p["Poster ID"] }}</span>
        <span class="poster-title">{{ p["Poster Title"] }}</span>
        <span class="poster-authors">{{ p["Poster Authors"] }}</span>
      </li>
      {% endfor %}
    </ul>
  </section>
  {% endif %}
  <hr>
  {% if day3 and day3.size > 0 %}
  <section id="day-3" class="poster-day">
    <h3 class="poster-day-title"><strong>Day 3</strong>: October 11, 2025 (Saturday) | Time: (Morning) 10:00 ~ 10:30, 11:30 ~ 12:00, (Lunch) 13:00 ~ 14:30, (Afternoon) 15:30 ~ 16:00  | Exhibition Hall (1F) <span class="count">({{ day3.size }})</span></h3>
    <ul class="poster-list">
      {% for p in day3 %}
      <li class="poster-item">
        <span class="poster-id">{{ p["Poster ID"] }}</span>
        <span class="poster-title">{{ p["Poster Title"] }}</span>
        <span class="poster-authors">{{ p["Poster Authors"] }}</span>
      </li>
      {% endfor %}
    </ul>
  </section>
  {% endif %}
</div>

For questions, contact: posters2025@ieeeismar.net

ISMAR 2025 Poster Chairs:
Byung-Kuk Seo, Sungchul Jung, Florian Weidner

<style>
.posters-wrapper { max-width: 1050px; margin: 8px 0 28px 0; }
.poster-day { margin-bottom: 26px; }
.poster-day-title { margin: 20px 0 8px; font-size: 1.35rem; border-bottom: 1px solid #e1e4e7; padding-bottom: 3px; }
.poster-day-title .count { font-size: 0.72rem; font-weight: 500; color: #666; }
.page-content ul.poster-list { list-style: none; margin: 0; padding: 0; }
.poster-item { margin: 0 0 6px 0; padding: 6px 9px 6px 10px; background: #fff; border:1px solid #e1e4e7; border-radius:8px; box-shadow:0 1px 1px rgba(0,0,0,.03); position:relative; }
.poster-item:hover { box-shadow:0 1px 4px rgba(0,0,0,.07); border-color:#d2d7db; }
.poster-id { display:inline-block; background: rgb(37, 37, 197); color:#fff; font-size:0.60rem; letter-spacing:.45px; font-weight:600; padding:5px 6px 5px; border-radius:6px; margin:0 8px 3px 0; vertical-align:middle; box-shadow:0 1px 2px rgba(0,0,0,.15); line-height:1; }
.poster-title { display:inline; font-weight:600; color: var(--blue); font-size:0.9rem; line-height:1.2; }
.poster-authors { display:block; font-size:0.66rem; line-height:1.15; margin:3px 0 0 0; color:#444; }

@media (max-width: 640px){
  .poster-item { padding:6px 8px 6px 8px; }
  .poster-title { display:inline; margin-top:0; }
  .poster-authors { font-size:0.64rem; }
  .poster-day-title { font-size:1.22rem; }
}
</style>

