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
<style>
.info-categories-section {
  width: min(100% - 2rem, 960px);
  margin: 2.5rem auto;
}

.info-categories-title {
  margin: 0 0 1.2rem;
  color: #333;
  font-size: 1.65rem;
  font-weight: 900;
  text-align: center;
}

.info-categories-container {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}

.info-category {
  padding: 1.35rem 1.55rem;
  border-left: 6px solid;
  border-radius: 16px;
  color: #1f2933;
  line-height: 1.5;
  text-align: left;
}

.info-category h4 {
  margin: 0 0 0.35rem;
  font-size: 1.15rem;
  font-weight: 900;
}

.info-category p {
  margin: 0.45rem 0 0;
}

.info-category a {
  font-weight: 900;
  text-decoration: none;
}

.info-category a:hover {
  text-decoration: underline;
}

/*
Info categories:
info = blue
important = red
news = yellow
reminder = orange
*/

.info-category.info {
  border-color: #3A8BF3;
  background: rgba(58, 139, 243, 0.10);
}

.info-category.info h4,
.info-category.info a {
  color: #2878DB;
}

.info-category.important {
  border-color: #D93838;
  background: rgba(217, 56, 56, 0.10);
}

.info-category.important h4,
.info-category.important a {
  color: #B42323;
}

.info-category.news {
  border-color: #E5B700;
  background: rgba(255, 211, 45, 0.18);
}

.info-category.news h4,
.info-category.news a {
  color: #8A6800;
}

.info-category.reminder {
  border-color: #F28C28;
  background: rgba(242, 140, 40, 0.12);
}

.info-category.reminder h4,
.info-category.reminder a {
  color: #D96F08;
}
</style>

<section class="info-categories-section">
  <h3 class="info-categories-title">News &amp; Announcements</h3>

  <div class="info-categories-container">

    <article class="info-category info">
      <h4>IEEE ISMAR 2026 Registration Opens in July</h4>

      <p>
        Online registration for IEEE ISMAR 2026 will open in July 2026.
        Visit the registration page for information about fees, deadlines,
        and registration options.
      </p>

      <p>
        <a href="https://www.ieeeismar.net/2026/registration/">
          View registration information →
        </a>
      </p>
    </article>

    <article class="info-category news">
      <h4>Continue Your Conference Experience at ACM SUI 2026</h4>

      <p class="announcement-date">
        October 10–11, 2026 · Bari, Italy
      </p>

      <p>
        ACM SUI 2026 will take place in Bari immediately after IEEE ISMAR 2026.
        Extend your stay and join the international community exploring spatial
        user interaction, immersive technologies, and interactive systems.
      </p>

      <p>
        <a
          href="https://sigchi.org/events/sui-2026/"
          target="_blank"
          rel="noopener noreferrer"
        >
          Discover ACM SUI 2026 →
        </a>
      </p>
    </article>

  </div>
</section>





<section class="important-dates-section">
    <h3 class="important-dates-title">Important Deadlines</h3>
    <style>
        .important-dates tr.expired {
            color: #b6b6b6;
            text-decoration: line-through;
            opacity: 0.7;
        }
    </style>
    <table class="important-dates">
        <thead>
            <tr>
                <th>Submission</th>
                <th>Deadline</th>
            </tr>
        </thead>
        <tbody>
            <tr data-deadline="2026-09-05T23:59:59-12:00">
                <td><b>Pitch Your Lab</b></td>
                <td><b>September 5th, 2026 (23:59 AoE, Saturday)</b></td>
            </tr>
            <tr data-deadline="2026-09-04T23:59:59-12:00">
                <td><b>Paper Presentation Videos</b></td>
                <td><b>September 4th, 2026 (23:59 AoE, Friday)</b></td>
            </tr>
            <tr data-deadline="2026-08-30T23:59:59-12:00">
                <td><b><a href="https://www.ieeeismar.net/2026/women@ismar/">Women@ISMAR</a></b></td>
                <td><b>August 30th, 2026 (23:59 AoE, Sunday)</b></td>
            </tr>
            <tr data-deadline="2026-07-17T23:59:59-12:00">
                <td><b>Demos</b></td>
                <td><b>July 17th, 2026 (23:59 AoE, Friday)</b></td>
            </tr>
            <tr data-deadline="2026-07-15T23:59:59-12:00">
                <td><b>Student Volunteers</b></td>
                <td><b>July 15th, 2026 (23:59 AoE, Wednesday)</b></td>
            </tr>
            <tr data-deadline="2026-06-25T23:59:59-12:00">
                <td><b>Posters</b></td>
                <td><b>June 25th, 2026 (23:59 AoE, Thursday)</b></td>
            </tr>
            <tr data-deadline="2026-06-03T23:59:59-12:00">
                <td><b>Doctoral Consortium</b></td>
                <td><b>June 3rd, 2026 (23:59 AoE, Wednesday)</b></td>
            </tr>
            <tr data-deadline="2026-05-22T23:59:59-12:00">
                <td><b>Tutorials</b></td>
                <td><b>May 22nd, 2026 (23:59 AoE, Friday)</b></td>
            </tr>
            <tr data-deadline="2026-05-22T23:59:59-12:00">
                <td><b>Workshops</b></td>
                <td><b>May 22nd, 2026 (23:59 AoE, Friday)</b></td>
            </tr>
            <tr data-deadline="2026-03-16T23:59:59-12:00">
                <td><b>Papers</b></td>
                <td><b>March 16th, 2026 (23:59 AoE, Monday)</b></td>
            </tr>
            <tr data-deadline="2026-03-09T23:59:59-12:00">
                <td><b>Paper Abstract</b></td>
                <td><b>March 9th, 2026 (23:59 AoE, Monday)</b></td>
            </tr>
        </tbody>
    </table>
</section>

<script>
    (function () {
        const now = new Date();
        document.querySelectorAll(".important-dates tr[data-deadline]").forEach(row => {
            if (new Date(row.dataset.deadline) < now) {
                row.classList.add("expired");
            }
        });
    })();
</script>



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



<!-- Sponsors Section -->
<section class="sponsors-section">
    <h2 class="sponsors-title">Sponsors</h2>

    <!-- Silver Sponsors -->
    {% if site.data["2026"].sponsors.silver_sponsors %}
    <div class="sponsor-tier silver-tier">
        <div class="tier-header">
            <div class="tier-label silver">Silver</div>
        </div>
        <div class="sponsor-grid">
            {% for sponsor in site.data["2026"].sponsors.silver_sponsors %}
            {% if sponsor %}
            <div class="sponsor-item">
                {% if sponsor.url and sponsor.url != "" %}
                <a href="{{ sponsor.url }}" target="_blank" class="sponsor-logo-link">
                    <img src="{{ sponsor.logo | relative_url }}" alt="{{ sponsor.name }} Logo" />
                </a>
                {% else %}
                <div class="sponsor-logo-link">
                    <img src="{{ sponsor.logo | relative_url }}" alt="{{ sponsor.name }} Logo" />
                </div>
                {% endif %}
            </div>
            {% endif %}
            {% endfor %}
        </div>
    </div>
    {% endif %}

    <!-- Bronze Sponsors -->
    {% if site.data["2026"].sponsors.bronze_sponsors %}
    <div class="sponsor-tier bronze-tier">
        <div class="tier-header">
            <div class="tier-label bronze">Bronze</div>
        </div>
        <div class="sponsor-grid">
            {% for sponsor in site.data["2026"].sponsors.bronze_sponsors %}
            {% if sponsor %}
            <div class="sponsor-item">
                {% if sponsor.url and sponsor.url != "" %}
                <a href="{{ sponsor.url }}" target="_blank" class="sponsor-logo-link">
                    <img src="{{ sponsor.logo | relative_url }}" alt="{{ sponsor.name }} Logo" />
                </a>
                {% else %}
                <div class="sponsor-logo-link">
                    <img src="{{ sponsor.logo | relative_url }}" alt="{{ sponsor.name }} Logo" />
                </div>
                {% endif %}
            </div>
            {% endif %}
            {% endfor %}
        </div>
    </div>
    {% endif %}

</section>