---
layout: 2025/page
title: Awards
---

{% assign awards = site.data["2025"]["awards"] %}
{% assign prev_title = "" %}

<div class="awards-collection">
{% for award in awards %}
  {% assign title = award["Award Title"] | strip %}
  {% assign publication = award["Publication Title"] | strip %}
  {% assign authors = award["Authors"] | strip %}
  {% if title != prev_title %}
    {% unless forloop.first %}
      </ul>
    </section>
    {% endunless %}
    <section class="award-group" id="{{ title | slugify }}">
      <h2 class="award-heading">{{ title }}</h2>
      <ul class="award-list">
    {% assign prev_title = title %}
  {% endif %}
  <li class="award-item">
    {% if publication != "" and authors != "" %}
      <span class="award-paper"><em>{{ publication }}</em></span>
      <span class="award-authors">{{ authors }}</span>
    {% elsif publication != "" %}
      <span class="award-paper"><em>{{ publication }}</em></span>
    {% elsif authors != "" %}
      <span class="award-authors">{{ authors }}</span>
    {% else %}
      <span class="award-note">Details forthcoming.</span>
    {% endif %}
  </li>
  {% if forloop.last %}
      </ul>
    </section>
  {% endif %}
{% endfor %}
</div>

<style>
.award-group { margin-bottom: 30px; }
h2.award-heading { font-size: 1.35rem; border-bottom: 2px solid #e0e5eb; padding-bottom: 6px; margin-bottom: 12px; }
.award-item { padding-bottom: 6px; }
.award-paper { display: block; font-size: 0.95rem; color: #0c4184; }
.award-authors { display: block; font-size: 0.85rem; color: #333333; margin-top: 4px; }
.award-note { font-size: 0.9rem; color: #555555; }

@media (max-width: 620px) {
  .award-heading { font-size: 1.2rem; }
  .award-item { padding: 10px 12px; }
  .award-paper { font-size: 0.92rem; }
  .award-authors { font-size: 0.82rem; }
}
</style>
