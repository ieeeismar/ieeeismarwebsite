---
layout: 2025/default
title: ISMAR 2025
redirect_from: /
---

<!-- Custom hero for the main page -->
<div class="hero">
    <img class="hero-image" src="{{ 'assets/2025/img/hero/hero-1920.jpg' | relative_url }}" srcset="
        {{ 'assets/2025/img/hero/hero-3840.jpg' | relative_url }} 3840w,
        {{ 'assets/2025/img/hero/hero-2560.jpg' | relative_url }} 2560w,
        {{ 'assets/2025/img/hero/hero-1920.jpg' | relative_url }} 1920w,
        {{ 'assets/2025/img/hero/hero-1280.jpg' | relative_url }} 1280w,
        {{ 'assets/2025/img/hero/hero-640.jpg' | relative_url }} 640w
    " sizes="(max-width: 640px) 100vw,
            (max-width: 1280px) 100vw,
            (max-width: 1920px) 100vw,
            100vw" alt="Hero Image" />
    <div class="content">
        <img class="hero-logo" src="{{ 'assets/2025/img/logo2.png' | relative_url }}" alt="IEEE ISMAR 2025 Logo" />
        <h1 class="heading">WELCOME TO</h1>
        <h1 class="heading">IEEE ISMAR 2025</h1>
        <h2 class="subheading">Daejeon, South Korea</h2>
        <h2 class="subheading">Oct. 8 - Oct. 12 2025</h2>

        <section class="description">
            <p>IEEE International Symposium on Mixed and Augmented Reality (ISMAR) is the premier conference for Augmented Reality (AR), Mixed Reality (MR) and Virtual Reality (VR), which attracts the world’s leading researchers from both academia and industry. ISMAR explores the advances in commercial and research activities related to AR, MR, and VR by continuing to expand its scope over the past several years.</p>
        </section>
    </div>

</div>

<div class="announcement">
    <h2>Discover the AR/MR/VR that will enable the future</h2>
    <p>We invite you to the 24th IEEE International Symposium on Mixed and Augmented Reality (ISMAR), which will be held at the Daejeon Convention Center (DCC), South Korea, from Oct. 8 to Oct. 12 2025.</p>
</div>

<section class="important-dates-section">
    <h2 class="important-dates-title">Important Dates</h2>

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
                <td><b>April 4th, 2025 (23:59 AoE, Friday)</b></td>
            </tr>
            <tr>
                <td><b>Papers</b></td>
                <td><b>April 11th, 2025 (23:59 AoE, Friday)</b></td>
            </tr>
            <tr>
                <td><b>Workshops</b></td>
                <td><b>May 2nd, 2025 (23:59 AoE, Friday)</b></td>
            </tr>
            <tr>
                <td><b>Workshops</b></td>
                <td><b>May 2nd, 2025 (23:59 AoE, Friday)</b></td>
            </tr>
            <tr>
                <td><b>Tutorials</b></td>
                <td>
                    <b>
                        <s style="color: #999;">May 9th, 2025 (23:59 AoE, Friday)</s><br>
                        <s>May 16th, 2025 (23:59 AoE, Friday)</s>
                    </b>
                </td>
            </tr>
            <tr>
                <td><b>Doctoral Consortium</b></td>
                <td>
                <b>
                    <s style="color: #999;">June 9th, 2025 (23:59 AoE, Monday)</s><br>
                    <s>June 30th, 2025 (23:59 AoE, Monday)</s>
                    </b>
                </td>
            </tr>
            <tr>
                <td><b>Workshop Papers</b></td>
                <td><b><a href="/2025/contribute/workshop-papers/">See workshop websites for deadlines</a></b></td>
            </tr>
            <tr>
                <td><b>Poster Papers</b></td>
                <td><b>July 29th, 2025 (23:59 AoE, Tuesday)</b></td>
            </tr>
            <tr>
                <td><b>Demos</b></td>
                <td>
                <b>
                July 29th, 2025 (23:59 AoE, Tuesday)<br>
                August 5th, 2025 (23:59 AoE, Tuesday)
                </b>
                </td>
                </tr>
        </tbody>
    </table>

</section>

<div class="video-container">
    <!-- YouTube Video Embed -->
    <iframe class="video"
            src="https://www.youtube.com/embed/ygxSQWsLR9E?si=ZfYWN9cAmTIQ-F8B"
            title="YouTube video player"
            frameborder="0"
            allow="autoplay; encrypted-media"
            allowfullscreen>
    </iframe>
</div>

<div class="venue-section">
    <!-- Venue Details -->
    <div class="venue-details">
        <h2 class="venue-title">Venue</h2>
        <p class="venue-name"><strong>Daejeon Convention Center (DCC)</strong></p>
        <p>107, Expo-ro, Yuseong-gu, Daejeon</p>
        <p><a href="http://www.dcckorea.or.kr" target="_blank">www.dcckorea.or.kr</a></p>
        <p>+82-42-250-1100</p>
    </div>

    <div class="google-map">
        <iframe src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d6424.8337529192995!2d127.391683!3d36.37490100000001!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x356549856f487a11%3A0xd03c3bec141f8760!2sDaejeon%20Convention%20Center!5e0!3m2!1sen!2skr!4v1732800254631!5m2!1sen!2skr"
        width="450" height="280" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
    </div>
</div>


<script>
document.addEventListener('DOMContentLoaded', function() {
    const now = new Date();
    console.log("Current time:", now.toISOString());

    const rows = document.querySelectorAll('.important-dates tbody tr');
    
    rows.forEach(row => {
        const submissionCell = row.querySelector('td:first-child b');
        const deadlineCell = row.querySelector('td:nth-child(2) b');

        // 🚫 Skip this row if it contains a manual-strike
        if (row.querySelector('.manual-strike')) {
            console.log("Skipped manual-strike row:", deadlineCell.textContent.trim());
            return;
        }

        const text = deadlineCell.textContent.trim();
        const dateMatch = text.match(/([A-Za-z]+) (\d+)(?:st|nd|rd|th), (\d{4}) \(23:59 AoE/);

        if (!dateMatch) {
            console.warn("Couldn't parse date from:", text);
            return;
        }

        const month = dateMatch[1];
        const day = dateMatch[2];
        const year = dateMatch[3];
        const deadline = new Date(`${month} ${day}, ${year} 11:59:00 GMT`);
        deadline.setDate(deadline.getDate() + 1); // AoE is UTC-12

        if (deadline < now) {
            submissionCell.classList.add('passed-deadline');
            deadlineCell.classList.add('passed-deadline');
            console.log(`Marked as passed: ${submissionCell.textContent}`);
        }
    });
});
</script>
