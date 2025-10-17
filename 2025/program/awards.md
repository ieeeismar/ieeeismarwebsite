---
layout: 2025/page
title: Awards
---

# ISMAR 2025 Awards

We are pleased to announce the recipients of the ISMAR 2025 awards, recognizing outstanding contributions to the field of Mixed and Augmented Reality.

## {{ site.data["2025"].awards.award_categories.conference.title }}

{{ site.data["2025"].awards.award_categories.conference.description }}

{% for award in site.data["2025"].awards.conference_awards %}
### {{ award.name }}
**Recipient:** {{ award.recipient }}
{% if award.description != "" %}
**Title:** {{ award.description }}
{% endif %}

{% endfor %}

## {{ site.data["2025"].awards.award_categories.impact.title }}

{{ site.data["2025"].awards.award_categories.impact.description }}

{% for award in site.data["2025"].awards.impact_awards %}
### {{ award.name }}
{% for recipient in award.recipients %}
**Recipient:** {{ recipient.name }}
{% endfor %}
{% if award.description != "" %}
**Title:** {{ award.description }}
{% endif %}

{% endfor %}

---

*Last updated: {{ site.time | date: "%B %d, %Y" }}*
