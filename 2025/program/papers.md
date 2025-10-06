---
layout: 2025/page
title: Papers
---

*Last updated: 2025-10-06 8:01AM GMT*

{% assign rows = site.data["2025"]["program"]["papers"] %}
{% assign days = "October 9 2025|October 10 2025|October 11 2025" | split: "|" %}

<!-- Table of Contents -->
<div class="papers-toc">

  {% for day in days %}
    {% assign day_rows = rows | where: "Session Day", day %}
    {% assign combos_str = "" %}
    {% for r in day_rows %}
      {% assign combo = r["Session Start Time"] | append: "||" | append: r["Session End Time"] | append: "||" | append: r["Session Location"] | append: "||" | append: r["Session Title"] %}
      {% unless combos_str contains combo %}{% assign combos_str = combos_str | append: combo | append: "~~" %}{% endunless %}
    {% endfor %}
    {% assign combos = combos_str | split: "~~" | sort %}
    <h3 class="toc-day">{{ day }}</h3>
    <table class="papers-toc-table">
      <thead>
        <tr><th>Time</th><th>Session</th><th>Location</th></tr>
      </thead>
      <tbody>
      {% for combo in combos %}
        {% if combo != "" %}
          {% assign parts = combo | split: "||" %}
          {% assign start = parts[0] %}
          {% assign end = parts[1] %}
          {% assign location = parts[2] %}
          {% assign title = parts[3] %}
          {% assign anchor_raw = day | append: '-' | append: start | append: '-' | append: end | append: '-' | append: location | append: '-' | append: title %}
          {% assign anchor = anchor_raw | slugify %}
          <tr>
            <td class="toc-time"><a href="#{{ anchor }}">{{ start }} – {{ end }}</a></td>
            <td class="toc-session"><a href="#{{ anchor }}">{{ title }}</a></td>
            <td class="toc-location"><a href="#{{ anchor }}">{{ location }}</a></td>
          </tr>
        {% endif %}
      {% endfor %}
      </tbody>
    </table>
  {% endfor %}
</div>

<div class="papers-container">
  {% for day in days %}
    {% assign day_id = day | downcase | replace: ' ', '-' %}
    {% assign day_rows = rows | where: "Session Day", day %}
    <section class="papers-day" id="{{ day_id }}">
      <h1 class="papers-day-title">{{ day }}</h1>

      {% assign time_keys_str = "" %}
      {% for r in day_rows %}
        {% assign tkey = r["Session Start Time"] | append: "||" | append: r["Session End Time"] %}
        {% unless time_keys_str contains tkey %}{% assign time_keys_str = time_keys_str | append: tkey | append: "~~" %}{% endunless %}
      {% endfor %}
      {% assign time_keys = time_keys_str | split: "~~" | sort %}

      {% for time_key in time_keys %}
        {% if time_key != "" %}
          {% assign parts = time_key | split: "||" %}
          <h2 class="papers-time">{{ parts[0] }} - {{ parts[1] }}</h2>

          {% assign session_keys_str = "" %}
          {% for r in day_rows %}
            {% if r["Session Start Time"] == parts[0] and r["Session End Time"] == parts[1] %}
              {% assign skey = r["Session Location"] | append: "||" | append: r["Session Title"] %}
              {% unless session_keys_str contains skey %}{% assign session_keys_str = session_keys_str | append: skey | append: "~~" %}{% endunless %}
            {% endif %}
          {% endfor %}
          {% assign session_keys = session_keys_str | split: "~~" | sort %}

          <div class="papers-time-block">
          {% for session_key in session_keys %}
            {% if session_key != "" %}
              {% assign sess = session_key | split: "||" %}
              {% assign anchor_raw = day | append: '-' | append: parts[0] | append: '-' | append: parts[1] | append: '-' | append: sess[0] | append: '-' | append: sess[1] %}
              {% assign anchor = anchor_raw | slugify %}
              <h3 id="{{ anchor }}" class="papers-session">{{ sess[1] }} <span class="papers-location">{{ sess[0] }}</span></h3>
              <ul class="paper-list">
                {% for r in day_rows %}
                  {% if r["Session Start Time"] == parts[0] and r["Session End Time"] == parts[1] and r["Session Title"] == sess[1] and r["Session Location"] == sess[0] %}
                    <li class="paper-item">
                      <span class="paper-id">{{ r["Paper ID"] }}</span>
                      <span class="paper-title">{{ r["Paper Title"] }}</span>
                      {% if r["Paper Authors"] %}<span class="paper-authors">{{ r["Paper Authors"] }}</span>{% endif %}
                    </li>
                  {% endif %}
                {% endfor %}
              </ul>
            {% endif %}
          {% endfor %}
          </div>
        {% endif %}
      {% endfor %}
    </section>
  {% endfor %}
</div>

<style>
.papers-container { width:100%; max-width:1100px; margin:0 auto; padding:0 8px 32px 8px; }
.papers-toc { width:100%; max-width:1100px; margin:0 auto 24px auto; padding:0 8px; }
.papers-day-title { margin:36px 0 12px 0; font-size:1.75rem; border-bottom:2px solid #e3e6e8; padding-bottom:4px; }
.papers-day:first-of-type .papers-day-title { margin-top:8px; }
.papers-time { margin:18px 0 4px 0; font-size:1.05rem; color:#0d47a1; font-weight:600; display:flex; align-items:center; gap:8px; }
.papers-time-block { margin:0 0 14px 0; }
.papers-session { margin:6px 0 3px 0; font-size:0.95rem; font-weight:600; display:flex; align-items:center; flex-wrap:wrap; gap:6px; }
.papers-location { font-weight:500; color:#0d47a1; background:#eef4ff; border:1px solid #d0e2ff; padding:2px 8px; border-radius:14px; font-size:0.93rem; letter-spacing:.4px; }
.papers-session .papers-location { margin-left:0; }
.papers-day-title { position:relative; }
.papers-day-title::after { content:'Sessions'; position:absolute; right:0; top:50%; transform:translateY(-50%); font-size:0.55rem; letter-spacing:.6px; background:#eef1f4; color:#555; padding:3px 6px; border-radius:10px; font-weight:600; text-transform:uppercase; }
.page-content ul.paper-list { margin:0 0 10px 0px; padding:0; }
.paper-list li { margin:1px 0; line-height:1.35; }

/* Card styling similar to posters */
.paper-list .paper-item { list-style:none; margin:0 0 6px 0; padding:6px 9px 6px 10px; background:#fff; border:1px solid #e1e4e7; border-radius:8px; box-shadow:0 1px 1px rgba(0,0,0,.03); }
.paper-list .paper-item:hover { box-shadow:0 1px 4px rgba(0,0,0,.07); border-color:#d2d7db; }
.paper-item .paper-id { display:inline-block; background: rgb(37, 37, 197); color:#fff; font-size:0.60rem; letter-spacing:.45px; font-weight:600; padding:5px 6px 5px; border-radius:6px; margin:0 8px 3px 0; vertical-align:middle; line-height:1; }
.paper-item .paper-title { font-weight:600; color: var(--blue); font-size:0.9rem; line-height:1.2; }
.paper-item .paper-authors { display:block; font-size:0.66rem; line-height:1.15; margin:3px 0 0 0; color:#444; font-style:italic; }

/* TOC tables */
.papers-toc-table { width:100%; border-collapse:collapse; font-size:0.9rem; background:#fff; }
.papers-toc-table th, .papers-toc-table td { padding:4px 6px; text-align:left; border:1px solid #dcdfe3; }
.papers-toc-table th { background: rgb(37, 37, 197); font-weight:600; font-size:0.72rem; letter-spacing:.5px; text-transform:uppercase; }
.papers-toc-table tbody tr:nth-child(even) { background:#fafbfc; }
.papers-toc-table tbody td:before { padding-right: 0; };
.toc-day { margin:18px 0 6px 0; font-size:1.05rem; font-weight:600; }
.toc-time a, .toc-session a, .toc-location a { text-decoration:none; color:#064686; }
.toc-time a:hover, .toc-session a:hover, .toc-location a:hover { text-decoration:underline; }
.toc-session { word-break:break-word; }

/* Responsive: transform table rows into cards */
@media (max-width: 720px){
  .papers-day-title { font-size:1.45rem; }
  .papers-time { font-size:0.95rem; }
  .papers-toc-table thead { display:none; }
  .papers-toc-table { border:0; }
  .papers-toc-table, .papers-toc-table tbody { display:block; width:100%; }
  .papers-toc-table tr { display:flex; flex-wrap:wrap; border:1px solid #dcdfe3; border-radius:8px; padding:8px 10px; background:#fff; box-shadow:0 1px 2px rgba(0,0,0,.05); }
  .papers-toc-table td { border:none; padding:2px 0; font-size:0.82rem; line-height:1.2; }
  .papers-toc-table td.toc-session { order:0; width:100%; font-size:0.95rem; font-weight:600; margin-bottom:4px; text-align:left; padding-left:0; }
  .papers-toc-table td.toc-session a { display:block; width:100%; }
  /* Time & location inline, left aligned */
  .papers-toc-table td.toc-time { order:1; width:auto; font-weight:500; font-size:0.8rem; margin-right:10px; }
  .papers-toc-table td.toc-location { order:2; width:auto; text-align:left; font-size:0.8rem; }
  .papers-toc-table td.toc-location:before { content:"• "; color:#999; margin-right:2px; }
  /* Remove prepended labels from previous layout */
  .papers-toc-table td.toc-time:before,
  .papers-toc-table td.toc-session:before,
  .papers-toc-table td.toc-location:before { content:""; }
  .papers-toc { margin-bottom:12px; }
  .toc-day { margin:14px 0 4px 0; font-size:0.95rem; }
  .page-content ul.paper-list { margin-left:0; padding-left:0; }
  .papers-toc-table td a { display:inline-block; max-width:100%; text-overflow:ellipsis; overflow:hidden; vertical-align:top; }
  .papers-session { font-size:0.9rem; }
}
</style>

