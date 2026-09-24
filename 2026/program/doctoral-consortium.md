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

## Doctoral Consortium Schedule

<strong>Day:</strong> Monday, 5th of October 2026

<strong>Room:</strong> Glasshaus

<strong style="font-size: 1.08em;">8:00 AM – 8:15 AM</strong>    <strong style="font-size: 1.08em;">Opening remarks</strong>

<strong style="font-size: 1.08em;">8:15 AM – 9:15 AM</strong>    <strong style="font-size: 1.08em;">Session1: Social XR (60 min: 10 min talk + 2 min Q&A)</strong>

{% assign session1_ids = "1024,1026,1034,1041,1048" | split: "," %}
{% for id in session1_ids %}
  {% assign dc = site.data["2026"]["program"].doctoral_consortium | where: "ID", id | first %}
&nbsp;&nbsp;&nbsp;<strong>DC{{ dc["ID"] }}:</strong> <span style="color: #1a73e8;">{{ dc["Submission title"] }}</span><br>
&nbsp;&nbsp;&nbsp;<strong>Presenter:</strong> {{ dc["Name"] | split: ", " | reverse | join: " " }}<br>
&nbsp;&nbsp;&nbsp;<strong>Mentor:</strong> {{ dc["Mentor"] | split: ", " | reverse | join: " " }}<br><br>
&nbsp;&nbsp;&nbsp;<strong>Abstract:</strong> {{ dc["Abstract"] }}
{% endfor %}

<strong style="font-size: 1.08em;">9:15 AM – 09:50 AM</strong>    <strong style="font-size: 1.08em;">Session2: XR Interaction (35 min: 10 min talk + 2 min Q&A)</strong>

{% assign session2_ids = "1025,1028,1032" | split: "," %}
{% for id in session2_ids %}
  {% assign dc = site.data["2026"]["program"].doctoral_consortium | where: "ID", id | first %}
&nbsp;&nbsp;&nbsp;<strong>DC{{ dc["ID"] }}:</strong> <span style="color: #1a73e8;">{{ dc["Submission title"] }}</span><br>
&nbsp;&nbsp;&nbsp;<strong>Presenter:</strong> {{ dc["Name"] | split: ", " | reverse | join: " " }}<br>
&nbsp;&nbsp;&nbsp;<strong>Mentor:</strong> {{ dc["Mentor"] | split: ", " | reverse | join: " " }}<br><br>
&nbsp;&nbsp;&nbsp;<strong>Abstract:</strong> {{ dc["Abstract"] }}
{% endfor %}

<strong style="font-size: 1.08em;">9:50 AM – 10:30 AM</strong>   <strong style="font-size: 1.08em;">Coffee break (40 mins)</strong>

<strong style="font-size: 1.08em;">10:30 AM – 11:00 AM</strong>    <strong style="font-size: 1.08em;">Session2: XR Interaction - continued (30 min: 10 min talk + 2 min Q&A)</strong>

{% assign session2b_ids = "1036,1038" | split: "," %}
{% for id in session2b_ids %}
  {% assign dc = site.data["2026"]["program"].doctoral_consortium | where: "ID", id | first %}
&nbsp;&nbsp;&nbsp;<strong>DC{{ dc["ID"] }}:</strong> <span style="color: #1a73e8;">{{ dc["Submission title"] }}</span><br>
&nbsp;&nbsp;&nbsp;<strong>Presenter:</strong> {{ dc["Name"] | split: ", " | reverse | join: " " }}<br>
&nbsp;&nbsp;&nbsp;<strong>Mentor:</strong> {{ dc["Mentor"] | split: ", " | reverse | join: " " }}<br><br>
&nbsp;&nbsp;&nbsp;<strong>Abstract:</strong> {{ dc["Abstract"] }}
{% endfor %}

<strong style="font-size: 1.08em;">11:00 AM – 12:00 PM</strong>    <strong style="font-size: 1.08em;">Session3: XR Training (60 min: 10 min talk + 2 min Q&A)</strong>

{% assign session3_ids = "1027,1039,1046,1049,1050" | split: "," %}
{% for id in session3_ids %}
  {% assign dc = site.data["2026"]["program"].doctoral_consortium | where: "ID", id | first %}
&nbsp;&nbsp;&nbsp;<strong>DC{{ dc["ID"] }}:</strong> <span style="color: #1a73e8;">{{ dc["Submission title"] }}</span><br>
&nbsp;&nbsp;&nbsp;<strong>Presenter:</strong> {{ dc["Name"] | split: ", " | reverse | join: " " }}<br>
&nbsp;&nbsp;&nbsp;<strong>Mentor:</strong> {{ dc["Mentor"] | split: ", " | reverse | join: " " }}<br><br>
&nbsp;&nbsp;&nbsp;<strong>Abstract:</strong> {{ dc["Abstract"] }}
{% endfor %}

<strong style="font-size: 1.08em;">12:00 PM – 2:00 PM</strong>   <strong style="font-size: 1.08em;">Lunch break (2h)</strong>

<strong style="font-size: 1.08em;">2:00 PM – 2:45 PM</strong>     <strong style="font-size: 1.08em;">1:1 Mentoring sessions (45min)</strong>

<strong style="font-size: 1.08em;">2:45 PM – 3:30 PM</strong>     <strong style="font-size: 1.08em;">Discussion & Closing remarks (45min)</strong>

