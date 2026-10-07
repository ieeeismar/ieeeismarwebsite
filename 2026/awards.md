---
layout: 2026/page-2026
title: Awards
permalink: /2026/awards/
---

<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-FQFFZGXF3Y"></script>

<script>
  window.dataLayer = window.dataLayer || [];

  function gtag(){dataLayer.push(arguments);}

  gtag('js', new Date());

  gtag('config', 'G-FQFFZGXF3Y');
</script>

<style>

  .award-nav {
    margin: 1.5rem 0 2.5rem;
  }

  .award-row {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 0.8rem;
    margin-bottom: 0.8rem;
  }

  .award-grid {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 0.8rem;
    margin-top: 0.8rem;
  }

  .award-card {
    display: block;
    background: #fff;
    border: 1px solid #e5e7eb;
    border-radius: 12px;
    padding: 0.7rem 0.85rem 0.6rem;
    box-shadow: 0 4px 12px rgba(15, 23, 42, 0.035);
    min-width: 0;
    box-sizing: border-box;
    color: #1f2937;
    text-decoration: none;
    cursor: pointer;
    transition: border-color 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease;
  }

  .award-card:hover,
  .award-card:focus-visible {
    background: #3A8BF3;
    border-color: #3A8BF3;
    color: #fff;
    box-shadow: 0 5px 14px rgba(58, 139, 243, 0.18);
    transform: translateY(-1px);
  }

  .award-card:focus-visible {
    outline: 3px solid #1f2937;
    outline-offset: 3px;
  }

  .award-card-featured {
    width: auto;
  }

  .award-card-secondary {
    width: auto;
  }

  .award-card h2 {
    margin: 0 0 0.4rem;
    padding-bottom: 0.3rem;
    border-bottom: 1px solid #edf2f7;
    font-size: 0.95rem;
    color: #1f2937;
  }

  .award-card h2 {
    color: #1f2937;
  }

  .award-card:hover h2,
  .award-card:focus-visible h2,
  .award-card:hover .award-list,
  .award-card:focus-visible .award-list,
  .award-card:hover .award-list li,
  .award-card:focus-visible .award-list li {
    color: #fff;
  }

  .award-list {
    margin: 0;
    padding-left: 1.05rem;
  }

  .award-list li {
    margin-bottom: 0.3rem;
    line-height: 1.45;
    color: #334155;
  }

  .award-list a {
    color: #1f2937;
    text-decoration: none;
    font-weight: 500;
    font-size: 0.88rem;
  }

  .award-sections {
    margin-top: 2.5rem;
  }

  .award-section {
    margin: 0 0 3rem;
    scroll-margin-top: 100px;
  }

  .award-section > h2 {
    margin: 0 0 1rem;
    padding-bottom: 0.45rem;
    border-bottom: 2px solid #3A8BF3;
    font-size: 1.45rem;
    color: #1f2937;
  }

  .award-entry {
    margin: 1.5rem 0;
    scroll-margin-top: 100px;
  }

  .award-entry h3 {
    margin: 0 0 0.5rem;
    font-size: 1.08rem;
    color: #3A8BF3;
    font-weight: 700;
  }

  .award-entry-title-with-icon {
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }

  .award-entry-title-with-icon img {
    width: 3.5rem;
    height: auto;
    flex: 0 0 auto;
  }

  .award-entry-subtitle {
    font-weight: 700;
  }

  .award-entry p {
    margin: 0;
    line-height: 1.7;
    color: #475569;
  }

  .best-paper-list {
    margin: 0;
    padding-left: 1.5rem;
  }

  .best-paper-list li {
    padding-left: 0.35rem;
    line-height: 1.7;
    margin-bottom: 1rem;
  }

  .best-paper-list li:last-child {
    margin-bottom: 0;
  }

  .best-paper-title {
    display: block;
    color: #1f2937;
  }

  .best-paper-authors {
    display: block;
    color: #475569;
  }

  @media (max-width: 768px) {
    .award-grid {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }
  }

  @media (max-width: 480px) {
    .award-grid {
      grid-template-columns: 1fr;
    }

    .award-card {
      padding: 0.85rem 1rem 0.75rem;
    }
  }

</style>

# Conference Awards

<div class="award-nav">

  <!-- SUMMARY CARDS -->
  <div class="award-grid">

    <a class="award-card award-card-secondary" href="#paper-awards-section">
      <h2>Paper Awards</h2>
      <ul class="award-list">
        <li>Best Paper Award</li>
        <li>Best Paper Award Honorable Mention</li>
      </ul>
    </a>

    {% comment %}
    <div class="award-card award-card-secondary">
      <h2><a href="#reviewer-awards-section">Reviewer Awards</a></h2>
      <ul class="award-list">
        <li><a href="#outstanding-reviewer-award">Outstanding Reviewer Award</a></li>
      </ul>
    </div>

    <div class="award-card">
      <h2><a href="#poster-awards-section">Poster Awards</a></h2>
      <ul class="award-list">
        <li><a href="#best-long-poster-award">Best Long Poster Award</a></li>
        <li><a href="#best-short-poster-award">Best Short Poster Award</a></li>
        <li><a href="#best-long-poster-honorable-mention">Best Long Poster Award Honorable Mention</a></li>
        <li><a href="#best-short-poster-honorable-mention">Best Short Poster Award Honorable Mention</a></li>
      </ul>
    </div>

    <div class="award-card">
      <h2><a href="#demonstration-awards-section">Demonstration Awards</a></h2>
      <ul class="award-list">
        <li><a href="#best-demonstration-award">Best Demonstration Award</a></li>
        <li><a href="#best-demonstration-award-honorable-mention">Best Demonstration Award Honorable Mention</a></li>
      </ul>
    </div>

    <div class="award-card">
      <h2><a href="#doctoral-consortium-awards-section">Doctoral Consortium Awards</a></h2>
      <ul class="award-list">
        <li><a href="#best-doctoral-consortium-award">Best Doctoral Consortium Award</a></li>
        <li><a href="#best-doctoral-consortium-award-honorable-mention">Best Doctoral Consortium Award Honorable Mention</a></li>
      </ul>
    </div>

    <div class="award-card">
      <h2><a href="#community-awards-section">Community &amp; Service Awards</a></h2>
      <ul class="award-list">
        <li><a href="#student-volunteer-award">Student Volunteer Award</a></li>
        <li><a href="#social-engagement-award">Social Engagement Award</a></li>
      </ul>
    </div>

    <div class="award-card">
      <h2><a href="#workshop-awards-section">Workshop Awards</a></h2>
      <ul class="award-list">
        <li><a href="#best-workshop-award">Best Workshop Award</a></li>
      </ul>
    </div>
    {% endcomment %}

  </div>

</div>


<div class="award-sections">

  {% comment %}
  <section
    class="award-section"
    id="impact-awards-section"
  >

    <h2>Impact Awards</h2>

    <div
      class="award-entry"
      id="career-impact-award"
    >
      <h3 class="award-entry-title-with-icon">
        <img
          src="{{ '/assets/2026/img/badges/award-1.png' | relative_url }}"
          alt="ISMAR Career Impact Award"
        >
        <span>ISMAR Career Impact Award</span>
      </h3>

      <p>
        Award information will be available here.
      </p>
    </div>


    <div
      class="award-entry"
      id="paper-impact-award"
    >
      <h3 class="award-entry-title-with-icon">
        <img
          src="{{ '/assets/2026/img/badges/award-1.png' | relative_url }}"
          alt="ISMAR Paper Impact Award"
        >
        <span>ISMAR Paper Impact Award</span>
      </h3>

      <p>
        Award information will be available here.
      </p>
    </div>

  </section>
  {% endcomment %}


  <section
    class="award-section"
    id="paper-awards-section"
  >

    <h2>Paper Awards</h2>
    <p>
      We gratefully acknowledge <a href="https://vera-xr.io/">VERA (Virtual Experience Research Accelerator)</a>
      for sponsoring the Best Paper Awards through its use grants.
    </p>

    <div
      class="award-entry"
      id="best-paper-award"
    >
      <h3 class="award-entry-title-with-icon">
        <img
          src="{{ '/assets/2026/img/badges/award-1.png' | relative_url }}"
          alt="Best Paper Award"
        >
        <span>Best Paper Award</span>
      </h3>

      <ol class="best-paper-list">
        <li>
          <strong class="best-paper-title">Posture-Adaptive Azimuthal Guidance via a Forearm Vibrotactile Interface for VR Navigation</strong>
          <span class="best-paper-authors">Jaehyeong Hwang, Hyeseong Jin, and Chaeyong Park</span>
        </li>
        <li>
          <strong class="best-paper-title">Olfactory Context Cues for Procedural Skill Transfer from Digital Twin-Based Mixed Reality Learning to Real-World Execution</strong>
          <span class="best-paper-authors">Mengting Lai, Xiaoxuan Zhao, Wen Li, Shirin Hajahmadi, Pasquale Cascarano, and Gustavo Marfia</span>
        </li>
        <li>
          <strong class="best-paper-title">CyberSelf: Embodied Self-Distancing for Emotional Support in Virtual Reality</strong>
          <span class="best-paper-authors">Bing Li, Yan Hu, Tinghui Li, Yinuo Zhang, Wen Ma, Yuanfeng Zhou, and Yiran Shen</span>
        </li>
        <li>
          <strong class="best-paper-title">One Finger Warrior: Thumb-to-Index Finger Interaction Technique for Mobile Use</strong>
          <span class="best-paper-authors">Omang Baheti, Sharif Am Faleel, Rishav Banerjee, Pourang Irani, and Khalad Hasan</span>
        </li>
        <li>
          <strong class="best-paper-title">Sharing Roughness with Hand-Outline Visualization to Reduce Sensory Asymmetry in VR Collaboration</strong>
          <span class="best-paper-authors">Minju Baeck, Yoonseok Shin, Hyunjin Lee, Boram Yoon, Sang Ho Yoon, and Woontack Woo</span>
        </li>
        <li>
          <strong class="best-paper-title">ReAlign: Closed-Loop Support for Continuous Virtual Reality Tasks</strong>
          <span class="best-paper-authors">Hayeon Kim and In-Kwon Lee</span>
        </li>
        <li>
          <strong class="best-paper-title">NPCRadar: Non-Player-Character-Centered Multi-User Virtual Reality Crowd Forecasting</strong>
          <span class="best-paper-authors">Yuan Yu, Chunlei Xu, Jiayi Wu, Yu Cao, and Boon Giin Lee</span>
        </li>
        <li>
          <strong class="best-paper-title">Actionable Guidance Outperforms Map and Compass Cues in Demanding Immersive VR Wayfinding</strong>
          <span class="best-paper-authors">Apurv Varshney, Lily M. Turkstra, Jiaxin Su, Mable Zhou, Scott T. Grafton, Barry Giesbrecht, Mary Hegarty, and Michael Beyeler</span>
        </li>
      </ol>
    </div>


    <div
      class="award-entry"
      id="best-paper-award-honorable-mention"
    >
      <h3 class="award-entry-title-with-icon">
        <img
          src="{{ '/assets/2026/img/badges/award-2.png' | relative_url }}"
          alt="Best Paper Award Honorable Mention"
        >
        <span>Best Paper Award Honorable Mention</span>
      </h3>

      <ol class="best-paper-list">
        <li>
          <strong class="best-paper-title">Understanding Organizational Strategies Across Multimodal Artifacts in Immersive Computational Notebooks</strong>
          <span class="best-paper-authors">Sungwon In, Minju Baeck, Yalong Yang, Sang Ho Yoon, Woontack Woo, and Mallesham Dasari</span>
        </li>
        <li>
          <strong class="best-paper-title">Evaluating the Vergence-Accommodation Conflict in Gaze-Based 3D Target Selection</strong>
          <span class="best-paper-authors">Mohammad Raihanul Bashar, Mohammadreza Amini, Aunnoy K Mutasim, Mayra Donaji Barrera Machuca, Wolfgang Stuerzlinger, and Anil Ufuk Batmaz</span>
        </li>
        <li>
          <strong class="best-paper-title">SemanticXR: Low Power, Real-time Queryable Semantic Mapping with a Device-Cloud Architecture</strong>
          <span class="best-paper-authors">Rahul Singh, Devdeep Ray, Connor Smith, and Sarita Adve</span>
        </li>
        <li>
          <strong class="best-paper-title">MURMR: A Multimodal Sensing Pipeline for Automated Group Behavior Analysis in Mixed Reality</strong>
          <span class="best-paper-authors">Diana Romero, Yasra Chandio, Fatima M. Anwar, and Salma Elmalaki</span>
        </li>
        <li>
          <strong class="best-paper-title">From Asymmetric Guidance to Shared Evidence: Governing the Visibility of Spatial Cues in Multi-User Virtual Reality</strong>
          <span class="best-paper-authors">Hayeon Kim and In-Kwon Lee</span>
        </li>
        <li>
          <strong class="best-paper-title">Effects of Spatial Perspective and Frame of Reference Integration on Gaze Behavior and Spatial Learning</strong>
          <span class="best-paper-authors">Yu Zhao, Jeanine Stefanucci, Sarah Creem-Regehr, and Bobby Bodenheimer</span>
        </li>
        <li>
          <strong class="best-paper-title">DP-LENS: A Density-Aware Polyfocal Lens with Topology-Driven Auto-Routing for Occlusion Management in Immersive 3D Analytics</strong>
          <span class="best-paper-authors">Nieyu Cao, Xian Wang, and Lik-Hang Lee</span>
        </li>
        <li>
          <strong class="best-paper-title">Grasping Real and Virtual Objects in AR: Study of Carry-Over Effects on Grasping Anticipatory Behavior</strong>
          <span class="best-paper-authors">Juri Yoneyama, Étienne Peillard, Guillaume Moreau, and Ferran Argelaguet</span>
        </li>
        <li>
          <strong class="best-paper-title">Towards General Motion Sickness Reduction via Semi-random Galvanic Vestibular Stimulation</strong>
          <span class="best-paper-authors">Ricardo Hendrichs, Johann Habakuk Israel, Marcus Magnor, and Colin Groth</span>
        </li>
        <li>
          <strong class="best-paper-title">Seeing Through the Surface: Evaluating Visualization Techniques for Depth Perception in Augmented Microscopy</strong>
          <span class="best-paper-authors">Trishia El Chemaly, Waly Niu, Yunxin Fan, Yuxuan Wu, Fanrui Fu, Christoph Leuze, Brian Hargreaves, Bruce Daniel, and Nikolas Blevins</span>
        </li>
        <li>
          <strong class="best-paper-title">MR-Compare: A Mixed-Reality Framework for Spatially Grounded Visual Comparison of 3D Gaussian Splatting and Mesh Reconstructions with the Physical Environment</strong>
          <span class="best-paper-authors">Changrui Zhu, Ernst Kruijff, Pengju Zhang, and Simon Julier</span>
        </li>
        <li>
          <strong class="best-paper-title">How Opacity and Background Affect Surface Contact Perception in Optical See-Through AR</strong>
          <span class="best-paper-authors">Min Ni, Hsiang-Ting Chen, Gilles Coppin, and Étienne Peillard</span>
        </li>
        <li>
          <strong class="best-paper-title">When Registration Error Becomes Ambiguous: Behavioural Effects of Static Misalignment in Augmented Reality</strong>
          <span class="best-paper-authors">Ziwen Lu, Kahlia Shapiro, Ernst Kruijff, Anthony Steed, and Simon Julier</span>
        </li>
        <li>
          <strong class="best-paper-title">Beyond the Black Patch: A Composable, Gaze-Contingent Framework for Simulating Central Vision Loss in XR</strong>
          <span class="best-paper-authors">Parisa Ghasemi, Susan A. Primo, Carolyn C. Seepersad, and Mohsen Moghaddam</span>
        </li>
        <li>
          <strong class="best-paper-title">How VR Systems Impact Virtual Navigation for Blind People</strong>
          <span class="best-paper-authors">Manuel Piçarra and João Guerreiro</span>
        </li>
        <li>
          <strong class="best-paper-title">Visual Cue Interactions in AR-Guided Needle Insertion: A Prostate Biopsy-Inspired Phantom Study</strong>
          <span class="best-paper-authors">Xinrui Zou, Mingxu Liu, Thomas T. Jones, Braden Millan, Sandeep Gurram, Peter A. Pinto, Raisa Z. Freidlin, and Alejandro Martin-Gomez</span>
        </li>
        <li>
          <strong class="best-paper-title">Comparing Pinch and Point Poses for Single-Stroke Drawing in Virtual Reality</strong>
          <span class="best-paper-authors">Tushar Billakanti and Jay Henderson</span>
        </li>
        <li>
          <strong class="best-paper-title">Exploring Object Recall in an Object-Rich AR Office Scene</strong>
          <span class="best-paper-authors">Sangita Kunapuli, Radha Kumaran, Shane Dirksen, You-Jin Kim, Yanxiu Jin, Misha Sra, and Tobias Höllerer</span>
        </li>
      </ol>
    </div>

  </section>

  {% comment %}

  <section
    class="award-section"
    id="reviewer-awards-section"
  >

    <h2>Reviewer Awards</h2>

    <div
      class="award-entry"
      id="outstanding-reviewer-award"
    >
      <h3 class="award-entry-title-with-icon">
        <img
          src="{{ '/assets/2026/img/badges/award-1.png' | relative_url }}"
          alt="Outstanding Reviewer Award"
        >
        <span>Outstanding Reviewer Award</span>
      </h3>

      <p>
        Award information will be available here.
      </p>
    </div>

  </section>


  <section
    class="award-section"
    id="poster-awards-section"
  >

    <h2>Poster Awards</h2>

    <div
      class="award-entry"
      id="best-long-poster-award"
    >
      <h3 class="award-entry-title-with-icon">
        <img
          src="{{ '/assets/2026/img/badges/award-1.png' | relative_url }}"
          alt="Best Long Poster Award"
        >
        <span>Best Long Poster Award</span>
      </h3>

      <p>
        Award information will be available here.
      </p>
    </div>


    <div
      class="award-entry"
      id="best-short-poster-award"
    >
      <h3 class="award-entry-title-with-icon">
        <img
          src="{{ '/assets/2026/img/badges/award-1.png' | relative_url }}"
          alt="Best Short Poster Award"
        >
        <span>Best Short Poster Award</span>
      </h3>

      <p>
        Award information will be available here.
      </p>
    </div>


    <div
      class="award-entry"
      id="best-long-poster-honorable-mention"
    >
      <h3 class="award-entry-title-with-icon">
        <img
          src="{{ '/assets/2026/img/badges/award-2.png' | relative_url }}"
          alt="Best Long Poster Award Honorable Mention"
        >
        <span>Best Long Poster Award Honorable Mention</span>
      </h3>

      <p>
        Award information will be available here.
      </p>
    </div>


    <div
      class="award-entry"
      id="best-short-poster-honorable-mention"
    >
      <h3 class="award-entry-title-with-icon">
        <img
          src="{{ '/assets/2026/img/badges/award-2.png' | relative_url }}"
          alt="Best Short Poster Award Honorable Mention"
        >
        <span>Best Short Poster Award Honorable Mention</span>
      </h3>

      <p>
        Award information will be available here.
      </p>
    </div>

  </section>


  <section
    class="award-section"
    id="demonstration-awards-section"
  >

    <h2>Demonstration Awards</h2>

    <div
      class="award-entry"
      id="best-demonstration-award"
    >
      <h3 class="award-entry-title-with-icon">
        <img
          src="{{ '/assets/2026/img/badges/award-1.png' | relative_url }}"
          alt="Best Demonstration Award"
        >
        <span>Best Demonstration Award</span>
      </h3>

      <p>
        Award information will be available here.
      </p>
    </div>


    <div
      class="award-entry"
      id="best-demonstration-award-honorable-mention"
    >
      <h3 class="award-entry-title-with-icon">
        <img
          src="{{ '/assets/2026/img/badges/award-2.png' | relative_url }}"
          alt="Best Demonstration Award Honorable Mention"
        >
        <span>Best Demonstration Award Honorable Mention</span>
      </h3>

      <p>
        Award information will be available here.
      </p>
    </div>

  </section>


  <section
    class="award-section"
    id="doctoral-consortium-awards-section"
  >

    <h2>Doctoral Consortium Awards</h2>

    <div
      class="award-entry"
      id="best-doctoral-consortium-award"
    >
      <h3 class="award-entry-title-with-icon">
        <img
          src="{{ '/assets/2026/img/badges/award-1.png' | relative_url }}"
          alt="Best Doctoral Consortium Award"
        >
        <span>Best Doctoral Consortium Award</span>
      </h3>

      <p>
        Award information will be available here.
      </p>
    </div>


    <div
      class="award-entry"
      id="best-doctoral-consortium-award-honorable-mention"
    >
      <h3 class="award-entry-title-with-icon">
        <img
          src="{{ '/assets/2026/img/badges/award-2.png' | relative_url }}"
          alt="Best Doctoral Consortium Award Honorable Mention"
        >
        <span>Best Doctoral Consortium Award Honorable Mention</span>
      </h3>

      <p>
        Award information will be available here.
      </p>
    </div>

  </section>


  <section
    class="award-section"
    id="workshop-awards-section"
  >

    <h2>Workshop Awards</h2>

    <div
      class="award-entry"
      id="best-workshop-award"
    >
      <h3 class="award-entry-title-with-icon">
        <img
          src="{{ '/assets/2026/img/badges/award-1.png' | relative_url }}"
          alt="Best Workshop Award"
        >
        <span>Best Workshop Award</span>
      </h3>

      <p>
        Award information will be available here.
      </p>
    </div>

  </section>


  <section
    class="award-section"
    id="community-awards-section"
  >

    <h2>Community &amp; Service Awards</h2>

    <div
      class="award-entry"
      id="student-volunteer-award"
    >
      <h3 class="award-entry-title-with-icon">
        <img
          src="{{ '/assets/2026/img/badges/award-1.png' | relative_url }}"
          alt="Student Volunteer Award"
        >
        <span>Student Volunteer Award</span>
      </h3>

      <p>
        Award information will be available here.
      </p>
    </div>


    <div
      class="award-entry"
      id="social-engagement-award"
    >
      <h3 class="award-entry-title-with-icon">
        <img
          src="{{ '/assets/2026/img/badges/award-1.png' | relative_url }}"
          alt="Social Engagement Award"
        >
        <span>Social Engagement Award</span>
      </h3>

      <p>
        Award information will be available here.
      </p>
    </div>

  </section>
  {% endcomment %}

</div>