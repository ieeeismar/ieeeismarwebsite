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

<!-- ISMAR 2026 AT A GLANCE -->

<section class="ismar-glance-section">
  <div class="ismar-glance-inner">

<h2 class="ismar-glance-title">ISMAR 2026 Program Highlights</h2>

<div class="ismar-glance-grid">

  <div class="ismar-stat">
    <span class="ismar-counter" data-target="218">0</span>
    <span class="ismar-stat-label">Papers</span>
  </div>

  <div class="ismar-stat">
    <span class="ismar-counter" data-target="173">0</span>
    <span class="ismar-stat-label">Workshop Papers</span>
  </div>

  <div class="ismar-stat">
    <span class="ismar-counter" data-target="150">0</span>
    <span class="ismar-stat-label">Poster Papers</span>
  </div>

  <div class="ismar-stat">
    <span class="ismar-counter" data-target="10">0</span>
    <span class="ismar-stat-label">Doctoral Consortium Papers</span>
  </div>

  <div class="ismar-stat">
    <span class="ismar-counter" data-target="29">0</span>
    <span class="ismar-stat-label">Demo Papers</span>
  </div>

  <div class="ismar-stat">
    <span class="ismar-counter" data-target="3">0</span>
    <span class="ismar-stat-label">Keynotes</span>
  </div>

  <div class="ismar-stat">
    <span class="ismar-counter" data-target="2">0</span>
    <span class="ismar-stat-label">Panels</span>
  </div>

</div>

<div class="ismar-program-cta">
  <a href="/2026/overview/" class="ismar-program-button">
    Discover the ISMAR 2026 Program →
  </a>
</div>

  </div>
</section>

<style>
  .ismar-glance-section {
    padding: 5rem 1.5rem;
    text-align: center;
  }

  .ismar-glance-inner {
    width: min(100%, 1100px);
    margin: 0 auto;
    padding: 0 1rem;
    box-sizing: border-box;
  }

  .ismar-glance-title {
    margin: 0 0 2.5rem;
    color: #333;
    font-size: 2rem;
    font-weight: 900;
  }

  .ismar-glance-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 2rem;
  }

  .ismar-stat {
    padding: 2rem 1.25rem;
    opacity: 0;
    transform: translateY(22px);
    transition:
      opacity 0.8s ease,
      transform 0.8s cubic-bezier(0.22, 1, 0.36, 1);
  }

  .ismar-stat.is-visible {
    opacity: 1;
    transform: translateY(0);
  }

  .ismar-counter {
    display: block;
    color: #3A8BF3;
    font-size: clamp(2.5rem, 5vw, 4rem);
    font-weight: 900;
    line-height: 1;
    margin-bottom: 0.65rem;
  }

  .ismar-stat-label {
    display: block;
    color: #333;
    font-size: 1rem;
    font-weight: 700;
  }

  .ismar-program-cta {
    margin-top: 2.8rem;
  }

  .ismar-program-button {
    display: inline-block;
    padding: 0.9rem 1.6rem;
    border-radius: 999px;
    background: #3A8BF3;
    color: #fff !important;
    font-weight: 900;
    text-decoration: none !important;
    transition:
      transform 0.2s ease,
      background-color 0.2s ease;
  }

  .ismar-program-button:hover {
    background: #2878DB;
    transform: translateY(-2px);
    text-decoration: none !important;
  }

  .ismar-program-button:focus-visible {
    outline: 3px solid rgba(58, 139, 243, 0.35);
    outline-offset: 3px;
  }

  @media (max-width: 850px) {
    .ismar-glance-grid {
      grid-template-columns: repeat(2, 1fr);
    }
  }

  @media (max-width: 500px) {
    .ismar-glance-section {
      padding: 4rem 1rem;
    }

    .ismar-glance-inner {
      padding: 0 0.5rem;
    }

    .ismar-glance-grid {
      grid-template-columns: 1fr 1fr;
      gap: 1rem;
    }

    .ismar-stat {
      padding: 1.5rem 0.75rem;
    }

    .ismar-stat-label {
      font-size: 0.9rem;
    }
  }
</style>

<script>
  (function () {
    const section = document.querySelector(".ismar-glance-section");
    const counters = document.querySelectorAll(".ismar-counter");
    const stats = document.querySelectorAll(".ismar-stat");

    if (!section || !counters.length) return;

    let hasAnimated = false;
    const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    function easeOutQuart(t) {
      return 1 - Math.pow(1 - t, 4);
    }

    function animateCounter(counter, delay) {
      const target = Number(counter.dataset.target);
      const duration = 2200;

      setTimeout(function () {
        const startTime = performance.now();

        function update(currentTime) {
          const elapsed = currentTime - startTime;
          const progress = Math.min(elapsed / duration, 1);
          const eased = easeOutQuart(progress);

          counter.textContent = Math.round(target * eased);

          if (progress < 1) {
            requestAnimationFrame(update);
          } else {
            counter.textContent = target;
          }
        }

        requestAnimationFrame(update);
      }, delay);
    }

    function startAnimation() {
      if (hasAnimated) return;
      hasAnimated = true;

      if (reduceMotion) {
        stats.forEach(function (stat) {
          stat.classList.add("is-visible");
        });

        counters.forEach(function (counter) {
          counter.textContent = counter.dataset.target;
        });

        return;
      }

      stats.forEach(function (stat, index) {
        setTimeout(function () {
          stat.classList.add("is-visible");
        }, index * 90);
      });

      counters.forEach(function (counter, index) {
        animateCounter(counter, index * 90);
      });
    }

    const observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            startAnimation();
            observer.disconnect();
          }
        });
      },
      {
        threshold: 0.2,
        rootMargin: "0px 0px -8% 0px"
      }
    );

    observer.observe(section);
  })();
</script>







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

.registration-button {
  display: inline-block;
  margin-top: 0.9rem;
  padding: 0.8rem 1.4rem;
  border-radius: 999px;
  background: #3a8bf3;
  color: #fff !important;
  font-weight: 900;
  line-height: 1;
  text-decoration: none !important;
  transition:
    background-color 0.2s ease,
    transform 0.2s ease;
}

.registration-button:hover {
  background: #2878db;
  color: #fff !important;
  text-decoration: none !important;
  transform: translateY(-1px);
}

.registration-button:focus-visible {
  outline: 3px solid rgba(58, 139, 243, 0.35);
  outline-offset: 3px;
}

.sui-header {
  display: flex;
  align-items: center;
  gap: 1.25rem;
  margin-bottom: 1rem;
}

.sui-logo {
  width: 120px;
  max-width: 100%;
  height: auto;
  object-fit: contain;
  flex-shrink: 0;
}

.sui-heading {
  flex: 1;
}

.sui-heading h4 {
  margin: 0 0 0.35rem;
}

.sui-heading .announcement-date {
  margin: 0;
  font-weight: 700;
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
.info-category.info a:not(.registration-button) {
  color: #2878db;
}

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
  color: #8a6800;
}

.news-button {
  display: inline-block;
  margin-top: 0.9rem;
  padding: 0.8rem 1.4rem;
  border-radius: 999px;
  background: #e5b700;
  color: #fff !important;
  font-weight: 900;
  line-height: 1;
  text-decoration: none !important;
  transition:
    background-color 0.2s ease,
    transform 0.2s ease;
}

.news-button:hover {
  background: #dcb103;
  color: #fff !important;
  text-decoration: none !important;
  transform: translateY(-1px);
}

.news-button:focus-visible {
  outline: 3px solid #caa20055;
  outline-offset: 3px;
}




.info-category.anouncement {
  border-color: #FFAA01;
  background: rgba(255, 143, 45, 0.18);
}

.info-category.anouncement h4,
.info-category.anouncement a {
  color: #d37700;
}


.anouncement-button {
  display: inline-block;
  margin-top: 0.9rem;
  padding: 0.8rem 1.4rem;
  border-radius: 999px;
  background: #da8804;
  color: #fff !important;
  font-weight: 900;
  line-height: 1;
  text-decoration: none !important;
  transition:
    background-color 0.2s ease,
    transform 0.2s ease;
}

.anouncement-button:hover {
  background: #d37700;
  color: #fff !important;
  text-decoration: none !important;
  transform: translateY(-1px);
}

.anouncement-button:focus-visible {
  outline: 3px solid #6e3f026a;
  outline-offset: 3px;
}

.info-category.reminder {
  border-color: #F28C28;
  background: rgba(242, 140, 40, 0.12);
}

.info-category.reminder h4,
.info-category.reminder a {
  color: #D96F08;
}

/* Mobile layout */

@media (max-width: 600px) {
  .sui-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.75rem;
  }

  .sui-logo {
    width: 100px;
  }
}
</style>

<section class="info-categories-section">
  <h3 class="info-categories-title">News &amp; Announcements</h3>

  <div class="info-categories-container">
    <article class="info-category info">
      <h4>IEEE ISMAR 2026 Registration is Open!</h4>

  <p>
    Visit the registration page for information about fees, deadlines,
    and registration options.
  </p>

  <p>
    <a href="https://www.ieeeismar.net/2026/registration/">
      Registration Information Page→
    </a>
  </p>

  <a
    class="registration-button"
    href="https://iscrizioni.cicsud.it/cmsweb/Login.asp?IDcommessa=2649&amp;Lang=EN"
    target="_blank"
    rel="noopener noreferrer"
  >
    Register Now
  </a>
</article>



<article class="info-category anouncement">
  <h4>Participate in Women@ISMAR</h4>

  <p>
    Submit your expression of interest by August 30, 2026, at 23:59 AoE.
  </p>

  <p>
    <a
      href="https://www.ieeeismar.net/2026/women@ismar/"
      target="_blank"
      rel="noopener noreferrer"
    >
      Learn more →
    </a>
  </p>
  <a
      class="anouncement-button"
        href="https://docs.google.com/forms/d/e/1FAIpQLSc75Sc-WwFlYs-hBJJOpRFJHX4eDgsAMvPBks9eueAnUjk_nA/viewform"
        target="_blank"
        rel="noopener noreferrer"
      >
        Apply to Women@ISMAR
      </a>
</article>

<article class="info-category news">
  <h4>Speed Mentorship Session Registration Open</h4>

  <p>
    Registration is now open for the IEEE ISMAR 2026 Speed Mentorship Session,
    taking place on Monday, 5 October, from 4:00–5:30pm.
    Students are invited to meet with working professionals, ask questions,
    and gain career advice in a friendly speed-networking format.
    <strong>Spots are limited, so be sure to register early to secure your place.</strong>
  </p>

  <p>
    <a href="/2026/speed-mentorship/">
      Learn more about the Speed Mentorship Session →
    </a>
  </p>

<a
  class="news-button"
  href="https://www.computer.org/conferences/ismar2026"
  target="_blank"
  rel="noopener noreferrer"
>
  RSVP for Speed Mentorship
</a>
</article>

  <article class="info-category info">
      <div class="sui-header">
        <img
          src="/assets/2026/img/sponsors/SUI.png"
          alt="ACM SUI 2026 logo"
          class="sui-logo"
        >

    <div class="sui-heading">
      <h4>Continue Your Conference Experience at ACM SUI 2026</h4>

      <p class="announcement-date">
        October 10–11, 2026 · Bari, Italy
      </p>
    </div>
  </div>

  <p>
    ACM SUI 2026 will take place in Bari immediately after IEEE ISMAR 2026.
    Extend your stay and join the international community exploring spatial
    user interaction, immersive technologies, and interactive systems.
  </p>

  <p>
    <strong>Attending both ISMAR and SUI?</strong>
    Enjoy 10% off your SUI registration.
  </p>

  <p>
    <a
      href="https://sui.acm.org/2026/"
      target="_blank"
      rel="noopener noreferrer"
    >
      For more details, visit ACM SUI 2026 →
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
                        <tr data-deadline="2026-08-14T23:59:59-12:00">
                <td><b><a href="https://www.ieeeismar.net/2026/DEIA-grant/">DEIA Grant</a></b></td>
                <td><b>August 14th, 2026 (23:59 AoE, Friday)</b></td>
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

<!-- Partners Section -->

<section class="partners-section">
    <h1 class="partners-title">Partners and Supporting Organizations</h1>
    <div class="partners-grid">
    {% for partner in site.data["2026"].sponsors.partners %}
        <div class="partner-item">
            {% if partner.url and partner.url != "" %}
            <a href="{{ partner.url }}" target="_blank" class="partner-logo-link">
                <img src="{{ partner.logo | relative_url }}" alt="{{ partner.name }} Logo" />
            </a>
            {% else %}
            <div class="partner-logo-link">
                <img src="{{ partner.logo | relative_url }}" alt="{{ partner.name }} Logo" />
            </div>
            {% endif %}
        </div>
        {% endfor %}
    </div>
</section>