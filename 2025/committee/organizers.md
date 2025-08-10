---
layout: 2025/page-full-width
title: Organizing Committee
---

<div class="organizers-container">
  {% assign chairs = site.data['2025'].committee.chairs %}
  {% for category in chairs %}
  <div class="chairs-category">
    {% if category.url %}
      <a href="{{ category.url }}">
        <h3>{{ category.title }}</h3>
      </a>
    {% else %}
      <h3>{{ category.title }}</h3>
    {% endif %}
    {% if category.email %}
      <p class="category-email">
        <a href="mailto:{{ category.email }}">{{ category.email }}</a>
      </p>
    {% endif %}
    <div class="chairs">
      {% for person in category.members %}
      <div class="chair">
        <img src="{{ person.img | relative_url }}" alt="{{ person.name }}" />
        <p class="name">{{ person.name }}</p>
        <p class="affiliation">{{ person.affiliation }}</p>
      </div>
      {% endfor %}
    </div>
  </div>
  {% endfor %}
</div>
