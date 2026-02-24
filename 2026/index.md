---
layout: 2026/default-2026
title: ISMAR 2026
redirect_from: /
---

<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-FQFFZGXF3Y"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-FQFFZGXF3Y');
</script>

<!-- Custom hero for the main page -->
<div class="hero">
  <img class="hero-image" src="{{ '/assets/2026/img/hero/hero-1920.jpg' | relative_url }}" srcset="
      {{ '/assets/2026/img/hero/hero-3840.jpg' | relative_url }} 3840w,
      {{ '/assets/2026/img/hero/hero-2560.jpg' | relative_url }} 2560w,
      {{ '/assets/2026/img/hero/hero-1920.jpg' | relative_url }} 1920w,
      {{ '/assets/2026/img/hero/hero-1280.jpg' | relative_url }} 1280w,
      {{ '/assets/2026/img/hero/hero-640.jpg' | relative_url }} 640w
  " sizes="(max-width: 640px) 100vw,
          (max-width: 1280px) 100vw,
          (max-width: 1920px) 100vw,
          100vw" alt="Hero Image" />

  <div class="content">
    <a href="https://www.ieeeismar.net/2026/visual-identity/" aria-label="ISMAR 2026 Visual Identity">
      <img class="hero-logo" id="hero-logo"
           src="{{ '/assets/2026/img/hero.gif' | relative_url }}"
           alt="IEEE ISMAR 2026 Logo">
    </a>

    <h1 class="heading">WELCOME TO</h1>
    <h1 class="heading">IEEE ISMAR 2026</h1>
    <h2 class="subheading">Bari, Italy</h2>
    <h2 class="subheading">Oct. 5 - Oct. 9 2026</h2>

    <script>
      window.onload = function() {
        var staticImagePath = "{{ '/assets/2026/img/static.png' | relative_url }}";
        var heroLogo = document.getElementById("hero-logo");

        setTimeout(function() {
          heroLogo.src = staticImagePath;
        }, 9500);
      };
    </script>

    <section class="description">
      <p></p>
    </section>
  </div>
</div>


<!-- INTRO SECTION -->
<div class="announcement">
    <h2>Experience IEEE ISMAR in Bari, Italy, from October 5th to 9th, 2026!</h2>
    <p>
        The <strong>25th IEEE International Symposium on Mixed and Augmented Reality (ISMAR)</strong> is the leading global venue for AR, MR, and VR, bringing together top researchers, practitioners, and innovators from academia and industry.
    </p>

</div>


<section class="important-dates-section">
    <h3 class="important-dates-title">Important Deadlines</h3>
    <table class="important-dates">
        <thead>
            <tr>
                <th>Submission</th>
                <th>Deadline</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><b>Paper Abstract</b></td>
                <td><b>March 9th, 2026 (23:59 AoE, Monday)</b></td>
            </tr>
            <tr>
                <td><b>Paper</b></td>
                <td><b>March 16th, 2026 (23:59 AoE, Monday)</b></td>
            </tr>
            <tr>
                <td><b>Tutorials</b></td>
                <td><b>May 22nd, 2026 (23:59 AoE, Friday)</b></td>
            </tr>
            <tr>
                <td><b>Workshops</b></td>
                <td><b>May 22nd, 2026 (23:59 AoE, Friday)</b></td>
            </tr>
        </tbody>
    </table>
</section>



<div class="video-wrap">
    <iframe
        src="https://www.youtube.com/embed/8QAu5aJcDCc"
        title="ISMAR 2026 trailer"
        loading="lazy"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen>
    </iframe>
    <div class="video-fallback">
        <p>Video unavailable in this region.</p>
        <a href="https://youtu.be/8QAu5aJcDCc" target="_blank" rel="noopener">
            Open video on YouTube
        </a>
    </div>
</div>
