---
layout: 2026/program-page-2026
title: Papers
permalink: /2026/papers/
---
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-FQFFZGXF3Y"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-FQFFZGXF3Y');
</script>
---
*Last updated: 2026-08-28 7:14PM EDT*

---

<div class="day-nav">
  <a href="#day-1" class="day-btn"><span class="day-full">Wednesday</span><span class="day-short">Wed</span> <span class="day-date">Oct 7</span></a>
  <a href="#day-2" class="day-btn"><span class="day-full">Thursday</span><span class="day-short">Thur</span> <span class="day-date">Oct 8</span></a>
  <a href="#day-3" class="day-btn"><span class="day-full">Friday</span><span class="day-short">Fri</span> <span class="day-date">Oct 9</span></a>
</div>

{% comment %}
Automatically generated papers listing.
Data source: _data/2026/program/papers.csv
Session ID format: Paper [day][timeslot][track] (e.g. Paper 1A1)
Colors: A, C, E = blue; B, D, F = orange

PS Number Calculation:
- Day offset: (day - 1) * 18
- Slot offset: A=0, B=3, C=6, D=9, E=12, F=15
- Track: 1, 2, or 3
- PS = day_offset + slot_offset + track
{% endcomment %}

{% comment %} Slot letter to offset mapping {% endcomment %}
{% assign slot_offsets = "A:0|B:3|C:6|D:9|E:12|F:15" | split: "|" %}

{% assign y2026 = site.data['2026'] %}
{% assign papers = y2026.program.papers %}

{% assign day1 = papers | where: "Day", "Wednesday, 7 October" %}
{% assign day2 = papers | where: "Day", "Thursday, 8 October" %}
{% assign day3 = papers | where: "Day", "Friday, 9 October" %}

<!-- Table of Contents -->
<div class="papers-toc">
  {% assign days_data = "Wednesday, 7 October|Thursday, 8 October|Friday, 9 October" | split: "|" %}
  {% assign day_nums = "1|2|3" | split: "|" %}

  {% for day in days_data %}
    {% assign day_index = forloop.index0 %}
    {% assign day_num = day_nums[day_index] %}
    {% if day_index == 0 %}
      {% assign day_papers = day1 %}
    {% elsif day_index == 1 %}
      {% assign day_papers = day2 %}
    {% else %}
      {% assign day_papers = day3 %}
    {% endif %}

    {% if day_papers.size > 0 %}
    <h3 class="toc-day">{{ day }}</h3>
    <table class="papers-toc-table">
      <thead>
        <tr><th>Time</th><th>Session</th><th>Chair</th><th>Room</th></tr>
      </thead>
      <tbody>
      {% assign slots = "A|B|C|D|E|F" | split: "|" %}
      {% for slot in slots %}
        {% assign slot_papers = day_papers | where: "TimeSlot", slot %}
        {% if slot_papers.size > 0 %}
          {% assign slot_time = slot_papers[0]["Time"] %}
          {% assign session_ids = "" %}
          {% for p in slot_papers %}
            {% unless session_ids contains p["Session ID"] %}
              {% assign session_ids = session_ids | append: p["Session ID"] | append: "|" %}
            {% endunless %}
          {% endfor %}
          {% assign session_ids_arr = session_ids | split: "|" | sort %}
          {% for sid in session_ids_arr %}
            {% if sid != "" %}
              {% assign sess_papers = slot_papers | where: "Session ID", sid %}
              {% assign sess_title = sess_papers[0]["Session Title"] %}
              {% assign sess_room = sess_papers[0]["Room"] %}
              {% assign anchor = "session-" | append: sid | slugify %}
              {% assign row_class = "toc-row-a" %}
              {% if slot == "B" or slot == "D" or slot == "F" %}{% assign row_class = "toc-row-b" %}{% endif %}
              {% comment %} Compute PS number from Session ID (e.g., "Paper 1A1") {% endcomment %}
              {% assign sid_day = sid | slice: 6, 1 | plus: 0 %}
              {% assign sid_slot = sid | slice: 7, 1 %}
              {% assign sid_track = sid | slice: 8, 1 | plus: 0 %}
              {% assign day_offset = sid_day | minus: 1 | times: 18 %}
              {% case sid_slot %}
                {% when "A" %}{% assign slot_offset = 0 %}
                {% when "B" %}{% assign slot_offset = 3 %}
                {% when "C" %}{% assign slot_offset = 6 %}
                {% when "D" %}{% assign slot_offset = 9 %}
                {% when "E" %}{% assign slot_offset = 12 %}
                {% when "F" %}{% assign slot_offset = 15 %}
              {% endcase %}
              {% assign ps_num = day_offset | plus: slot_offset | plus: sid_track %}
              <tr class="{{ row_class }}">
                <td class="toc-time"><a href="#{{ anchor }}">{{ slot_time }}</a></td>
                <td class="toc-session"><a href="#{{ anchor }}">PS{{ ps_num }}: {{ sess_title }}</a></td>
                <td class="toc-chair">—</td>
                <td class="toc-location"><a href="#{{ anchor }}">{{ sess_room }}</a></td>
              </tr>
            {% endif %}
          {% endfor %}
        {% endif %}
      {% endfor %}
      </tbody>
    </table>
    {% endif %}
  {% endfor %}
</div>

<div class="papers-wrapper">
  {% if day1.size > 0 %}
  <section id="day-1" class="paper-day">
    <h3 class="paper-day-title"><strong>Wednesday</strong> – 7 October 2026</h3>
    <div class="session-nav">
      {% assign day1_slots = "A|B|C|D|E|F" | split: "|" %}
      {% for slot in day1_slots %}
        {% assign slot_papers = day1 | where: "TimeSlot", slot %}
        {% if slot_papers.size > 0 %}
          {% assign slot_time = slot_papers[0]["Time"] %}
          {% assign slot_class = "session-btn-a" %}
          {% if slot == "B" or slot == "D" or slot == "F" %}{% assign slot_class = "session-btn-b" %}{% endif %}
          <a href="#day-1-slot-{{ slot | downcase }}" class="session-btn {{ slot_class }}">Session {{ slot }} <span class="session-time">{{ slot_time }}</span></a>
        {% endif %}
      {% endfor %}
    </div>
    {% for slot in day1_slots %}
      {% assign slot_papers = day1 | where: "TimeSlot", slot %}
      {% if slot_papers.size > 0 %}
        {% assign slot_time = slot_papers[0]["Time"] %}
        {% assign session_class = "session-a" %}
        {% assign title_class = "session-title-a" %}
        {% if slot == "B" or slot == "D" or slot == "F" %}
          {% assign session_class = "session-b" %}
          {% assign title_class = "session-title-b" %}
        {% endif %}
        <div id="day-1-slot-{{ slot | downcase }}" class="paper-slot {{ session_class }}">
          <h4 class="slot-title {{ title_class }}"><span class="slot-label">Session {{ slot }}</span>{{ slot_time }}</h4>
          {% comment %} Group by Session ID to get each parallel session {% endcomment %}
          {% assign session_ids = "" %}
          {% for p in slot_papers %}
            {% unless session_ids contains p["Session ID"] %}
              {% assign session_ids = session_ids | append: p["Session ID"] | append: "|" %}
            {% endunless %}
          {% endfor %}
          {% assign session_ids = session_ids | split: "|" | sort %}
          <div class="parallel-sessions">
          {% for sid in session_ids %}
            {% if sid != "" %}
              {% assign session_papers = slot_papers | where: "Session ID", sid %}
              {% assign session_title = session_papers[0]["Session Title"] %}
              {% assign session_room = session_papers[0]["Room"] %}
              {% comment %} Compute PS number from Session ID {% endcomment %}
              {% assign sid_day = sid | slice: 6, 1 | plus: 0 %}
              {% assign sid_slot = sid | slice: 7, 1 %}
              {% assign sid_track = sid | slice: 8, 1 | plus: 0 %}
              {% assign day_offset = sid_day | minus: 1 | times: 18 %}
              {% case sid_slot %}
                {% when "A" %}{% assign slot_offset = 0 %}
                {% when "B" %}{% assign slot_offset = 3 %}
                {% when "C" %}{% assign slot_offset = 6 %}
                {% when "D" %}{% assign slot_offset = 9 %}
                {% when "E" %}{% assign slot_offset = 12 %}
                {% when "F" %}{% assign slot_offset = 15 %}
              {% endcase %}
              {% assign ps_num = day_offset | plus: slot_offset | plus: sid_track %}
              <div class="paper-session" id="session-{{ sid | slugify }}">
                <h5 class="session-header {{ title_class }}">PS{{ ps_num }}: {{ session_title }} <span class="session-room">{{ session_room }}</span></h5>
                <ul class="paper-list">
                  {% for p in session_papers %}
                  <li class="paper-item">
                    <details class="paper-details">
                      <summary class="paper-summary">
                        <span class="paper-id">{{ p["Paper ID"] }}</span>
                        <span class="paper-title">{{ p["Paper Title"] }}</span>
                        <span class="paper-authors">{{ p["Authors"] }}</span>
                      </summary>
                      {% if p["Abstract"] and p["Abstract"] != "" %}
                      <div class="paper-abstract">{{ p["Abstract"] }}</div>
                      {% endif %}
                    </details>
                  </li>
                  {% endfor %}
                </ul>
              </div>
            {% endif %}
          {% endfor %}
          </div>
        </div>
      {% endif %}
    {% endfor %}
  </section>
  {% endif %}

  <div class="paper-separator" aria-hidden="true"></div>

  {% if day2.size > 0 %}
  <section id="day-2" class="paper-day">
    <h3 class="paper-day-title"><strong>Thursday</strong> – 8 October 2026</h3>
    <div class="session-nav">
      {% assign day2_slots = "A|B|C|D|E|F" | split: "|" %}
      {% for slot in day2_slots %}
        {% assign slot_papers = day2 | where: "TimeSlot", slot %}
        {% if slot_papers.size > 0 %}
          {% assign slot_time = slot_papers[0]["Time"] %}
          {% assign slot_class = "session-btn-a" %}
          {% if slot == "B" or slot == "D" or slot == "F" %}{% assign slot_class = "session-btn-b" %}{% endif %}
          <a href="#day-2-slot-{{ slot | downcase }}" class="session-btn {{ slot_class }}">Session {{ slot }} <span class="session-time">{{ slot_time }}</span></a>
        {% endif %}
      {% endfor %}
    </div>
    {% for slot in day2_slots %}
      {% assign slot_papers = day2 | where: "TimeSlot", slot %}
      {% if slot_papers.size > 0 %}
        {% assign slot_time = slot_papers[0]["Time"] %}
        {% assign session_class = "session-a" %}
        {% assign title_class = "session-title-a" %}
        {% if slot == "B" or slot == "D" or slot == "F" %}
          {% assign session_class = "session-b" %}
          {% assign title_class = "session-title-b" %}
        {% endif %}
        <div id="day-2-slot-{{ slot | downcase }}" class="paper-slot {{ session_class }}">
          <h4 class="slot-title {{ title_class }}"><span class="slot-label">Session {{ slot }}</span>{{ slot_time }}</h4>
          {% assign session_ids = "" %}
          {% for p in slot_papers %}
            {% unless session_ids contains p["Session ID"] %}
              {% assign session_ids = session_ids | append: p["Session ID"] | append: "|" %}
            {% endunless %}
          {% endfor %}
          {% assign session_ids = session_ids | split: "|" | sort %}
          <div class="parallel-sessions">
          {% for sid in session_ids %}
            {% if sid != "" %}
              {% assign session_papers = slot_papers | where: "Session ID", sid %}
              {% assign session_title = session_papers[0]["Session Title"] %}
              {% assign session_room = session_papers[0]["Room"] %}
              {% comment %} Compute PS number from Session ID {% endcomment %}
              {% assign sid_day = sid | slice: 6, 1 | plus: 0 %}
              {% assign sid_slot = sid | slice: 7, 1 %}
              {% assign sid_track = sid | slice: 8, 1 | plus: 0 %}
              {% assign day_offset = sid_day | minus: 1 | times: 18 %}
              {% case sid_slot %}
                {% when "A" %}{% assign slot_offset = 0 %}
                {% when "B" %}{% assign slot_offset = 3 %}
                {% when "C" %}{% assign slot_offset = 6 %}
                {% when "D" %}{% assign slot_offset = 9 %}
                {% when "E" %}{% assign slot_offset = 12 %}
                {% when "F" %}{% assign slot_offset = 15 %}
              {% endcase %}
              {% assign ps_num = day_offset | plus: slot_offset | plus: sid_track %}
              <div class="paper-session" id="session-{{ sid | slugify }}">
                <h5 class="session-header {{ title_class }}">PS{{ ps_num }}: {{ session_title }} <span class="session-room">{{ session_room }}</span></h5>
                <ul class="paper-list">
                  {% for p in session_papers %}
                  <li class="paper-item">
                    <details class="paper-details">
                      <summary class="paper-summary">
                        <span class="paper-id">{{ p["Paper ID"] }}</span>
                        <span class="paper-title">{{ p["Paper Title"] }}</span>
                        <span class="paper-authors">{{ p["Authors"] }}</span>
                      </summary>
                      {% if p["Abstract"] and p["Abstract"] != "" %}
                      <div class="paper-abstract">{{ p["Abstract"] }}</div>
                      {% endif %}
                    </details>
                  </li>
                  {% endfor %}
                </ul>
              </div>
            {% endif %}
          {% endfor %}
          </div>
        </div>
      {% endif %}
    {% endfor %}
  </section>
  {% endif %}

  <div class="paper-separator" aria-hidden="true"></div>

  {% if day3.size > 0 %}
  <section id="day-3" class="paper-day">
    <h3 class="paper-day-title"><strong>Friday</strong> – 9 October 2026</h3>
    <div class="session-nav">
      {% assign day3_slots = "A|B|C|D|E|F" | split: "|" %}
      {% for slot in day3_slots %}
        {% assign slot_papers = day3 | where: "TimeSlot", slot %}
        {% if slot_papers.size > 0 %}
          {% assign slot_time = slot_papers[0]["Time"] %}
          {% assign slot_class = "session-btn-a" %}
          {% if slot == "B" or slot == "D" or slot == "F" %}{% assign slot_class = "session-btn-b" %}{% endif %}
          <a href="#day-3-slot-{{ slot | downcase }}" class="session-btn {{ slot_class }}">Session {{ slot }} <span class="session-time">{{ slot_time }}</span></a>
        {% endif %}
      {% endfor %}
    </div>
    {% for slot in day3_slots %}
      {% assign slot_papers = day3 | where: "TimeSlot", slot %}
      {% if slot_papers.size > 0 %}
        {% assign slot_time = slot_papers[0]["Time"] %}
        {% assign session_class = "session-a" %}
        {% assign title_class = "session-title-a" %}
        {% if slot == "B" or slot == "D" or slot == "F" %}
          {% assign session_class = "session-b" %}
          {% assign title_class = "session-title-b" %}
        {% endif %}
        <div id="day-3-slot-{{ slot | downcase }}" class="paper-slot {{ session_class }}">
          <h4 class="slot-title {{ title_class }}"><span class="slot-label">Session {{ slot }}</span>{{ slot_time }}</h4>
          {% assign session_ids = "" %}
          {% for p in slot_papers %}
            {% unless session_ids contains p["Session ID"] %}
              {% assign session_ids = session_ids | append: p["Session ID"] | append: "|" %}
            {% endunless %}
          {% endfor %}
          {% assign session_ids = session_ids | split: "|" | sort %}
          <div class="parallel-sessions">
          {% for sid in session_ids %}
            {% if sid != "" %}
              {% assign session_papers = slot_papers | where: "Session ID", sid %}
              {% assign session_title = session_papers[0]["Session Title"] %}
              {% assign session_room = session_papers[0]["Room"] %}
              {% comment %} Compute PS number from Session ID {% endcomment %}
              {% assign sid_day = sid | slice: 6, 1 | plus: 0 %}
              {% assign sid_slot = sid | slice: 7, 1 %}
              {% assign sid_track = sid | slice: 8, 1 | plus: 0 %}
              {% assign day_offset = sid_day | minus: 1 | times: 18 %}
              {% case sid_slot %}
                {% when "A" %}{% assign slot_offset = 0 %}
                {% when "B" %}{% assign slot_offset = 3 %}
                {% when "C" %}{% assign slot_offset = 6 %}
                {% when "D" %}{% assign slot_offset = 9 %}
                {% when "E" %}{% assign slot_offset = 12 %}
                {% when "F" %}{% assign slot_offset = 15 %}
              {% endcase %}
              {% assign ps_num = day_offset | plus: slot_offset | plus: sid_track %}
              <div class="paper-session" id="session-{{ sid | slugify }}">
                <h5 class="session-header {{ title_class }}">PS{{ ps_num }}: {{ session_title }} <span class="session-room">{{ session_room }}</span></h5>
                <ul class="paper-list">
                  {% for p in session_papers %}
                  <li class="paper-item">
                    <details class="paper-details">
                      <summary class="paper-summary">
                        <span class="paper-id">{{ p["Paper ID"] }}</span>
                        <span class="paper-title">{{ p["Paper Title"] }}</span>
                        <span class="paper-authors">{{ p["Authors"] }}</span>
                      </summary>
                      {% if p["Abstract"] and p["Abstract"] != "" %}
                      <div class="paper-abstract">{{ p["Abstract"] }}</div>
                      {% endif %}
                    </details>
                  </li>
                  {% endfor %}
                </ul>
              </div>
            {% endif %}
          {% endfor %}
          </div>
        </div>
      {% endif %}
    {% endfor %}
  </section>
  {% endif %}
</div>

For questions, contact: papers2026@ieeeismar.net

<style>
/* Day navigation buttons */
.day-nav { display:flex; flex-wrap:nowrap; gap:10px; padding:12px 10px; margin:-8px -10px 20px; position:sticky; top:70px; background:#F4E8D4; z-index:11; animation:none !important; }
.day-btn { display:inline-flex; align-items:center; justify-content:center; gap:8px; padding:10px 18px; border-radius:8px; font-size:0.9rem; font-weight:600; text-decoration:none; background:#3A8BF3; color:#fff !important; box-shadow:0 2px 4px rgba(0,0,0,.12); animation:none !important; flex:1 1 0; min-width:0; }
.day-btn:hover { background:#2878DB; transform:translateY(-1px); box-shadow:0 3px 8px rgba(0,0,0,.18); text-decoration:none !important; color:#fff !important; }
.day-date { font-size:0.75rem; font-weight:500; opacity:0.85; }
.day-short { display:none; }

/* Table of Contents */
.papers-toc { max-width: 1050px; margin: 0 0 24px 0; }
.papers-toc-table { width:100%; border-collapse:collapse; font-size:0.85rem; background:#fff; margin-bottom:16px; }
.papers-toc-table th, .papers-toc-table td { padding:5px 8px; text-align:left; border:1px solid #dcdfe3; }
.papers-toc-table th { background:#3A8BF3; color:#fff; font-weight:600; font-size:0.72rem; letter-spacing:.5px; text-transform:uppercase; }
.papers-toc-table td.toc-chair { font-size:0.8rem; }
.papers-toc-table tbody tr.toc-row-a { background:rgba(58, 139, 243, 0.12); color:#2878DB; }
.papers-toc-table tbody tr.toc-row-b { background:rgba(242, 140, 40, 0.10); color:#D96F08; }
.papers-toc-table tbody tr.toc-row-a:hover { background:rgba(58, 139, 243, 0.22); }
.papers-toc-table tbody tr.toc-row-b:hover { background:rgba(242, 140, 40, 0.18); }
.toc-day { margin:20px 0 8px 0; font-size:1.1rem; font-weight:700; color:#333; }
.toc-row-a .toc-time a, .toc-row-a .toc-session a, .toc-row-a .toc-location a { text-decoration:none; color:#2878DB; }
.toc-row-b .toc-time a, .toc-row-b .toc-session a, .toc-row-b .toc-location a { text-decoration:none; color:#D96F08; }
.toc-time a:hover, .toc-session a:hover, .toc-location a:hover { text-decoration:underline; }
.toc-session { font-weight:500; }
.toc-location { font-size:0.8rem; }

.papers-wrapper { max-width: 1050px; margin: 8px 0 28px 0; }
.paper-day { margin-bottom: 26px; scroll-margin-top: 130px; }
.paper-day-title { margin: 0; font-size: 1.35rem; border-bottom: none; padding: 8px 10px 6px; position:sticky; top:128px; background:#F4E8D4; z-index:10; margin-left:-10px; margin-right:-10px; }
.session-nav { display:flex; flex-wrap:nowrap; gap:6px; margin:0 -10px 16px; position:sticky; top:168px; background:#F4E8D4; z-index:9; padding:0 10px 12px; box-shadow: 0 -30px 0 #F4E8D4; }
.paper-separator { height:1px; background:#ddd; margin:24px 0; }

/* Session navigation buttons */
.session-btn { display:inline-flex; align-items:center; gap:4px; padding:6px 10px; border-radius:6px; font-size:0.72rem; font-weight:600; text-decoration:none; transition: all 0.2s ease; box-shadow:0 1px 3px rgba(0,0,0,.1); }
.session-btn:hover { transform:translateY(-1px); box-shadow:0 2px 6px rgba(0,0,0,.15); text-decoration:none; }
.session-btn-a, .session-btn-a:link, .session-btn-a:visited { background:#3A8BF3; color:#fff !important; }
.session-btn-a:hover { background:#2878DB; color:#fff !important; }
.session-btn-b, .session-btn-b:link, .session-btn-b:visited { background:#F28C28; color:#fff !important; }
.session-btn-b:hover { background:#D96F08; color:#fff !important; }
.session-time { font-size:0.62rem; font-weight:500; opacity:0.9; }

/* Slot containers */
.paper-slot { margin-bottom:20px; padding:12px 14px 14px; border-radius:10px; scroll-margin-top:240px; }
.session-a { background:rgba(58, 139, 243, 0.18); border-left:4px solid #3A8BF3; }
.session-b { background:rgba(242, 140, 40, 0.12); border-left:4px solid #F28C28; }

/* Slot titles */
.slot-title { margin:0 0 12px 0; font-size:1rem; font-weight:600; display:flex; flex-wrap:wrap; align-items:center; gap:4px 12px; }
.session-title-a { color:#2878DB; }
.session-title-b { color:#D96F08; }
.slot-label { display:block; width:100%; font-size:1.1rem; font-weight:700; margin-bottom:2px; }

/* Parallel sessions grid */
.parallel-sessions { display:grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap:12px; }

/* Individual session */
.paper-session { background:#fff; border-radius:8px; padding:10px 12px; box-shadow:0 1px 3px rgba(0,0,0,.08); scroll-margin-top:270px; }
.session-header { margin:0 0 8px 0; font-size:0.95rem; font-weight:600; display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; gap:6px; }
.session-room { font-size:0.75rem; font-weight:500; background:#f0f0f0; padding:2px 8px; border-radius:12px; color:#555; }

/* Paper list */
.page-content ul.paper-list { list-style: none; margin: 0; padding: 0; }
.paper-item { margin: 0 0 6px 0; padding: 0; background: #fafafa; border:1px solid #e1e4e7; border-radius:8px; box-shadow:0 1px 1px rgba(0,0,0,.03); position:relative; }
.paper-item:hover { box-shadow:0 1px 4px rgba(0,0,0,.07); border-color:#d2d7db; }

/* Expandable paper details */
.paper-details { width:100%; }
.paper-summary { display:block; padding:6px 9px 6px 10px; cursor:pointer; list-style:none; position:relative; padding-left:22px; }
.paper-summary::-webkit-details-marker { display:none; }
.paper-summary::marker { display:none; }
.paper-summary::before { content:""; position:absolute; left:8px; top:10px; width:0; height:0; border-left:6px solid #2878DB; border-top:4px solid transparent; border-bottom:4px solid transparent; transition:transform 0.2s ease; }
.session-b .paper-summary::before { border-left-color:#F28C28; }
.paper-details[open] .paper-summary::before { transform:rotate(90deg); }
.paper-details[open] .paper-summary { border-bottom:1px solid #e8eaed; }
.paper-abstract { padding:10px 12px; font-size:0.82rem; line-height:1.5; color:#333; background:#f8f9fa; border-radius:0 0 7px 7px; }
.session-b .paper-abstract { background:#fef8f4; }

.paper-id { display:inline-block; background: #2878DB; color:#fff; font-size:0.60rem; letter-spacing:.45px; font-weight:600; padding:5px 6px 5px; border-radius:6px; margin:0 8px 3px 0; vertical-align:middle; box-shadow:0 1px 2px rgba(0,0,0,.15); line-height:1; }
.session-b .paper-id { background: #F28C28; }
.paper-title { display:inline; font-weight:600; color: #2878DB; font-size:0.9rem; line-height:1.2; cursor:pointer; }
.paper-title:hover { text-decoration:underline; }
.session-b .paper-title { color: #D96F08; }
.paper-authors { display:block; font-size:0.66rem; line-height:1.15; margin:3px 0 0 0; color:#444; }

/* Mobile: transform TOC table rows into cards */
@media (max-width: 720px){
  .papers-toc-table thead { display:none; }
  .papers-toc-table { border:0; }
  .papers-toc-table, .papers-toc-table tbody { display:block; width:100%; }
  .papers-toc-table tr { display:flex; flex-wrap:wrap; border-radius:8px; padding:8px 10px; margin-bottom:6px; box-shadow:0 1px 2px rgba(0,0,0,.05); }
  .papers-toc-table tr.toc-row-a { border:1px solid rgba(58, 139, 243, 0.3); }
  .papers-toc-table tr.toc-row-b { border:1px solid rgba(242, 140, 40, 0.3); }
  .papers-toc-table td { border:none; padding:2px 0; font-size:0.82rem; line-height:1.2; }
  .papers-toc-table td.toc-session { order:0; width:100%; font-size:0.95rem; font-weight:600; margin-bottom:4px; text-align:left; padding-left:0; }
  .papers-toc-table td.toc-session a { display:block; width:100%; }
  .papers-toc-table td.toc-time { order:1; width:auto; font-weight:500; font-size:0.8rem; margin-right:10px; }
  .papers-toc-table td.toc-location { order:2; width:auto; text-align:left; font-size:0.8rem; }
  .papers-toc-table td.toc-location:before { content:"• "; opacity:0.5; margin-right:2px; }
  .papers-toc-table td.toc-chair { order:3; width:100%; font-size:0.75rem; margin-top:2px; opacity:0.8; }
  .toc-day { margin:14px 0 6px 0; font-size:0.95rem; }
}

@media (max-width: 640px){
  .day-nav { gap:4px; padding:6px 10px; }
  .day-btn { padding:5px 8px; font-size:0.65rem; gap:4px; }
  .day-btn:hover, .day-btn:active { background:#3A8BF3; transform:none; box-shadow:0 2px 4px rgba(0,0,0,.12); }
  .day-date { font-size:0.55rem; }
  .day-full { display:none; }
  .day-short { display:inline; }
  .paper-day-title { top:100px; }
  .session-nav { top:138px; }
  .paper-title { display:inline; margin-top:0; }
  .paper-authors { font-size:0.64rem; }
  .paper-day-title { font-size:1.22rem; }
  .session-nav { gap:6px; flex-wrap:wrap; }
  .session-btn { padding:8px 12px; font-size:0.75rem; flex:1 1 auto; min-width:calc(33% - 6px); justify-content:center; }
  .session-btn .session-time { margin-left:4px; }
  .session-time { font-size:0.62rem; }
  .paper-slot { padding:10px 10px 12px; scroll-margin-top:300px; }
  .slot-title { font-size:0.9rem; }
  .parallel-sessions { grid-template-columns: 1fr; }
  .session-header { font-size:0.88rem; }
}
</style>
