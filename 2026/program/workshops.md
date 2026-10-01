---
layout: 2026/program-page-2026
title: Workshops
permalink: /2026/workshops/
---


<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-FQFFZGXF3Y"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-FQFFZGXF3Y');
</script>

## Workshops

{% assign all_workshops = site.data["2026"].workshops %}
{% assign monday_all = all_workshops | where_exp: "w", "w['Day/Time'] contains 'Monday 5 October, All Day'" | sort: "Title" %}
{% assign monday_morning = all_workshops | where_exp: "w", "w['Day/Time'] contains 'Monday 5 October, Morning'" | sort: "Title" %}
{% assign monday_afternoon = all_workshops | where_exp: "w", "w['Day/Time'] contains 'Monday 5 October, Afternoon'" | sort: "Title" %}
{% assign tuesday_all = all_workshops | where_exp: "w", "w['Day/Time'] contains 'Tuesday 6 October, All Day'" | sort: "Title" %}
{% assign tuesday_morning = all_workshops | where_exp: "w", "w['Day/Time'] contains 'Tuesday 6 October, Morning'" | sort: "Title" %}
{% assign tuesday_afternoon = all_workshops | where_exp: "w", "w['Day/Time'] contains 'Tuesday 6 October, Afternoon'" | sort: "Title" %}

<div class="day-nav">
  <a href="#day-1" class="day-btn"><span class="day-full">Monday</span><span class="day-short">Mon</span> <span class="day-date">Oct 5</span></a>
  <a href="#day-2" class="day-btn"><span class="day-full">Tuesday</span><span class="day-short">Tue</span> <span class="day-date">Oct 6</span></a>
</div>

### Monday - October 5, 2026
{: #day-1 .workshop-day-title }

<div class="session-nav">
  <a href="#monday-all-day" class="session-btn">All Day <span class="session-count">{{ monday_all.size }}</span></a>
  <a href="#monday-morning" class="session-btn">Morning <span class="session-count">{{ monday_morning.size }}</span></a>
  <a href="#monday-afternoon" class="session-btn">Afternoon <span class="session-count">{{ monday_afternoon.size }}</span></a>
</div>

{% if monday_all.size > 0 %}
<section id="monday-all-day" class="workshop-session">
  <h4 class="workshop-session-title">All Day</h4>
  <ul class="workshop-list">
    {% for workshop in monday_all %}
    {% assign contact_name = workshop["Main Contact Person"] | default: "" | strip %}
    {% assign contact_email = workshop["Main Contact Email"] | default: "" | strip %}
    {% assign workshop_website = workshop["Website"] | default: "" | strip %}
    {% assign workshop_cfp = workshop["CFP"] | default: "" | strip %}
    <li class="workshop-item">
      <details class="workshop-details" id="{{ workshop['Title'] | slugify }}">
        <summary class="workshop-summary">
          {% if workshop["Room"] and workshop["Room"] != "" %}<span class="workshop-room">{{ workshop["Room"] }}</span>{% endif %}
          <span class="workshop-title">{{ workshop["Title"] }}</span>
        </summary>
        <div class="workshop-expanded">
          <p><strong>Day/Time:</strong> {{ workshop["Day/Time"] }}</p>
          {% if contact_name != "" and contact_email != "" %}
          <p><strong>Main Contact Person:</strong> <a href="mailto:{{ contact_email }}">{{ contact_name }}</a></p>
          {% elsif contact_name != "" %}
          <p><strong>Main Contact Person:</strong> {{ contact_name }}</p>
          {% endif %}
          {% if workshop_website != "" or workshop_cfp != "" %}
          <p class="workshop-links">
            {% if workshop_website != "" %}<a href="{{ workshop_website }}" target="_blank" rel="noopener">Workshop Website</a>{% endif %}
            {% if workshop_cfp != "" %}<a href="{{ workshop_cfp | relative_url }}" download>Download CfP</a>{% endif %}
          </p>
          {% endif %}
          <h5>Abstract</h5>
          <p>{{ workshop["Abstract"] | newline_to_br }}</p>
        </div>
      </details>
    </li>
    {% endfor %}
  </ul>
</section>
{% endif %}
{% if monday_morning.size > 0 %}
<section id="monday-morning" class="workshop-session">
  <h4 class="workshop-session-title">Morning</h4>
  <ul class="workshop-list">
    {% for workshop in monday_morning %}
    {% assign contact_name = workshop["Main Contact Person"] | default: "" | strip %}
    {% assign contact_email = workshop["Main Contact Email"] | default: "" | strip %}
    {% assign workshop_website = workshop["Website"] | default: "" | strip %}
    {% assign workshop_cfp = workshop["CFP"] | default: "" | strip %}
    <li class="workshop-item">
      <details class="workshop-details" id="{{ workshop['Title'] | slugify }}">
        <summary class="workshop-summary">
          {% if workshop["Room"] and workshop["Room"] != "" %}<span class="workshop-room">{{ workshop["Room"] }}</span>{% endif %}
          <span class="workshop-title">{{ workshop["Title"] }}</span>
        </summary>
        <div class="workshop-expanded">
          <p><strong>Day/Time:</strong> {{ workshop["Day/Time"] }}</p>
          {% if contact_name != "" and contact_email != "" %}
          <p><strong>Main Contact Person:</strong> <a href="mailto:{{ contact_email }}">{{ contact_name }}</a></p>
          {% elsif contact_name != "" %}
          <p><strong>Main Contact Person:</strong> {{ contact_name }}</p>
          {% endif %}
          {% if workshop_website != "" or workshop_cfp != "" %}
          <p class="workshop-links">
            {% if workshop_website != "" %}<a href="{{ workshop_website }}" target="_blank" rel="noopener">Workshop Website</a>{% endif %}
            {% if workshop_cfp != "" %}<a href="{{ workshop_cfp | relative_url }}" download>Download CfP</a>{% endif %}
          </p>
          {% endif %}
          <h5>Abstract</h5>
          <p>{{ workshop["Abstract"] | newline_to_br }}</p>
        </div>
      </details>
    </li>
    {% endfor %}
  </ul>
</section>
{% endif %}
{% if monday_afternoon.size > 0 %}
<section id="monday-afternoon" class="workshop-session">
  <h4 class="workshop-session-title">Afternoon</h4>
  <ul class="workshop-list">
    {% for workshop in monday_afternoon %}
    {% assign contact_name = workshop["Main Contact Person"] | default: "" | strip %}
    {% assign contact_email = workshop["Main Contact Email"] | default: "" | strip %}
    {% assign workshop_website = workshop["Website"] | default: "" | strip %}
    {% assign workshop_cfp = workshop["CFP"] | default: "" | strip %}
    <li class="workshop-item">
      <details class="workshop-details" id="{{ workshop['Title'] | slugify }}">
        <summary class="workshop-summary">
          {% if workshop["Room"] and workshop["Room"] != "" %}<span class="workshop-room">{{ workshop["Room"] }}</span>{% endif %}
          <span class="workshop-title">{{ workshop["Title"] }}</span>
        </summary>
        <div class="workshop-expanded">
          <p><strong>Day/Time:</strong> {{ workshop["Day/Time"] }}</p>
          {% if contact_name != "" and contact_email != "" %}
          <p><strong>Main Contact Person:</strong> <a href="mailto:{{ contact_email }}">{{ contact_name }}</a></p>
          {% elsif contact_name != "" %}
          <p><strong>Main Contact Person:</strong> {{ contact_name }}</p>
          {% endif %}
          {% if workshop_website != "" or workshop_cfp != "" %}
          <p class="workshop-links">
            {% if workshop_website != "" %}<a href="{{ workshop_website }}" target="_blank" rel="noopener">Workshop Website</a>{% endif %}
            {% if workshop_cfp != "" %}<a href="{{ workshop_cfp | relative_url }}" download>Download CfP</a>{% endif %}
          </p>
          {% endif %}
          <h5>Abstract</h5>
          <p>{{ workshop["Abstract"] | newline_to_br }}</p>
        </div>
      </details>
    </li>
    {% endfor %}
  </ul>
</section>
{% endif %}

### Tuesday - October 6, 2026
{: #day-2 .workshop-day-title }

<div class="session-nav">
  <a href="#tuesday-all-day" class="session-btn">All Day <span class="session-count">{{ tuesday_all.size }}</span></a>
  <a href="#tuesday-morning" class="session-btn">Morning <span class="session-count">{{ tuesday_morning.size }}</span></a>
  <a href="#tuesday-afternoon" class="session-btn">Afternoon <span class="session-count">{{ tuesday_afternoon.size }}</span></a>
</div>

{% if tuesday_all.size > 0 %}
<section id="tuesday-all-day" class="workshop-session">
  <h4 class="workshop-session-title">All Day</h4>
  <ul class="workshop-list">
    {% for workshop in tuesday_all %}
    {% assign contact_name = workshop["Main Contact Person"] | default: "" | strip %}
    {% assign contact_email = workshop["Main Contact Email"] | default: "" | strip %}
    {% assign workshop_website = workshop["Website"] | default: "" | strip %}
    {% assign workshop_cfp = workshop["CFP"] | default: "" | strip %}
    <li class="workshop-item">
      <details class="workshop-details" id="{{ workshop['Title'] | slugify }}">
        <summary class="workshop-summary">
          {% if workshop["Room"] and workshop["Room"] != "" %}<span class="workshop-room">{{ workshop["Room"] }}</span>{% endif %}
          <span class="workshop-title">{{ workshop["Title"] }}</span>
        </summary>
        <div class="workshop-expanded">
          <p><strong>Day/Time:</strong> {{ workshop["Day/Time"] }}</p>
          {% if contact_name != "" and contact_email != "" %}
          <p><strong>Main Contact Person:</strong> <a href="mailto:{{ contact_email }}">{{ contact_name }}</a></p>
          {% elsif contact_name != "" %}
          <p><strong>Main Contact Person:</strong> {{ contact_name }}</p>
          {% endif %}
          {% if workshop_website != "" or workshop_cfp != "" %}
          <p class="workshop-links">
            {% if workshop_website != "" %}<a href="{{ workshop_website }}" target="_blank" rel="noopener">Workshop Website</a>{% endif %}
            {% if workshop_cfp != "" %}<a href="{{ workshop_cfp | relative_url }}" download>Download CfP</a>{% endif %}
          </p>
          {% endif %}
          <h5>Abstract</h5>
          <p>{{ workshop["Abstract"] | newline_to_br }}</p>
        </div>
      </details>
    </li>
    {% endfor %}
  </ul>
</section>
{% endif %}
{% if tuesday_morning.size > 0 %}
<section id="tuesday-morning" class="workshop-session">
  <h4 class="workshop-session-title">Morning</h4>
  <ul class="workshop-list">
    {% for workshop in tuesday_morning %}
    {% assign contact_name = workshop["Main Contact Person"] | default: "" | strip %}
    {% assign contact_email = workshop["Main Contact Email"] | default: "" | strip %}
    {% assign workshop_website = workshop["Website"] | default: "" | strip %}
    {% assign workshop_cfp = workshop["CFP"] | default: "" | strip %}
    <li class="workshop-item">
      <details class="workshop-details" id="{{ workshop['Title'] | slugify }}">
        <summary class="workshop-summary">
          {% if workshop["Room"] and workshop["Room"] != "" %}<span class="workshop-room">{{ workshop["Room"] }}</span>{% endif %}
          <span class="workshop-title">{{ workshop["Title"] }}</span>
        </summary>
        <div class="workshop-expanded">
          <p><strong>Day/Time:</strong> {{ workshop["Day/Time"] }}</p>
          {% if contact_name != "" and contact_email != "" %}
          <p><strong>Main Contact Person:</strong> <a href="mailto:{{ contact_email }}">{{ contact_name }}</a></p>
          {% elsif contact_name != "" %}
          <p><strong>Main Contact Person:</strong> {{ contact_name }}</p>
          {% endif %}
          {% if workshop_website != "" or workshop_cfp != "" %}
          <p class="workshop-links">
            {% if workshop_website != "" %}<a href="{{ workshop_website }}" target="_blank" rel="noopener">Workshop Website</a>{% endif %}
            {% if workshop_cfp != "" %}<a href="{{ workshop_cfp | relative_url }}" download>Download CfP</a>{% endif %}
          </p>
          {% endif %}
          <h5>Abstract</h5>
          <p>{{ workshop["Abstract"] | newline_to_br }}</p>
        </div>
      </details>
    </li>
    {% endfor %}
  </ul>
</section>
{% endif %}
{% if tuesday_afternoon.size > 0 %}
<section id="tuesday-afternoon" class="workshop-session">
  <h4 class="workshop-session-title">Afternoon</h4>
  <ul class="workshop-list">
    {% for workshop in tuesday_afternoon %}
    {% assign contact_name = workshop["Main Contact Person"] | default: "" | strip %}
    {% assign contact_email = workshop["Main Contact Email"] | default: "" | strip %}
    {% assign workshop_website = workshop["Website"] | default: "" | strip %}
    {% assign workshop_cfp = workshop["CFP"] | default: "" | strip %}
    <li class="workshop-item">
      <details class="workshop-details" id="{{ workshop['Title'] | slugify }}">
        <summary class="workshop-summary">
          {% if workshop["Room"] and workshop["Room"] != "" %}<span class="workshop-room">{{ workshop["Room"] }}</span>{% endif %}
          <span class="workshop-title">{{ workshop["Title"] }}</span>
        </summary>
        <div class="workshop-expanded">
          <p><strong>Day/Time:</strong> {{ workshop["Day/Time"] }}</p>
          {% if contact_name != "" and contact_email != "" %}
          <p><strong>Main Contact Person:</strong> <a href="mailto:{{ contact_email }}">{{ contact_name }}</a></p>
          {% elsif contact_name != "" %}
          <p><strong>Main Contact Person:</strong> {{ contact_name }}</p>
          {% endif %}
          {% if workshop_website != "" or workshop_cfp != "" %}
          <p class="workshop-links">
            {% if workshop_website != "" %}<a href="{{ workshop_website }}" target="_blank" rel="noopener">Workshop Website</a>{% endif %}
            {% if workshop_cfp != "" %}<a href="{{ workshop_cfp | relative_url }}" download>Download CfP</a>{% endif %}
          </p>
          {% endif %}
          <h5>Abstract</h5>
          <p>{{ workshop["Abstract"] | newline_to_br }}</p>
        </div>
      </details>
    </li>
    {% endfor %}
  </ul>
</section>
{% endif %}

<style>
.day-nav { display:flex; gap:10px; padding:12px 10px; margin:-8px -10px 8px; position:sticky; top:70px; background:#F4E8D4; z-index:11; }
.day-btn { display:inline-flex; align-items:center; justify-content:center; gap:8px; padding:10px 18px; border-radius:8px; font-size:.9rem; font-weight:600; text-decoration:none; background:#3A8BF3; color:#fff !important; box-shadow:0 2px 4px rgba(0,0,0,.12); flex:1 1 0; min-width:0; }
.day-btn:hover { background:#2878DB; text-decoration:none !important; color:#fff !important; }
.day-date { font-size:.75rem; font-weight:500; opacity:.85; }
.day-short { display:none; }
.workshop-day-title { margin:0; font-size:1.35rem; border:0; padding:8px 10px 6px; position:sticky; top:128px; background:#F4E8D4; z-index:10; margin-left:-10px; margin-right:-10px; scroll-margin-top:130px; }
.session-nav { display:flex; flex-wrap:wrap; gap:8px; margin:0 -10px 16px; padding:0 10px 12px; position:sticky; top:168px; background:#F4E8D4; z-index:9; box-shadow:0 -30px 0 #F4E8D4; }
.session-btn { display:inline-flex; align-items:center; gap:8px; padding:8px 14px; border-radius:8px; font-size:.8rem; font-weight:600; text-decoration:none; background:#3A8BF3; color:#fff !important; box-shadow:0 1px 3px rgba(0,0,0,.1); }
.session-btn:hover { background:#2878DB; color:#fff !important; text-decoration:none; }
.session-count { font-size:.68rem; font-weight:500; opacity:.9; }
.workshop-session { margin-bottom:20px; padding:12px 14px 14px; border-radius:10px; background:rgba(58,139,243,.18); border-left:4px solid #3A8BF3; scroll-margin-top:240px; }
.workshop-session-title { margin:0 0 10px; font-size:1rem; font-weight:600; color:#2878DB; }
.page-content ul.workshop-list { list-style:none; margin:0; padding:0; }
.workshop-item { margin:0 0 6px; padding:0; background:#fff; border:1px solid #e1e4e7; border-radius:8px; box-shadow:0 1px 1px rgba(0,0,0,.03); }
.workshop-details { scroll-margin-top:240px; }
.workshop-summary { display:block; padding:6px 9px 6px 22px; cursor:pointer; list-style:none; position:relative; }
.workshop-summary::-webkit-details-marker, .workshop-summary::marker { display:none; }
.workshop-summary::before { content:""; position:absolute; left:8px; top:10px; width:0; height:0; border-left:6px solid #2878DB; border-top:4px solid transparent; border-bottom:4px solid transparent; transition:transform .2s ease; }
.workshop-details[open] .workshop-summary::before { transform:rotate(90deg); }
.workshop-details[open] .workshop-summary { border-bottom:1px solid #e8eaed; }
.workshop-room { display:inline-block; background:#fff4d6; color:#7a4b00; font-size:.65rem; font-weight:700; padding:4px 6px; border-radius:6px; margin:0 6px 3px 0; vertical-align:middle; line-height:1; }
.workshop-title { display:inline; font-weight:600; color:#2878DB; font-size:.9rem; line-height:1.2; }
.workshop-expanded { padding:10px 12px; font-size:.82rem; line-height:1.5; color:#333; background:#f8f9fa; border-radius:0 0 7px 7px; }
.workshop-expanded p { margin:0 0 8px; }
.workshop-expanded h5 { margin:10px 0 4px; font-size:.9rem; }
.workshop-links { display:flex; flex-wrap:wrap; gap:12px; margin:8px 0; }
.workshop-links a { font-weight:600; }
@media (max-width:640px) {
  .day-nav { gap:4px; padding:6px 10px; }
  .day-btn { padding:5px 8px; font-size:.65rem; gap:4px; }
  .day-date { font-size:.55rem; }
  .day-full { display:none; }
  .day-short { display:inline; }
  .workshop-day-title { top:100px; font-size:1.22rem; }
  .session-nav { top:138px; gap:6px; }
  .session-btn { padding:8px 12px; font-size:.75rem; }
  .workshop-session { padding:10px 10px 12px; scroll-margin-top:300px; }
  .workshop-details { scroll-margin-top:300px; }
}
</style>

<script>
  function openLinkedWorkshop() {
    const workshop = document.getElementById(decodeURIComponent(window.location.hash.slice(1)));
    if (workshop && workshop.matches("details.workshop-details")) {
      workshop.open = true;
    }
  }

  openLinkedWorkshop();
  window.addEventListener("hashchange", openLinkedWorkshop);
</script>