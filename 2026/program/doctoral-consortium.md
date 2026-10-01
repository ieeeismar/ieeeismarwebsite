---
layout: 2026/program-page-2026
title: Doctoral Consortium
permalink: /2026/doctoral-consortium/
---

<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-FQFFZGXF3Y"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-FQFFZGXF3Y');
</script>

## Overview

The Doctoral Consortium at ISMAR 2026 is a concentrated event where students present their research interests, plans, and results to a panel of researchers in related fields and receive specific and constructive feedback, including opportunities to meet with mentors one-on-one. Accepted students will give in-depth presentations of their research and will receive valuable comments from mentors. Additionally, they will also have the opportunity to present a poster or a demo of their work at the respective sessions.

## Doctoral Consortium Schedule

<section id="day-1" class="dc-day">
  <h3 class="dc-day-title"><strong>Monday</strong><span>- October 5, 2026</span><span class="dc-room">Glasshaus</span></h3>
  <div class="session-nav">
    <a href="#session-1" class="session-btn session-btn-a">Social XR <span class="session-time">8:15–9:15</span></a>
    <a href="#session-2" class="session-btn session-btn-b">XR Interaction <span class="session-time">9:15–9:50</span></a>
    <a href="#session-2b" class="session-btn session-btn-b">XR Interaction continued <span class="session-time">10:30–11:00</span></a>
    <a href="#session-3" class="session-btn session-btn-a">XR Training <span class="session-time">11:00–12:00</span></a>
  </div>

  <div class="dc-schedule-event"><span class="dc-event-time">8:00 AM – 8:15 AM</span><strong>Opening remarks</strong></div>

  <section id="session-1" class="dc-session session-a">
    <h4 class="dc-session-title"><span>Session 1: Social XR</span><span class="session-time">8:15 AM – 9:15 AM · 60 min</span></h4>
    <ul class="dc-list">
      {% assign session1_ids = "1041,1026,1034,1024,1048" | split: "," %}
      {% for id in session1_ids %}
      {% assign dc = site.data["2026"]["program"].doctoral_consortium | where: "ID", id | first %}
      <li class="dc-item">
        <details class="dc-details" id="dc-{{ dc['ID'] }}">
          <summary class="dc-summary"><span class="dc-id">DC{{ dc["ID"] }}</span><span class="dc-title">{{ dc["Submission title"] }}</span><span class="dc-presenter">{{ dc["Name"] | split: ", " | reverse | join: " " }}</span></summary>
          <div class="dc-expanded">
            <p><strong>Presenter:</strong> {{ dc["Name"] | split: ", " | reverse | join: " " }}<br><strong>Mentor:</strong> {{ dc["Mentor"] | split: ", " | reverse | join: " " }}</p>
            <h5>Abstract</h5>
            <p>{{ dc["Abstract"] | newline_to_br }}</p>
          </div>
        </details>
      </li>
      {% endfor %}
    </ul>
  </section>

  <section id="session-2" class="dc-session session-b">
    <h4 class="dc-session-title"><span>Session 2: XR Interaction</span><span class="session-time">9:15 AM – 9:50 AM · 35 min</span></h4>
    <ul class="dc-list">
      {% assign session2_ids = "1025,1028,1032" | split: "," %}
      {% for id in session2_ids %}
      {% assign dc = site.data["2026"]["program"].doctoral_consortium | where: "ID", id | first %}
      <li class="dc-item">
        <details class="dc-details" id="dc-{{ dc['ID'] }}">
          <summary class="dc-summary"><span class="dc-id">DC{{ dc["ID"] }}</span><span class="dc-title">{{ dc["Submission title"] }}</span><span class="dc-presenter">{{ dc["Name"] | split: ", " | reverse | join: " " }}</span></summary>
          <div class="dc-expanded">
            <p><strong>Presenter:</strong> {{ dc["Name"] | split: ", " | reverse | join: " " }}<br><strong>Mentor:</strong> {{ dc["Mentor"] | split: ", " | reverse | join: " " }}</p>
            <h5>Abstract</h5>
            <p>{{ dc["Abstract"] | newline_to_br }}</p>
          </div>
        </details>
      </li>
      {% endfor %}
    </ul>
  </section>

  <div class="dc-schedule-event dc-coffee"><span class="dc-event-time">9:50 AM – 10:30 AM</span><strong>Coffee break · 40 min</strong></div>

  <section id="session-2b" class="dc-session session-b">
    <h4 class="dc-session-title"><span>Session 2: XR Interaction - continued</span><span class="session-time">10:30 AM – 11:00 AM · 30 min</span></h4>
    <ul class="dc-list">
      {% assign session2b_ids = "1036,1038" | split: "," %}
      {% for id in session2b_ids %}
      {% assign dc = site.data["2026"]["program"].doctoral_consortium | where: "ID", id | first %}
      <li class="dc-item">
        <details class="dc-details" id="dc-{{ dc['ID'] }}">
          <summary class="dc-summary"><span class="dc-id">DC{{ dc["ID"] }}</span><span class="dc-title">{{ dc["Submission title"] }}</span><span class="dc-presenter">{{ dc["Name"] | split: ", " | reverse | join: " " }}</span></summary>
          <div class="dc-expanded">
            <p><strong>Presenter:</strong> {{ dc["Name"] | split: ", " | reverse | join: " " }}<br><strong>Mentor:</strong> {{ dc["Mentor"] | split: ", " | reverse | join: " " }}</p>
            <h5>Abstract</h5>
            <p>{{ dc["Abstract"] | newline_to_br }}</p>
          </div>
        </details>
      </li>
      {% endfor %}
    </ul>
  </section>

  <section id="session-3" class="dc-session session-a">
    <h4 class="dc-session-title"><span>Session 3: XR Training</span><span class="session-time">11:00 AM – 12:00 PM · 60 min</span></h4>
    <ul class="dc-list">
      {% assign session3_ids = "1027,1039,1046,1049,1050" | split: "," %}
      {% for id in session3_ids %}
      {% assign dc = site.data["2026"]["program"].doctoral_consortium | where: "ID", id | first %}
      <li class="dc-item">
        <details class="dc-details" id="dc-{{ dc['ID'] }}">
          <summary class="dc-summary"><span class="dc-id">DC{{ dc["ID"] }}</span><span class="dc-title">{{ dc["Submission title"] }}</span><span class="dc-presenter">{{ dc["Name"] | split: ", " | reverse | join: " " }}</span></summary>
          <div class="dc-expanded">
            <p><strong>Presenter:</strong> {{ dc["Name"] | split: ", " | reverse | join: " " }}<br><strong>Mentor:</strong> {{ dc["Mentor"] | split: ", " | reverse | join: " " }}</p>
            <h5>Abstract</h5>
            <p>{{ dc["Abstract"] | newline_to_br }}</p>
          </div>
        </details>
      </li>
      {% endfor %}
    </ul>
  </section>

  <div class="dc-schedule-event"><span class="dc-event-time">12:00 PM – 2:00 PM</span><strong>Lunch break · 2 hours</strong></div>
  <div id="mentoring-sessions" class="dc-schedule-event"><span class="dc-event-time">2:00 PM – 2:45 PM</span><strong>1:1 Mentoring sessions · 45 min</strong></div>
  <div class="dc-schedule-event"><span class="dc-event-time">2:45 PM – 3:30 PM</span><strong>Discussion &amp; Closing remarks · 45 min</strong></div>
</section>

<style>
.day-nav { display:flex; gap:10px; padding:12px 10px; margin:-8px -10px 8px; position:sticky; top:70px; background:#F4E8D4; z-index:11; }
.day-btn { display:inline-flex; align-items:center; justify-content:center; gap:8px; padding:10px 18px; border-radius:8px; font-size:.9rem; font-weight:600; text-decoration:none; background:#3A8BF3; color:#fff !important; box-shadow:0 2px 4px rgba(0,0,0,.12); }
.day-btn:hover { background:#2878DB; text-decoration:none !important; color:#fff !important; }
.day-date { font-size:.75rem; font-weight:500; opacity:.85; }
.dc-day { scroll-margin-top:130px; }
.dc-day-title { margin:0; padding:8px 10px 6px; font-size:1.35rem; border:0; display:flex; flex-wrap:wrap; justify-content:flex-start; align-items:center; gap:6px; }
.dc-room { display:inline-block; font-size:.75rem; font-weight:500; background:#f0f0f0; padding:2px 8px; border-radius:12px; color:#555; }
.session-nav { display:flex; flex-wrap:wrap; gap:8px; margin:0 -10px 16px; padding:0 10px 12px; }
.session-btn { display:inline-flex; align-items:center; justify-content:space-between; gap:8px; padding:8px 14px; border-radius:8px; font-size:.8rem; font-weight:600; text-decoration:none; box-shadow:0 1px 3px rgba(0,0,0,.1); }
.session-btn-a, .session-btn-a:link, .session-btn-a:visited { background:#3A8BF3; color:#fff !important; }
.session-btn-a:hover { background:#2878DB; color:#fff !important; }
.session-btn-b, .session-btn-b:link, .session-btn-b:visited { background:#F28C28; color:#fff !important; }
.session-btn-b:hover { background:#D96F08; color:#fff !important; }
.session-time { font-size:.68rem; font-weight:500; opacity:.9; }
.dc-schedule-event { display:flex; flex-wrap:wrap; gap:8px 16px; align-items:center; margin:0 0 8px; padding:10px 14px; background:#fff; border:1px solid #e1e4e7; border-radius:8px; scroll-margin-top:130px; }
.dc-event-time { min-width:150px; color:#555; font-size:.85rem; }
.dc-coffee { margin:10px 0; background:#f8f9fa; }
.dc-session { margin-bottom:20px; padding:12px 14px 14px; border-radius:10px; scroll-margin-top:130px; }
.session-a { background:rgba(58,139,243,.18); border-left:4px solid #3A8BF3; }
.session-b { background:rgba(242,140,40,.12); border-left:4px solid #F28C28; }
.dc-session-title { margin:0 0 10px; font-size:1rem; font-weight:600; display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; gap:4px 12px; color:#2878DB; }
.session-b .dc-session-title { color:#D96F08; }
.page-content ul.dc-list { list-style:none; margin:0; padding:0; }
.dc-item { margin:0 0 6px; padding:0; background:#fff; border:1px solid #e1e4e7; border-radius:8px; box-shadow:0 1px 1px rgba(0,0,0,.03); }
.dc-details { scroll-margin-top:130px; }
.dc-summary { display:block; padding:6px 9px 6px 22px; cursor:pointer; list-style:none; position:relative; }
.dc-summary::-webkit-details-marker, .dc-summary::marker { display:none; }
.dc-summary::before { content:""; position:absolute; left:8px; top:10px; width:0; height:0; border-left:6px solid #2878DB; border-top:4px solid transparent; border-bottom:4px solid transparent; transition:transform .2s ease; }
.session-b .dc-summary::before { border-left-color:#F28C28; }
.dc-details[open] .dc-summary::before { transform:rotate(90deg); }
.dc-details[open] .dc-summary { border-bottom:1px solid #e8eaed; }
.dc-id { display:inline-block; background:#2878DB; color:#fff; font-size:.6rem; font-weight:600; padding:5px 6px; border-radius:6px; margin:0 8px 3px 0; vertical-align:middle; line-height:1; }
.session-b .dc-id { background:#F28C28; }
.dc-title { display:inline; font-weight:600; color:#2878DB; font-size:.9rem; line-height:1.2; }
.session-b .dc-title { color:#D96F08; }
.dc-presenter { display:block; font-size:.68rem; line-height:1.2; margin:3px 0 0; color:#444; }
.dc-expanded { padding:10px 12px; font-size:.82rem; line-height:1.5; color:#333; background:#f8f9fa; border-radius:0 0 7px 7px; }
.session-b .dc-expanded { background:#fef8f4; }
.dc-expanded p { margin:0 0 8px; }
.dc-expanded h5 { margin:10px 0 4px; font-size:.9rem; }
@media (max-width:640px) {
  .day-nav { gap:4px; padding:6px 10px; }
  .day-btn { padding:5px 8px; font-size:.65rem; gap:4px; }
  .day-date { font-size:.55rem; }
  .dc-day-title { font-size:1.22rem; }
  .session-nav { gap:6px; flex-direction:column; }
  .session-btn { padding:8px 12px; font-size:.75rem; min-height:48px; width:100%; }
  .dc-session { padding:10px 10px 12px; scroll-margin-top:130px; }
  .dc-schedule-event { scroll-margin-top:130px; }
  .dc-details { scroll-margin-top:130px; }
  .dc-event-time { min-width:0; }
}
</style>

